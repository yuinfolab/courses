from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys



import time
import random

import pandas as pd

from tqdm import tqdm

import urllib

#%%



URL = 'https://www.instagram.com/'

browser = webdriver.Chrome('./chromedriver')

browser.get(URL)


#%%

#random delayer
def randdelay(a, b):
	time.sleep(random.uniform(a, b))


def nextScroll():
    dummy = browser.find_element_by_tag_name('a')
    dummy.send_keys(Keys.PAGE_DOWN)
    randdelay(1, 3)



#create set for images
image_set = set()

#instagram image scraper fn
def getImagesInsta():
    images = browser.find_elements_by_tag_name("img")
    for x in range(len(images)):
        image_set.add(images[x].get_attribute("src"))



#run script return src list
def runScript(trial):
    for x in tqdm(range(trial)):
        getImagesInsta()
        nextScroll()
    return print("Trial has complete!")

#%%
		


df_images = pd.read_csv('/home/debian/Desktop/webscrap/elonmuskphotos.csv', index_col="index")

#%%

def downloadToFolder(setofImages):
    imagesrc_list = list(setofImages)
    df_source_images = pd.DataFrame(imagesrc_list)
    for i in tqdm(range(len(df_source_images))):
			try:
        urllib.request.urlretrieve(df_source_images[0][i], '/home/debian/Desktop/webscrap/elonmusk/'+str(i)+'.jpg')
			except:
				pass
    return print("Download has completed successfully!")


#%%

	downloadToFolder(img_list)










