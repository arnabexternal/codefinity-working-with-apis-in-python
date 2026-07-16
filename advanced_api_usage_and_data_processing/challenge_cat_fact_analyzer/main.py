import requests

def count_cat_facts_with_cat():
    url = "https://catfact.ninja/facts?limit=10"
    response = requests.get(url)
    data = response.json()
    facts = data["data"]
    count = 0
    # your code here
    for items in facts:
        value = items.get("fact", "").lower()
        if 'cat' in value:
            count += 1
    print(count)

count_cat_facts_with_cat()
