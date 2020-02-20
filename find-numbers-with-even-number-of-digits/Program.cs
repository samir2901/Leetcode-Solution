using System;

namespace find_numbers_with_even_number_of_digits
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array = {12,345,2,6,7896};
            Console.WriteLine(FindNumbers(array));
            
        }
        static int FindNumbers(int[] nums){
            int count = 0;
            foreach (var num in nums)
            {
                if ((Convert.ToString(num)).Length % 2 == 0){
                    count++;
                }
            }
            return count;
        }
    }
}
