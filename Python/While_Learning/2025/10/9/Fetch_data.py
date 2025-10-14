# fetch_data.py
import requests

def fetch_data(url):
    """Fetches data from the given URL using the requests library."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    url = "https://roadmap.sh/ai/course/python-basics-for-beginners" # replace with any URL
    data = fetch_data(url)
    if data:
        print("Data fetched successfully!")
        #print(data) # Uncomment to print the fetched data
    else:
        print("Failed to fetch data.")