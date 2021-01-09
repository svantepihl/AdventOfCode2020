using System.Linq;

namespace day2
{
    class RulePartOne
    {
        private int MinOccurrences { get; }
        private int MaxOccurrences { get; }
        private char Chr { get; }

        public RulePartOne(int minOccurrences, int maxOccurrences, char chr)
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
}