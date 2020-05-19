import os

CHROMEDRIVER = 'chromedriver'
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CHROMEDRIVER_PATH = '{}/bin/{}'.format(BASE_PATH, CHROMEDRIVER)

DEBUG = False
SOUNDCLOUD_LANDING_URL = "https://soundcloud.com/discover"
