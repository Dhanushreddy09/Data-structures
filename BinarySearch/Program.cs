using System;

namespace BinarySearch
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the key you wanna search for :");
            int key=Int32.Parse(Console.ReadLine());

            int[] Array={23,56,78,549,632,1024,2048,12365,88596};
           int n=Array.Length-1;

            int result=BinarySearch(Array,key,0,n);

           if (result==-1){
           Console.WriteLine("Your key wasn't found in the resource") ;
           }
            Console.WriteLine($"your key was found at {result}");
        }

        static int BinarySearch(int[] array,int key,int l,int r){
            if(r>=1){
                int middle=(l+r)/2;

            if(array[middle]==key){
                return middle;
            }
            if(array[middle]>key){
                return BinarySearch(array,key,0,middle-1);
            }
            return BinarySearch(array,key,middle+1,r);
        }
        return -1;
        }
    }
}
