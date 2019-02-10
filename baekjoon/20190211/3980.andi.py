def main():
    num_testcases = int(input())
    for _ in range(num_testcases):
        print(solve([[int(x) for x in input().strip().split(" ")] for _ in range(11)]))

def solve(data: "List[List[int]]"):
    return solve_helper(data, [])

def solve_helper(data: "List[List[int]]", selected_positions: "List[int]"):
    current_player = len(selected_positions)
    if current_player == 11:
        sum = 0
        for player, position in enumerate(selected_positions):
            sum += data[player][position]
        return sum
    player_stats = data[current_player]
    available_positions = [i for i, s in enumerate(player_stats) if i not in selected_positions and s > 0]

    if len(available_positions) == 0:
        return -1

    largest_sum = -1
    for pos in available_positions:
        sum = solve_helper(data, selected_positions + [pos])
        if largest_sum < sum:
            largest_sum = sum

    return largest_sum

main()
