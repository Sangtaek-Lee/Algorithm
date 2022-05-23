import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M, F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
taxi_position = list(map(int, input().split()))
person_position = [0] * M
goal_position = [0] * M
for i in range(M):
    temp = list(map(int, input().split()))
    person_position[i] = temp[0:2]
    goal_position[i] = temp[2:4]
    board[temp[0]-1][temp[1]-1] = 2
    board[temp[2]-1][temp[3]-1] = 3

# 출발지에서 목표까지 가는 거리 계산
def bfs(start, goal):
    global taxi_position, next_goal_idx
    rlt = 0
    sr, sc = taxi_position[0] - 1, taxi_position[1] - 1
    visited = [[0]*N for _ in range(N)]
    q = [[sr, sc]]
    visited[sr][sc] = 1
    while q:
        temp = q.pop(0)
        r, c = temp[0], temp[1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and board[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append([nr, nc])
                print(goal)
                #그중 행 번호가 가장 작은 승객을
                if goal == 2:
                    if board[nr][nc] == goal:          # 목표까지 가는 연료를 구하는걸로 바꾸자
                        rlt = visited[r][c]
                        taxi_position = [nr, nc]
                        print(rlt)
                        for i in range(M):
                            if [nr + 1, nc + 1] == person_position[i]:
                                next_goal_idx = i
                                print('next_goal',next_goal_idx)
                                print(goal_position[next_goal_idx])
                                break
                        print(next_goal_idx)
                        break
                else:
                    if [nr, nc] == goal:
                        rlt = visited[r][c]
                        taxi_position = [nr, nc]
                        break
        if rlt != 0:
            break
    print('return')
    return rlt


rlt = F
next_goal_idx = 0
for i in range(M):
    goal = 2
    fc_1 = bfs(taxi_position, goal)
    rlt = rlt - fc_1
    print(f'fc_1:{rlt}')
    if rlt <= 0:
        rlt = -1
        break
    print(f'taxi_position_2:{taxi_position}')
    print(next_goal_idx)
    goal_position[next_goal_idx] = [goal_position[next_goal_idx][0] - 1, goal_position[next_goal_idx][1] - 1]
    print(f'goal_position_2:{goal_position[next_goal_idx]}')
    fc_2 = bfs(taxi_position, goal_position[next_goal_idx])
    print(fc_2)
    rlt = rlt - fc_2
    print(f'fc_2:{fc_2}')
    print(f'rlt_2:{rlt}')
    if rlt <= 0:
        rlt = -1
        break
    rlt = rlt + fc_2 * 2
    print(f'i: {i}, rlt: {rlt}')

print(rlt)

