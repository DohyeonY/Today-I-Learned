import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3/search/movie'
    # movie_id = .get('id')

    # URL = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
    
    params = {
        'api_key':'b38eab9e566911474038dee3caf82c37',
        'language':'ko',
        'region':'KR',
        'query' : title}

    response = requests.get(URL, params=params).json()
    
    try:
        results = response.get('results')
        movie_id = results[0].get('id')

        URL_rec = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'

        params_rec = {
            'api_key':'b38eab9e566911474038dee3caf82c37',
            'language':'ko',
            'region':'KR',
            'query' : title
            }

        response_rec = requests.get(URL_rec, params=params_rec).json()
        results_rec = response_rec['results']
        titles = []
        
        for i in results_rec:
            titles.append(i.get('title'))
    
    except: return None

    return titles


    # try :
        
    # except :
    #     None
    # pprint(response)
    # lst = []
    # i = []
    # for i in response.get('results') :
    #     print(i)

    #     if i['title'] == title :
    #         lst.append(i)
    #         if lst == [] :
    #             return []

    #         for k in lst :
                
    #             movie_id = k.get('id')

    #             a = response.get('results')
                
    #             c = []
    #             for b in a :
    #                 c.append(b.get('title'))
                    

    # return c

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
