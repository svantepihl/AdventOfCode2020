using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day4
{
    class Program
    {
        static void Main(string[] args)
        {
            var rawData = File.ReadAllText("../../../input-day4.txt");
            var rawStrings = rawData.Split("\r\n\r\n", StringSplitOptions.RemoveEmptyEntries);

            var allPassports = new List<Passport>();
            foreach (var rawString in rawStrings)
            {
                allPassports.Add(new Passport(rawString.Trim()));
            }

            //------------
            // Part 1
            //------------
            int validPassportsPartOne = allPassports.Count(passport => passport.ValidatePartOne());
            Console.WriteLine(validPassportsPartOne);

            //------------
            // Part 2
            //------------
            int validPassportsPartTwo = allPassports.Count(passport => passport.ValidatePartTwo());
            Console.WriteLine(validPassportsPartTwo);
        }
    }
}