import csv
import os
import glob

print()
print("-------------------------------------------------------------------------------------------------")
print("Starting training data Preprocessing")
print("-------------------------------------------------------------------------------------------------")
print()

rootpath = os.getcwd()
print("root", rootpath)

# Preprocess Train data

# Read the input
input_folder = os.path.join(os.getcwd(), 'HMM_train_data')
output_folder = os.path.join(os.getcwd(), 'Train_data')

behavior_phase = 15  # 12-indexed

# List of sub-folder names
sub_folder_names = ['BENIGN', 'RAM', 'HERD']

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# To preprocess data and put preprocessed data into behavior folders
# Loop over each sub-folder name
for sub_folder_name in sub_folder_names:
    # Get the path of the current sub-folder
    subfolder_path = os.path.join(input_folder, sub_folder_name)

    for subdir in os.listdir(subfolder_path):
        subdir_path = os.path.join(subfolder_path, subdir)
        sub_folder_path = os.path.join(input_folder, subdir_path)
        print("sub", sub_folder_path)
        # Get the list of all the csv files in the sub-folder that end with "output"
        csv_files = glob.glob(os.path.join(sub_folder_path, '*.csv'))
        csv_files = [f for f in csv_files if f.endswith('hmm_formatted.csv')]
        print("csv_files", csv_files)

        for csv_file_path in csv_files:
            with open(csv_file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                print(csv_file_path)

                # Create the output file
                output_file_path = os.path.join(output_folder, os.path.basename(csv_file_path))
                with open(output_file_path, 'w', newline='') as out_file:
                    csv_writer = csv.writer(out_file)

                    for row in csv_reader:
                        if row[behavior_phase] == '1':
                            row[behavior_phase] = '0'
                        elif row[behavior_phase] == '6':
                            row[behavior_phase] = '1'
                        elif row[behavior_phase] == '7':
                            row[behavior_phase] = '2'

                        behavior_label = row.pop(behavior_phase)  # Remove behavior_label from the row
                        row.append(behavior_label)  # Append behavior_label to the end of the row

                        csv_writer.writerow(row)

                # Check if the output csv file is empty, delete it if it is
                if os.path.getsize(output_file_path) == 0:
                    os.remove(output_file_path)

print()
print("-------------------------------------------------------------------------------------------------")
print("Starting testing data Preprocessing")
print("-------------------------------------------------------------------------------------------------")
print()

# Preprocess Test data

# Read the input
input_folder = os.path.join(os.getcwd(), 'HMM_test_data')
output_folder = os.path.join(os.getcwd(), 'Test_data')

behavior_phase = 15  # 12-indexed

# List of sub-folder names
sub_folder_names = ['BENIGN', 'RAM', 'HERD']

# To preprocess data and put preprocessed data into behavior folders
# Loop over each sub-folder name
for sub_folder_name in sub_folder_names:
    # Get the path of the current sub-folder
    subfolder_path = os.path.join(input_folder, sub_folder_name)
    output_folder_path = os.path.join(output_folder, sub_folder_name)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    for subdir in os.listdir(subfolder_path):
        subdir_path = os.path.join(subfolder_path, subdir)
        sub_folder_path = os.path.join(input_folder, subdir_path)
        print("sub", sub_folder_path)
        # Get the list of all the csv files in the sub-folder that end with "output"
        csv_files = glob.glob(os.path.join(sub_folder_path, '*.csv'))
        csv_files = [f for f in csv_files if f.endswith('hmm_formatted.csv')]
        print("csv_files", csv_files)

        for csv_file_path in csv_files:
            with open(csv_file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                print(csv_file_path)

                # Create the output file
                print("out", output_folder)
                output_file_path = os.path.join(output_folder_path, os.path.basename(csv_file_path))
                print("output_file_path", output_file_path)
                with open(output_file_path, 'w', newline='') as out_file:
                    csv_writer = csv.writer(out_file)

                    for row in csv_reader:
                        if row[behavior_phase] == '1':
                            row[behavior_phase] = '0'
                        elif row[behavior_phase] == '6':
                            row[behavior_phase] = '1'
                        elif row[behavior_phase] == '7':
                            row[behavior_phase] = '2'

                        behavior_label = row.pop(behavior_phase)  # Remove behavior_label from the row
                        row.append(behavior_label)  # Append behavior_label to the end of the row

                        csv_writer.writerow(row)

                # Check if the output csv file is empty, delete it if it is
                if os.path.getsize(output_file_path) == 0:
                    os.remove(output_file_path)
