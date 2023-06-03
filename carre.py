import turtle

t = turtle.Turtle()


def carre(taille):
    for i in range(4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nb):
    for i in range(0, nb):
        taille = (i+1)*taille_depart
        carre(taille)


carres(10, 10)

turtle.done()
