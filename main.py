import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Cờ Tổ Quốc Việt Nam")

flag = turtle.Turtle()
flag.speed(3)

# Tỷ lê cờ Tổ Quốc Việt Nam
# https://vtcnews.vn/ty-le-chuan-cua-la-co-to-quoc-viet-nam-ar889882.html
a = 200
rectangle_width = 3 * a
rectangle_height = 2 * a

# Công thức tính toán ngôi sao 5 cạnh
# https://www.omnicalculator.com/math/star-shape

star_radius = 0.2 * rectangle_width
star_length = rectangle_width / 2.5
golden_ratio = 1.618
star_size = star_length / golden_ratio / golden_ratio


def draw_rectangle(color, x, y, width, height):
    flag.penup()
    flag.goto(x, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()


draw_rectangle("red", -rectangle_width / 2, rectangle_height / 2, rectangle_width, rectangle_height)


def draw_outline_star(color, x, y, size):
    flag.penup()
    flag.goto(x, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    flag.right(72)
    for _ in range(5):
        flag.forward(size)
        flag.left(72)
        flag.forward(size)
        flag.right(144)
    flag.end_fill()


draw_outline_star("yellow", 0, star_radius, star_size)

flag.hideturtle()
wn.mainloop()
