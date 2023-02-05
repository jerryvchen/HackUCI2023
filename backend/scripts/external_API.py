import json
import urllib.parse
import urllib.request
import requests

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
        url = "https://api.github.com/search/repositories"

        querystring = {"q":"chess", "per_page":"100"}

        payload = ""
        headers = {"Authorization": "Bearer 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"}
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        # json_txt = response.read().decode(encoding='utf-8')

        # return json.loads(json_txt)
        return json.loads(response.text)
    
    finally:
        if response != None:
            response.close()


def get_3_most_used_language_github(query) -> dict:
    """This functions takes a query and returns the 3 most used 
    programming languages used on github for the query
    """
    data = get_result(build_search_github_url(query))
    repositories = data["items"]
    languages = {}
    for repository in repositories:
        language = repository["language"]
        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1
    languages = sorted(languages.items(), key=lambda languages: languages[1], reverse=True)

    top_3 = languages[:3]
    top_3_dict = dict()
    for i in range(0, 3): 
        top_3_dict[top_3[i][0]] = top_3[i][1]

    return top_3_dict

        

print(get_3_most_used_language_github("chess"))