from fake_useragent import UserAgent
import time
from scripts.getLinks import link_tracker
from scripts.getBycategory import category_tracker

ua = UserAgent(browsers=["edge", "chrome"])


user__agent = ua.random


headers = {
    "User-Agent": user__agent,
}


dict = {
    "top_fav_url": "https://www.imdb.com/chart/top/?ref_=nv_mv_250",
    "Box_office_link": "https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht",
    "my_top_100": "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm",
}
for key in dict:
    link_tracker(dict[key], headers,key)
    time.sleep(5)
    print(" Item Succesfully tracked")


