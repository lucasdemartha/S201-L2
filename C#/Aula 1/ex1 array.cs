using System;

class Program {
    public static void ChamaArray(int num)
{
    int[] array = new int[10];
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = i * num;
    }
    Console.WriteLine(string.Join(", ", array));
}
  public static void Main (string[] args){
    
    int num1 = int.Parse(Console.ReadLine());
    int num2 = int.Parse(Console.ReadLine());
    int soma = num1 + num2;
    ChamaArray(soma);
    
  }
}