import math as m
#definindo o inicio das variáveis
maior_distancia= 0
menor_distancia= 10000000
maior_distancia_x=0
maior_distancia_y=0
menor_distancia_y=0
menor_distancia_x=0
quadrante1=0
quadrante2=0
quadrante3=0
quadrante4=0
#definindo a origem do plano cartesiano
origem_x=int(input("Digite o ponto de origem do x : "))
origem_y=int(input("Digete o ponto de origem do y : "))
#definindo a quantidade de pontos que serão analisados
pontos=int(input("Número de pontos para analisar : "))
#estrutura de repetição para analisar os pontos
while pontos != 0 :
  x=int(input("Digite o ponto x : "))
  y=int(input("Digete o ponto y : "))
  distancia_x= x - origem_x
  distancia_y= y - origem_y

  #distancia dos pontos ate o meio do plano por meio de pitagoras
  distancia_total = m.sqrt((distancia_x**2)+(distancia_y**2))
  #descobrindo o ponto com a maior distancia
  if distancia_total > maior_distancia :
    maior_distancia = distancia_total
    maior_distancia_x=x
    maior_distancia_y=y
  #descobrindo o ponto com a menor distancia
  if distancia_total < menor_distancia :
    menor_distancia = distancia_total
    menor_distancia_x = x
    menor_distancia_y= y
#condicionando o quadrante dos pontos
  if x == origem_x or y == origem_y:
    
    print("Ponto","(",x,",",y,")""está sobre o eixo de coordenadas")
  elif x>origem_x and y>origem_y:
    quadrante1=quadrante1+1
    print("Ponto","(",x,",",y,")""está no 1° quadrante")
  elif x<origem_x and y>origem_y:
    quadrante2=quadrante2+1
    print("Ponto","(",x,",",y,")""está no 2° quadrante")
  elif x<origem_x and y<origem_y:
    quadrante3=quadrante3+1
    print("Ponto","(",x,",",y,")""está no 3° quadrante")
  elif x>origem_x and y<origem_y:   
    quadrante4=quadrante4+1
    print("Ponto","(",x,",",y,")""está no 4° quadrante")
  #removendo um ponto para que o programa continue e tenha fim
  pontos=pontos-1
#prints finais, mostrando a menor e maior distancia e quantidades de pontos em cada quadrante
print("O ponto mais distante da origem é (",maior_distancia_x,",",maior_distancia_y,") ele está a",round(maior_distancia,2),"unidades de distância")
print("O ponto mais proximo da origem é (",menor_distancia_x,",",menor_distancia_y,") ele está a",round(menor_distancia,2),"unidades de distância")
print("Existe(m)",quadrante1,"ponto(s) no 1° quadrante ,",quadrante2,"no 2° quadrante ," ,quadrante3,"no 3° quadrante  e",quadrante4,"no 4° quadrante")