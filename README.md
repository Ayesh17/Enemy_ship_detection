# Enemy_ship_detection


This is for predictiong nearby vessel behavior using different deep learning models.

1) As the input we use the following data folders which we got from the ONR-UNR project
         1. HMM_train_data_preprocessed
         2. HMM_test_data

2) Step 01: data_preprocess_v1.py We load the dataset and select only files with atleast 200 frames and linit frame count to 200 and max 500 files per behavior. Output files will be placed in,
         1. Train_data
         2. Test_data
   
3) Step 02: Convert_dataset.py We read data from the 'Train_data' and 'Test_data' folders and convert data into pickle files. Output files will be placed in,
         1. data

4) Step 03: Read data from pickle files, train, test and evaluate data based on different Deep Learning models.
   
