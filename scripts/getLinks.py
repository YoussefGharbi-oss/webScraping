# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from bs4 import BeautifulSoup

import time

ref_list = [
    "chttp_i",
    "chtbo_i",
    "chtmvm_i",
]


def check_items_not_in_string(item_list, input_string):
    for item in item_list:
        if item in input_string:
            return False

    return True


def link_tracker(url, headers, name):
    """

    a simple function return links from html page
    """
    for _ in range(10):
        page = requests.get(url, headers=headers)

        if page.status_code == 200:
            soup = BeautifulSoup(page.text, "html.parser")
            links = soup.find_all("a")
          
            with open(f"./files/{name}.txt", "w") as f:
                for link in links:
                    data = link.get("href")
                    try:
                        if "/title" in data   and check_items_not_in_string(ref_list, data) != False :
                          
                            final_link = "https://m.imdb.com/" + data
                            f.write(final_link + "\n")

                    except Exception as e:
                        raise e
        else:
            print("Request failed:", page.status_code)


    
