import requests
query=input("Enter your topic you are interested in: ")
api_key="Enter your API key here"
url=f"https://newsapi.org/v2/everything?q={query}&from=2026-06-27&sortBy=publishedAt&apiKey={api_key}"

r=requests.get(url)
data=r.json()
print(url)
articles=data["articles"]
for index, article in enumerate(articles):
    print(f"{index + 1}. {article['title']}")
    print(article['description'])
    print(article['url'])
    print("\n****************************************\n")