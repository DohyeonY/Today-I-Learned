def solution(id_list, report, k):
    froud_by = dict({key:[] for key in id_list})
    counts = dict({key:0 for key in id_list})
    idx_info = dict({key:i for i, key in enumerate(id_list)})
    answers = [0] * len(id_list)
    
    for val in report:
        src, dst = val.split()
        if dst in froud_by[src]:
            continue
        counts[dst] += 1
        froud_by[src].append(dst)
    
    for f, num in counts.items():
        if num >= k:
            for u_id, f_id in froud_by.items():
                if f in f_id:
                    answers[idx_info[u_id]] += 1

    return answers