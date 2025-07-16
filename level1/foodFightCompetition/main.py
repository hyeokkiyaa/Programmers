# My code

def solution(food):
        answer = []
            left = []
                for i in range(1, len(food)):
                            for j in range(0, food[i] // 2):
                                            left.append(i)
                                                right = left.copy()
                                                    right.reverse()
                                                        left.append(0)
                                                            left.extend(right)
                                                                answer = left
                                                                    return ''.join(map(str, answer))
