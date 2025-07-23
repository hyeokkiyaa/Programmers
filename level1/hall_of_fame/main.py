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

# it is not that effecitive. 
# I have searched and this is what gemini has given 

import heapq

def solution(k, score):
    answer = []
    honor = [] # 명예의 전당을 힙으로 사용

    for s in score:
        # 힙의 크기가 아직 k가 아니라면, 점수를 그냥 추가
        if len(honor) < k:
            heapq.heappush(honor, s)
        # 힙의 크기가 k이고, 새 점수가 힙의 최솟값(명예의 전당 최하위)보다 높다면
        elif s > honor[0]:
            # 가장 작은 점수를 빼고, 새 점수를 추가
            heapq.heappushpop(honor, s)
        
        # 매일의 발표 점수는 현재 명예의 전당 중 최하위 점수(힙의 루트)
        answer.append(honor[0])
        
    return answer
