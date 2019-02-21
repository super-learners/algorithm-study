def main():
    [num_n, num_m] = [int(x) for x in input().strip().split(" ")]
    map = []
    for _ in range(num_n):
        map.append([int(x) for x in input().strip().split(" ")])
    answer = solve(map)
    print(answer)

def solve(map: 'list[list[int]]') -> int:
    virus_positions = []
    for rn, r in enumerate(map):
        for tn, t in enumerate(r):
            if t == 2:
                virus_positions.append((rn, tn))
    total_cnt = len(map) * len(map[0])
    max_result = 0
    for i in range(total_cnt):
        for j in range(i+1, total_cnt):
            for k in range(j+1, total_cnt):
                (iy, ix) = (i//len(map[0]), i%len(map[0]))
                (jy, jx) = (j//len(map[0]), j%len(map[0]))
                (ky, kx) = (k//len(map[0]), k%len(map[0]))
                if map[iy][ix] != 0 or map[jy][jx] != 0 or map[ky][kx] != 0:
                    continue
                map[iy][ix],map[jy][jx],map[ky][kx] = 1,1,1
                result = zeroes_after_filling(map, virus_positions)
                if result > max_result:
                    max_result = result
                map[iy][ix],map[jy][jx],map[ky][kx] = 0,0,0
    return max_result

def zeroes_after_filling(map: 'list[list[int]]', virus_positions: 'list[tuple(int, int)]') -> int:
    def fill(map, r, c):
        filled = 0
        if r >= 0 and r < len(map) and c >= 0 and c < len(map[0]) and map[r][c] == 0:
            map[r][c] = 3
            filled += 1
            filled += fill(map, r+1, c)
            filled += fill(map, r-1, c)
            filled += fill(map, r, c+1)
            filled += fill(map, r, c-1)
        return filled
    def clear(map):
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 3:
                    map[i][j] = 0
    def count(map, what):
        c = 0
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == what:
                    c += 1
        return c
    for (vy, vx) in virus_positions:
        fill(map, vy + 1, vx)
        fill(map, vy - 1, vx)
        fill(map, vy, vx + 1)
        fill(map, vy, vx - 1)
    result = count(map, 0)
    clear(map)
    return result

main()
