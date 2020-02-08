using System;

namespace prob_1342
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a number: ");
            int x = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Steps: " + NumberOfSteps(x));
        }

        static int NumberOfSteps (int num) {
        int steps=0;
        while(num!=0){
            if(num % 2==0){
                num = num/2;
                steps += 1;
            }else{
                num = num-1;
                steps += 1;
            }
        }
        return steps;
    }
    }
}
