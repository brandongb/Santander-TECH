import lifestore_file as data #Primero importamos los datos con el nombre de data

boleano_usuario = True #Boleano hasta que el usuario haya sido el correcto
boleano_contraseña = True #Boleano hasta que la contraseña sea la correcta

print("Ingrese el nombre del usuario:")
while boleano_usuario : 
    usuario = input()
    if usuario != "Gerente": #Si el nombre es distinto de gerente, tiene que volver a ingresar el nombre
        print("El usuario no está registrado en el sistema")
    else:
        boleano_usuario = False

print("Ingrese la contraseña")
while boleano_contraseña : 
    contraseña = input()
    if contraseña != "1234": #Si el nombre es distinto de gerente, tiene que volver a ingresar el nombre
        print("Contraseña incorrecta")
    else:
        boleano_contraseña = False   
        
#Debido a que se ocupa el mismo procedimiento para casi todos los pasos
# Es mejor definir una función en vez de escribir el codigo decenas de veces

def Sorteo(Data, x): #Data es el array y x el índice por el que se quiere ordenar
    Data_copy = [i for i in Data] #Generamos una copia Data, para no modificar el array original
    num_data = len(Data_copy) #El número de datos que se tienen
    for i in range(0, num_data): 
        for j in range(0, num_data-i-1):
            if (Data_copy[j][x] > Data_copy[j+1][x]): #Comparamos el j-esimo y j+1-esimo elementos, por su entrada "x" 
                ref = Data_copy[j] #Guardamos la j-esima lista
                Data_copy[j] = Data_copy[j+1] #Se reordenan
                Data_copy[j+1] = ref #Lo que sea hace es intercambiar de posicion  entre j y j+1 
    return Data_copy #Regresa la lista de listas ordenadas por el x-ésimo elemento 

num_productos = len(data.lifestore_products) #Vemos cuántos productos hay 

print('A continuación se muestra la lista de los productos más vendidos y los menos vendidos \n ¿Cuántos elementos desea ver? (Lo recomendado es 50)')
print(f'** Debe ser un número entero menor a {num_productos}**') #Preguntamos al usuario cuantos elementos desea ver
ventas_num = int(input())
print()
print(f'Se muestran el número de ventas y los detalles de los {ventas_num} más vendidos')
print()
ventas_por_producto = [[i+1,0] for i in range(0, num_productos)] #Generamos una lista de lista
#La primera entrada es el id del producto y el segundo va a ser el número de ventas de dicho producto

for i in data.lifestore_sales: #Revisamos todas las ventas
    index = i[1]-1 #El índice correspondiente al id_producto. El menos uno es debido a que Python empieza en 0
    ventas_por_producto[index][1] += 1 #Aumentamos el valor del número de ventas de ese producto

ventas_por_producto_ord = Sorteo(ventas_por_producto, 1)   #Lo ordenamos por el indice 1, es decir, el número de ventas

for i in range(num_productos, num_productos-ventas_num, -1):#Recordemos la lista al reves, para empezar por los mas vendidos
    producto_id = ventas_por_producto_ord[i-1][0]-1 #Imprimimos el número de ventas y los detalles del producto
    print(ventas_por_producto_ord[i-1][1], data.lifestore_products[producto_id])

print()
print(f'Se muestran el número de ventas y los detalles de los {ventas_num} menos vendidos')
print()

for i in range(0, ventas_num, 1): #Lo mismo pero ahora empezamos la lista de menor a mayor
    producto_id = ventas_por_producto_ord[i][0]-1
    print(ventas_por_producto_ord[i][1],data.lifestore_products[producto_id])
    
    
busquedas_por_producto = [[i+1,0] for i in range(0, num_productos)] #lista de listas, el primero es el id del producto, el segundo el numero de busqeudas
for i in data.lifestore_searches: #Revisamos todas las busquedas
    index = i[1]-1 #El índice correspondiente al id_producto
    busquedas_por_producto[index][1] += 1 #Aumentamos el valor del número de ventas de ese producto
    
busquedas_por_producto_ord = Sorteo(busquedas_por_producto, 1) #Ordenamos los elementos por el número de busquedas

