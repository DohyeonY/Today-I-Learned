# 요청과 응답에 따른 데이터 수집
words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

w_lst = list(words_dict)
k_value = list(words_dict.values())
n_lst =[]

for i in w_lst :
    if i[0] in ('b', 'm', 'p') :
        n_lst.append(f'im{i}')
    elif i[0] == 'l':
        n_lst.append(f'il{i}')
    elif i[0] == 'r':
        n_lst.append(f'ir{i}')
    else :
        n_lst.append(f'in{i}')

print(sorted(n_lst))