import requests
import json
import time
import argparse
import logging

def get_itunes_album_art(album_name, artist_name, num_images=1, retries=5, backoff_factor=1):
    search_url = "https://itunes.apple.com/search"
    query = f"{album_name} {artist_name}"
    params = {
        "term": query,
        "media": "music",
        "entity": "album",
        "limit": num_images
    }
    
    for attempt in range(retries):
        try:
            response = requests.get(search_url, params=params)
            response.raise_for_status()
            search_results = response.json()
            
            image_urls = []
            for album in search_results.get("results", []):
                artwork_url = album.get("artworkUrl100")
                if artwork_url:
                    high_quality_url = artwork_url.replace("100x100bb.jpg", "{width}x{height}bb.jpg")
                    image_urls.append(high_quality_url)
            
            return image_urls[0] if image_urls else None
        except requests.RequestException as e:
            logging.error(f"Error fetching album art for query '{query}' on attempt {attempt + 1}: {e}")
            if response.status_code == 403:
                logging.warning(f"Rate limit reached. Retrying after {backoff_factor * (2 ** attempt)} seconds...")
                time.sleep(backoff_factor * (2 ** attempt))
            else:
                break

    return None

def update_album_artwork(input_file, initial_delay=1, retries=5, backoff_factor=1):
    logging.info(f"Loading albums from {input_file}")
    
    with open(input_file, 'r+') as file:
        albums = json.load(file)
    
        not_found = []
        for index, album in enumerate(albums):
            if "artwork_url" in album and album["artwork_url"]:
                continue  # Skip if artwork_url already exists
            
            album_name = album.get("name")
            artist_name = album.get("artist")
            if album_name and artist_name:
                logging.info(f"Searching for artwork for album: {album_name} by {artist_name}")
                artwork_url = get_itunes_album_art(album_name, artist_name, retries=retries, backoff_factor=backoff_factor)
                if artwork_url:
                    album["artwork_url"] = artwork_url
                    logging.info(f"Found artwork for album: {album_name} by {artist_name} - {artwork_url}")
                else:
                    not_found.append(f"{album_name} by {artist_name}")
                    logging.warning(f"No artwork found for album: {album_name} by {artist_name}")
            else:
                logging.warning(f"Album name or artist name is missing in entry: {album}")
            
            time.sleep(initial_delay)  # Respect rate limiting
            
            # Update the JSON file in-place
            file.seek(0)
            json.dump(albums, file, indent=4)
            file.truncate()
        
        if not_found:
            logging.info("Unable to find artwork for the following albums:")
            for name in not_found:
                logging.info(name)

def main():
    parser = argparse.ArgumentParser(description="Update JSON file with album artwork URLs from iTunes API.")
    parser.add_argument('input_file', type=str, help="Path to the input JSON file.")
    parser.add_argument('--initial_delay', type=float, default=1, help="Initial delay between API requests in seconds (default: 1 second).")
    parser.add_argument('--retries', type=int, default=5, help="Number of retries for failed requests (default: 5).")
    parser.add_argument('--backoff_factor', type=float, default=1, help="Backoff factor for exponential backoff (default: 1).")
    parser.add_argument('--log', type=str, default='update_album_artwork.log', help="Path to the log file (default: update_album_artwork.log).")
    
    args = parser.parse_args()
    
    logging.basicConfig(filename=args.log, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Started processing")
    
    try:
        update_album_artwork(args.input_file, args.initial_delay, args.retries, args.backoff_factor)
    except KeyboardInterrupt:
        logging.info("Script interrupted by user. Progress has been saved.")

    logging.info("Finished processing")

if __name__ == '__main__':
    main()
