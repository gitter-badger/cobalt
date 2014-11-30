import requests
import http.cookiejar
import time

class CourseFinder:
    """ Some sort of description
    - stuff
    """

    def __init__(self):
        pass

    def search(self, query='', requirements=''):
        """ Perform a UofT Course Finder search and return the data.
        """
        url = 'http://coursefinder.utoronto.ca/course-search/search/courseSearch/course/search'

        data = {
            'queryText': query,
            'requirements': requirements,
            'campusParam': 'St. George,Scarborough,Mississauga'
        }

        cookies = http.cookiejar.CookieJar()
        s = requests.Session()

        # Keep trying to get data until a proper response is given
        json = None
        while json is None:
            r = s.get(url, params=data, cookies=cookies)
            if r.status_code == 200:
                json = r.json()
            else:
                time.sleep(0.5)

        return json
