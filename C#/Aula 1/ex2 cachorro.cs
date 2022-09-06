using System;

  public  class Cachorro {
        public string nome;
        public int idade;
        public Cachorro(string nome, int idade) {
            this.nome = nome;
            this.idade = idade;
        }
        public void showNome() {
            Console.WriteLine(nome);
        }
        public virtual void showIdade() {
            Console.WriteLine(idade);
        }
    }

    public class CachorroPequeno : Cachorro {
        public CachorroPequeno(string nome, int idade) : base(nome, idade) {
        }

        public override void showIdade() {
            Console.WriteLine(idade+"<<< idade do pequeno");
        }
    }


    public class CachorroGrande : Cachorro {
         private string tamanho = "0";
        public string getTamanho() {
            return tamanho;
        }
        public void setTamanho(string tamanho) {
            this.tamanho = tamanho;
        }
        public CachorroGrande(string nome, int idade) : base(nome, idade) {
        }
    
        public override void showIdade() {
            Console.WriteLine(idade+"<<< idade do cachorro grande");
        }
    }
class Program {

  
    static void Main(string[] args) {
        Cachorro cachorro = new Cachorro("Bobby", 3);
        cachorro.showNome();
        cachorro.showIdade();
        CachorroPequeno cachorroPequeno = new CachorroPequeno("Jimmy", 7);
        cachorroPequeno.showNome();
        cachorroPequeno.showIdade();
        CachorroGrande cachorroGrande = new CachorroGrande("Bob", 9);
        cachorroGrande.showNome();
        cachorroGrande.showIdade();
        Console.WriteLine(cachorroGrande.getTamanho());
        cachorroGrande.setTamanho("Grande");
        Console.WriteLine(cachorroGrande.getTamanho());

        
    }



}