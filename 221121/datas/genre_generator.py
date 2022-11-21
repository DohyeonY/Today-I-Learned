import json
gen_dir = []
gen_name = ['전체', '드라마', '판타지', '서부', '공포', '로맨스', '모험', '스릴러', '느와르', '컬트', '다큐멘터리', '코미디', '가족', '미스터리', '전쟁', '애니메이션', '범죄', '뮤지컬', 'SF', '액션', '무협', '에로', '서스펜스', '서사', '블랙코미디', '실험', '영화카툰', '영화음악', '영화패러디포스터']
for num in range(29):
    new_dic = {
        "pk": num,
        "model": "movies.genre",
        "fields": {
            "name": gen_name[num]
        }
    }
    gen_dir.append(new_dic)
with open('genre.json', 'w', encoding='UTF-8') as fp:
    json.dump(gen_dir, fp, ensure_ascii=False, indent=4)