def solution(k, score):
    answer = []
    klist = []
    length = len(score)
    
    for no in score:
        if (not klist or (len(klist) < k)):
            klist.append(no)
            klist.sort(reverse=True)
            answer.append(klist[len(klist)-1])
        else:
            if (klist[k-1] < no):
                klist[k-1] = no
            klist.sort(reverse=True)
            answer.append(klist[k-1])
        
    return answer
