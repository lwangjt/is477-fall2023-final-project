import requests
import os
import hashlib

# URLs for downloading files
url = "https://archive.ics.uci.edu/static/public/545/rice+cammeo+and+osmancik.zip"
csv_url = "https://drive.google.com/uc?export=download&id=1Mxn9gqtvI3SMS0XZohuS910c9RQgGUoP"

# File names
zip_filename = 'rice+cammeo+and+osmancik.zip'
csv_filename = 'Rice_Cammeo_Osmancik.csv'

# Check if the data directory exists. If not, create it.
data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Download the zip file
response = requests.get(url)
if response.status_code == 200:
    with open(os.path.join(data_dir, zip_filename), 'wb') as file:
        file.write(response.content)
    print("Zip file downloaded successfully")
else:
    print(f"Failed to download the zip file. Status code: {response.status_code}")

# Download the CSV file
response_csv = requests.get(csv_url)
if response_csv.status_code == 200:
    with open(os.path.join(data_dir, csv_filename), 'wb') as file:
        file.write(response_csv.content)
    print("CSV file downloaded successfully")
else:
    print(f"Failed to download the CSV file. Status code: {response_csv.status_code}")

# Compare hashes for integrity
rice_sha256 = 'fe94e42046b829de21b92b0ffb6a22774fde021328cae799faa802a14e8dbed9'
csv_sha256 = 'deda3f9399998b3af54ad24abf63947e020875cf16041301e425176e9f42e0bf'

def compare_hashes(file_path, expected_hash):
    with open(file_path, mode='rb') as file:
        data = file.read()
        sha256hash = hashlib.sha256(data).hexdigest()
        if expected_hash != sha256hash:
            print(f"The computed hash for {file_path} does not match the expected hash")
        else:
            print(f"The computed hash for {file_path} matches the expected hash")

# Compare hashes for integrity
compare_hashes(os.path.join(data_dir, zip_filename), rice_sha256)
compare_hashes(os.path.join(data_dir, csv_filename), csv_sha256)