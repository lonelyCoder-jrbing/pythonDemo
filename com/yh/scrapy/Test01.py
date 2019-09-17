import requests

import os, sys, time

import bs4

url = 'https://xkcd.com'

os.makedirs('xkcd', exist_ok=True)

# re = requests.get('https://xkcd.com')

# status = re.status_code()

# while not url.endswith('#'):
#     print('downing the %s...' % url)

re = requests.get('https://xkcd.com')

re.raise_for_status()

soup = bs4.BeautifulSoup(re.text)

comicElen = soup.select('#comic img')

print(type(comicElen))

# print(comicElen)

if comicElen == []:

    print('not find pic')

else:

    # print('2')

    comicUrl = comicElen[0].get('src')

    comicUrl = 'https:' + comicUrl

    print('downing image %s ' % (comicUrl))

    re = requests.get(comicUrl)

    re.raise_for_status()

# print('1')

imageFile = open(os.path.join('xkcd' + os.path.basename(comicUrl)), 'wb')

for chunk in re.iter_content(100000):
    imageFile.write(chunk)

imageFile.close()

prevlink = soup.select('a[rel="prev"]')[0]

url = 'https://xkcd.com' + prevlink.get('href')

print('done!')
