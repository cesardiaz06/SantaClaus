import threading
import time
#def funcion (inicio, fin):

def hola_mundo (nombre, segundos): 
    print("Hilo "+nombre +" activo, espere...")
    #print("Hilo activo" + nombre)
    #print("Wait hilo #1")
    #print("Wait hilo #2")
    time.sleep(segundos)

    print("Finalizo hilo" + nombre)
    #time.sleep(5)

if __name__ == '__main__':
    thread1 = threading.Thread(target=hola_mundo, args=("#1", 5))
    thread2 = threading.Thread(target=hola_mundo, args=("#2", 13))
    thread3 = threading.Thread(target=hola_mundo, args=("#3", 10))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

#global hilo terminado
#Bucle de inicio a fin, con espera de un segundo
#for valor in range(inicio, Fin):
#print "Hilo: "+str(valor)
#time.sleep(5)
#narca hilo terminado
#hilo terminado True
#print "Terminado hilo "