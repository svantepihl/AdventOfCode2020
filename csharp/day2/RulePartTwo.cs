namespace day2
{
    class RulePartTwo
    {
        private int PosOne { get; }
        private int PosTwo { get; }
        private char Chr { get; }

        public RulePartTwo(int posOne, int posTwo, char chr)
        {
            Chr = chr;
            PosOne = posOne-1;
            PosTwo = posTwo-1;
        }

        public bool CheckString(string str)
        {
            char charOne = str[this.PosOne];
            char charTwo = str[this.PosTwo];
            return (charOne == this.Chr && charTwo  != this.Chr) || (charOne != this.Chr && charTwo  == this.Chr) ;
        }
    }
}