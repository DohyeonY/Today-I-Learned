# OOP의 다중 상속 예제 2
def hanoi(N, start, to, via):
    if N == 1:
        print(f"{start}번 기둥의 {N}번 원반을 {to}번 기둥에 옮깁니다.")
    else:
        hanoi(N-1, start, via, to)
        print(f"{start}번 기둥의 {N}번 원반을 {to}번 기둥에 옮깁니다.")
        hanoi(N-1, via, to, start)
        
        
hanoi(3, 'A', 'C', 'B')

# A번 기둥의 1번 원반을 B번 기둥에 옮긴다.    23  1  -
# A번 기둥의 2번 원반을 B번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# A번 기둥의 3번 원반을 C번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# B번 기둥의 2번 원반을 C번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 C번 기둥에 옮긴다.
