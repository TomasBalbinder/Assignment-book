import requests

def motivation_api(request):

    url = "https://quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com/quote"

    querystring = {"token":"ipworld.info"}

    headers = {
        "X-RapidAPI-Key": "b759e8af49msh997448b4abf5531p145c04jsn0fbbcd9d4ba8",
        "X-RapidAPI-Host": "quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response