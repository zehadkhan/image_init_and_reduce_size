import os
import requests
import csv
from urllib.parse import urlparse

def download_images_from_csv(csv_file, download_folder='downloaded_images'):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            url = row[0]
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    parsed_url = urlparse(url)
                    filename = os.path.basename(parsed_url.path)
                    with open(os.path.join(download_folder, filename), 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded: {filename}")
                else:
                    print(f"Failed to download: {url} - Status code: {response.status_code}")
            except Exception as e:
                print(f"Error downloading {url}: {str(e)}")

if __name__ == "__main__":
    csv_file = 'image_urls.csv'  # csv URLs
    download_images_from_csv(csv_file)