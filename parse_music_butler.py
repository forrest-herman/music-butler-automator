import re
import time
import datetime
from selenium.webdriver.common.by import By

from web_scraping import open_url_using_selenium
from utils import write_to_file, read_from_file

DATA_ID = 'p.dl0kLG6C8Jgola'


def get_latest_date(new_date):
    old_date_txt = read_from_file('latest_date.txt')
    if old_date_txt == '':
        old_date = None
    else:
        old_date = datetime.datetime.strptime(old_date_txt, '%Y-%m-%d')

    if (old_date is None) or (old_date < new_date):
        print("old", old_date, "new", new_date)
        new_date_txt = new_date.strftime('%Y-%m-%d')
        print(new_date_txt)
        write_to_file(new_date_txt, 'latest_date.txt')
        return True
    # file unchanged
    return False


def add_music_butler_feed_to_playlist(url, playlist_id=DATA_ID):
    # open the web page
    driver, html = open_url_using_selenium(url)

    # write_to_file(html, 'music_butler.html')

    add_buttons_XPATH = "//a[@data-toggle='modal'][@data-target[contains(.,'#social-share-modal')]]"
    close_button_XPATH = "//button[text()='Close'][@data-dismiss='modal']"
    add_to_playlist_button_XPATH = "//div[@class[contains(.,'add-to-apple-playlist')]]"
    playlist_XPATH = f"//div[@data-id='{playlist_id}']"
    dates_XPATH = "//p[text()[contains(.,'released on')]]"

    # get all the add buttons in a list
    add_btns = driver.find_elements(By.XPATH, add_buttons_XPATH)
    close_btns = driver.find_elements(By.XPATH, close_button_XPATH)
    playlist_btns = driver.find_elements(By.XPATH, add_to_playlist_button_XPATH)

    # get all the dates in a list
    release_dates = driver.find_elements(By.XPATH, dates_XPATH)

    # loop through all the albums
    for i, button in enumerate(add_btns):
        # get the date
        date_html = release_dates[i].get_attribute('innerHTML')
        regex_pattern = r'released\son\s([A-z]*)\.?\s(\d+),\s(\d+)'
        re_object = re.search(regex_pattern, date_html)

        month = get_month(re_object.group(1))
        day = int(re_object.group(2))
        year = int(re_object.group(3))
        release_date = datetime.datetime(year, month, day)

        if get_latest_date(release_date):
            # date is newer, add the song

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


# utils
def get_month(month_str):
    months = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    a = month_str.strip()[:3].lower()
    try:
        return months[a]
    except KeyError:
        raise ValueError('Not a month string')
