import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import urllib
import re

url = "https://www.tipico.com/us"
try:
    page = urllib.request.urlopen(url)
except:
    print("error")

soup = BeautifulSoup(page, 'html.parser')

# storing relevant information, waiting on Tipico account

