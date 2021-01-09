﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day2
{

    class Rule
    {
        private int MinOccurrences { get; }
        private int MaxOccurrences { get; }
        private char Chr { get; }

        public Rule(int minOccurrences, int maxOccurrences, char chr)
        {
            MinOccurrences = minOccurrences;
            MaxOccurrences = maxOccurrences;
            Chr = chr;
        }

        public bool CheckString(string s)
        {
            var count = s.Count(c => c == this.Chr);

            return count >= MinOccurrences && count <= MaxOccurrences;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            List<string> puzzleInputStrings = File.ReadAllLines("../../../input-day1.txt").ToList();
            
            
        }
    }
}
