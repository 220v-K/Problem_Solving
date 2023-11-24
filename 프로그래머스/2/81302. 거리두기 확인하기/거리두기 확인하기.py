def solution(places):
    answer = []

    dr1 = [1, -1, 0, 0]
    dc1 = [0, 0, 1, -1]

    dr2 = [1, 1, -1, -1]
    dc2 = [1, -1, 1, -1]

    dr3 = [2, -2, 0, 0]
    dc3 = [0, 0, 2, -2]

    for room in places:
        result = 1
        # 모든 칸에 대해
        for r, row in enumerate(room):
            for c, cell in enumerate(row):
                # 응시자가 아니면 패스
                if cell != "P":
                    continue

                # 응시자라면
                # 거리 1 체크
                for i in range(4):
                    nr = r + dr1[i]
                    nc = c + dc1[i]
                    if 0 <= nr < 5 and 0 <= nc < 5:
                        if room[nr][nc] == "P":
                            result = 0

                # 거리 2 체크 - (대각선)
                for i in range(4):
                    nr = r + dr2[i]
                    nc = c + dc2[i]
                    if 0 <= nr < 5 and 0 <= nc < 5:
                        if room[nr][nc] == "P":
                            # 거리 2인 사람이 존재한다면, 파티션 여부 체크
                            if room[r+dr2[i]][c] != "X" or room[r][c+dc2[i]] != "X":
                                result = 0

                # 거리 2 체크 - (직선)
                for i in range(4):
                    nr = r + dr3[i]
                    nc = c + dc3[i]
                    if 0 <= nr < 5 and 0 <= nc < 5:
                        if room[nr][nc] == "P":
                            # 거리 2인 사람이 존재한다면, 파티션 여부 체크
                            if room[r+dr1[i]][c+dc1[i]] != "X":
                                result = 0

        answer.append(result)
    return answer