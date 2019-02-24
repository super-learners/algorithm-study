def readline():
    from sys import stdin
    return stdin.readline()
def printline(*args, **kwargs):
    from sys import stdout
    print(*args, **kwargs)
    stdout.flush()

def main():
    num_t = int(readline())
    for _ in range(num_t):
        [num_a, num_b] = [int(x) for x in readline().split(" ")]
        _num_n = int(readline())
        answer_range = (num_a + 1, num_b)
        while True:
            guess = (answer_range[0] + answer_range[1]) // 2
            printline(guess)
            response = readline().strip()
            if response == "CORRECT":
                break
            elif response == "TOO_SMALL":
                answer_range = (guess + 1, answer_range[1])
            elif response == "TOO_BIG":
                answer_range = (answer_range[0], guess - 1)
            else:
                break
main()