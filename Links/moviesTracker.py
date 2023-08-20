from fake_useragent import UserAgent
import time
from scripts.getLinks import link_tracker
from scripts.getBycategory import category_tracker

ua = UserAgent(browsers=["edge", "chrome"])


user__agent = ua.random


headers = {
    "User-Agent": user__agent,
}


movies_url = {
    "top_fav_url": "https://www.imdb.com/chart/top/?ref_=nv_mv_250",
    "Box_office_link": "https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht",
    "my_top_100": "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm",
}
def get_movies():
    """
    Purpose: one
    """
    for key in movies_url:
        link_tracker(movies_url[key], headers,key)
        time.sleep(5)
        print(" Item Succesfully tracked")
    
# end def


