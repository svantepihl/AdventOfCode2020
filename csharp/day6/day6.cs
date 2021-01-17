using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day6
{
    class Program
    {
        private static IEnumerable<char> _enumerable;

        static void Main()
        {
            var rawText = File.ReadAllText("../../../input-day6.txt");

            var groupsStrings = rawText.Split(Environment.NewLine + Environment.NewLine,
                StringSplitOptions.RemoveEmptyEntries);
            
            var groups = groupsStrings.Select(@group => @group.Split(Environment.NewLine)).ToList();
            
            //------------
            // Part 1
            //------------
            var partOne = 0;
            foreach (var group in groups)
            {
                var questionsAnswered = new HashSet<char>();
                foreach (var person in group)
                {
                    person.ToList().ForEach(chr => questionsAnswered.Add(chr));
                }

                partOne += questionsAnswered.Count;
            }
            Console.WriteLine("Part 1: " + partOne); 
           
            //------------
            // Part 2
            //------------
            var partTwo = 0;

            foreach (var group in groups)
            {
                HashSet<char> allAnswered = null;
                foreach (var person in group)
                {
                    if (allAnswered == null)
                    {
                        allAnswered = new HashSet<char>(person);
                    }
                    else
                    {
                        allAnswered.IntersectWith(person);
                    }
                }
                partTwo += allAnswered.Count;
            }
            
            Console.WriteLine("Part 2: " + partTwo); 
        }
    }
}