set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

if [ "$CREATE_SUPERUSER" ]; then
  python manage.py createsuperuser --noinput
fi



python -c '
import threading
import datetime
import time
import openai_image

def my_background_task():
    while True: 
        target_time = datetime.datetime.now().replace(hour=13, minute=23, second=00, microsecond=0)


        while datetime.datetime.now() < target_time:
            openai_image()
            time.sleep(60)

threading.Thread(target=my_background_task).start()
' &