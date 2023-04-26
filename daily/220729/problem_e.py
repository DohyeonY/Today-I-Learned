from ctypes import cast
import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3/search/movie'
    # movie_id = .get('id')
    
    params = {
        'api_key':'b38eab9e566911474038dee3caf82c37',
        'language':'ko',
        'region':'KR',
        'query' : title
        }

    response = requests.get(URL, params=params).json()

    try :
        result = response.get('results')[0]
        movie_id = result.get('id')
        # print(movie_id)

        URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
        params = {
            'api_key':'b38eab9e566911474038dee3caf82c37',
            'language':'ko',
            'region':'KR',
            'query' : cast,
            }

        response_r = requests.get(URL, params=params).json()
        resul = response_r.get('cast')
        resul2 = response_r.get('crew')
        
        # print(resul)

        direc = []
        cul = []

        for i in resul : 
            # direc.append(i.get())
            if i.get('cast_id') < 10 :
                cul.append(i.get('name'))
        # print(cul)
            # elif i.get('known_for_department') == 'Directing' :
            #     direc.append(i.get('name'))
        for j in resul2 :
            if j.get('known_for_department') == 'Directing' :
                direc.append(j.get('name'))


    #     for i in resul :
    #         names.append(i.get('name'))
            
    except : return None
# {'cast' : cul,  'directing' : direc}
    return {'cast' : cul,  'directing' : direc}

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
