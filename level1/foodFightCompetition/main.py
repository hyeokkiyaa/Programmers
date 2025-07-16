# My code

def solution(food):
    answer = []
    left = []
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            left.append(i)
    
    right = left.copy()
    right.reverse()
    
    answer.extend(left)
    answer.append(0)
    answer.extend(right)
    
    return ''.join(map(str, answer))

# Somebody else code

def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer


def solution(food):
    answer = ''
    rev=''
    for i in range(1,len(food)):
        answer+=str(i)*(food[i]//2)
    rev=answer[::-1] # Reverse
    answer+='0'

    return answer+rev

return food_str+ food_str[0:-1][::-1] # 자르고 reverse
