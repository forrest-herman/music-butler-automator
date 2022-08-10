import time
from selenium.webdriver.common.by import By

from web_scraping import open_url_using_selenium
# from utils import write_to_file

DATA_ID = 'p.dl0kLG6C8Jgola'


def add_music_butler_feed_to_playlist(url, playlist_id=DATA_ID):
    # open the web page
    driver, html = open_url_using_selenium(url)

    # write_to_file(html, 'music_butler.html')

    add_buttons_XPATH = "//a[@data-toggle='modal'][@data-target[contains(.,'#social-share-modal')]]"
    close_button_XPATH = "//button[text()='Close'][@data-dismiss='modal']"
    add_to_playlist_button_XPATH = "//div[@class[contains(.,'add-to-apple-playlist')]]"
    playlist_XPATH = f"//div[@data-id='{playlist_id}']"

    # get all the add buttons in a list
    add_btns = driver.find_elements(By.XPATH, add_buttons_XPATH)
    close_btns = driver.find_elements(By.XPATH, close_button_XPATH)
    playlist_btns = driver.find_elements(By.XPATH, add_to_playlist_button_XPATH)

    print(add_btns)

    # loop through all the albums
    for i, button in enumerate(add_btns):
        if i > 2:
            break

        # open the share modal
        button.click()
        time.sleep(1)

        # open the playlist selector
        playlist_btns[i].click()
        time.sleep(2)

        # click the In Testing playlist
        driver.find_element(By.XPATH, playlist_XPATH).click()
        time.sleep(1)

        # close the share modal
        close_btns[i].click()
        time.sleep(1)

    driver.quit()
