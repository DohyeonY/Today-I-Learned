# 2. .extend()와 .append()

x = ['a', 'b', 'c']
y = ['d', 'e']
x.append(y)
print('x : ', x)
x.extend(y)
print('x : ', x)


# list.append(x)는 리스트 끝에 x 1개를 그대로 넣습니다.

# list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣습니다.