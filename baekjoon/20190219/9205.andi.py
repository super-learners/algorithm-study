def main():
    def get_tuple():
        return tuple([int(x) for x in input().strip().split(" ")])
    num_testcases = int(input())
    for __ in range(num_testcases):
        num_stores = int(input())
        house = get_tuple()
        stores = []
        for _ in range(num_stores):
            stores.append(get_tuple())
        fest = get_tuple()
        answer = solve(house, stores, fest, {})
        print(answer)

def solve(house, stores, fest, visited):
    def distance(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    def test(stores, fest, route):
        position = route[-1]
        if distance(position, fest) <= 1000:
            return True
        store_len = len(stores)
        for i in [x for x in range(store_len) if distance(stores[x], position) <= 1000 and stores[x] not in visited]:
            route.append(stores[i])
            visited[stores[i]] = True
            stores.pop(i)
            success = test(stores, fest, route)
            if success:
                return True
            stores.insert(i, route.pop())
        return False
    if len(stores) == 0:
        if distance(house, fest) <= 1000:
            return "happy"
        return "sad"
    if test(stores, fest, [house]):
        return "happy"
    return "sad"

main()