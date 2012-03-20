package uk.me.eldog.fface;

import java.io.File;
import java.io.IOException;
import java.util.List;

import android.content.Context;
import android.graphics.Bitmap;
import android.os.AsyncTask;
import android.os.Environment;
import android.util.Log;
import android.view.SurfaceHolder;

class FaceCaptureView extends FaceCaptureViewBase
{
    private static final String TAG = FaceCaptureView.class.getSimpleName();
    private boolean mInitialized = false;
    private long mCnnPointer;
    private long NULL_POINTER = 0L;
    private FaceCaptureActivity mFaceCaptureActivity;

    private class InitializeFaceDetectorTask 
            extends AsyncTask<Void, Void, Long>
    {
        protected void onPreExecute()
        {
            mFaceCaptureActivity.showDialog(
                    FaceCaptureActivity.DIALOG_LOAD_FACE_DETECTOR_ID);
        } // onPreExecute

        // Set up the face detector
        protected Long doInBackground(Void... params)
        {
            if (Environment.MEDIA_MOUNTED.equals(
                        Environment.getExternalStorageState()))
            {
                File externalStorageDir 
                    = new File(Environment.getExternalStorageDirectory(),
                               FaceCaptureActivity.EXTERNAL_STORAGE_DIR);
                File cascadeFile = new File(externalStorageDir,
                                            FaceCaptureActivity.CASCADE_FILE);
                String cascadeFileName = cascadeFile.toString();
                File cnnFile = new File(externalStorageDir,
                                        FaceCaptureActivity.CNN_FILE);
                String cnnFileName = cnnFile.toString();

                Log.d(TAG, "Loading face detector");
                long cptr = loadFaceDetector(cascadeFileName, cnnFileName);

                return cptr;
            } // if
            else
            {
                Log.e(TAG, "Unable to mount external storage");
                return 0L;
            } // else
        } // doInBackground

        protected void onProgressUpdate(Void... params)
        {
            // not much to update
        } // onProgressUpdate

        protected void onPostExecute(Long cptr)
        {
            mFaceCaptureActivity.removeDialog(FaceCaptureActivity.DIALOG_LOAD_FACE_DETECTOR_ID);
            if (cptr != NULL_POINTER)
            {
                Log.d(TAG, "Face detector loaded");
                mInitialized = true;
                mCnnPointer = cptr;
            } // if
            else
            {
                Log.e(TAG, "Unable to load face detector");
            } // else
        } // onPostExecute;

    } // InitializeFaceDetectorTask

    public FaceCaptureView(Context context)
    {
        super(context);
        mFaceCaptureActivity = (FaceCaptureActivity) context;
        new InitializeFaceDetectorTask().execute();
    } // FaceCaptureView

    @Override
    protected Bitmap processFrame(byte[] data)
    {
        Bitmap bmp = Bitmap.createBitmap(getFrameWidth(), 
                                         getFrameHeight(),
                                         Bitmap.Config.ARGB_8888);
        if (mInitialized)
        {
            Log.d(TAG, "finding faces");
            int[] rgba = new int[getFrameWidth() * getFrameHeight()];
            findFaces(mCnnPointer, getFrameWidth(), getFrameHeight(), data, rgba);
            Log.d(TAG, "found faces");
            bmp.setPixels(rgba, 
                          0 /* offset */,
                          getFrameWidth(),
                          0,
                          0,
                          getFrameWidth(),
                          getFrameHeight());
        } // if
        return bmp;
    } // processFrame

    @Override
    public void surfaceDestroyed(SurfaceHolder holder)
    {
        super.surfaceDestroyed(holder);

        if (mInitialized)
        {
            releaseFaceDetector(mCnnPointer);
        } // if
    } // release

    static native long loadFaceDetector(String cascadeFile, String cnnFile);
    static native long findFaces(long cnnPointer, int width, int height, byte[] yuv, int[] rgba);
    static native void releaseFaceDetector(long cnnPointer);

    static
    {
        System.loadLibrary("FaceCapture");
    }
} // class FaceCaptureView

