using System;

namespace System.Linq
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

              MultiplenumbersGCD(12,20,24);

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

        // Multiple Numbers

        static void MultiplenumbersGCD(params int[] values){
            int gcd  = values.Aggregate((current,next)=>calculate(current,next)); 
               Console.WriteLine(gcd);
               }

    }
}
