import pip._vendor.requests 

def get_languages(query):
    response = requests.get(f"https://api.github.com/search/repositories?q={query}")
    data = response.json()
    repositories = data["items"]
    languages = {}
    for repository in repositories:
        language = repository["language"]
        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1
    return languages

languages = get_languages("chatbot")
print(languages)