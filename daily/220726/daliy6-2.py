# 크롤링을 통한 서비스 개발 예제2

grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

n_lst =dict(grain_lst)
# print(n_lst)
mx = max(n_lst.values())
# print(mx)
reserve_dict = dict(map(reversed, n_lst.items()))
# print(reserve_dict)

print(reserve_dict[mx])
