"""
Copyright (c) 2024 Ralph Esposito
Website: https://www.esposito.pro/

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

If you use this script, please reference the original author: Ralph Esposito (https://www.esposito.pro/).
"""

import os
import requests
import pandas as pd

# Function to download an image from a URL
def download_image(url, save_path):
    """
    Downloads an image from a given URL and saves it to the specified path.
    """
    try:
        response = requests.get(url, stream=True)  # Send a GET request to the URL
        if response.status_code == 200:  # Check if the request was successful
            with open(save_path, 'wb') as file:  # Open file in write-binary mode
                for chunk in response.iter_content(1024):  # Write the response in chunks
                    file.write(chunk)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url} - Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Main function to process all subfolders and download images
def process_folders_and_download_images(main_folder, url_column):
    """
    Processes all subfolders in the specified main folder, finds CSV files, extracts image URLs,
    and downloads the images to a 'downloaded images' folder within each subfolder.
    """
    # Iterate through all subfolders in the main folder
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.endswith(".csv"):  # Check if the file is a CSV
                # Full path to the CSV file
                sheet_path = os.path.join(root, file)

                # Output folder inside the subfolder
                output_folder = os.path.join(root, "downloaded images")

                # Load the CSV file into a DataFrame
                df = pd.read_csv(sheet_path)

                # Ensure output folder exists, create it if necessary
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                # Iterate through the URLs in the specified column and download the images
                for index, row in df.iterrows():
                    url = row[url_column]
                    if pd.notna(url):  # Check if the URL is not empty
                        # Construct the file name for the downloaded image
                        file_name = os.path.join(output_folder, f"image_{index + 1}.jpg")
                        download_image(url, file_name)  # Download the image

if __name__ == "__main__":
    """
    Entry point of the script. Prompts the user for the main folder path and the column name
    containing image URLs, and processes the folders to download images.
    """
    # Get the main folder path from the user
    main_folder = input("Enter the path to the main folder containing subfolders with CSV files: ").strip()
    main_folder = os.path.abspath(main_folder)  # Normalize and resolve full path

    # Get the column name containing image URLs from the user
    url_column = input("Enter the column name containing the image URLs: ").strip()

    # Process the folders and download the images
    process_folders_and_download_images(main_folder, url_column)
