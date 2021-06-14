import requests
import pyscreenshot
import threading
import os


def take_screenshot():
    image = pyscreenshot.grab()
    rgb_im = image.convert('RGB')
    rgb_im.save("image.jpg",optimization=9,quality=5)


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def main_function():
    take_screenshot()
    url = API_ENDPOINT
    my_img = {'image': open('image.jpg', 'rb')}
    r = requests.post(url, files=my_img, auth=(API_USERNAME, API_PASSWORD))
    os.remove("image.jpg")
    print(r.json)


set_interval(main_function, 10)
