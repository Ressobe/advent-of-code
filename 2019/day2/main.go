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

func readFile(filename string) (*os.File, error) {
  file, err := os.Open("input.txt")
  if err != nil {
    return nil, err 
  }
  return file, nil
}

func partOne() int {
  file, err := readFile("input.txt")
  if err != nil {
    fmt.Println("Error while reading input file")
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

func partTwo() int {
  file, err := readFile("input.txt")
  if err != nil {
    fmt.Println("Error while reading input file")
    return -1
  }
  defer file.Close()

	scanner := bufio.NewScanner(file)
  scanner.Scan()
  line := scanner.Text()

  orginal_program := program(line)

  p := make([]int, len(orginal_program))
  copy(p, orginal_program)


  for i := 0; i <= 100; i++  {
    for j := 0; j <= 100; j++ {
      p[1] = i
      p[2] = j

      instruction_pointer := 0
      for instruction_pointer < len(p)  {
        if p[instruction_pointer] == 99 {
          break
        }

        num1_pos := p[instruction_pointer + 1] 
        num2_pos := p[instruction_pointer + 2] 
        output_pos := p[instruction_pointer + 3]

        if p[instruction_pointer] == 1 {
          p[output_pos] = p[num1_pos] + p[num2_pos]
        }

        if p[instruction_pointer] == 2 {
          p[output_pos] = p[num1_pos] * p[num2_pos]
        }
        instruction_pointer += 4
      }
      if p[0] == 19690720 {
        return 100 * p[1] + p[2]
      }
      // reset program
      copy(p, orginal_program)
    }
  }
     
  return -1
}

func main() {
  fmt.Println(partOne())
  fmt.Println(partTwo())
}
