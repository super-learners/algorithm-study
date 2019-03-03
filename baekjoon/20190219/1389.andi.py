from collections import deque

def main():
  n, m = map(int, input().split(" "))
  matrix = [[None for _ in range(n)] for __ in range(n)]
  network = [deque() for _ in range(n)]
  for _ in range(m):
    a, b = map(int, input().split(" "))
    network[a-1].append(b-1)
    network[b-1].append(a-1)

  bfs(matrix, network)
  min_kevin_bacon = None
  min_kevin_bacon_person = None
  for p in range(n):
    kevin_bacon = sum(matrix[p][:p]+matrix[p][p+1:])
    if min_kevin_bacon is None or kevin_bacon < min_kevin_bacon:
      min_kevin_bacon = kevin_bacon
      min_kevin_bacon_person = p + 1
  print(min_kevin_bacon_person)

def bfs(matrix, network):
  n = len(matrix)
  for p in range(n):
    hops = 1
    q = deque(network[p])
    while True:
      newq = deque()
      updated = False
      while len(q) > 0:
        f = q.popleft()
        if f != p and (matrix[p][f] is None or matrix[p][f] > hops):
          matrix[p][f] = hops
          updated = True
          for f_of_f in network[f]:
            newq.append(f_of_f)
      if not updated:
        break
      for to_enqueue in newq:
        q.append(to_enqueue)
      hops += 1

main()
