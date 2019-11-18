class Somador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def soma(self):
        return self.x + self.y

class Main:
    def main(self):
        teste = Somador(10, 50)
        print(teste.soma())

Main().main()