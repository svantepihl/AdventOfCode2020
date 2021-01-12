using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day3
{
    
    class Program
    {
        static int TraverseMap(List<String> map,int yStepSize,int xStepSize)
        {
            // Map dimensions
            var mapHeight = map.Count();
            var mapWidth = map[0].Length;
            
            // Starting pos
            var xPos = 0;
            var yPos = 0;
            
            var treesEncountered = 0;

            while (yPos < mapHeight)
            {
                // Check if tree at current pos
                if (map[yPos][xPos] == '#')
                {
                    treesEncountered++;
                }
                // Take step
                xPos = (xPos + xStepSize) % mapWidth;
                yPos += yStepSize;
            }

            return treesEncountered;
        }
        
        
        static void Main()
        {
            // Our given map
            var map = File.ReadAllLines("../../../input-day3.txt").ToList();

            //------------
            // Part 1
            //------------
            var partOne = TraverseMap(map,1,3);
            Console.WriteLine("Part 1: " + partOne.ToString());

            //------------
            // Part 2
            //------------
            var slopes = new (int yStepSize,int xStepSize)[]
            {
                (1,1),
                (1,3),
                (1,5),
                (1,7),
                (2,1) 
            };
            

            // Multiply the number of trees found for each of the slopes
            ulong partTwo = 1;
            foreach (var slope in slopes)
            {
                partTwo *= (ulong) TraverseMap(map,slope.yStepSize,slope.xStepSize);
            }

            Console.WriteLine("Part 2: " + partTwo);
        }
    }
}