using System;

public interface Ilinearsearch{
     void calculate(int[] array,int key);
}

class calculation:Ilinearsearch{
    public void calculate(int[] array,int key){
            int index=-1;

            for(var i=0;i<array.Length;i++){
               if(array[i]==key){
                   index=i;
               }
            }

            if(index==-1){
                Console.WriteLine("key wasn't found");
            }
            else{
            Console.WriteLine($"key was found at {index}");
            }
    }
}
namespace Linearsearch
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array={23,56,87,23,12,49,25};

            Console.WriteLine("Enter a key you want to find out");
            int key=Int32.Parse(Console.ReadLine());

             Ilinearsearch lsearch=new calculation();
              lsearch.calculate(array,key);
        }
    }
}
