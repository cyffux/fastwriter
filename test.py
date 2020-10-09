"""
programe conçu et développé par paul-loup DAVID
"""
print("racine: créé une racine carré. mettre un ! a la fin de la racine")
print("exp2: met le signe en exposant 2")
print("exp3: met le signe en exposant 3")
print("*: multiplier")
print("/:diviser")
while True:
    calcul = input()
    if "racine" in calcul:
        calcul=calcul.replace("racine","√(")
        calcul=calcul.replace("!",")")
    if "exp2" in calcul:
        calcul=calcul.replace("exp2","²")
    if "exp3" in calcul:
        calcul=calcul.replace("exp3","³")
    if "*" in calcul:
        calcul=calcul.replace("*","×")
    if "/" in calcul:
        calcul=calcul.replace("/","÷")
    print(calcul)
