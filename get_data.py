import requests
import simplejson as json
from django.http import JsonResponse

username = 'kaleapi'
password = 'kaleapi'


def get():
    url = "http://94.158.52.249/Base/hs/info/stocks/"
    try:
        response = requests.get(url, auth=(username, password))
        response.raise_for_status()  # raise an exception for any HTTP error status code
        json_data = response.json()
        print(json_data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except json.JSONDecodeError as err:
        print(f"JSON decoding error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")


# get()

import requests


def my_view():
    # Define the API endpoint URL
    url = 'http://94.158.52.249/Base/hs/info/stocks/'

    # Define the authentication credentials
    auth = ('kaleapi', 'kaleapi')

    # Define any additional request parameters
    # params = {'param1': 'value1', 'param2': 'value2'}

    # Make the request to the API endpoint
    response = requests.get(url, auth=auth)

    # Process the API response as needed
    data = response.json()
    print(data)
    # # Return the response to the client
    # return JsonResponse(data)


my_view()
