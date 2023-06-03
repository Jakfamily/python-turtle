import turtle

t = turtle.Turtle()  # create a turtle object
# def escalier(taille, nb_marche):


def escalier(taille, nb_marche):
    for i in range(0, nb_marche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)


# 10 marche de 30 px
escalier(30, 10)
turtle.done()
