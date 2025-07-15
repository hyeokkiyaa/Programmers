# My Code

def solution(s):
    answer = [-1] * len(s)
    
    for i in range(len(s)-1):
        count = 0
        for j in range(i+1, len(s)):
            count += 1
            if (s[i] == s[j]):
                answer[j] = count
                break
    return answer

# Somebody else code
def solution(s):
    answer = []
    dic = dict() # 1️⃣ 빈 딕셔너리 생성
    for i in range(len(s)):
        # 2️⃣ 현재 문자가 dic에 Key로 존재하는지 확인
        if s[i] not in dic: 
            answer.append(-1)
        else:
            # 4️⃣ 존재한다면, 현재 위치 - 저장된 위치
            answer.append(i - dic[s[i]])
        
        # 3️⃣ 현재 문자를 Key로, 현재 위치(i)를 Value로 저장 (또는 갱신)
        dic[s[i]] = i

    return answer
