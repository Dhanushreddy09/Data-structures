using System;

namespace BubbleSort
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array={23,98,78,56,42,963};
            //int temp;
            
            for(var i=0;i<array.Length;i++){
                Console.WriteLine(array[i+1]);
               /* for(var j=0;j<array.Length-i;i++){
                    if(array[j]>array[j+1]){
                    temp=array[j];
                    array[j]=array[j+1];
                    array[j+1]=temp;
                    }
                    Console.Write(array[i]+" ");
                }
                */
            }
          
        }
    }
}
