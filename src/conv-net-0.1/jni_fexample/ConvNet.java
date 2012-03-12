class ConvNet 
{
    private native double runConv(String xmlFile, String imageFilePath);
    public static void main(String args[])
    {
        double result = new ConvNet().runConv(args[0], args[1]);
        System.out.println("The output of the cnn was " + result);
    } // main(String args[])
    static
    {
        System.loadLibrary("ConvNet");
    } // static
} // class ConvNet
