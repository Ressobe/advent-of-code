import { readFileSync } from "fs";

let content: Array<string> = readFileSync("dane.txt", "utf-8").split("\n");

const part_one = (content: Array<string>) => {
  let sum: number = 0;
  for (let i = 0; i < content.length - 1; i++) {
    let line: string = content[i].toString();
    let array: Array<string> = line.split(",");

    let first_pair: Array<string> = array[0].toString().split("-");
    let second_pair: Array<string> = array[1].toString().split("-");

    let min: number = Math.min(
      parseInt(first_pair[0]),
      parseInt(second_pair[0])
    );

    if (min == parseInt(first_pair[0])) {
      if (parseInt(first_pair[1]) >= parseInt(second_pair[1])) {
        sum++;
        continue;
      }
    }
    if (min == parseInt(second_pair[0])) {
      if (parseInt(second_pair[1]) >= parseInt(first_pair[1])) {
        sum++;
      }
    }
  }
  return sum;
};

const part_two = (content: Array<string>) => {
  let sum: number = 0;

  for (let i = 0; i < content.length - 1; i++) {
    let line: string = content[i].toString();
    let array: Array<string> = line.split(",");

    let first_pair: Array<string> = array[0].toString().split("-");
    let second_pair: Array<string> = array[1].toString().split("-");

    let first_pair_nums = new Array(
      parseInt(first_pair[0]),
      parseInt(first_pair[1])
    );

    let second_pair_nums = new Array(
      parseInt(second_pair[0]),
      parseInt(second_pair[1])
    );

    let min: number = Math.min(first_pair_nums[0], second_pair_nums[0]);

    if (min === first_pair_nums[0]) {
      if (second_pair_nums[0] <= first_pair_nums[1]) {
        sum++;
        continue;
      }
    }

    if (min === second_pair_nums[0]) {
      if (first_pair_nums[0] <= second_pair_nums[1]) {
        sum++;
        continue;
      }
    }
  }
  return sum;
};

// 528
console.log(`Part one: ${part_one(content)}`);
// 881
console.log(`Part two: ${part_two(content)}`);
