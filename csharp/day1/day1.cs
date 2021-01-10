using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day1
{
    
    class Program
    {
        static void Main()
        {
            // Read the file
            var puzzleInputStrings = File.ReadAllLines("../../../input-day1.txt").ToList();


            var puzzleIntputHashSet = new HashSet<int>();
            var puzzleIntputInts = new List<int>();

            foreach (var s in puzzleInputStrings) {
                puzzleIntputHashSet.Add(int.Parse(s));
                puzzleIntputInts.Add(int.Parse(s));
            }

            //------------
            // Part 1
            //------------
            

            foreach (var intOne  in puzzleIntputInts)
            {
                var intTwo = 2020 - intOne;

                
                if (puzzleIntputInts.Contains(intTwo) && intOne != intTwo)
                {
                    Console.WriteLine("Part 1: " + (intTwo * intOne).ToString());
                    break;
                }
            }

            //------------
            // Part 2
            //------------
            var len = puzzleIntputInts.Count();
            for (var i = 0; i < len-2; i++)
            {
                if (puzzleIntputInts[i] > 2020)
                {
                    continue;
                }
                for (var ii = i; ii < len-1; ii++)
                {
                    if (puzzleIntputInts[i] + puzzleIntputInts[ii] > 2020)
                    {
                        continue;
                    } 
                    for (var iii = ii; iii < len; iii++)
                    {
                        if (puzzleIntputInts[i] + puzzleIntputInts[ii] + puzzleIntputInts[iii] == 2020)
                        {
                            Console.WriteLine("Part 2: " + (puzzleIntputInts[i] * puzzleIntputInts[ii] * puzzleIntputInts[iii]));
                        }
                    }
                }
            }

        }
    }
}
