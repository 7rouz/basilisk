# This code is inspired from the sample provided her
# http://selenium-python.readthedocs.io/getting-started.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_song(song_name):
    driver = webdriver.Firefox()
    driver.get("http://www.mp3juices.cc/")
    # make sure we are in the right site
    assert "MP3Juices" in driver.title
    # look for the search field
    elem = driver.find_element_by_name("input")
    elem.clear()
    elem.send_keys(song_name)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

if __name__ == "__main__":
    search_song("the greatest - sia")