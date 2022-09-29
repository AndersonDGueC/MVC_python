from ModeloSencillo import Sistema
from VistaSencilla import VentanaPrincipal
from PyQt5.QtWidgets import QApplication
import sys

class Coordinador():
        def __init__(self, vista, modelo):
            self.__mi_vista=vista
            self.__mi_modelo=modelo
        #recibe desde la vista y lo envia al modelo directamente
        def recibirInfoVista(self,n,d,e):
            return self.__mi_modelo.agregarReserva(n,d,e)
        #recibir desde la vista el documento
        def recibirDocVista(self,d):
            return self.__mi_modelo.recibirDoc(d)
        

def main():
    app=QApplication([])
    mi_modelo=Sistema()
	#indexamos la vista a la instancia de la clase controlador
    mi_vista=VentanaPrincipal()
    mi_controlador=Coordinador(mi_vista,mi_modelo)
	#con el metodo del objeto mi vista de la clase Ventana Principal
	#conectamos el controlador e igualmente a mi modelo
    mi_modelo.asignarCoordinadorM(mi_controlador)
    mi_vista.asignarCoordinadorV(mi_controlador)
    mi_vista.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()	
