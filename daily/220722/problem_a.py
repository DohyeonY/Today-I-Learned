# 1. id, title, poster_path, vote_average. overview, gemre_ids의 키를 추출하기
# 2. 그걸 딕셔너리화해서 출력
import json
from pprint import pprint


def movie_info(movie):
    pass
    d = {'genre ids' : movie.get('genre_ids'), 'id': movie.get('id'), 'title': movie.get('title'), 'overview' : movie.get('overview'), 'poster_path' : movie.get('poster_path'), 'title' : movie.get('title'), 'vote_average' : movie.get('vote_average')}
    return d
    
    # 여기에 코드를 작성합니다.    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
   
    movie_dict = json.load(movie_json)

    
    # t = movie_info(movie_dict)
    # print(t)
    pprint(movie_info(movie_dict))
