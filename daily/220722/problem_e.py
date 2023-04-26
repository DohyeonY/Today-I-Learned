## 1. 무비폴더의 파일을 오픈해야함
## 2. 개봉일이 12월인 영화를 찾아 리스트를 출력

import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    dec = 0
    
    lst = []
    # 여기에 코드를 작성합니다.  
    for i in movies :
        mov = open(f'data/movies/{i.get("id")}.json', encoding='utf-8')
        movlst = json.load(mov)
        movlst.get('release_date')
        if movlst.get('release_date')[5:7] == '12' :
            dec = movlst.get('release_date')
            lst.append(movlst.get('title'))

    return lst
    print(lst)        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
