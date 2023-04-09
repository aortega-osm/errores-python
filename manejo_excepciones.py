# 10/0
# Zerodivisionerror
from error_personalizado import numeroIdenticos
resultado= None
a=int(input("Proporciona un numero: "))
b=int(input("Proporciona un numero: "))
c=10
# Siempre hay que definir la variable ya que seran utilizadas fuera del bloque
# En cambio a, b y c. no, por lo tanto pueden ser utilizadas exclusivamente dentro del codigo

try:
    resultado= a / b
    if a == b:
        raise numeroIdenticos("numeros identicos")
except ZeroDivisionError as e:
 print(f"ZeroDivision---Hubo un error por {e}")
except TypeError as e:
 print(f"TypeError---Hubo un error:{e}")
except Exception as e:
 print(f"Hubo un error:{e}")
 print(resultado)
else:
    print("No occurrio ningun error")
# Si en vez de un numero pusieramos una cadena se generaria otro tipo de error nuevo TypeError