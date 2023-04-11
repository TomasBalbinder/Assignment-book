import openai
import urllib.request
import os
from dotenv import load_dotenv



load_dotenv()


def create_image():

    openai.api_key = os.environ.get('OPENAI_API_KEY')   
    response = openai.Image.create(
    prompt="animal in the library , digital art, fairytale",
    n=1,
    size="512x512"
    )
    url = response['data'][0]['url']

    #download_image = urllib.request.urlretrieve(url, "ToDoProjectFolder\ToDoApp\static\ToDoApp\openai_image.png")

    return url




