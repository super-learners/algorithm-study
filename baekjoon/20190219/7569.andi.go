package main

import (
	"fmt"
)

func main() {
	var m, n, h int
	fmt.Scan(&m)
	fmt.Scan(&n)
	fmt.Scan(&h)

	var tomatoes = make([][][]int, h)

	for i := 0; i < h; i++ {
		tomatoes[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			tomatoes[i][j] = make([]int, m)
			for k := 0; k < n; k++ {
				fmt.Scan(&tomatoes[i][j][k])
			}
		}
	}

	fmt.Println(solve(tomatoes))
}

// func main() {
// 	// tomatoes := [][]int{[]int{1}, []int{3, 4}}
// 	tomatoes := [][][]int{
// 		[][]int{
// 			[]int{0, 0, 0, 0, 0},
// 			[]int{0, 0, 0, 0, 0},
// 			[]int{0, 0, 1, 0, 0}},
// 		[][]int{
// 			[]int{0, 0, 0, 0, 0},
// 			[]int{0, 0, 1, 0, 0},
// 			[]int{0, 0, 0, 0, 0}},
// 	}

// 	fmt.Println(solve(tomatoes))
// }

func solve(tomatoes [][][]int) int {
	visited := make([][][]bool, len(tomatoes))
	seeds := make([]intt, 0, len(tomatoes)*len(tomatoes[0])*len(tomatoes[0][0]))
	zeroCount := 0
	for i := 0; i < len(tomatoes); i++ {
		visited[i] = make([][]bool, len(tomatoes[i]))
		for j := 0; j < len(tomatoes[i]); j++ {
			visited[i][j] = make([]bool, len(tomatoes[i][j]))
			for k := 0; k < len(tomatoes[i][j]); k++ {
				visited[i][j][k] = false
				if tomatoes[i][j][k] == 1 {
					seeds = append(seeds, intt{x: i, y: j, z: k})
				}
				if tomatoes[i][j][k] == 0 {
					zeroCount++
				}
			}
		}
	}

	return bfs(seeds, zeroCount, tomatoes, visited)
}

func bfs(seeds []intt, zeroCount int, tomatoes [][][]int, visited [][][]bool) int {
	if zeroCount == 0 {
		return 0
	}
	queue := make([]intt, 0, len(tomatoes)*len(tomatoes[0])*len(tomatoes[0][0]))
	insertAdjecent := func(queue []intt, s intt) []intt {
		if s.x+1 < len(tomatoes) && !visited[s.x+1][s.y][s.z] {
			queue = append(queue, intt{x: s.x + 1, y: s.y, z: s.z})
		}
		if s.x-1 >= 0 && !visited[s.x-1][s.y][s.z] {
			queue = append(queue, intt{x: s.x - 1, y: s.y, z: s.z})
		}
		if s.y+1 < len(tomatoes[0]) && !visited[s.x][s.y+1][s.z] {
			queue = append(queue, intt{x: s.x, y: s.y + 1, z: s.z})
		}
		if s.y-1 >= 0 && !visited[s.x][s.y-1][s.z] {
			queue = append(queue, intt{x: s.x, y: s.y - 1, z: s.z})
		}
		if s.z+1 < len(tomatoes[0][0]) && !visited[s.x][s.y][s.z+1] {
			queue = append(queue, intt{x: s.x, y: s.y, z: s.z + 1})
		}
		if s.z-1 >= 0 && !visited[s.x][s.y][s.z-1] {
			queue = append(queue, intt{x: s.x, y: s.y, z: s.z - 1})
		}
		return queue
	}
	for i := 0; i < len(seeds); i++ {
		s := seeds[i]
		visited[s.x][s.y][s.z] = true
		queue = insertAdjecent(queue, intt{x: s.x, y: s.y, z: s.z})
	}
	d := 1
	for ; len(queue) > 0; d++ {
		cnt := len(queue)
		for c := 0; c < cnt; c++ {
			item := queue[0]
			queue = queue[1:]
			i, j, k := item.x, item.y, item.z
			tomato := tomatoes[i][j][k]
			if tomato == 0 {
				if !visited[i][j][k] {
					zeroCount--
					if zeroCount == 0 {
						return d
					}
					queue = insertAdjecent(queue, intt{x: i, y: j, z: k})
				}
			}
			visited[i][j][k] = true
		}
	}
	return -1
}

type intt struct {
	x, y, z int
}
