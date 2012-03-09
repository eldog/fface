package uk.me.eldog.fface;

import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.text.SimpleDateFormat;

import android.app.Activity;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.content.ContentResolver;
import android.content.ContentValues;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.PointF;
import android.graphics.RectF;
import android.media.FaceDetector;
import android.media.FaceDetector.Face;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.provider.MediaStore.Images;
import android.provider.MediaStore.Images.ImageColumns;
import android.util.Log;
import android.util.Pair;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewGroup.LayoutParams;

import uk.me.eldog.fface.R;

public class FaceCaptureActivity extends Activity
{
    private final static String TAG = FaceCaptureActivity.class.getSimpleName();
    final static int DIALOG_ENSURE_DATA_FILES_EXIST_ID = 0;
    final static int DIALOG_LOAD_FACE_DETECTOR_ID = 1;
    final static int DIALOG_FINDING_FACES_ID = 2;
    final static int DIALOG_ANALYSING_ATTRACTIVENESS_ID = 3;
    final static String EXTERNAL_STORAGE_DIR 
                                    = "/Android/data/uk.me.eldog.fface/files/";
    final static String EXTERNAL_CAMERA_DIR = "/Camera/";
    final static String CASCADE_FILE = "lbpcascade_frontalface.xml";
    final static String CNN_FILE = "cnn.xml";
    private final static Map<String, Integer> sDataFileMap;
    private final static int MAX_FACES = 5;

    static
    {
        sDataFileMap = new HashMap<String, Integer>();
        sDataFileMap.put(CASCADE_FILE, R.raw.lbpcascade_frontalface);
        sDataFileMap.put(CNN_FILE, R.raw.cnn);
    } // static

    private class EnsureDataFilesExistTask 
            extends AsyncTask<File, Void, Boolean>
    {
        protected void onPreExecute()
        {
            // Show busy waiting dialog
            showDialog(DIALOG_ENSURE_DATA_FILES_EXIST_ID);
        } // onPreExecute

        protected Boolean doInBackground(File... files)
        {
            // check that files exists and create if necessary
            if (Environment.MEDIA_MOUNTED.equals(
                        Environment.getExternalStorageState()))
            {
                File externalStorageDir = new File(Environment.getExternalStorageDirectory(),
                                                  EXTERNAL_STORAGE_DIR);
                boolean createdDir = externalStorageDir.mkdirs();
                Log.i(TAG, createdDir 
                       ? "Created new directory for files" 
                       : "Directory exists");
                for (Map.Entry<String, Integer> dataEntry : sDataFileMap.entrySet())
                {
                    String fileName = dataEntry.getKey();
                    Integer resource = dataEntry.getValue(); 
                    File file = new File(externalStorageDir, fileName);
                    if (file.exists())
                    {
                        Log.i(TAG, "File " + fileName + " exists");
                        continue;
                    } // if
                    InputStream is = null;
                    FileOutputStream os = null;
                    
                    try
                    {
                        is = FaceCaptureActivity.this.getResources().openRawResource(resource);
                        os = new FileOutputStream(file);
                        byte[] buffer = new byte[4096];
                        int bytesRead;
                        while ((bytesRead = is.read(buffer)) != -1)
                        {
                            os.write(buffer, 0, bytesRead);
                        } // while
                    } // try
                    catch (IOException e)
                    {
                        Log.e(TAG, 
                              "Problem happened writing file " + fileName, 
                              e);
                        return false;
                    } // catch
                    finally
                    {
                        if (is != null)
                        {
                            try
                            {
                                is.close();
                            } // try
                            catch (IOException e)
                            {
                                Log.e(TAG, "Problem closing input stream", e);
                            } // catch
                        } // if
                        if (os != null)
                        {
                            try
                            {
                                os.close();
                            } // try
                            catch (IOException e)
                            {
                                Log.e(TAG, "Problem closing output stream", e);
                            } // catch
                        } // if
                    } // finally
                } // for
                    return true;
            } // if
            else
            {
                return false;
            } // else
        } // doInBackground

        protected void onProgressUpdate(Void... progress)
        {
            // Not much to update on the ui
        } // onProgressUpdate

        protected void onPostExecute(Boolean result)
        {
            // check whether that we were able to ensure the files exist
            // Dismiss the dialog
            removeDialog(DIALOG_ENSURE_DATA_FILES_EXIST_ID);
            //setContentView(new FaceCaptureView(FaceCaptureActivity.this));
            new EnsureExternalDirectory().execute();
        } // onPostExecute

    } // class EnsureDataFilesExistTask

