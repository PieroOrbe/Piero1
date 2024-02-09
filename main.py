import base
#ACA ESTUVO EL OTRO PIERO
#prueba 2 de edit pc
Piero = base("Piero", 100, 20)
JefeFinal = base ("JefeFinal",100,10)

Piero.atributo()
JefeFinal.atributo()

def combate (j1,jf):
    turno= 0
    while j1.esta_vivo() and jf.esta_vivo():
        print("TURNO ", turno)
        print("VIDA: ", j1.nombre, " : ", j1.vida)
        print("VIDA: ", jf.nombre, " : ", jf.vida)
        print("==========================")
        print("ACCION DE ",j1.nombre, " ",sep="")
        print("==========================")
        print("1. ATACAR")
        print("2. ESQUIVAR")
        opcion= input("Accion ")
        if opcion=="1":
                print("Decides atacar a ", jf.nombre)
                j1.ataque(jf)
                #print("ACCION DE ",jf.nombre, " ",sep="")
        else:
                j1.escudo()
        print("==========================")
        print("Accion del BOSS")
        if opcion=="2" :
                print(j1.nombre, " Uso escudo")
        else :
                jf.ataque(j1)
        print("==========================")
        
        turno += 1
    if j1.esta_vivo():
            print("HA GANADAO",j1.nombre)
    elif jf.esta_vivo():
            print("HA GANADO: ", jf.nombre)
    else: 
            print("EMPATE")
        
combate(Piero,JefeFinal)