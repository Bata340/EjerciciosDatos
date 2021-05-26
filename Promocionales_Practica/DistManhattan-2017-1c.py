puntos = [[1,2], [1,3], [1,5], [2,3], [2,8], [3,3], [4,1], [4,9], [7,8], [9,9], [12,2], [13,4]]
distancias = []


#Distancias
for i in range(len(puntos)):
    for j in range(len(puntos)-(i+1)):
        puntos_comparados = [puntos[i], puntos[i+1+j]]
        distancia_puntos_comparados = abs(puntos[i][0]-puntos[i+1+j][0]) + abs(puntos[i][1]-puntos[i+1+j][1])
        par_distancia = [puntos_comparados, distancia_puntos_comparados]
        distancias.append(par_distancia)

#Selection Sort
for i in range(len(distancias)):
    minimo_index = i
    minimo = distancias[i][1]
    for j in range(len(distancias)-i-1):
        if(distancias[j+i+1][1] < minimo):
            minimo_index = j+1+i
            minimo = distancias[j+i+1][1]
    aux = distancias[minimo_index]
    distancias[minimo_index] = distancias[i]
    distancias[i] = aux

for distancia in distancias:
    print("Punto 1:" + str(distancia[0][0]) + ", Punto 2:" + str(distancia[0][1]) + ", Distancia: " + str(distancia[1]))

print("\nCant Distancias = " +str(len(distancias)))
