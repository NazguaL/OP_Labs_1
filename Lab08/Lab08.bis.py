import turtle
from turtle import Screen, Turtle, Vec2D

p = 0.08


def draw_rectangle(points, turtle):

    turtle.up()
    turtle.goto(points[0])
    turtle.down()

    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[3])
    turtle.goto(points[0])


def get_p(p1, p2):
    return p1 + (p2 - p1) * p
    # return p2 + (p1 - p2) * p


s_p = [[200, 200], [200, -200], [-200, -200], [-200, 200]]
start_points = [Vec2D(s_p[0][0], s_p[0][1]),
                Vec2D(s_p[1][0], s_p[1][1]),
                Vec2D(s_p[2][0], s_p[2][1]),
                Vec2D(s_p[3][0], s_p[3][1])]
p_p = s_p.copy()
points_list = list()
points_list.append(start_points)


for i in range(50):
    n_p = [
            [get_p(p_p[0][0], p_p[1][0]), get_p(p_p[0][1], p_p[1][1])],
            [get_p(p_p[1][0], p_p[2][0]), get_p(p_p[1][1], p_p[2][1])],
            [get_p(p_p[2][0], p_p[3][0]), get_p(p_p[2][1], p_p[3][1])],
            [get_p(p_p[3][0], p_p[0][0]), get_p(p_p[3][1], p_p[0][1])]
          ]

    next_points = [
                    Vec2D(n_p[0][0], n_p[0][1]),
                    Vec2D(n_p[1][0], n_p[1][1]),
                    Vec2D(n_p[2][0], n_p[2][1]),
                    Vec2D(n_p[3][0], n_p[3][1])
                   ]

    points_list.append(next_points)
    p_p = n_p.copy()


def main():
    screen = Screen()
    turtle = Turtle()

    for i in range(len(points_list)):
        draw_rectangle(points_list[i], turtle)

    turtle.hideturtle()
    screen.exitonclick()

main()
