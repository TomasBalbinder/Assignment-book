import openai
import urllib.request
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')
def openai_image():
    
    response = openai.Image.create(
    prompt="animal in the library , digital art, fairytale",
    n=1,
    size="512x512"
    )
    image_url = response['data'][0]['url']

    url = image_url

    download_image = urllib.request.urlretrieve(url, "ToDoProjectFolder\ToDoApp\static\ToDoApp\openai_image.png")

    return download_image




"""while True: 
    target_time = datetime.datetime.now().replace(hour=1, minute=2, second=55, microsecond=0)


    while datetime.datetime.now() < target_time:
        openai_image()
        time.sleep(10)
        """


