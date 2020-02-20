using System;

namespace jewels_and_stones
{
    class Program
    {
        static void Main(string[] args)
        {
            string J, S;
            Console.Write("Enter J: ");
            J = Console.ReadLine();
            Console.Write("Enter S: ");
            S = Console.ReadLine();
            Console.WriteLine(NumJewelsInStones(J,S));        
        }
        static int NumJewelsInStones(string J, string S){
            var count = 0;
            foreach (var character in S)            
            {
                if(J.Contains(character)){
                    count++;
                }
            }
            return count;
        }
    }
}
