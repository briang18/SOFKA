#Brian David Guevara Niñoss
import random
import json
listaCarros=[]
listaJugadores=[]
listaConductores=[]
listaPodio=[]
listaCarril=[]
class Pista:
    pass
    def __init__(self,limite):
        self.carriles=6
        self.limite=10000
class Carro:
    pass
    def __init__(self,numCarro,conductorCarro,carrilCarro,velocidad,posicion):
        self.numCarro=numCarro
        self.conductorCarro=conductorCarro
        self.carrilCarro=carrilCarro
        self.velocidad=velocidad
        self.posicion=posicion
    def recorrido(self):
        self.posicion=self.posicion+ self.velocidad
    def turno(self):
        self.velocidad=(random.randrange(6)+1)*100
        print(f'Avanza {self.velocidad}')

class Juego:
    pass
    def __init__(self,jugadores):
        self.jugadores=jugadores
class Carril:
    pass
    def __init__(self,numCarril,numCarro):
        self.numCarril=numCarril
        self.numCarro=numCarro
#jugador carro conductor juego podio pista jugador

class Conductor:
    pass
    def __init__(self,nombreConductor,numCarro):
        self.nombreConductor=nombreConductor
        self.numCarro=numCarro
class Podio:
    pass
    def __init__(self,primero,segundo,tercero):
        self.primero=primero
        self.segundo=segundo
        self.tercero=tercero
    def resultado(self):
        print(f'Resultado\nPrimer lugar: {self.primero.conductorCarro}\nSegundo lugar: {self.segundo.conductorCarro}\nTercer lugar: {self.tercero.conductorCarro}')     
    def llenarpodio(self):
        listaPodio.append(self.primero.conductorCarro)
        listaPodio.append(self.segundo.conductorCarro)
        listaPodio.append(self.tercero.conductorCarro)
class Jugador:
    pass
    def __init__(self,nombreJugador,numeroCarro):
        self.nombreJugador=nombreJugador
        self.numeroCarro=numeroCarro

def configurarJuego():
    while(True):
        a=int(input('Ingrese la cantidad de jugadores, minimo 3 y maximo 6 '))
        if a>=3 and a<=6:
            objeto =Juego(a)
            break
        else:
            print('El numero de jugadores que ingresó no es valido')
            continue

    return objeto

def llenarjugadores(objJuego):
    count=1
    for i in range(objJuego.jugadores):
        nombrec=input(f'Ingrese el nombre del jugador {count} ')
        objeto=Jugador(nombrec,count)
        listaJugadores.append(objeto)
        objeto=Carro(count,nombrec,count,0,0)
        listaCarros.append(objeto)
        objeto= Conductor(nombrec,count)
        listaConductores.append(objeto)
        objeto= Carril(count,count)
        listaCarril.append(objeto)
        count+=1   
       
def jugar():
    count=0
    l=[]
    count=0
    while(True):    
        for i in listaCarros:
            if i.posicion >=10000:
                while(True):    
                    if i in l:
                        break
                    l.append(i)
                    count+=1
                    break
                #print(l)
            else:
                print(f'Es el turno del jugador {i.numCarro} {i.conductorCarro}')
                i.turno()
                i.recorrido()
                print(f'Posicion= {i.posicion}')
           
        if count>=3:
            break
    objeto=Podio(l[0],l[1],l[2])
    return objeto
def leerbase():
    try:    
        f=open("juegos.txt","r")
        base=f.read()
        f.close()
        base=json.loads(base)
    except:
        base=[]
        base=json.dumps(base, indent=4)
        f=open("juegos.txt","w")
        f.write(base)
        f.close()
        f=open("juegos.txt","r")
        base=f.read()
        f.close()
        base=json.loads(base)
    return base

def escribirbase(a):
    j= json.dumps(a, indent=4)
    f=open("juegos.txt","w")
    f.write(j)
    f.close()
    

#Programa
juego=configurarJuego()
llenarjugadores(juego)
podio=jugar()
podio.resultado()
base=leerbase()
podio.llenarpodio()
base.append(listaPodio)
escribirbase(base)


