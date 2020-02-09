using System;

namespace prob_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = {2,7,11,15};
            Console.Write("Enter a number: ");
            int target = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("[{0}]",string.Join(", ", TwoSum(arr,target)));
        }
        static int[] TwoSum(int[] nums, int target){
            int i=0;
            int j=0;
            for(i=0;i<nums.Length;i++){
                for(j=i+1;j<nums.Length;j++){
                    if(nums[i] + nums[j] == target){
                        int[] arr = new int[] {i,j};
                        return arr;
                    }
                }
            }
            return new int[] {-1,-1};                        
        }
    }
}
