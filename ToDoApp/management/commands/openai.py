import openai
import urllib.request
from django.core.management.base import BaseCommand
import environ
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
     
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        response = openai.Image.create(
            prompt="animal in the library , digital art, fairytale",
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        url = image_url
        download_image = urllib.request.urlretrieve(url, "ToDoProjectFolder\ToDoApp\static\ToDoApp\openai_image.png")
        return download_image






