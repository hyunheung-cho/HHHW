import requests
from bs4 import BeautifulSoup
import re

url = "https://unsplash.com/s/photos/food"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

img_urls = []
for img in soup.find_all("img", src=re.compile("https://images.unsplash.com/photo")):
    img_urls.append(img["src"])

with open("food_images.txt", "w") as f:
    for url in img_urls:
        f.write(url + "\n")
