스택의 특성

3-1.
스택은 나무 막대기에 원판을 하나씩 끼워놓는 것과 같이 후입선출의 방식이다.
스택에 pop을 해도 실제로 데이터가 사라지는건 아니고 쓰레기 데이터로 남아있다 top의 값만 낮아지는것 뿐이다.
스택의 후입선출 방식덕분에 가장 최근에 push한 데이터와 그 이전 데이터를 확인하는데 용이하다.



3-2.
먼저 A가 저장되고 그 뒤로 B가 저장됩니다. pop을 하여서 가장 나중에 들어간 B가 삭제되고 다시 차례대로 D, C, F, E순으로 입력됩니다.
현재 스택에 저장된 원소는 A, D, C, F, E입니다. 그리고 다시 한 번 pop을 진행하여 마지막에 들어간 E가 빠지게 되고 그 자리에 A가 들어가
최종으론 A, D, C, F, A의 형태가 됩니다