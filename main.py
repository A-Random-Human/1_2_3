#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) 
wn.bgpic("background.gif")
wn.tracer(True)

drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()

apple = trtl.Turtle()
apple.penup()
apple_x = 0
apple_y = 0

#-----functions-----
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def update_apple():
  apple.goto(apple.xcor(),-250) 

#-----function calls-----
draw_apple(apple)

# This function takes care of font and color.
def draw_an_A():
  x2 = apple.xcor() - 35
  y2 = apple.ycor() + 10
  drawer.goto(x2, y2)
  drawer.color("white")
  drawer.write("A", font=("Arial", 74, "bold")) 

def clear_screen():
  apple.hideturtle()
  drawer.clear()

def on_drop():
  draw_an_A()
  update_apple()
  clear_screen()

wn.onkeypress(on_drop, "a")

wn.listen()
wn.mainloop()

#https://youtu.be/pal1QQLSN_Y