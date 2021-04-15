import os
import requests
from cachetools import cached, TTLCache


class CountryService:
    """This class provide country info"""

    # 3 hours cache
    cache = TTLCache(maxsize=100, ttl=10800)

    #method for getting country info by lat nat lng
    @cached(cache)
    def get_country_information(self, latitude, longitude):
        url = "https://api.geonames.org/countrysubdivisionjson"
        query_string = {"lat": latitude, "lng": longitude, "username": os.getenv("GEO_NAME_API_KEY")}
        geo_result = requests.request("GET", url, params=query_string)
        return geo_result.json()