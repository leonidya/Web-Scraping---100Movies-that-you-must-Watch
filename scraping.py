from bs4 import BeautifulSoup
import requests

responce = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = responce.text

soup = BeautifulSoup(content, "html.parser")
list_of_titles = soup.select("h3", class_="title")
list_of_titles = list_of_titles[::-1]

new_list = []
for title in list_of_titles:
    text = title.getText()
    print(type(text))
    new_list.append(text)
print(new_list)

with open ("new_file_titles.text", mode="w", encoding="utf-8") as file:
    for title in new_list:
        file.write(f"\n{title}")


