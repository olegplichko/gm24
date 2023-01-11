import os
from datetime import datetime
import tweepy
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

load_dotenv()

parent_directory = os.path.dirname(os.path.abspath(__file__))

FOREGROUND_COLOR = "#000000"
BACKGROUND_COLOR = "#FFFFFF"
FONT = ImageFont.load_default()


def get_twitter_api():
    auth = tweepy.OAuthHandler(
        os.getenv("API_KEY"), os.getenv("API_SECRET"))
    auth.set_access_token(
        os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    return tweepy.API(auth)


def draw_header(image, text_image):
    header = Image.new('RGB', (1500, 500), color=BACKGROUND_COLOR)
    header.paste(image)
    header.paste(text_image, (0,0), text_image)
    d = ImageDraw.Draw(header)
    d.rectangle((30, 30, 200, 60), None, FOREGROUND_COLOR, 5)
    current_time_text = "My current time is: {}".format(datetime.now().strftime("%H:%M"))
    d.text(
        (40, 40), current_time_text,
        font=FONT, fill=FOREGROUND_COLOR, anchor="mm"
    )

    header.save(os.path.join(parent_directory, "header.png"))


if __name__ == '__main__':
    api = get_twitter_api()
    image = Image.open('image.jpeg')
    text_image = Image.open('followme.png')
    draw_header(image, text_image)
    image.close()
    text_image.close()

