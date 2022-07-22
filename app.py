import requests
from bs4 import BeautifulSoup


dct = {}

def check(x):
    url = f'https://virtualsoccer.ru/viewmatch.php?day=20434&match_id={x}'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'accept': '*/*'
    }

    r = requests.get(url=url, headers=headers)
    with open('index.html', 'w', encoding='UTF-8') as f:
        f.write(r.text)

    with open('index.html', 'r', encoding='UTF-8') as f:
        src = f.read()

    soup = BeautifulSoup(src, 'lxml')
    corners = soup.find(text='Угловые').parent.parent.find_all('td')


    if corners[0].text not in dct.keys():
        dct[corners[0].text] = [url]
    else:
        dct[corners[0].text].append(url)


    if corners[-1].text not in dct.keys():
        dct[corners[-1].text] = [url]
    else:
        dct[corners[-1].text].append(url)

if __name__ == '__main__':
    x = 6121
    for i in range(x, x+100):
        print(f'Матч номер {i}')
        check(i)
    with open('res.txt', 'w', encoding='UTF-8') as f:
        for k, v in dct.items():
            f.write(f'{k} : {v}\n')
    # print(dct)
