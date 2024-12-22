# Olapic/Social Native CHURN File Image Downloader

This Python script automates the process of downloading images referenced in a CHURN file exported from Olapic or Social Native. It simplifies the workflow during the churning process by downloading images based on the URLs in the CSV files.

## Features
- Recursively scans subfolders within a specified main folder for CSV files.
- Extracts image URLs from a user-defined column in each CSV file.
- Downloads images into a `downloaded images` folder within the same subfolder as the CSV file.

## Requirements
- **Python**: Version 3.6 or later.
- **Libraries**: Install the required Python packages:
  ```bash
  pip install requests pandas
  ```

## How to Use
### Step 1: Clone the Repository
Clone the repository containing the script to your local machine:
```bash
git clone https://github.com/yourusername/image-downloader.git
cd image-downloader
```

### Step 2: Prepare Your Data
1. Ensure your main folder contains subfolders with CSV files exported from Olapic or Social Native.
2. Verify that the CSV files include a column with image URLs.

### Step 3: Run the Script
1. Open a terminal and navigate to the folder containing the script.
2. Execute the script:
   ```bash
   python download_images.py
   ```
3. Provide the following inputs when prompted:
   - **Path to the main folder**: The directory containing subfolders with CSV files.
   - **Column name**: The name of the column in the CSV files that contains the image URLs (e.g., `Original Media URL`).

### Step 4: Access the Downloaded Images
- The script creates a `downloaded images` folder inside each subfolder that contains a CSV file.
- Images are saved in this folder with sequential filenames like `image_1.jpg`, `image_2.jpg`, etc.

## Example
Suppose you have the following folder structure:
```
MainFolder/
    Subfolder1/
        file1.csv
    Subfolder2/
        file2.csv
```
After running the script, the structure will look like this:
```
MainFolder/
    Subfolder1/
        file1.csv
        downloaded images/
            image_1.jpg
            image_2.jpg
    Subfolder2/
        file2.csv
        downloaded images/
            image_1.jpg
            image_2.jpg
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

If you use this script, please reference the author:
- **Ralph Esposito**
- Website: [https://www.esposito.pro/](https://www.esposito.pro/)

---

### Contributing
Feel free to fork the repository and submit pull requests with improvements or bug fixes. Contributions are welcome!

