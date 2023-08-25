def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    nid = ''
    for value in new_id :
        if 97 <= ord(value) <= 122 or "0" <= value <= "9" or value == "-" or value == "_" or value == "." :
            nid += value

    flag = True
    new_id = ''
    for value in nid :
        if value == "." :
            if flag :
                new_id += value
                flag = False
        else:
            new_id += value
            flag = True

    if new_id :
        if new_id[0] == "." :
            if len(new_id) >= 2 :
                new_id = new_id[1:]
            else :
                new_id = ""
    if new_id :
        if new_id[-1] == "." :
            if len(new_id) >= 2 :
                new_id = new_id[:-1]
            else :
                new_id = ""

    if not new_id :
        new_id = "a"
 

    if len(new_id) >= 16 :
        new_id = new_id[:15]
        if new_id[-1] == "." :
            new_id = new_id[:-1]
 

    if len(new_id) <= 2 :
        while len(new_id) <= 2 :
            new_id += new_id[-1]
    return new_id
