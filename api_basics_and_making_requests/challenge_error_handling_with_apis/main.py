import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    # Write your code here
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cat_fact = data["fact"]  
        print(cat_fact)
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve cat fact.")
    except Exception:
        print("Failed to retrieve cat fact.")

get_cat_fact()
