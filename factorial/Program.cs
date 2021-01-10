using System;

namespace factorial
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number to find out factorial for :");
            string x=Console.ReadLine();
            int y=Convert.ToInt32(x);
            int fact=factorial(y);
            Console.WriteLine(fact);
            static int factorial(int num){
                if(num<0){
                    throw new ArgumentException("factorial cannot be calculated for numbers less than zero");
                }
        return num==0?1:num*factorial(num-1);           
            }
        }
    }
}