print()
print()   
print('A continuación se muestra la lista de los productos más buscados y los menos buscados \n ¿Cuántos elementos desea ver? (Lo recomendado es 50)')
print(f'** Debe ser un número entero menor a {num_productos}**')
busquedas_num = int(input())    #PEddimos un numero entero de elementos que el usuario desee ver
print()  
print(f'Se muestran el número de busquedas y los detalles de los {busquedas_num} más buscados')
print()
for i in range(num_productos, num_productos-busquedas_num, -1): #Empezamos al revés para ir del más buscado al menos
    producto_id = busquedas_por_producto_ord[i-1][0]-1
    print(busquedas_por_producto_ord[i-1][1],data.lifestore_products[producto_id])
print()
print()
print(f'Se muestran el número de busquedas y los detalles de los {busquedas_num} menos buscados')
print()
for i in range(0, busquedas_num, 1):
    producto_id = busquedas_por_producto_ord[i][0]-1 #Imprimimos el número de busquedas y los detalles del producto
    print(busquedas_por_producto_ord[i][1],data.lifestore_products[producto_id])
    
    
promedio_score = [[i+1, 0, 0, 0] for i in range(0, num_productos)]
#Lista de listas, el primero es el id del producto, el segundo es la suma de las reseñas
#la tercera es el número de reseñas y la cuarta es el promedio, es decir,, la segunda entre la primera
for i in data.lifestore_sales:
    index = i[1]-1
    promedio_score[index][1] += i[2]
    promedio_score[index][2] += 1
for i in promedio_score: #Para obtener el promedio nos fijamos que no se divida entre 0
    if i[2] != 0:
        i[3] = i[1]/i[2]

print()
print()   
print('A continuación se muestra la lista de los productos con mejores y peores reseñas \n ¿Cuántos elementos desea ver? (Lo recomendado es 20)')
print(f'** Debe ser un número entero menor a 42**') #Debe ser 42 porque si su score es 0, significa que no ha tenido ventas
num_reseñas = int(input())  
promedio_score_ord = Sorteo(promedio_score, 3) #Ordenamos la lista de listas respecto al promedio
print(f'Se muestran el score y los detalles de los {num_reseñas} con mejores reseñas')
print()
for i in range(num_productos,num_productos-num_reseñas, -1): #Empezamos de mayor  a menor
    producto_id = promedio_score_ord[i-1][0]-1 #id_product
    print(promedio_score_ord[i-1][3],data.lifestore_products[producto_id])
print()
print()
print(f'Se muestran el score y los detalles de los {num_reseñas} con las peores reseñas')
print()
flag = 0
indice = 0
while (flag < num_reseñas): #Aqui es con un while porque si su score 0 no signifca que haya tenido la peor reseña, sino que no ha tenido reseñas
    if promedio_score_ord[indice][3] != 0:
        producto_id = promedio_score_ord[indice][0]-1
        print(promedio_score_ord[indice][3],data.lifestore_products[producto_id])
        flag += 1
    indice += 1
    
categorias = [] #Array donde vamos a guardar el nombre de las categorias
for i in data.lifestore_products: #recorremos todos los productos
    categoria_pro = i[3] #Obtenemos la categoria del producto
    if categoria_pro not in categorias: #Si no ha sido agregada a categorias
        categorias.append(categoria_pro) #La agregamos
        
num_categorias = len(categorias) #Guardamos el número de categorias hechas
 
#Lista de listas, la primera la categoria y la segunda el número de ventas de dicha categoria
categorias_ventas = [[categorias[i],0] for i in range(0, num_categorias)]
#Lista de listas, la primera la categoria y la segunda el número de busquedas de dicha categoria
categorias_busquedas = [[categorias[i],0] for i in range(0, num_categorias)]

for i in data.lifestore_searches: #Revisamos todas las busqeudas hechas
    id_producto = i[1]-1 #Id del producto
    tipo_de_produto = data.lifestore_products[id_producto][3] #Vemos la categoria del producto
    for j in range(0, num_categorias):
        checar_categoria = categorias[j] #Tenemos que ver que categoria es
        if tipo_de_produto == checar_categoria:
            categorias_busquedas[j][1] += 1 #Agregamos +1 a la categoria que pertence
            break

for i in data.lifestore_sales: #Lo mismo que la anteior pero ahora con las ventas
    id_producto = i[1]-1
    tipo_de_produto = data.lifestore_products[id_producto][3]
    for j in range(0, num_categorias):
        checar_categoria = categorias[j]
        if tipo_de_produto == checar_categoria:
            categorias_ventas[j][1] += 1
            break
            
