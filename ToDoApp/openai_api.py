import openai
import urllib.request
import os
#from dotenv import load_dotenv
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

#load_dotenv()

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




def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(openai_image, 'interval', minutes=5)
    scheduler.start()
    print("Scheduler started")


if __name__ == '__main__':
    start()

"""while True: 
    target_time = datetime.datetime.now().replace(hour=1, minute=2, second=55, microsecond=0)


    while datetime.datetime.now() < target_time:
        openai_image()
        time.sleep(10)
        """


