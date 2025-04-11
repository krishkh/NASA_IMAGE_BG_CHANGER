'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''
import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.environ.get("API_KEY")  # This right here is our API key

def main():
    # TODO: Add code to test the functions in this module
    print(get_apod_info('2022-01-01'))
    return

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
    # TODO: Complete the function body
    # Hint: The APOD API uses query string parameters: https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
    # Hint: Set the 'thumbs' parameter to True so the info returned for video APODs will include URL of the video thumbnail image 
    # print("apod data is", apod_date, type(apod_date))
    params = {
        'api_key': API_KEY,
        'date': str(apod_date),
        'thumbs': True
    }
    
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=params)
    if response.status_code == 400:
        return response.status_code
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    # TODO: Complete the function body
    # Hint: The APOD info dictionary includes a key named 'media_type' that indicates whether the APOD is an image or video
    if apod_info_dict['media_type'] == 'image':
        return apod_info_dict['hdurl']
    else:
        return apod_info_dict['thumbnail_url']

if __name__ == '__main__':
    main()