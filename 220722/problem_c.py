## 1. 20개의 영화데이터에서 서비스 구성에 필요한 정보만 추출해 반환하는 함수를 완성하라
import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    d = []
    for k in movies :
    #여기에 코드를 작성합니다.  
        lst = []
        for i in k.get('genre_ids') : 
            for j in genres : # 장르파일의 딕셔너리 키밸류 값들이 j에 
                if i == j.get('id') : # i에 있는 값이랑 j에 저장된 id키의 밸류랑 같으면
                    lst.append(j.get('name')) # 리스트에 name을 넣는다
        d.append({'genre names' : lst , 'id': k.get('id'), 'title': k.get('title'), 'overview' : k.get('overview'), 'poster_path' : k.get('poster_path'), 'title' : k.get('title'), 'vote_average' : k.get('vote_average')})
    # d = {'genre names' : lst , 'id': k.get('id'), 'title': k.get('title'), 'overview' : k.get('overview'), 'poster_path' : k.get('poster_path'), 'title' : k.get('title'), 'vote_average' : k.get('vote_average')}
    return d     

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
