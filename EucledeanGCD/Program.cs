using System;

namespace EucledeanGCD
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the value of 1st number :");
              int n=Int32.Parse(Console.ReadLine());
              Console.WriteLine("Enter the value of 2nd number :");
              int m=Int32.Parse(Console.ReadLine());
              int x=calculate(n,m);
              Console.WriteLine(x);
        }

        // calculate Method

        static int calculate(int m,int n){
            // Base cases

            if(m==0)
            return n;

            if(n==0)
            return m;
            
            if(m==n){
                return m;
            }
            int max,min;
            if(n>m){
                max=n;
                min=m;
            }
            else{
               max=m;
               min=n;
            }
            return calculate(min,max-min);

        } 

    }
}
