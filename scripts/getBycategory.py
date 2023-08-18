import requests
from bs4 import BeautifulSoup

import time

category_set = set()


def category_tracker(url, headers, name):
    """

    a simple function return links from html page
    """

    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        links = soup.find_all("a")

        with open(f"./files/{name}.txt", "w") as f:
            for link in links:
                data = link.get("href")
                text = link.text

                try:
                    if "/search" in data and "ft_movie" in data and text in data:
                        final_link = text + ":" + " https://www.imdb.com/" + data
                        f.write(final_link + "\n")

                except Exception as e:
                    raise e
    else:
        print("Request failed:", page.status_code)
