import requests


def motivation_api(request):
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {
        "key1": "value",
        "key2": "value"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "b759e8af49msh997448b4abf5531p145c04jsn0fbbcd9d4ba8",
        "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response