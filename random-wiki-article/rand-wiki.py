import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_ = "firstHeading").text
    print(f"{title} \n Do you want to view it? (Y/N)")

    ans = input("").lower()
    if ans.lower() == 'y':
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans.lower() == "n":
        print("Try again!")
        continue
    else:
        print("Wrong choice!")
        break
