import requests
import bs4
counter = 0

url = f'https://hotlines.tel/en/branches/1654'
page = requests.get(url)

soup = bs4.BeautifulSoup(page.content, "html.parser")
branch = []
body = []


branch = soup.findAll('div', {'class': "branch-heading"})
body = soup.findAll('div', {'class': "branch-body px-2"})
for j in range(len(branch)):
        print(f'number of Branches is :({counter + 1})')
        counter += 1

        branch.append(print("Orange Branch :" + branch[j].text))
        body.append(print("Orange Branch Body :" + body[j].text))
        print()
