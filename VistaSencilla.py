import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit, QTextEdit
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.uic import loadUi
#ventana principal creada
class VentanaPrincipal(QMainWindow):
	def __init__(self,ppal=None):
	    super().__init__(ppal)
	    loadUi('ventana_menu.ui',self)
	    self.setup()

	def setup(self):
	    self.ingresar_reserva.clicked.connect(self.abrir_ventana_ingresar)
	    self.ventanas=list()

	def abrir_ventana_ingresar(self):
	    ventanaIngreso=VentanaIngresar(self)
	    self.ventanas.append(ventanaIngreso)
	    ventanaIngreso.show()
        #metodo para conectar el controlador a la vista
        #este metodo se realiza desde el controlador
	def asignarCoordinadorV(self,c):
	    self.__miControlador=c
        #funcion para enviar los datos recolectados al controlador

	def recibir_info2daVen(self,n,d,e):
            r=self.__miControlador.recibirInfoVista(n,d,e)
            QMessageBox.information(self,'mensaje informativo',r)
#ventana ingresar datos creada
class VentanaIngresar(QDialog):
	def __init__(self,ppal=None):
	   super().__init__(ppal)
	   loadUi("ventana_ingreso.ui",self)
	   #Este atributo coloca a la ventana Principal como padre
	   self.__ventana_padre=ppal
	   self.setup()
	
	def setup(self):
	    self.campo_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
	    self.campo_documento.setValidator(QIntValidator())
	    self.campo_equipo.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
	    self.boton_ingresar.accepted.connect(self.opcion_aceptar)
	    self.boton_ingresar.rejected.connect(self.opcion_cancelar)

	def opcion_aceptar(self):
	    n=self.campo_nombre.text()
	    #print(n)
	    d=self.campo_documento.text()
	    #print(d)
	    e=self.campo_equipo.text()
	    #print(e)
	    self.__ventana_padre.recibir_info2daVen(n,d,e)
	    self.__ventana_padre.show()
	
	def opcion_cancelar(self):
	    self.__ventana_padre.show()

#Test de la vista, para encontrar posibles fallas
"""			
def main():
	app=QApplication([])
	mi_vista=VentanaPrincipal()
	mi_vista.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
"""	
