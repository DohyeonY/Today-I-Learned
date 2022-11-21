from bs4 import BeautifulSoup
import urllib.request
from pprint import pprint
from datetime import date, timedelta
import json

def make_str(st):
    new_st = ''
    for s in st:
        if s == '-':
            continue
        else:
            new_st += s
    return new_st
 
today = date.today()
tg_list = [1,2]
for tg in tg_list:
    db = {}
    for _ in range(365):
        target_date = str(today)
        target_date = make_str(target_date)

        url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn?tg={}&date={}'.format(tg, target_date)
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        titles = soup.find_all('td', 'title')
        for title in titles:
            name = title.find('a').text
            link = title.find('a')['href']
            if name not in db:
                db[name] = link
                # print("adding:", name)

        today -= timedelta(days=7)


    
    if tg == 1:
        file_name = 'actor_list.json'
    elif tg == 2:
        file_name = 'staff_list.json'
    with open(file_name, 'w', encoding='UTF-8') as fp:
        json.dump(db, fp, ensure_ascii=False, indent=4)


# print(str(rank_dir))
# pprint(rank_dir)
# test = json.loads(str(rank_dir))
# pprint(test)

# with open('genre_ranking.json', 'w', encoding='UTF-8-sig') as fp:
#     json.dump(rank_dir, fp, ensure_ascii=False, indent=4)