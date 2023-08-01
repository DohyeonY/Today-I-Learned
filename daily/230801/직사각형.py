def solution(sizes):

    sorted_sizes = []

    max_width = -1
    max_height = -1

    for size in sizes :
        n, m = size 

        if n >= m:
            sorted_sizes.append(size)

        else:
            sorted_sizes.append([m, n])

    for size in sorted_sizes:
        n, m = size 

        if max_width < n:
            max_width = n

        if max_height < m :
            max_height = m

    answer = max_width * max_height 

    return answer