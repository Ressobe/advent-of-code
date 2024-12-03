

class Program
{
  static int partOne()
  {
    string path = "plik.txt";
    string[] lines = File.ReadAllLines(path);

    int sum = 0;
    foreach (string line in lines)
    {
      string[] parts = line.Split(" ");
      bool isIncreasing = false;
      bool isSafe = true;
      for (int i = 0; i < parts.Count() - 1; i++)
      {
        int difference = int.Parse(parts[i + 1]) - int.Parse(parts[i]);
        if (i == 0)
        {
          if (difference > 0)
          {
            isIncreasing = true;
          }
        }

        if (Math.Abs(difference) > 3 || difference == 0) isSafe = false;
        if (difference > 0 && !isIncreasing) isSafe = false;
        if (difference < 0 && isIncreasing) isSafe = false;
      }
      if (isSafe) sum++;
    }
    return sum;
  }
  static bool check(string[] parts)
  {
    bool isIncreasing = false;
    bool isSafe = true;
    for (int i = 0; i < parts.Count() - 1; i++)
    {
      int difference = int.Parse(parts[i + 1]) - int.Parse(parts[i]);
      if (i == 0)
      {
        if (difference > 0)
        {
          isIncreasing = true;
        }
      }

      if (Math.Abs(difference) > 3 || difference == 0) isSafe = false;
      if (difference > 0 && !isIncreasing) isSafe = false;
      if (difference < 0 && isIncreasing) isSafe = false;
    }
    return isSafe;
  }


  static string[] RemoveElementAt(string[] array, int indexToRemove)
  {
    return array.Where((_, index) => index != indexToRemove).ToArray();
  }

  static int partTwo()
  {
    string path = "plik.txt";
    string[] lines = File.ReadAllLines(path);

    int safeReports = 0;

    foreach (string line in lines)
    {
      string[] parts = line.Split(" ");
      if (check(parts))
      {
        safeReports++;
        continue;
      }

      bool isSafeAfterRemoval = false;
      for (int i = 0; i < parts.Length; i++)
      {
        string[] modifiedParts = RemoveElementAt(parts, i);
        if (check(modifiedParts))
        {
          isSafeAfterRemoval = true;
          break;
        }
      }

      if (isSafeAfterRemoval)
      {
        safeReports++;
      }
    }

    return safeReports;
  }

  static void Main()
  {
    Console.WriteLine(partTwo());
  }
}
