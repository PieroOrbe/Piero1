import random

class base:
    def __init__(self, nombre, vida, daño):
        self.nombre= nombre
        self.vida= vida
        self.daño= daño
        
    def atributo(self):
        print("Los atributos de ",self.nombre)
        print("VIDA: ",self.vida)
        print("DAÑO: ",self.daño)
    
    def esta_vivo(self):
        return self.vida>0
    
    def morir(self):
        self.vida=0
        print(self.nombre," ha muerto")
    
    def ataque (self, boss):
        #print(self.daño, " + ", boss.daño)
        crit= random.randint(1,100)
        if crit >0 and crit < 21 :
            self.daño= self.daño * (1.5)
            print(self.nombre,"*SACO CRITICO*")
        boss.vida= boss.vida - self.daño
        if boss.esta_vivo():
            pass
            #print("la vida de ",boss.nombre," es :", boss.vida)
            #print("la vida de ", self.nombre, " es : ", self.vida)
        else :
            boss.morir()
                
    def escudo(self):
        print("Uso un escudo ")
        
            
    