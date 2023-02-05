import requests


# counts the instances of each language, prints the one with highest instances
def get_most_used_language(query):
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
    return max(languages, key=languages.get)

most_used_language = get_most_used_language("chatbot") #test code

print(f"The most used language is: {most_used_language}")
