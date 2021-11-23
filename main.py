#   a123_apple_1.py
import turtle as trtl
import random as rand

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
apple.speed(7)

apple_letter = 'a'

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#-----functions-----

def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def update_apple():
  apple.goto(apple.xcor(),-150) 

#-----function calls-----


# This function takes care of font and color.
def draw_letter():
  global apple_letter
  x2 = apple.xcor() - 18
  y2 = apple.ycor() + -37
  drawer.goto(x2, y2)
  drawer.color("white")
  apple_letter = letters[rand.randint(0,25)]
  drawer.write(apple_letter, font=("Arial", 40, "bold")) 

def clear_screen():
  apple.hideturtle()
  drawer.clear()

def reset_apple_position():
  apple_x = rand.randint(-150,150)
  apple_y = rand.randint(-15,145)
  apple.goto(apple_x,apple_y)

#Draw Apple for 1st time
draw_apple(apple)
draw_letter()
apple.showturtle()

def on_drop():
  update_apple()
  clear_screen()
  reset_apple_position()
  draw_apple(apple)
  draw_letter()
  apple.showturtle()
  wn.update

#Why is on-key press active for the whole program :'( i.e. if you allow x to make the apple drop, x can always make the apple drop. There's no way with on-key press to clear or disable that even if the apple_letter is not x anymore. The following below just feels wrong :(, but it has to be done for it to

def a():
  if apple_letter == 'a':
    on_drop()
def b():
  if apple_letter == 'b':
    on_drop()
def c():
  if apple_letter == 'c':
    on_drop()
def d():
  if apple_letter == 'd':
    on_drop()
def e():
  if apple_letter == 'e':
    on_drop()
def f():
  if apple_letter == 'f':
    on_drop()
def g():
  if apple_letter == 'g':
    on_drop()
def h():
  if apple_letter == 'h':
    on_drop()
def i():
  if apple_letter == 'i':
    on_drop()
def j():
  if apple_letter == 'j':
    on_drop()
def k():
  if apple_letter == 'k':
    on_drop()
def l():
  if apple_letter == 'l':
    on_drop()
def m():
  if apple_letter == 'm':
    on_drop()
def n():
  if apple_letter == 'n':
    on_drop()
def o():
  if apple_letter == 'o':
    on_drop()
def p():
  if apple_letter == 'p':
    on_drop()
def q():
  if apple_letter == 'q':
    on_drop()
def r():
  if apple_letter == 'r':
    on_drop()
def s():
  if apple_letter == 's':
    on_drop()
def t():
  if apple_letter == 't':
    on_drop()
def u():
  if apple_letter == 'u':
    on_drop()
def v():
  if apple_letter == 'v':
    on_drop()
def w():
  if apple_letter == 'w':
    on_drop()
def x():
  if apple_letter == 'x':
    on_drop()
def y():
  if apple_letter == 'y':
    on_drop()
def z():
  if apple_letter == 'z':
    on_drop()

wn.onkeypress(a,'a')
wn.onkeypress(b,'b')
wn.onkeypress(c, 'c')
wn.onkeypress(d, 'd')
wn.onkeypress(e, 'e')
wn.onkeypress(f, 'f')
wn.onkeypress(g, 'g')
wn.onkeypress(h, 'h')
wn.onkeypress(i, 'i')
wn.onkeypress(j, 'j')
wn.onkeypress(k, 'k')
wn.onkeypress(l, 'l')
wn.onkeypress(m, 'm')
wn.onkeypress(n, 'n')
wn.onkeypress(o, 'o')
wn.onkeypress(p, 'p')
wn.onkeypress(q, 'q')
wn.onkeypress(r, 'r')
wn.onkeypress(s, 's')
wn.onkeypress(t, 't')
wn.onkeypress(u, 'u')
wn.onkeypress(v, 'v')
wn.onkeypress(w, 'w')
wn.onkeypress(x, 'x')
wn.onkeypress(y, 'y')
wn.onkeypress(z, 'z')

wn.listen()
wn.mainloop()