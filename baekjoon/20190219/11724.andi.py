def main():
  n, m = [int(x) for x in input().strip().split(" ")]
  nodes = [[] for _ in range(n)]
  visited = [False for _ in range(n)]
  for _ in range(m):
    u, v = [int(x) for x in input().strip().split(" ")]
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)
  cc_count = 0
  for i, _ in enumerate(nodes):
    if not visited[i]:
      cc_count += 1
    else:
      continue
    dfs(nodes, i, visited)
  print(cc_count)

def dfs(nodes, i, visited):
  if visited[i]:
    return
  visited[i] = True
  for a in nodes[i]:
    dfs(nodes, a, visited)

main()
