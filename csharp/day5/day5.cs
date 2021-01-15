using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day5
{
    class Program
    {
        static void Main()
        {
            var boardingPassesStrings = File.ReadLines("../../../input-day5.txt");

            var ticketIds = (from boardingPass in boardingPassesStrings
                let row = Convert.ToInt32(boardingPass.Substring(0, 7)
                    .Replace('B', '1')
                    .Replace('F', '0'), 2)
                let col = Convert.ToInt32(boardingPass.Substring(7, boardingPass.Length - 7)
                    .Replace('L', '0')
                    .Replace('R', '1'), 2)
                select row * 8 + col).ToList();

            //------------
            // Part 1
            //------------

            int max = ticketIds.Max();

            Console.WriteLine("Part 1: " + max);
            
            //------------
            // Part 2
            //------------
            var mySeat = ticketIds
                .Where(ticketId => !ticketIds.Contains(ticketId + 1) && ticketIds.Contains(ticketId + 2)).Select(ticketId => ticketId+1).Min();

            Console.WriteLine("Part 2: " + mySeat);
        }
    }
}