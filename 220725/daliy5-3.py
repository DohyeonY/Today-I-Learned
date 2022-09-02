# 데일리 실습 과제 5-3 요청과 응답에 따른 데이터 수집

st = '@#~I NeVEr DrEamEd abouT SuCCeSs, i woRkEd foR iT.!>!'
restr = st.strip('@' '#' '~' '.' '!' '>')
restr1 = restr[1:].lower()
restr2 = restr[:1].upper()
print(restr2 + restr1)