class Cavalo:
    def __init__(self,velocidade, nome, cor):
        self.velocidade = velocidade
        self.nome = nome
        self.cor = cor
        self.pos = 0
    
    def move(self):
        if(self.pos < 200):
            self.pos += self.velocidade*4
        if(self.pos >= 200):
            print(f"{self.nome} terminou a corrida!")
    
if __name__ == '__main__':
    
    cav1 = Cavalo(10,"pangare","branco")
    cav2 = Cavalo(11,"bidu","preto")
    cav3 = Cavalo(12,"jorge","marrom")

    cav1.move()
    cav2.move()
    cav3.move()
    cav1.move()
    cav2.move()
    cav3.move()
    cav1.move()
    cav2.move()
    cav3.move()
    cav1.move()
    cav2.move()
    cav3.move()
    cav1.move()
    cav2.move()
    cav3.move()

