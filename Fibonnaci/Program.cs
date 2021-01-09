using System;

namespace factorial
{
    class fibonacci{
        public fibonacci(int num){
if(num<=0){
    throw new ArgumentException("fibonacci series is not possible for numbers less than or equal to 0");
}
   var prev=0;
   var current=1;
Console.Write(prev);
   while(num!=0){
       Console.Write(",");
       Console.Write(current);
var next=prev+current;
prev=current;
current=next;
num--;
   }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number to find out the fibonacci series");
            string x=Console.ReadLine();
            int y=Convert.ToInt32(x);
            fibonacci series=new fibonacci(y);
        }
    }
}
