class Reserva:
    def __init__(self,ppal=None):
       self.__nombre=''
       self.__documento=0
       self.__equipo=''

    def asignarNombre(self,n):
       self.__nombre=n

    def asignarDocumento(self,d):
       self.__documento=d

    def asignarEquipo(self,e):
       self.__equipo=e

    def verNombre(self):
       return self.__nombre

    def verDocumento(self):
       return self.__documento

    def verEquipo(self):
       return self.__equipo

class Sistema:
    def __init__(self):
       self.__stock={}

    def verificarExiste(self,d):
       return d in self.__stock

    def agregarReserva(self, n, d, e):
       if self.verificarExiste(d):
         return 'el paciente ya esta registrado'
       else:
         print(n)
         print(d)
         print(e)
         m=Reserva()
         m.asignarNombre(n)
         m.asignarDocumento(d)
         m.asignarEquipo(e)
         self.__stock[d]=m
         return 'reserva exitosa'

    def camposDialogo(self,d):
       if self.verificarExiste(d)==False:
         return None
       else:
         rec=self.__stock[d]
         dicm={'nombre':rec.verNombre(), 'documento':rec.verDocumento(), 'equipo':rec.verEquipo()}

    def asignarCoordinadorM(self,c):
        self.__miControlador=c
