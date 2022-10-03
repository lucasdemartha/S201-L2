class Televisao:
    def __init__(self, modelo):
        self.modelo = modelo
        self.volumemais = 0
        self.volumemenos = 0
    
    def aumentarVolume(self, volumealto):
        self.volumemais = self.volumemenos + volumealto
 
    def diminuirVolume(self, volumebaixo):
        self.volumemenos = self.volumemais - volumebaixo

    def trocarCanal(self, canal):
        self.canal = canal

    def imprime(self):
        print(f'Modelo da TV: {self.modelo}')
        print(f'Volume aumentado: {self.volumemais}')
        print(f'Volume diminuido: {self.volumemenos}')
        print(f'Canal: {self.canal}')

if __name__ == '__main__':
    tv = Televisao(input("Insira o modelo da TV: "))
    tv.aumentarVolume(70)
    tv.diminuirVolume(27)
    tv.trocarCanal("Canal#1")
    tv.imprime()