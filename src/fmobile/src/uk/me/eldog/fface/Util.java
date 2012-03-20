package uk.me.eldog.fface;

import android.app.ProgressDialog;
import android.app.Activity;

public final class Util
{
    private Util()
    {
    } // Util

    public static ProgressDialog createBasicProgressDialog(int stringId, 
                                                           Activity activity)
    {
        ProgressDialog dialog = new ProgressDialog(activity);
        dialog.setCancelable(false);
        dialog.setIndeterminate(true);
        dialog.setMessage(activity.getString(stringId));
        return dialog;
    } // createBasicProgressDialog

} // class Util
