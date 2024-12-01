
class Program
{
  static int partOne()
  {
    string path = "plik.txt";
    string[] lines = File.ReadAllLines(path);
    List<int> leftSide = new List<int>();
    List<int> rightSide = new List<int>();

    foreach (string line in lines)
    {
      string[] parts = line.Split("   ");
      leftSide.Add(int.Parse(parts[0].Trim()));
      rightSide.Add(int.Parse(parts[1].Trim()));
    }
    leftSide.Sort();
    rightSide.Sort();

    int sum = 0;
    for (int i = 0; i < leftSide.Count; i++)
    {
      int distance = Math.Abs(leftSide[i] - rightSide[i]);
      sum += distance;
    }
    return sum;
  }

  static int partTwo()
  {
    string path = "plik.txt";
    string[] lines = File.ReadAllLines(path);
    List<int> leftSide = new List<int>();
    List<int> rightSide = new List<int>();

    foreach (string line in lines)
    {
      string[] parts = line.Split("   ");
      leftSide.Add(int.Parse(parts[0].Trim()));
      rightSide.Add(int.Parse(parts[1].Trim()));
    }
    leftSide.Sort();
    rightSide.Sort();

    int sum = 0;
    foreach (int leftNum in leftSide)
    {
      sum += rightSide.Count(x => x == leftNum) * leftNum;
    }
    return sum;
  }

  static void Main()
  {
    Console.WriteLine(partTwo());
  }
}
