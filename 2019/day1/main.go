package main


import (
  "fmt"
  "math"
  "os"
  "bufio"
  "strconv"
)


func calculateFuel(number float64) int {
  return int(math.Floor(number / 3)) - 2
}


func partOne() int {
  file, err := os.Open("input.txt")
  if err != nil {
    fmt.Println("Error opening file: ", err)
    return -1
  }
  defer file.Close()

  var sum int

	scanner := bufio.NewScanner(file)

  for scanner.Scan() {
      line := scanner.Text()
      number, err := strconv.ParseFloat(line, 64)

      if err != nil {
        fmt.Println("Error while converting string to float", err)
        return -1
      }
      sum += calculateFuel(number)
  }
  return sum
}

func calculateFuelPartTwo(number int) int {
  fuel := 0
  
  for number >= 0 {
    f := calculateFuel(float64(number))
    if f >= 0 { fuel += f }
    number = f
  } 

  return fuel
}

func partTwo() int {
  file, err := os.Open("input.txt")
  if err != nil {
    fmt.Println("Error opening file: ", err)
    return -1
  }
  defer file.Close()

  var sum int

	scanner := bufio.NewScanner(file)

  for scanner.Scan() {
      line := scanner.Text()
      number, err := strconv.ParseFloat(line, 64)

      if err != nil {
        fmt.Println("Error while converting string to float", err)
        return -1
      }
      sum += calculateFuelPartTwo(int(number))
  }
  return sum
}


func main() {
  fmt.Println("Part one: ", partOne())
  fmt.Println("Part two: ", partTwo())

}
