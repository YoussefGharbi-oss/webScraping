import os
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import sys
import time

sys.path.append("/home/user-pc/webScraping/")
from typing import Dict

ua = UserAgent(browsers=["edge", "chrome"])
user_agent = ua.random

headers = {
    "User-Agent": user_agent,
}

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "files", "moviesBycategory.txt")
output_file_path = os.path.abspath("/home/user-pc/webScraping/files/category.txt")
based_url = "https://www.imdb.com/"
def remove_file(file_path):
 
    try:
        os.remove(file_path)
        print(f"File {file_path} removed successfully.")
    except OSError as e:
            print(f"Error removing the file: {e}")

def get_file_links(file_path) -> Dict:
    """
    The function `get_file_links` takes a file path and returns a dictionary of categories and URLs.
    :param file_path: The `file_path` parameter is the path to the file containing the categories and
    URLs.
    :return: a dictionary of categories and URLs.
    """
    try:
        categories_urls = {}
        with open(file_path, mode="r") as f:
            for line in f:
                category, url = line.split(": ")
                categories_urls[category] = url.strip()
        return categories_urls
    except FileNotFoundError as e:
        raise e
    


    """
    The function writes the href attribute of links that contain a specific category to a file.
    
    :param links: The "links" parameter is a list of HTML elements that contain the "href" attribute.
    These elements are typically obtained by parsing an HTML document using a library like BeautifulSoup
    :param category: The category parameter is a string that represents a specific category. It is used
    to filter the links and only write the ones that contain this category in the data
    :param file: The "file" parameter is the file object that you want to write the data to. It should
    be opened in write mode before passing it to the function. For example, you can open a file named
    "output.txt" in write mode like this:
    """
def write_on_file(links, category, file):
    for link in links:
        data = link.get("href")
        if category in data and "login" not in data :
            try:
                file.write(based_url + data + "\n")
                time.sleep(2)  # import time


            except Exception as e:
                print(f"Error writing data to file: {e}")
             


def get_category_link():
    """
    The function `get_category_link()` retrieves links from a given URL, categorizes them, and writes
    them to a file.
    """
    with open(output_file_path, mode="a") as f:
        category_dict = get_file_links(file_path)
        for category, url in category_dict.items():
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.text, "html.parser")
            links = soup.find_all("a")
            write_on_file(links, category, f)
            
            time.sleep(10)  


get_category_link()
remove_file(file_path)
