from urllib import response
import requests 


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    URL = 'https://api.themoviedb.org/3/movie/popular'
    
    params = {
        'api_key':'b38eab9e566911474038dee3caf82c37',
        'language':'ko',
        'region':'KR'}

    response = requests.get(URL, params=params).json()
    
    return len(response['results'])

0000000
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
