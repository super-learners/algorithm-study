def main():
    from collections import deque
    [m, n, h] = [int(x) for x in input().split(" ")]
    tomatoes = [
        [
            [int(x) for x in input().split(" ")] for _ in range(n)
        ] for __ in range(h)
    ]
    copy = [
        [
            [None for _ in range(m)] for __ in range(n)
        ] for ___ in range(h)
    ]
    def bfs(seeds):
        q = deque([])
        def insert_adjecent(l,r,c,d):
            q.append((l+1,r,c,d))
            q.append((l-1,r,c,d))
            q.append((l,r+1,c,d))
            q.append((l,r-1,c,d))
            q.append((l,r,c+1,d))
            q.append((l,r,c-1,d))
        for seed in seeds:
            lev, row, cel = seed
            copy[lev][row][cel] = 0
            insert_adjecent(lev, row, cel, 1)
        while q:
            item = q.popleft()
            t = item[:3]
            d = item[3]
            try:
                tomato = tomatoes[t[0]][t[1]][t[2]]
                if tomato == 0:
                    if copy[t[0]][t[1]][t[2]] is None:
                        copy[t[0]][t[1]][t[2]] = d
                        insert_adjecent(t[0],t[1],t[2],d+1)
            except IndexError:
                continue
    seeds = deque([])
    for level in range(len(tomatoes)):
        for row in range(len(tomatoes[level])):
            for cell in range(len(tomatoes[level][row])):
                tomato = tomatoes[level][row][cell]
                if tomato == 1:
                    seeds.append((level, row, cell))
    bfs(seeds)
    maxvalue = 0
    for level in range(len(tomatoes)):
        for row in range(len(tomatoes[level])):
            for cell in range(len(tomatoes[level][row])):
                tomato = tomatoes[level][row][cell]
                if tomato != -1 and copy[level][row][cell] is None:
                    print(-1)
                    return
                if copy[level][row][cell] is None:
                    continue
                else:
                    maxvalue = max(maxvalue, copy[level][row][cell])
    print(maxvalue)

main()

