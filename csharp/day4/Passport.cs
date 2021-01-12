using System.Linq;
using System.Text.RegularExpressions;

namespace day4
{
    class Passport
    {
        public Passport()
        {
        }
        public Passport(string stringToParse)
        {
            Parse(stringToParse);
        }

        public string BirthYear { get; set; }

        public string IssueYear { get; set; }

        public string ExpirationYear { get; set; }

        public string Height { get; set; }

        public string EyeColor { get; set; }

        public string HairColor { get; set; }

        public string PassportID { get; set; }

        public string CountryId { get; set; }

        public bool ValidatePartOne()
        {
            return BirthYear is not null &&
                   IssueYear is not null &&
                   ExpirationYear is not null &&
                   Height is not null &&
                   EyeColor is not null &&
                   HairColor is not null &&
                   PassportID is not null;
        }

        public bool ValidatePartTwo()
        {
            return ValidateBirthYear() &&
                   ValidateIssueYear() &&
                   ValidateExpirationYear() &&
                   ValidateHeight() &&
                   ValidateHairColor() &&
                   ValidateEyeColor() &&
                   ValidatePassportID();
        }

        private bool ValidateBirthYear()
        {
            if (BirthYear == null || BirthYear.Length != 4) return false;

            return int.Parse(BirthYear) >= 1920 &&
                   int.Parse(BirthYear) <= 2002;
        }

        private bool ValidateIssueYear()
        {
            if (IssueYear == null || IssueYear.Length != 4) return false;

            return int.Parse(IssueYear) >= 2010 &&
                   int.Parse(IssueYear) <= 2020;
        }

        private bool ValidateExpirationYear()
        {
            if (ExpirationYear == null || ExpirationYear.Length != 4) return false;
            
            return int.Parse(ExpirationYear) >= 2020 && 
                   int.Parse(ExpirationYear) <= 2030;
        }

        private bool ValidatePassportID()
        {
            if (PassportID == null || PassportID.Length != 9) return false;
            
            Regex PatternPassportID = new Regex(@"\d{9}");
            return PatternPassportID.IsMatch(PassportID);
        }

        private bool ValidateEyeColor()
        {
            if (EyeColor == null) return false;
            
            var validEyeColors = new []
            {
                "amb",
                "blu",
                "brn",
                "gry",
                "grn",
                "hzl",
                "oth"
            };
            return validEyeColors.Any(validEyeColor => validEyeColor == EyeColor);
        }

        private bool ValidateHairColor()
        {
            if (HairColor == null || HairColor.Length != 7) return false;
            
            Regex PatternHairColor = new Regex(@"(#[a-fA-F0-9]{6})");
            return PatternHairColor.IsMatch(HairColor);
        }

        private bool ValidateHeight()
        {
            if (Height == null) return false;
            
            Regex cmPattern = new Regex(@"\d+cm");
            Regex inPattern = new Regex(@"\d+in");
            
            var val = int.Parse(Regex.Match(Height, @"\d+").Value);
            if (cmPattern.IsMatch(Height) && (val >= 150 && val <= 193))
            {
                return true;
            }

            if (inPattern.IsMatch(Height) && (val >= 59 && val <= 76))
            {
                return true;
            }
            
            return false;
        }

        public void Parse(string str)
        {
            var parameters = str.Replace("\n","").Split(null);
            foreach (var row in parameters)
            {
                var field = row.Split(':');
                
                var name = field[0].Trim();
                var val = field[1].Trim();
                switch (name)
                {
                    case "byr":
                        BirthYear = val.Trim();
                        break;
                    case "iyr":
                        IssueYear = val.Trim();
                        break;
                    case "eyr":
                        ExpirationYear = val.Trim();
                        break;
                    case "hgt":
                        Height = val.Trim();
                        break;
                    case "hcl":
                        HairColor = val.Trim();
                        break;
                    case "ecl":
                        EyeColor = val.Trim();
                        break;
                    case "pid":
                        PassportID = val.Trim();
                        break;
                    case "cid":
                        CountryId = val.Trim();
                        break;
                }
            }
        }
    }
}