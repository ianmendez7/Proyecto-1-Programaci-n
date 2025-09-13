gana_pierde_1=0
contador_1=0
gana_pierde_2=0
contador_2=0
gana_pierde_3=0
contador_3=0
gana_pierde_4=0
contador_4=0
gana_pierde_5=0
contador_5=0
gana_pierde_6=0
contador_6=0
gana_pierde_7=0
contador_7=0
gana_pierde_8=0
contador_8=0
def puntos_1(gana_pierde_1,contador_1):
    gana_pierde_1=int(input(print("gano= 1, empato=2 o perdio=3: ")))
    if gana_pierde_1==1:
        contador_1=contador_1+3
        return contador_1
    elif gana_pierde_1==2:
        contador_1= contador_1+1
        return contador_1
    else:
        contador_1=contador_1+0
        return contador_1

def puntos_2(gana_pierde_2,contador_2):
    gana_pierde_2=int(input(print("gano= 1, empato=2 o perdio=3: ")))
    if gana_pierde_2==1:
        contador_2= contador_2 + 3
        return contador_2
    elif gana_pierde_2==2:
        contador_2= contador_2+1
        return contador_2
    else:
        contador_2==contador_2+0
        return contador_2
                                
def puntos_3(gana_pierde_3,contador_3):
    gana_pierde_3=int(input(print("gano= 1, empato=2 o perdio=3: ")))
    if gana_pierde_3==1:
        contador_3= contador_3 + 3
        return contador_3
    elif gana_pierde_3==2:
        contador_3= contador_3+1
        return contador_3
    else:
        contador_3=contador_3+0
        return contador_3

def puntos_4(gana_pierde_4,contador_4):
    gana_pierde_4=int(input(print("gano= 1, empato=2 o perdio=3: ")))
    if gana_pierde_4==1:
        contador_4= contador_4 + 3
        return contador_4
    elif gana_pierde_4==2:
        contador_4= contador_4+1
        return contador_4
    else:
        contador_4=contador_4+0
        return contador_4
                                    
def puntos_5(gana_pierde_5,contador_5):
    gana_pierde_5=int(input(print("gano= 1, empato=2 o perdio=3: ")))
    if gana_pierde_5==1:
        contador_5= contador_5 + 3
        return contador_5
    elif gana_pierde_5==2:
        contador_5= contador_5+1
        return contador_5
    else:
        contador_5=contador_5+0
        return contador_5
def puntos_6(gana_pierde_6,contador_6):
    gana_pierde_6=int(input(print("gano= 1, empato=2 o perdio=3: ")))
    if gana_pierde_6==1:
        contador_6= contador_6 + 3
        return contador_6
    elif gana_pierde_6==2:
        contador_6= contador_6+1
        return contador_6
    else:
        contador_6=contador_6+0
        return contador_6
    
def puntos_7(gana_pierde_7,contador_7):
    gana_pierde_7=int(input(print("gano= 1, empato=2 o perdio=3: ")))
    if gana_pierde_7==1:
        contador_7= contador_7 + 3
        return contador_7
    elif gana_pierde_7==2:
        contador_7= contador_7+1
        return contador_7
    else:
        contador_7=contador_7+0
        return contador_7
    
def puntos_8(gana_pierde_8,contador_8):
    gana_pierde_8=(input(print("gano= 1, empato=2 o perdio=3: ")))
    if gana_pierde_8==1:
        contador_8= contador_8 + 3
        return contador_8
    elif gana_pierde_8==2:
        contador_8= contador_8+1
        return contador_8
    else:
        contador_8=contador_8+0
        return contador_8     

equipo=int(input(print("Introduce número de equipo")))
while equipo!=9:
    if equipo==1:
        contador_1=puntos_1(gana_pierde_1,contador_1)
        print("Ese equipo tiene",contador_1,"puntos")
    elif equipo==2:
        contador_2=puntos_2(gana_pierde_2,contador_2)
        print("Ese equipo tiene",contador_2,"puntos")
    elif equipo==3:
        contador_3=puntos_3(gana_pierde_3,contador_3)
        print("Ese equipo tiene",contador_3,"puntos")
    elif equipo==4:
        contador_4=puntos_4(gana_pierde_4,contador_4)
        print("Ese equipo tiene",contador_4,"puntos")
    elif equipo==5:
        contador_5=puntos_5(gana_pierde_5,contador_5)
        print("Ese equipo tiene",contador_5,"puntos")
    elif equipo==6:
        contador_6=puntos_6(gana_pierde_6,contador_6)
        print("Ese equipo tiene",contador_6,"puntos")
    elif equipo==7:
        contador_7=puntos_7(gana_pierde_7,contador_7)
        print("Ese equipo tiene",contador_7,"puntos")
    elif equipo==8:
        contador_8=puntos_8(gana_pierde_8,contador_8)
        print("Ese equipo tiene",contador_8,"puntos")
    else:
       print("Eso es todo") 
    