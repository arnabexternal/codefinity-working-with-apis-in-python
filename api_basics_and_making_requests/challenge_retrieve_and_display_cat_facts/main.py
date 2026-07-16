import requests

def print_three_cat_facts():
    # Your code goes here
    try:
        for i in range(0,3):
            response = requests.get("https://catfact.ninja/fact")
            data = response.json()
            cat_fact = data["fact"]  
            print(cat_fact)
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
    except KeyError:
        print("The 'fact' field is missing in the response.")
    except ValueError:
        print("Failed to decode JSON from the response.")
    

print_three_cat_facts()
