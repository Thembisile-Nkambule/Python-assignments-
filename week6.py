import requests
import os
from urllib.parse import urlparse

def fetch_image(url, downloaded_files):
   
    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad HTTP status codes
        
        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"
        
        # Prevent duplicate filenames
        if filename in downloaded_files:
            print(f"⚠ Skipping duplicate image: {filename}")
            return
        downloaded_files.add(filename)
        
        # Save the image
        os.makedirs("Fetched_Images", exist_ok=True)
        filepath = os.path.join("Fetched_Images", filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get multiple URLs from user, separated by commas
    urls_input = input("Enter image URLs (separate multiple URLs with commas): ")
    urls = [url.strip() for url in urls_input.split(',') if url.strip()]
    
    # Keep track of already downloaded files
    downloaded_files = set()
    
    for url in urls:
        fetch_image(url, downloaded_files)
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
