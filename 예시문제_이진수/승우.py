N = int(input())

answer = list()

def backtracking(N, prev, check):
    if N == 0:
        answer.append(prev)
        return
    if check:
        backtracking(N-1, prev+'0', False)
    else:
        backtracking(N-1, prev+'0', False)
        backtracking(N-1, prev+'1', True)
    
backtracking(N, '', False)
print(answer)