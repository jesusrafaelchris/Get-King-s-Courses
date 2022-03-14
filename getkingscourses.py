
# importing the modules
import requests
from bs4 import BeautifulSoup

# target url
counter = 0
for i in range(0,9):
    url = 'https://www.kcl.ac.uk/search/courses?coursesPage=' + str(i) + '&level=undergraduate'

    # making requests instance
    reqs = requests.get(url)

    # using the BeaitifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')

    # displaying the title

    for title in soup.find_all('h3'):
        print(title.get_text())
        counter += 1
print(counter)
