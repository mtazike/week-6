import requests
import pandas as pd

class Genius:
    def __init__(self, access_token):
        self.access_token = access_token

    # Exercise 2 
    def get_artist(self, search_term):
        headers = {'Authorization': f'Bearer {self.access_token}'}
        search_url = f"https://api.genius.com/search?q={search_term}"
        response = requests.get(search_url, headers=headers)
        json_data = response.json()
        artist_id = json_data["response"]["hits"][0]["result"]["primary_artist"]["id"]
        artist_url = f"https://api.genius.com/artists/{artist_id}"
        artist_response = requests.get(artist_url, headers=headers)
        artist_data = artist_response.json()
        return artist_data

    # Exercise 3 
    def get_artists(self, search_terms):
        results = []
        headers = {'Authorization': f'Bearer {self.access_token}'}

        for term in search_terms:
            print("Searching for:", term)

            search_url = f"https://api.genius.com/search?q={term}"
            response = requests.get(search_url, headers=headers)
            json_data = response.json()

            first_hit = json_data["response"]["hits"][0]["result"]["primary_artist"]
            artist_id = first_hit["id"]
            artist_name = first_hit["name"]

            artist_url = f"https://api.genius.com/artists/{artist_id}"
            artist_response = requests.get(artist_url, headers=headers)
            artist_data = artist_response.json()

            followers = artist_data["response"]["artist"].get("followers_count", None)

            results.append({
                "search_term": term,
                "artist_name": artist_name,
                "artist_id": artist_id,
                "followers_count": followers
            })

        df = pd.DataFrame(results)
        return df
