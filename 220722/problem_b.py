## 장르 아이디를 번호가 아닌 네임으로 나오게 하여라
import json
from pprint import pprint


def movie_info(movie, genres):
    pass 

    lst = []
    for i in movie.get('genre_ids') : # 18 80
        for j in genres : # 장르파일의 딕셔너리 키밸류 값들이 j에 
            if i == j.get('id') : # i에 있는 값이랑 j에 저장된 id키의 밸류랑 같으면
                lst.append(j.get('name')) # 리스트에 name을 넣는다
        
    d = {'genre names' : lst , 'id': movie.get('id'), 'title': movie.get('title'), 'overview' : movie.get('overview'), 'poster_path' : movie.get('poster_path'), 'title' : movie.get('title'), 'vote_average' : movie.get('vote_average')}
    return d
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
