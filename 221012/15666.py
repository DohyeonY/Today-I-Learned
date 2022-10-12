
from itertools import combinations_with_replacement
n , m = map(int, input().split())
stack = list(map(int, input().split()))
stack.sort()

ans = list(combinations_with_replacement(stack, m))
# print(ans)
ans = list(set(ans))
# print(ans)
ans.sort()
# print(ans)
# if m == 1:
#     for t in range(0, len(ans)):
#         s = list(ans[t])
#         # print(s)
#         print(s[0])
# else:
for t in range(0,len(ans)):
    s = list(ans[t])
    # s = ' '.join(s)
    # print(s)
    for u in range(0,len(s)-1):
        print(s[u],end=" ")
    print(s[len(s)-1])