#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) 
wn.bgpic("background.gif")

drawer = trtl.Turtle()

apple = trtl.Turtle()
apple.penup()
apple_x = 0
apple_y = 0

#-----functions-----
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def update_apple():
  apple.goto(apple.xcor(),-200) 

#-----function calls-----
draw_apple(apple)

# This function takes care of font and color.
def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold")) 

wn.onkeypress(draw_an_A, "a")

wn.onkeypress(update_apple, "d")

wn.listen()
wn.mainloop()

#https://youtu.be/pal1QQLSN_Y