from bs4 import BeautifulSoup
import urllib.request
from pprint import pprint
from datetime import datetime, timedelta
import json

def make_str(st):
    new_st = ''
    for s in st:
        if s == '-':
            continue
        else:
            new_st += s
    return new_st

# rank_dir = []
# movie_dir = dict()
# today = str(date.today())
# today = make_str(today)

check = []
db = []
today = datetime.today()
for _ in range(50):
    target_date = str(today)[:10]
    target_date = make_str(target_date)

    sel_list = ['cur', 'pnt']
    for sel in sel_list:
        url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel={}&date={}'.format(sel, target_date)
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        titles = soup.find_all('td', 'title')

        for title in titles:
            name = title.find('a').text
            if name not in check:
                info={}
                info['name'] = name
                info['link'] = title.find('a')['href']
                db.append(info)
                check.append(name)

        today -= timedelta(days=7)


with open('checker.json', 'w', encoding='UTF-8-sig') as fp:
    json.dump(db, fp, ensure_ascii=False, indent=4)


# print(str(rank_dir))
# pprint(rank_dir)
# test = json.loads(str(rank_dir))
# pprint(test)

# with open('genre_ranking.json', 'w', encoding='UTF-8-sig') as fp:
#     json.dump(rank_dir, fp, ensure_ascii=False, indent=4)