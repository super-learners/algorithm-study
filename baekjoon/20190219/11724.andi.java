import java.util.*;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    final String[] split1 = scanner.nextLine().split(" ");
    final int n = Integer.parseInt(split1[0]);
    final int m = Integer.parseInt(split1[1]);
    ArrayList<LinkedList<Integer>> nodes = new ArrayList<>(n);
    boolean[] visited = new boolean[n];
    for (int i = 0; i < n; i++) {
      nodes.add(new LinkedList<>());
      visited[i] = false;
    }

    for (int i = 0; i < m; i++) {
      final String[] split2 = scanner.nextLine().split(" ");
      final int u = Integer.parseInt(split2[0]) - 1;
      final int v = Integer.parseInt(split2[1]) - 1;
      nodes.get(u).add(v);
      nodes.get(v).add(u);
    }

    scanner.close();

    int ccCount = 0;
    for (int i = 0; i < n; i++) {
      if (visited[i]) {
        continue;
      }
      ccCount++;
      dfs(nodes, i, visited);
    }
    System.out.println(ccCount);
  }

  private static void dfs(ArrayList<LinkedList<Integer>> nodes, int i, boolean[] visited) {
    if (visited[i]) {
      return;
    }
    visited[i] = true;
    for (int adj : nodes.get(i)) {
      dfs(nodes, adj, visited);
    }
  }

}