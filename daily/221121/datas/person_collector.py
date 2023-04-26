import json
import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
from pprint import pprint

def find_code(st):
    buffer = ''
    for c in st[::-1]:
        if c == '=':
            break
        buffer += c
    return int(buffer[::-1])

BASE_URL='https://movie.naver.com/movie/bi/pi/basic.nhn?code='

actor_db, director_db = [], []
actor_book, director_book = {}, {} #중복 확인을 위한 딕셔너리
files = ['actor_list.json', 'staff_list.json']
for file_name in files:
    with open(file_name, 'rb') as fr:
        person_dic = json.load(fr)

    for name in person_dic:
        link = person_dic[name]
        code = find_code(link)

        # 크롤링
        url = BASE_URL + str(code)
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'lxml')

        # 이미지
        img_url = soup.find('div', 'poster').find('img')['src']

        # 설명(프로필에 있을 경우에만 저장)
        description = soup.find('div', 'con_tx')
        if description == None:
            description = '정보 없음'
        else:
            description = description.text

        person = {
            'pk': code,
            'model': 'movies.movier',
            'fields': {
                'name': name,
                'role': '',
                'img_url': img_url,
                'description': description,
            }
        }
        if file_name == 'actor_list.json':
            person['fields']['role'] = '배우'
            person['model'] = 'movies.actor'
            actor_book[code] = 1
            actor_db.append(person)
        else:
            person['fields']['role'] = '감독/각본/제작'
            person['model'] = 'movies.director'
            director_book[code] = 1
            director_db.append(person)

fr.close()

#####################################################################################

# movies.json을 순회하면서, 현재 movier db에 저장되지 않은 사람들을 추가해준다.
SEARCH_BASE_URL_QUERY = 'https://movie.naver.com/movie/search/result.nhn?query='
SEARCH_BASE_URL_OPTION = '&section=people&ie=utf8'


with open('movies.json', 'rb') as fr:
    movie_dic = json.load(fr)

for movie in movie_dic:
    directors = movie['fields']['director']
    actors = movie['fields']['actor']
    newbies = [directors, actors]

    # newbies = directors + actors # 0~len(directors)-1 | len(directors)~len(actors)-1
    # for idx, code in enumerate(newbies):
    for i in range(2):
        for code in newbies[i]:
            target_set = {}
            #directors
            if i == 0:
                target_set = director_book
            #actors
            else:
                target_set = actor_book

            if code not in target_set:
                url = BASE_URL + str(code)
                html = urllib.request.urlopen(url)
                soup = BeautifulSoup(html, 'lxml')

                # 이미지
                target = soup.find('div', 'poster')
                if target == None:
                    img_url = '정보 없음'
                else:
                    img_url = target.find('img')['src']

                # 설명(프로필에 있을 경우에만 저장)
                description = soup.find('div', 'con_tx')
                if description == None:
                    description = '정보 없음'
                else:
                    description = description.text

                # 이름
                name = soup.find('h3', 'h_movie').find('a').text   
                
                person = {
                    'pk': code,
                    'model': 'movies.movier',
                    'fields': {
                        'name': name,
                        'role': '',
                        'img_url': img_url,
                        'description': description,
                    }
                }     
                if i == 0:
                    person['fields']['role'] = '감독/각본/제작'
                    person['model'] = 'movies.director'
                    director_book[code] = 1
                    director_db.append(person)
                else:
                    person['fields']['role'] = '배우'
                    person['model'] = 'movies.actor'
                    actor_book[code] = 1
                    actor_db.append(person)

fr.close()

with open('directors.json', 'w', encoding='UTF-8') as fp:
    json.dump(director_db, fp, ensure_ascii=False, indent=4)
fp.close()
with open('actors.json', 'w', encoding='UTF-8') as fp:
    json.dump(actor_db, fp, ensure_ascii=False, indent=4)
fp.close()