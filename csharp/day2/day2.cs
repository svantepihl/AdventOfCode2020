using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day2
{
    class Program
    {
        /// <summary>
        /// Takes a string of following format "MinOccurrences-MaxOccurrences char: stringToCheck"
        /// and returns a true if the string follows the rule and false otherwise.
        /// </summary>
        private static bool CheckRulePartOne(string str)
        {
            string[] tempStrings = str.Split(':');

            string stringToCheck = tempStrings[1].Trim();
            char chr = char.Parse(tempStrings[0].Split(' ')[1].Trim());
            string counts = tempStrings[0].Split(' ')[0].Trim();

            int min = int.Parse(counts.Split('-')[0].Trim());
            int max = int.Parse(counts.Split('-')[1].Trim());

            RulePartOne rulePartOne = new RulePartOne(min,max,chr);

            return rulePartOne.CheckString(stringToCheck);
        }

        /// <summary>
        /// Takes a string of following format "posOne-posTwo char: stringToCheck"
        /// and returns a true if the string follows the rule and false otherwise.
        /// </summary>
        private static bool CheckRulePartTwo(string str)
        {
            string[] tempStrings = str.Split(':');

            string stringToCheck = tempStrings[1].Trim();
            char chr = char.Parse(tempStrings[0].Split(' ')[1].Trim());
            string counts = tempStrings[0].Split(' ')[0];

            int posOne = int.Parse(counts.Split('-')[0].Trim());
            int PosTwo = int.Parse(counts.Split('-')[1].Trim());

            RulePartTwo rulePartTwo = new RulePartTwo(posOne,PosTwo,chr);

            return rulePartTwo.CheckString(stringToCheck);
        }

        static void Main()
        {
            List<string> puzzleInputStrings = File.ReadAllLines("../../../input-day2.txt").ToList();

            var partOne = 0;
            var partTwo = 0;

            foreach (var str in puzzleInputStrings)
            {
                if (CheckRulePartOne(str))
                {
                    partOne++;
                }

                if (CheckRulePartTwo(str))
                {
                    partTwo++;
                }
            }

            // Part 1
            Console.WriteLine("Part 1: " + partOne.ToString());

            // Part 2
            Console.WriteLine("Part 2: " + partTwo.ToString());

        }
    }
}
