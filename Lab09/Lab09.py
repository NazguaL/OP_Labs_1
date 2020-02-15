from turtle import Screen, Turtle, Vec2D


def drawTriangle(points, turtle):

    turtle.up()
    turtle.goto(points[0])
    turtle.down()

    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])



def getMid(p1, p2):
    return(p1 + p2) * 0.5


def sierpinski(points, degree, turtle):
    drawTriangle(points, turtle)

    if degree < 1:
        return

    # sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, turtle)
    # sierpinski([getMid(points[0], points[1]), points[1], getMid(points[1], points[2])], degree - 1, turtle)
    # sierpinski([getMid(points[0], points[2]), getMid(points[2], points[1]), points[2],], degree - 1, turtle)

    sierpinski([getMid(points[0], points[2]), getMid(points[2], points[1]), points[2], ], degree - 1, turtle)
    sierpinski([getMid(points[0], points[1]), points[1], getMid(points[1], points[2])], degree - 1, turtle)
    sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, turtle)


def main():
    screen = Screen()
    turtle = Turtle()

    myPoints = [Vec2D(-200, -100), Vec2D(0, 200), Vec2D(200, -100)]
    sierpinski(myPoints, 5, turtle)

    turtle.hideturtle()
    screen.exitonclick()

main()