    private Uri mImageUri = null;

    private static final int INTENT_PICTURE_TAKEN = 0;

    private class EnsureExternalDirectory extends AsyncTask<Void, Void, Uri>
    {
        protected Uri doInBackground(Void... params)
        {
            if (Environment.MEDIA_MOUNTED.equals(
                        Environment.getExternalStorageState()))
            {
                File imageDir = new File(Environment.getExternalStorageDirectory(),
                                      Environment.DIRECTORY_DCIM 
                                      + EXTERNAL_CAMERA_DIR);
                boolean createdDirs = imageDir.mkdirs();
                Log.i(TAG, imageDir + (createdDirs ? " created" : " exists"));
                
                Uri fileUri = Uri.fromFile(new File(imageDir, getImageFileName()));
                Log.i(TAG, "Image uri will be " + fileUri);
                return fileUri;

            } // if
            else
            {
                return null;
            } // else
        } // doInBackground

        protected void onProgressUpdate(Void... progress)
        {
        } // onProgressUpdate

        protected void onPostExecute(Uri result)
        {
            if (result != null)
            {
                mImageUri = result;
                Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                intent.putExtra(MediaStore.EXTRA_OUTPUT, mImageUri);
                startActivityForResult(intent, INTENT_PICTURE_TAKEN);
            } // if
            else
            {
                Log.e(TAG, "Could not get access to external directory");
            } // else
        } // onPostExecute

    } // EnsureExternalDirectory

    private class InsertImageIntoMediaStore 
            extends AsyncTask<Pair<ContentResolver, Uri>, 
                              Void, 
                              Pair<Bitmap, Map<Integer, FaceRect>>>
    {
        protected void onPreExecute()
        {
            showDialog(DIALOG_FINDING_FACES_ID);
        } // onPreExecute

        protected Pair<Bitmap, Map<Integer, FaceRect>> 
            doInBackground(Pair<ContentResolver, Uri>... param)
        {
            ContentResolver cr = param[0].first;
            Uri uri = param[0].second;
            getContentResolver().notifyChange(uri, null);
            File imageFile = null;
            try
            {
                // note it's a java.net URI
                imageFile = new File(new URI(uri.toString()));
            }
            catch(URISyntaxException e)
            {
                Log.e(TAG, "Could not create URI from android uri", e);
                return null;
            }
                        
            Uri imageUri = null;
            try
            {
                imageUri = Uri.parse(
                        Images.Media.insertImage(cr, 
                                                 imageFile.toString(), 
                                                 imageFile.getName(), 
                                                 "Taken by FMobile"));
            } // try
            catch (Throwable thr)
            {
                Log.e(TAG, "Unable to write to media store" + thr);
            } // catch

            // Update the media provider to have the date information to display
            // correctly in the gallery application
            ContentValues values = new ContentValues(1);
            values.put(ImageColumns.DATE_TAKEN, imageFile.lastModified());
            cr.update(imageUri, 
                      values, 
                      null /* where */,
                      null /* selectionArgs */);

            Bitmap imageBitmap;
            try
            {
                imageBitmap = Images.Media.getBitmap(cr, imageUri);
            } // try
            catch (IOException e)
            {
                Log.e(TAG, "Could not open bitmap file");
                return null;
            } // catch
            imageBitmap = Bitmap.createScaledBitmap(imageBitmap, 
                                                    imageBitmap.getWidth() / 4,
                                                    imageBitmap.getHeight() / 4,
                                                    true);
            FaceDetector faceDetector = new FaceDetector(imageBitmap.getWidth(),
                                                         imageBitmap.getHeight(),
                                                         MAX_FACES);
            Face[] faces = new Face[MAX_FACES];
            int numberFacesFound = faceDetector.findFaces(imageBitmap, faces);
            Map<Integer, FaceRect> faceMap 
                = new HashMap<Integer, FaceRect>(numberFacesFound);
            for (int faceIndex = 0; faceIndex < numberFacesFound; faceIndex ++)
            {
                faceMap.put(faceIndex, new FaceRect(faces[faceIndex]));
            } // for

            Log.i(TAG, "Found " + numberFacesFound  + " faces");

            return new Pair<Bitmap, Map<Integer, FaceRect>>(imageBitmap, faceMap);
        } // onPreExecute

        protected void onProgressUpdate(Void... params)
        {
        } // onProgressUpdate

        protected void 
            onPostExecute(Pair<Bitmap, Map<Integer, FaceRect>> result)
        {
            if (result != null)
            {
                Log.i(TAG, "Image succesfully processed");
            } // if
            else
            {
                Log.e(TAG, "Unable to process image");
            } // else
            removeDialog(DIALOG_FINDING_FACES_ID);

            mBitmap= result.first;
            mFaceMap = result.second;
            
            RectImageView fiv = new RectImageView(FaceCaptureActivity.this);
            fiv.setImageBitmap(mBitmap);
            
            for (Entry<Integer, FaceRect> entry : mFaceMap.entrySet())
            {
                int id = entry.getKey();
                FaceRect faceRect = entry.getValue();
                fiv.addRect(id, faceRect);
            } // for
            
            fiv.addRectTouchListener(new RectImageView.RectTouchListener()
                {
                    private boolean pressed = false;
                    public boolean onRectTouchEvent(int id, MotionEvent event)
                    {
                        FaceRect face = mFaceMap.get(id);
                        if (face == null)
                        {
                            Log.e(TAG, "We touched a face that wasn't in our map");
                            return false;
                        } // if
                        else if (!pressed)
                        {
                            pressed = true;
                            new CropAndScaleBitmap().execute(new Pair<Bitmap, RectF>(mBitmap, face));
                            return true;
                        }
                        else
                        {
                            return false;
                        }
                    } // onRectTouchEvent
                });

            setContentView(fiv);
        } // onPostExecute
    } // class

