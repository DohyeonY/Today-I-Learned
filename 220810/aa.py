# 우영우

while True:
    wyw = input()
    
    if wyw == "0":
        break
    
    results = "no"

    if wyw == wyw[::-1]:  # 처음부터 끝까지 -1칸 간격으로 ( == 역순으로)
        results = "yes"
    
    print(results)