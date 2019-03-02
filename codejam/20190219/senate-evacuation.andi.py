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
  plan = []
  party_n_senators = [(chr(ord("A") + x[0]), x[1]) for x in enumerate(senators)]
  party_n_senators = sorted(party_n_senators, key=lambda e: e[1], reverse=True)
  def party_of(pns):
    return pns[0]
  def num_senator_of(pns):
    return pns[1]
  def dec_num_senator_of(pns_list, idx):
    pns_list[idx] = (pns_list[idx][0], pns_list[idx][1] - 1)

  while True:
    plan.append(party_of(party_n_senators[0]))
    dec_num_senator_of(party_n_senators, 0)
    if num_senator_of(party_n_senators[0]) == 0:
      party_n_senators.pop(0)

    if len(party_n_senators) == 0:
      return plan

    party_n_senators = sorted(party_n_senators, key=lambda e: e[1], reverse=True)

    if num_senator_of(party_n_senators[0]) * 2 <= sum([num_senator_of(x) for x in party_n_senators]):
      continue

    plan.append(plan.pop() + party_of(party_n_senators[0]))
    dec_num_senator_of(party_n_senators, 0)
    if num_senator_of(party_n_senators[0]) == 0:
      party_n_senators.pop(0)

    if len(party_n_senators) == 0:
      return plan

    party_n_senators = sorted(party_n_senators, key=lambda e: e[1], reverse=True)

  return plan

main()
