def main():
    m = int(input())
    answer = solve(m)
    print(answer)

def solve(num: "int"):
    half_triangle = [1]

    tuples = []
    for n in range(2, num):
        new_half_triangle = next_half_triangle(half_triangle, n, num)
        print(new_half_triangle)
        if num in new_half_triangle:
            k = new_half_triangle.index(num)
            tuples.append([n, k])
            if num % 2 == 0 or k * 2 < n:
                tuples.append([n, n - k])
        half_triangle = new_half_triangle
    tuples.append([num, 1])
    tuples.append([num, num - 1])

    answer = str(len(tuples)) + "\n"
    answer += "\n".join([" ".join([str(xx) for xx in x]) for x in tuples])
    return answer

def next_half_triangle(half_triangle: "List[int]", n: "int", max_value: "int"):
    result = [1]
    for i in range(1, len(half_triangle)):
        if half_triangle[i] is None:
            result += [None]
            return result

        sum = half_triangle[i - 1] + half_triangle[i]
        if sum > max_value:
            result += [None]
            return result
        result += [sum]
    if n % 2 == 0:
        result += [half_triangle[-1] * 2]
    return result

main()
