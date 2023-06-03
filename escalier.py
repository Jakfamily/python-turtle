import turtle

t = turtle.Turtle()  # create a turtle object
# 5 marche de 30px
marche = 0

while marche <= 5:
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    marche += 1

turtle.done()

# correction de l'exercice :
"""
for i in range(0,5):
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
"""
