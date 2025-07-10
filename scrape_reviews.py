
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import pandas as pd
import numpy as np



def get_reviews(id,driver):
    soup = BeautifulSoup(driver, "html.parser")

    review_card = soup.find_all("div",class_="ipc-list-card__content")
    reviews=[]
    for card in review_card:
        # print(card)
        rating = card.find("span", class_="ipc-rating-star--rating")
        title = card.find("h3", class_="ipc-title__text ipc-title__text--reduced")
        content = card.find("div", class_="ipc-html-content-inner-div")
        if rating:
            rating= rating.text
        if title:
            title = title.text
        if content:
            content = content.text
        reviews.append({"id":id,"title":title,"review_rating":rating,"review":content})
    return reviews

def scroll_click(id,driver):
    
    driver.get(f"https://www.imdb.com/title/{id}/reviews/?sort=featured%2Cdesc")

    # Wait for page to load
    time.sleep(2)
    # Optionally click a "Show More" button
    buttons = driver.find_elements(By.CLASS_NAME,"review-spoiler-button")

    # Loop through and click each one
    for idx, button in enumerate(buttons):
        try:
            # Scroll the button into view
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            time.sleep(1)

            # Wait until the button is clickable
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME,"review-spoiler-button"))
            )

            # Use ActionChains to click (more reliable)
            ActionChains(driver).move_to_element(button).click().perform()
            print(f"✅ Clicked button #{idx + 1}")

            time.sleep(0.5)  # delay between clicks

        except Exception as e:
            print(f"⚠️ Skipping button #{idx + 1} due to error: {e}")
    time.sleep(1)
    rev =get_reviews(id,driver.page_source)
    
    return rev

# let th scraping begin 🔥
ids =list(pd.read_csv("./data/imdb_list.csv")["id"])

driver = webdriver.Chrome()
imdb_review=[]
for i in range(len(ids)):
    print(f"Movie:{i}- {ids[i]}")
    if (i)%25==0:
        data = pd.DataFrame(imdb_review)
        data.to_csv("./data/imdb_reviews.csv",mode="a",index=False,header=False)
        imdb_review =[]
    imdb_review+=scroll_click(ids[i],driver)
driver.quit()


