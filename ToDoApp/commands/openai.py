import openai
import urllib.request
from django.core.management.base import BaseCommand

class Openai(BaseCommand):


    def handle(self, *args, **options):
     
        openai.api_key = ("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")
        response = openai.Image.create(
            prompt="animal in the library , digital art, fairytale",
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        url = image_url
        download_image = urllib.request.urlretrieve(url, "ToDoProjectFolder\ToDoApp\static\ToDoApp\openai_image.png")
        self.stdout.write(self.style.SUCCESS('Obrázek byl úspěšně stažen.'))
        return download_image






