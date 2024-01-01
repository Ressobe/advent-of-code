package main


import (
  "fmt"
  "os"
  "bufio"
  "strconv"
  "strings"
)

func program(line string) []int {
  values := strings.Split(line, ",")

  var integers []int

	for _, value := range values {
		num, err := strconv.Atoi(value)
		if err != nil {
			fmt.Println("Error converting to integer:", err)
			return nil
		}
		integers = append(integers, num)
	}

  return integers
}

func partOne() int {
  file, err := os.Open("input.txt")
  if err != nil {
    fmt.Println("Error opening file: ", err)
    return -1
  }
  defer file.Close()

	scanner := bufio.NewScanner(file)
  scanner.Scan()
  line := scanner.Text()

  p := program(line)
  p[1] = 12
  p[2] = 2
  i := 0

  // 1  +
  // 2  *
  // 99 end program

  for i < len(p) {
    if p[i] == 99 {
      break
    }

    num1_pos := p[i + 1] 
    num2_pos := p[i + 2] 
    output_pos := p[i + 3]

    if p[i] == 1 {
      p[output_pos] = p[num1_pos] + p[num2_pos]
    }

    if p[i] == 2 {
      p[output_pos] = p[num1_pos] * p[num2_pos]
    }

    i += 4
  }

  return p[0]
}

func main() {
  fmt.Println(partOne())
}
