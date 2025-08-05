import os
import random
import json
from rembg import remove, new_session
from PIL import Image

#Add Folder PATH containing all the images to be processed as dataset_folder
dataset_folder = ''
record_file = os.path.join(dataset_folder, '/processed_files.json')

#sample_size is number of random images to process.
sample_size = 100
output_path = os.path.join(dataset_folder, '/Edited')

#model_name is image remover trained model used
model_name = "birefnet-general"
rembg_session = new_session(model_name)

# Step 1: Load record of processed files
if os.path.exists(record_file):
    with open(record_file, 'r') as f:
        processed_files = set(json.load(f))
else:
    processed_files = set()

# Step 2: List all files in dataset
all_files = set(os.listdir(dataset_folder))

# Step 3: Exclude already processed files
remaining_files = list(all_files - processed_files)

# Step 4: Select random files to process
files_to_process = random.sample(remaining_files, min(sample_size, len(remaining_files)))

print(f"Found {len(remaining_files)} unprocessed files.")
print(f"Processing {len(files_to_process)} files...")

# Step 5: Process the selected files
for index, filename in enumerate(files_to_process):
    filepath = os.path.join(dataset_folder, filename)
    # Your processing code here
    ImageFile = Image.open(dataset_folder + filename)
    print(f"Processing file {index + 1}: {filename}")
    output = remove(ImageFile, session=rembg_session, alpha_matting=True, alpha_matting_foreground_threshold=270,
                    alpha_matting_background_threshold=20, alpha_matting_erode_size=11)
    output.save(output_path + filename[:-4] + ".png")

# Step 6: Update record
processed_files.update(files_to_process)
with open(record_file, 'w') as f:
    json.dump(list(processed_files), f)

print("Done!")
