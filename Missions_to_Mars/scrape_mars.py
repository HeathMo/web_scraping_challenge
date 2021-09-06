# Dependencies
import time
import json
from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
from flask import Flask, render_template
#from selenium import webdriver

#Mongo
#conn = 'mongodb://localhost:27017'
#client = pymongo.MongoClient(conn)

#db = client.mars_db
#collection = db.mars_db



def init_browswer():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

# Mars News Info
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    #time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_="content_title").get_text()
    news_snip = soup.find('div', class_="rollover_description_inner").get_text()

    # Featured Image
    feature_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(feature_image_url)
    response = browser.html
    jpl_soup = BeautifulSoup(response, 'html.parser')
    images = jpl_soup.find_all('a', class_="fancybox")
    img_src = []
    for image in images:
        img = image['data-fancybox-href']
        img_src.append(img)

    featured_image_url = "https://www.jpl.nasa.gov" + img_src[2]


    # Mars Facts
    mars_facts = "https://galaxyfacts-mars.com"
    mars_table = pd.read_html(mars_facts)
    df = mars_table[0]

    mars_facts_html = df.to_html()
    mars_facts_html = mars_facts_html.replace("\n", "")
    mars_facts_html

    # Mars Hemispheres
    hemisphere_image_urls = []

    # Cerberus
    cerb_url = "https://marshemispheres.com/cerberus.html"
    browser.visit(cerb_url)
    response_cerb = browser.html
    cerb_soup = BeautifulSoup(response_cerb, 'html.parser')
    cerb_img = cerb_soup.find_all('div', class_="wide-image-wrapper")

    for img in cerb_img:
        cerb_pic = img.find('li')
        cerb_full_img = img.find('a')['href']
    cerb_title = cerb_soup.find('h2', class_='title').get_text()
    cerb_hemi = {"Title": cerb_title, "url": cerb_full_img}

    hemisphere_image_urls.append(cerb_hemi)

    # Schiaparelli 
    schia_url = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(schia_url)
    response_schia = browser.html
    schia_soup = BeautifulSoup(response_schia, 'html.parser')
    schia_img = schia_soup.find_all('div', class_="wide-image-wrapper")

    for img in schia_img:
        schia_pic = img.find('li')
        schia_full_img = img.find('a')['href']
    schia_title = schia_soup.find('h2', class_='title').get_text()
    schia_hemi = {"Title": schia_title, "url": schia_full_img}

    hemisphere_image_urls.append(schia_hemi)

    # Syrtis
    syrtis_url = "https://marshemispheres.com/syrtis.html"
    browser.visit(syrtis_url)
    response_syrtis = browser.html
    syrtis_soup = BeautifulSoup(response_syrtis, 'html.parser')
    syrtis_img = syrtis_soup.find_all('div', class_="wide-image-wrapper")

    for img in syrtis_img:
        syrtis_pic = img.find('li')
        syrtis_full_img = img.find('a')['href']
    syrtis_title = syrtis_soup.find('h2', class_='title').get_text()
    syrtis_hemi = {"Title": syrtis_title, "url": syrtis_full_img}

    hemisphere_image_urls.append(syrtis_hemi)

    # Valles
    valles_url = "https://marshemispheres.com/valles.html"
    browser.visit(valles_url)
    response_valles = browser.html
    valles_soup = BeautifulSoup(response_valles, 'html.parser')
    valles_img = valles_soup.find_all('div', class_="wide-image-wrapper")

    for img in valles_img:
        valles_pic = img.find('li')
        valles_full_img = img.find('a')['href']
    valles_title = valles_soup.find('h2', class_='title').get_text()
    valles_hemi = {"Title": valles_title, "url": valles_full_img}

    hemisphere_image_urls.append(valles_hemi)

    mars_data = {
        'news_title': news_title,
        'news_p': news_snip,
        'featured_image_url': featured_image_url,
        'facts_table_html': mars_facts_html,
        'hemisphere_images_urls': hemisphere_image_urls
    }

    browser.quit()

    return mars_data
    