categorias_ventas_ord = Sorteo(categorias_ventas, 1) #Ordenamos las categorias por el numero de ventas
categorias_busquedas_ord = Sorteo(categorias_busquedas, 1) #Ordenamos las categorias por el numero de busquedas

print()
print()
print("A continuación se muestra el número de busquedas por categoria:")
print()
for i in range(num_categorias-1, -1, -1): #Recorremos las categorias de mayores busquedas a menores
    cate = categorias_busquedas_ord[i]
    print(cate[1], cate[0]) #Imprimos el numero de busquedas y la categoria

print()
print()
print("A continuación se muestra el número de ventas por categoria:")
print()
for i in range(num_categorias-1, -1, -1): #Lo mismo pero para ventas
    cate = categorias_ventas_ord[i]
    print(cate[1], cate[0])
    
    
#Lista de listas, el primero es el nombre del mes
#el segundo el mes en numero, el tercero el numero de ventas en ese mes
#El cuarto el numero de ingresos en dicho mes
ventas_meses = [['Enero',1,0,0],['Febrero',2,0,0],['Marzo',3,0,0],
                ['Abril',4,0,0],['Mayo',5,0,0],['Junio',6,0,0],
                ['Julio',7,0,0],['Agosto',8,0,0],['Septiembre',9,0,0],
                ['Octubre',10,0,0],['Noviembre',11,0,0],['Diciembre',12,0,0]]

for i in data.lifestore_sales: #Recorremos las ventas
    mes_index = int(i[3][3:5])-1 #obtenemos el indice del mes
    prod_index = i[1]-1 #El producto del indice
    if i[4] == 0: #La cuarta entrada del producto es si fue regresado
        #Si fue regresado no lo contamos como venta y no contamos los ingresos
        precio = data.lifestore_products[prod_index][2] #Obtenemos el precio
        ventas_meses[mes_index][2] += 1 #Aumentamos una venta
        ventas_meses[mes_index][3] += precio #El ingreso de dicha venta
        
#Ordenamos por el segundo indice, es decir, por el numero de ventas
mes_numero_ventas_ord = Sorteo(ventas_meses, 2) 
#Ordenamos por el tercer indice, es decir, por el ingreso obtenido
mes_ingresos_ord = Sorteo(ventas_meses, 3)

print()
print()
print('A continuación se muestra el mes y el número de ventas:')
print()
#Lo recorremos la revés para mostrar primero los meses con mayores ventas
for i in range(len(mes_numero_ventas_ord)-1,-1,-1): 
    print(mes_numero_ventas_ord[i][0],':', mes_numero_ventas_ord[i][2])
print()
print()
print('A continuación se muestra el mes y el número de ingresos:')
print()
#Lo recorremos la revés para mostrar primero los meses con mayores ingresos
for i in range(len(mes_ingresos_ord)-1,-1,-1):
    print(mes_ingresos_ord[i][0],':', mes_ingresos_ord[i][3])
    
ingreso_total = 0
print()
print()
for i in ventas_meses:
    ingreso_total += i[3] #Aumentamos el numero de ingresos por mes para obtener el total
print('Total de ingreso anual:', ingreso_total) #Imprimos el ingreso total del año



#Lista de lista, el primero es el nombre de la categoria
#El segundo es el número de distintos producots
#El tercero es el total de productos, de esta categoria, guardados en stock
categorias_stock = [[categorias[i],0,0] for i in range(0, num_categorias)]
for i in data.lifestore_products: #Revisamos los productos
    tipo_de_produto = i[3]
    for j in range(0, num_categorias):
        checar_categoria = categorias[j]
        if tipo_de_produto == checar_categoria:
            categorias_stock[j][1] += 1 #Agregamos mas un producto encontrado
            categorias_stock[j][2] += i[4] #Agregamos cuantos hay en stock del mismo producto
            break
            
#Lista de liista, el primero es el nombre de la categoria
#el segundo los ingresos de los productos vendidos
categorias_ingresos = [[categorias[i],0] for i in range(0, num_categorias)]
for i in data.lifestore_sales: #Revisamos en las ventas
    id_producto = i[1]-1
    tipo_de_produto = data.lifestore_products[id_producto][3]
    costo = data.lifestore_products[id_producto][2]
    for j in range(0, num_categorias):
        checar_categoria = categorias[j]
        if tipo_de_produto == checar_categoria:
            categorias_ingresos[j][1] += costo #Guardamos el ingreso por categoria
            break