    private Map<Integer, FaceRect> mFaceMap = new HashMap<Integer, FaceRect>();
    private Bitmap mBitmap = null;

    private class CropAndScaleBitmap 
            extends AsyncTask<Pair<Bitmap, RectF>, Void, Pair<Bitmap, Double>>
    {

        protected void onPreExecute()
        {
            showDialog(DIALOG_ANALYSING_ATTRACTIVENESS_ID);
        } // onPreExecute

        protected Pair<Bitmap, Double> doInBackground(Pair<Bitmap, RectF>... params)
        {
            Bitmap bitmap = params[0].first;
            RectF faceRect = params[0].second;
            Log.d(TAG, "CReating cropped bitmap");
            Bitmap faceBitmap = Bitmap.createBitmap(bitmap, 
                                                    (int)faceRect.left,
                                                    (int)faceRect.top,
                                                    (int) (faceRect.right - faceRect.left),
                                                    (int) (faceRect.bottom - faceRect.top));
            Log.d(TAG, "Scaling bitmap");
            Bitmap scaledBitmap = Bitmap.createScaledBitmap(faceBitmap, 128, 128, true);
            Log.d(TAG, "done scaling");
            Log.d(TAG, "Calculating attractiveness");
            int[] pixels = new int[128 * 128];
            scaledBitmap.getPixels(pixels, 0, 128, 0, 0, 128, 128);
            Log.d(TAG, "pixels length = " + pixels.length);
            double score = -1000.0;
            if (Environment.MEDIA_MOUNTED.equals(
                        Environment.getExternalStorageState()))
            {
                File externalStorageDir = new File(Environment.getExternalStorageDirectory(),
                                                  EXTERNAL_STORAGE_DIR);
                score = runConv(new File(externalStorageDir, CNN_FILE).toString(), 
                                       pixels);
                Log.d(TAG, "SCORE = " + score);
            }
            else
            {
                Log.e(TAG, "Could not access external storage - unable to score!");
            } // else
            return new Pair<Bitmap, Double>(scaledBitmap, score);
        } // doInBackground

        protected void onPostExecute(Pair<Bitmap, Double> result)
        {
            Bitmap bitmap = result.first;
            double score = result.second;
            Log.d(TAG, "Post executing");
            LinearLayout ll = new LinearLayout(FaceCaptureActivity.this);
            ll.setOrientation(LinearLayout.VERTICAL);
            ll.setLayoutParams(new LayoutParams(LayoutParams.FILL_PARENT, 
                                                LayoutParams.FILL_PARENT));
            ImageView img = new ImageView(FaceCaptureActivity.this); 
            img.setScaleType(ImageView.ScaleType.CENTER_INSIDE);
            img.setImageBitmap(bitmap);
            img.setLayoutParams(new LinearLayout.LayoutParams(
                                                LayoutParams.FILL_PARENT, 
                                                LayoutParams.WRAP_CONTENT));
            ll.addView(img);
            TextView scoreText = new TextView(FaceCaptureActivity.this);
            scoreText.setText(String.format("%s %.3f", 
                                            FaceCaptureActivity.this.getString(R.string.attractiveness_score),
                                            score));
            scoreText.setLayoutParams(new LinearLayout.LayoutParams(
                                                LayoutParams.FILL_PARENT,
                                                LayoutParams.WRAP_CONTENT));
            ll.addView(scoreText);
            removeDialog(DIALOG_ANALYSING_ATTRACTIVENESS_ID);
            setContentView(ll);
            Log.d(TAG, "Post exectutsed");
        } // onPostExecute
    } // CropAndScaleBitmap

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data)
    {
        super.onActivityResult(requestCode, resultCode, data);
        switch (requestCode)
        {
            case INTENT_PICTURE_TAKEN:
                if (resultCode == FaceCaptureActivity.RESULT_OK)
                {
                    Log.i(TAG, "Picture taken succesfully");
                    new InsertImageIntoMediaStore().execute(
                            new Pair<ContentResolver, Uri>(
                                getContentResolver(), mImageUri));
                } // if
                else
                {
                    Log.w(TAG, "Picture was not taken");
                } // else
        } // switch
    } // onActivityResult
  
    private static SimpleDateFormat mFormat = new SimpleDateFormat("yyyyMMdd_HHmmssZ");
    private static long mLastDate = 0L;
    private static int mSameSecondCount = 0;
    private static String getImageFileName()
    {
        // Number of names generated for the same second.
        Long dateTaken = System.currentTimeMillis();
        Date date = new Date(dateTaken);
        String result = "IMG" + mFormat.format(date);

        // If the last name was generated for the same second,
        // we append _1, _2, etc to the name.
        if (dateTaken / 1000 == mLastDate / 1000) 
        {
            mSameSecondCount++;
            result += "_" + mSameSecondCount;
        } // if
        else 
        {
            mLastDate = dateTaken;
            mSameSecondCount = 0;
        } // else
        return result + ".jpg";
    } // getImageFileName

    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        new EnsureDataFilesExistTask().execute(new File("/sd"));
    } // onCreate

    protected Dialog onCreateDialog(int id)
    {
        ProgressDialog dialog;
        switch(id)
        {
            case DIALOG_ENSURE_DATA_FILES_EXIST_ID:
                dialog = createBasicProgressDialog(R.string.ensure_data_file_exists);
                break;
            case DIALOG_LOAD_FACE_DETECTOR_ID:
                dialog = createBasicProgressDialog(R.string.load_face_detector);
                break;
            case DIALOG_FINDING_FACES_ID:
                dialog = createBasicProgressDialog(R.string.finding_faces);
                break;
            case DIALOG_ANALYSING_ATTRACTIVENESS_ID:
                dialog = createBasicProgressDialog(R.string.analyzing_attractiveness);
                break;
            default:
                dialog = null;
        } // switch
        return dialog;
    } // onCreateDialog

    private ProgressDialog createBasicProgressDialog(int stringId)
    {
        ProgressDialog dialog = new ProgressDialog(this);
        dialog.setCancelable(false);
        dialog.setIndeterminate(true);
        dialog.setMessage(getString(stringId));
        return dialog;
    }

    static native double runConv(String cnnFile, int[] data);

    static
    {
        System.loadLibrary("FaceCapture");
    } // static

} // class FaceCaptureActivity

