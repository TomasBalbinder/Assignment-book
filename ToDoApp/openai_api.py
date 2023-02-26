import openai
import urllib.request
import datetime,time


openai.api_key = ("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")

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





