#1.la siguiente funcion debera retornar la suma de sus parametros
def suma(a,b):
  #reemplazar pass por la sintaxis correcta
  return a+b

#2. la funcion debera retornar 'es menor' o 'es mayor' segun la edad que pase por parametro
def is_greater_than(edad):
  #reemplazar pass por la sintaxis correcta
  
  if edad >=18:
    return("es mayor")
  else :
    return("es menor")

#3. la funcion recibe como parametros dos datos el primero arr recibe una array(lista) el segundo num un numero entero positivo, 
# la funcion debera retornar un nuevo array con el num insertado en la tercera posicion del array
def new_array(arr,num):
  #reemplazar pass por la sintaxis correcta
  if isinstance(arr, list) and isinstance(num, int) and num >= 0:
        if len(arr) >= 3:
            arr.insert(2, num)
        else:
            arr.append(num)
        return arr
  else:
        return "Error: El primer argumento debe ser una lista y el segundo un número entero positivo."

#4. la funcion recibe una array debera retornar la suma de los numero ejm: [4,2,8,10] retornara 24
numero=[1,2,3]
suma =0
for  x in numero:
  suma +=x
  numero.remove(x)
  print (suma)

