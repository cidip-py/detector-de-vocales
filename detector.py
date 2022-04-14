from random import shuffle

# El siguiente codigo busca las vocales y consonantes del texto ingresado
#vocales

palabra = input("ingrese palabra:")
def vocales():
    for letra in palabra:
        if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
            print(letra, "Es una vocal")

#consonantes
def consonantes():
    for letra in palabra:
     if(letra == "b" or letra == "c" or letra == "d" or letra == "f"
        or letra == "g" or letra == "h" or letra == "j" or letra == "k" or letra == "l"
        or letra == "m" or letra == "n" or letra == "ñ" or letra == "p"
        or letra == "q" or letra == "r" or letra == "s" or letra == "t"
        or letra == "v" or letra == "w" or letra == "x" or letra == "y" or letra == "z"):
      print(letra, "Es una consonante")


vocales()
consonantes()

