def main():
    while True:
        num_arr = [int(x) for x in input().strip().split(" ")]
        if len(num_arr) == 1 and num_arr[0] == -1:
            return
        num_arr = num_arr[:-1]
        d = {}
        for num in num_arr:
            d[num] = True
        count = 0
        for num in num_arr:
            if num * 2 in d:
                count += 1
        print(count)

main()
