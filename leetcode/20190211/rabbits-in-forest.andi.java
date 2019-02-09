import java.util.HashMap;

class Solution {
    public int numRabbits(int[] answers) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int answer : answers) {
            if (map.containsKey(Integer.valueOf(answer))) {
                map.put(answer, map.get(answer) + 1);
            } else {
                map.put(answer, 1);
            }
        }

        int answer = 0;
        for (int k : map.keySet()) {
            int v = map.get(k);
            if (k + 1 == v) {
                answer += v;
            } else if (k + 1 > v) {
                answer += k + 1;
            } else {
                answer += (v / (k + 1)) * (k + 1);
                if (v % (k + 1) != 0) {
                    answer += k + 1;
                }
            }
        }

        return answer;
    }
}
