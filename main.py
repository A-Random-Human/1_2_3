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

letters = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

apples = []
apple_letters = []

for z in range(5):
  apples.append(trtl.Turtle())
  apple_letters.append(rand.choice(letters))

#-----functions-----
def draw_apple(index):
  apple_letters[index] = rand.choice(letters)
  #Apple set up
  apples[index].penup()
  apples[index].speed(5)
  apples[index].shape(apple_image)
  wn.tracer(False)
  #Sets Apple position
  apples[index].setx (rand.randint(-150,150))
  apples[index].sety (rand.randint(-15,145))
  #Draws letter
  apples[index].sety (apples[index].ycor()-35)
  apples[index].color("white")
  apples[index].write(apple_letters[index], align ="center", font=("Arial", 40, "bold")) 
  apples[index].sety (apples[index].ycor()+35)
  #Showing turtle, tracing, and updating
  apples[index].showturtle()
  wn.tracer(True)
  wn.update()

def on_drop(index):
  apples[index].penup()
  apples[index].clear()
  apples[index].sety(-150)
  apples[index].hideturtle()
  draw_apple(index)

#Why is on-key press active for the whole program :'( i.e. if you allow x to make the apple drop, x can always make the apple drop. There's no way with on-key press to clear or disable that even if the apple_lette is not x anymore. The following below just feels wrong :(, but it has to be done for it to work.

def a():
  for i in range(5):
    if apple_letters[i] == 'a':
      on_drop(i)
def b():
  for i in range(5):
    if apple_letters[i] == 'b':
      on_drop(i)
def c():
  for i in range(5):
    if apple_letters[i] == 'c':
      on_drop(i)
def d():
  for i in range(5):
   if apple_letters[i] == 'd':
     on_drop(i)
def e():
  for i in range(5):
   if apple_letters[i] == 'e':
      on_drop(i)
def f():
  for i in range(5):
   if apple_letters[i] == 'f':
     on_drop(i)
def g():
  for i in range(5):
    if apple_letters[i] == 'g':
     on_drop(i)
def h():
  for i in range(5):
    if apple_letters[i] == 'h':
      on_drop(i)
def j():
  for i in range(5):
   if apple_letters[i] == 'j':
      on_drop(i)
def k():
  for i in range(5):
    if apple_letters[i] == 'k':
      on_drop(i)
def l():
  for i in range(5):
    if apple_letters[i] == 'l':
     on_drop(i)
def m():
  for i in range(5):
   if apple_letters[i] == 'm':
     on_drop(i)
def n():
  for i in range(5):
   if apple_letters[i] == 'n':
     on_drop(i)
def o():
  for i in range(5):
    if apple_letters[i] == 'o':
      on_drop(i)
def p():
  for i in range(5):
   if apple_letters[i] == 'p':
      on_drop(i)
def q():
  for i in range(5):
    if apple_letters[i] == 'q':
     on_drop(i)
def r():
  for i in range(5):
   if apple_letters[i] == 'r':
     on_drop(i)
def s():
  for i in range(5):
   if apple_letters[i] == 's':
      on_drop(i)
def t():
  for i in range(5):
   if apple_letters[i] == 't':
      on_drop(i)
def u():
  for i in range(5):
   if apple_letters[i] == 'u':
      on_drop(i)
def v():
  for i in range(5):
   if apple_letters[i] == 'v':
     on_drop(i)
def w():
  for i in range(5):
   if apple_letters[i] == 'w':
      on_drop(i)
def x():
  for i in range(5):
   if apple_letters[i] == 'x':
     on_drop(i)
def y():
  for i in range(5):
    if apple_letters[i] == 'y':
      on_drop(i)
def z():
  for i in range(5):
   if apple_letters[i] == 'z':
     on_drop(i)

for i in range(5):
  draw_apple(i)

wn.onkeypress(a,'a')
wn.onkeypress(b,'b')
wn.onkeypress(c,'c')
wn.onkeypress(d,'d')
wn.onkeypress(e,'e')
wn.onkeypress(f,'f')
wn.onkeypress(g,'g')
wn.onkeypress(h,'h')
wn.onkeypress(j,'j')
wn.onkeypress(k,'k')
wn.onkeypress(l,'l')
wn.onkeypress(m,'m')
wn.onkeypress(n,'n')
wn.onkeypress(o,'o')
wn.onkeypress(p,'p')
wn.onkeypress(q,'q')
wn.onkeypress(r,'r')
wn.onkeypress(s,'s')
wn.onkeypress(t,'t')
wn.onkeypress(u,'u')
wn.onkeypress(v,'v')
wn.onkeypress(w,'w')
wn.onkeypress(x,'x')
wn.onkeypress(y,'y')
wn.onkeypress(z,'z')

wn.listen()
wn.mainloop()