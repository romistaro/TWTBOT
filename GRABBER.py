from google_images_download import google_images_download
import os


def dayCount():
    f = open('/home/kamui/Documents/PROGRAMMING/TWTBOT/DAY COUNT.txt').read().splitlines()
    n = f[0]
    return n


def images(n, e):
    response = google_images_download.googleimagesdownload()
    absolute_image_paths = response.download(
        {"keywords": e, 
        "limit":10,
        "print_urls":False,
        "output_directory": '/home/kamui/Documents/PROGRAMMING/TWTBOT/downloads',
        "time": 'past-24-hours'
        }
    )

def newDay(n):
    f = open('/home/kamui/Documents/PROGRAMMING/TWTBOT/DAY COUNT.txt', 'w')
    n = int(n)
    f.write(str(n+1))
    f.close


















