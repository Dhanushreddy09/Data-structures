using System;

namespace HelloWorld
{
    class Program
    {
      static void Main(string[] args)
        {
            string userinput;
          int  i,j;
          Console.WriteLine("enter the value of i..");
           userinput=Console.ReadLine();
           i=Convert.ToInt32(userinput);
           Console.WriteLine("enter the value of j");
           userinput=Console.ReadLine();
           j=Convert.ToInt32(userinput);
            int[,] matrix=new int[i,j];
         for(int k=0;k<i;k++){
             for(int l=0;l<j;l++){
                 Console.WriteLine($"Enter the value of matrix[{k},{l}]");
                 userinput=Console.ReadLine();
                 matrix[k,l]=Convert.ToInt32(userinput);
             }
         }
         for(int m=0;m<i;m++){
             for(int n=0;n<j;n++){
                 Console.Write(matrix[m,n]);
                 Console.Write(" ");
             }
             Console.WriteLine();
         }
        }

    }
    
    
           
}
