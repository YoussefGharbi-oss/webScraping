from fake_useragent import UserAgent
from scripts.getBycategory import category_tracker

ua = UserAgent(browsers=["edge", "chrome"])


user__agent = ua.random


headers = {
    "User-Agent": user__agent,
}

def get_links_by_category():
    """
    Purpose: one
    """
    category_url = "https://www.imdb.com/feature/genre/?ref_=nv_ch_gr"
    category_tracker(category_url,headers,'moviesBycategory')
