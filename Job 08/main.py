a = int(input("Donne moi la longueur de A :"))
b = int(input("Donne moi la longueur de B :"))
c = int(input("Donne moi la longueur de C :"))

if a + b <= c or a + c <= b or b + c <= a:
    print("Ce n'est pas un triangle valide")
else:
    print("C'est un triangle valide.")


if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2  == a ** 2 or a ** 2 + c ** 2 == b ** 2:
    print("Le triangle", a, b , c, "est un triangle rectangle")
elif a == b == c: 
    print("Le triangle", a, b , c, "est un triangle équilatéral")
elif a == b or a == c or b == c:
    print("Le triangle", a, b , c, "est un triangle isocèle")
else:
    print("Le triangle", a, b , c, "est un triangle quelconque")

