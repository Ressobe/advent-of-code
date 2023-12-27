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

func main() {

  file, err := os.Open("input.txt")
  if err != nil {
    fmt.Println("Error opening file: ", err)
    return
  }
  defer file.Close()

  var sum int

	scanner := bufio.NewScanner(file)

  for scanner.Scan() {
      line := scanner.Text()
      number, err := strconv.ParseFloat(line, 64)

      if err != nil {
        fmt.Println("Error while converting string to float", err)
        return
      }
      sum += calculateFuel(number)
  }

  fmt.Println(sum)
}
