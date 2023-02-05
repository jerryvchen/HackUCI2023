import json
import urllib.parse
import urllib.request

GOOGLE_API_KEY = 'AIzaSyBAaXTy6FFFcGRfSS1CJiI8sXYyTOshAkE'

BASE_GITHUB_URL = 'https://api.github.com/'
BASE_YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3'



def build_search_github_url(query: str, max_results=100) -> str:
    """This function takes in a query parameter and maximum number of results
    to display to build a URL that can be used to ask the GitHub data API. 
    """

    query_params = [
        ('q', query), ('per_page', str(max_results))
    ]

    return f'{BASE_GITHUB_URL}search/repositories?{urllib.parse.urlencode(query_params)}'


def build_search_youtube_url(query: str, max_results=50) -> str:
    """This function takes in a query parameter and maximum number of results
    to display to build a URL that can be used to ask the YT data API. 
    """

    query_params = [
        ('key', GOOGLE_API_KEY), ('part', 'snippet'), 
        ('type', 'video'), ('maxResults', str(max_results)),
        ('q', query)
    ]

    return f'{BASE_YOUTUBE_URL}/search?{urllib.parse.urlencode(query_params)}'


def get_result(url: str) -> dict:
    """This function takes a URL and returns a dict of the parsed
    JSON returned. 
    """

    response = None

    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        json_txt = response.read().decode(encoding='utf-8')

        return json.loads(json_txt)
    
    finally:
        if response != None:
            response.close()


def get_3_most_used_language_github(query) -> list:
    data = get_result(build_search_github_url(query))
    repositories = data["items"]
    languages = {}
    for repository in repositories:
        language = repository["language"]
        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1
    sorted(repositories, key=repositories.get, reverse=True)
    return repositories[:3]
