using System;
public interface Iarithmetic{
     int divisorsum(int n);
}
class Calculator:Iarithmetic{
    int sum=0;
    public int divisorsum(int n){
      for(int i=1;i<=n;i++){
          if(n%i==0){
              sum+=i;
          }
      }
      return sum;
    }
}
namespace DivisorSum.arithmetic
{
    class Program
    {
        static void Main(string[] args)
        {
            int n=Int32.Parse(Console.ReadLine());
             Iarithmetic divsum=new Calculator();
            int x= divsum.divisorsum(n);
            Console.WriteLine(x);
        }
    }
}
