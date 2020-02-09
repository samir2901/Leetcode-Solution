using System;

namespace defanging_an_ip_address
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter ipv4: ");
            string ip = Console.ReadLine();
            Console.WriteLine(DefangIPaddr(ip));            
        }
        static string DefangIPaddr(string address) {
            string x = string.Join("[.]",address.Split('.'));
            return x;
        }
    }
}
