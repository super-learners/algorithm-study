def write(*args, **kwargs):
  from sys import stdout
  print(*args, **kwargs)
  stdout.flush()

def main():
  testcases = int(input())
  for idx_testcase in range(1, testcases+1):
    _parties = int(input())
    senators = [int(x) for x in input().strip().split(" ")]
    plan = solve(senators)
    write("Case #{}: {}".format(str(idx_testcase), " ".join(plan)))

def solve(senators):
  num_senators = sum(senators)
  plan = []
  sorted_senators = sorted(enumerate(senators), key=lambda e: e[1], reverse=True)
  while num_senators > 0:
    plan.append(chr(ord("A") + sorted_senators[0][0]))
    sorted_senators[0] = (sorted_senators[0][0], sorted_senators[0][1] - 1)
    num_senators -= 1
    if sorted_senators[0][1] == 0:
      sorted_senators.pop(0)

    if len(sorted_senators) == 0:
      return plan
    largest_num_senators_party_idx = 0
    if len(sorted_senators) > 1 and sorted_senators[1][1] > sorted_senators[0][1]:
      largest_num_senators_party_idx = 1
    if sorted_senators[largest_num_senators_party_idx][1] * 2 <= sum([x[1] for x in sorted_senators]):
      continue

    plan.append(plan.pop() + chr(ord("A") + sorted_senators[largest_num_senators_party_idx][0]))
    sorted_senators[largest_num_senators_party_idx] = (sorted_senators[largest_num_senators_party_idx][0], sorted_senators[largest_num_senators_party_idx][1] - 1)
    num_senators -= 1
    if sorted_senators[largest_num_senators_party_idx][1] == 0:
      sorted_senators.pop(largest_num_senators_party_idx)

  return plan

main()
