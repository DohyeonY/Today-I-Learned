## 1. revenue가 가장 높은 영화의 제목을 출력하라
import json


def max_revenue(movies):
    pass 
    max_value = 0
    title = ''
    # 여기에 코드를 작성합니다.  
    for i in movies :
        # for j in i.get('id') 
        mov = open(f'data/movies/{i.get("id")}.json', encoding='utf-8')
        movlst = json.load(mov)
            # for k in .get('revenue')
        movlst.get('revenue')
        # print(movlst.get('revenue'))
        if movlst.get('revenue') > max_value :
            max_value = movlst.get('revenue')
            title = movlst.get('title')
    return title
    print(title)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

