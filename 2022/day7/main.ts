import { readFileSync } from "fs";

let arr: Array<string> = readFileSync("dane.txt", "utf-8").split("\n");
arr.pop();

let path = new Array("/");
let root_folder_size = 0;

let foldersArray = new Array();

const addSize = (size: number, folder_name: any) => {
  foldersArray.forEach((element) => {
    if (element.folder_name === folder_name) {
      element.size += size;
    }
  });
};

arr.forEach((element) => {
  let command_line = element.split(" ");
  let command = command_line[1];

  if (command === "cd") {
    let argv = command_line[2];
    if (argv === "..") {
      path.pop();
    } else {
      let folder_object = {
        folder_name: `${argv}`,
        parent_folder: path.at(-1),
        size: 0,
      };
      foldersArray.push(folder_object);
      path.push(`${argv}`);
    }
  } else if (command != "ls" && command_line[0] != "dir") {
    let file_size: number = parseInt(command_line[0]);
    let folder = path.at(-1);

    if (folder === "/") {
      root_folder_size += file_size;
    } else {
      addSize(file_size, folder);
    }
  }
});

foldersArray.forEach((element) => {
  if (element.parent_folder !== "/") {
    addSize(element.size, element.parent_folder);
  }
});

foldersArray.forEach((element) => {
  console.log(element.folder_name, element.size);
});

// foldersArray.forEach((element) => console.log(element));

// foldersArray.forEach((element) => {
//   if (element.parent_folder === "/") {
//     let folder_size = element.size;
//     root_folder_size += folder_size;
//   }
// });

// foldersArray.push({ folder_name: "/", size: root_folder_size });
