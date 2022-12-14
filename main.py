import pygame
import pygame.font
import time
import string

pygame.init()
width, height = 514, 800
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Airbus MCDU")

#texture init
mcduframe = pygame.image.load("textures/mcduframe.png").convert()
framerect = mcduframe.get_rect()
#buttons
#line select key
mcdubutton = pygame.image.load("textures/mcdubutton.png").convert()
#page select key
blankbtn = pygame.image.load("textures/pageselect/blankbtn.png").convert() 
initbtn = pygame.image.load("textures/pageselect/initbtn.png").convert() 
mcdumenu = pygame.image.load("textures/pageselect/mcdumenu.png").convert() 
inopbtn = pygame.image.load("textures/pageselect/inopbtn.png").convert() 
#keypad
for i in list(string.ascii_lowercase):
  globals()[i + "key"] = pygame.image.load("textures/keypad/" + i + "key.png").convert()
spkey = pygame.image.load("textures/keypad/spkey.png").convert()
clrkey = pygame.image.load("textures/keypad/clrkey.png").convert()
slashkey = pygame.image.load("textures/keypad/slashkey.png").convert()
ovfykey = pygame.image.load("textures/keypad/ovfykey.png").convert()
#numpad
for i in range(0,10):
  globals()["key" + str(i)] = pygame.image.load("textures/numpad/" + str(i) + "key.png").convert()
keydot =  pygame.image.load("textures/numpad/dotkey.png").convert()
keyplus =  pygame.image.load("textures/numpad/pluskey.png").convert()
#logic vars
currPage = ""
scratch = ""
scratchpadact = True

#colour vars
red = (255, 0, 0)
green = (0, 255, 0)
cyan = (94, 198, 255)
grey = (70, 70, 70)
white = (255, 255, 255)
orange = (255, 147, 0)

#initAvars
depdest = "____/____"
depdestclr = orange
corte = "__________"
corteclr = orange
fltnbrclr = orange
altncorte = "----/----------"
fltnbr = "________"
costi = "---"
crzalt = 0
crzfl = "-----"
ciclr = white
flclr = white
initrqvis = True
tropo = "36090"
gtemp = "---°"

#init route database
db = open("cortedb.txt", "r")
rteList = []
for l in db:
  line = l.strip()
  nextline = line.split()
  rteList.append(nextline)
db.close()
print(rteList)

class Button():
  def __init__(self, x, y, image):
    self.image = image 
    self.rect = self.image.get_rect()
    self.rect.topleft = (x,y)
    self.clicked = False
    
  def draw(self):
    actvted = False

    pygame.event.get()
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        actvted = True
    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False
        
    screen.blit(self.image, (self.rect.x, self.rect.y))
    return actvted

class fmgc():
  def __init__(self):
    self.rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(82, 48, 353, 329))

  def resetdispl(self):
    screen.fill(backgroundColor)
    screen.blit(mcduframe, framerect)
    
  def inopPages(self):
    font = pygame.font.Font("HoneywellMCDU.ttf", 30)
    text_surface = font.render('PAGE INOP', True, red)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (165,188)
    screen.blit(text_surface, text_rect)
    
  def InitA(self):
    global currPage
    global depdest
    global depdestclr
    global corteclr
    global corte
    global altncorte
    global fltnbr
    global costi
    global crzalt
    global crzfl
    global initrqvis
    global fltnbrclr
    global ciclr
    global flclr
    global tropo
    global gtemp
    currPage = "initA"
    scrtchpd.pad("")
    self.depdest = depdest
    self.corte = corte
    font = pygame.font.Font("HoneywellMCDU.ttf", 21)
    title = font.render("INIT", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (224, 68)
    screen.blit(title, title_rect)
    title = font.render("WIND/TEMP>", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (281, 243)
    screen.blit(title, title_rect)
    title = font.render("←→", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (395, 65)
    screen.blit(title, title_rect)
    title = font.render(depdest, True, depdestclr)
    title_rect = title.get_rect()
    title_rect.topleft = (290, 106)
    screen.blit(title, title_rect)
    title = font.render(corte, True, corteclr)
    title_rect = title.get_rect()
    title_rect.topleft = (91, 106)
    screen.blit(title, title_rect)
    title = font.render(fltnbr, True, fltnbrclr)
    title_rect = title.get_rect()
    title_rect.topleft = (91, 197)
    screen.blit(title, title_rect)
    title = font.render(fltnbr, True, fltnbrclr)
    title_rect = title.get_rect()
    title_rect.topleft = (91, 198)
    screen.blit(title, title_rect)
    title = font.render(costi, True, ciclr)
    title_rect = title.get_rect()
    title_rect.topleft = (91, 288)
    screen.blit(title, title_rect)
    if crzalt == "-----":
      title = font.render(crzalt + "/---°", True, flclr)
      title_rect = title.get_rect()
      title_rect.topleft = (91, 334)
      screen.blit(title, title_rect)
    elif crzalt != 0:
      crzfl = "FL" + str(int(int(crzalt)/100)).zfill(3)
      title = font.render(crzfl + "/---°", True, flclr)
      title_rect = title.get_rect()
      title_rect.topleft = (91, 334)
      screen.blit(title, title_rect)
      print(crzfl)
    else:
      title = font.render(crzfl + "/---°", True, flclr)
      title_rect = title.get_rect()
      title_rect.topleft = (91, 334)
      screen.blit(title, title_rect)
    font = pygame.font.Font("HoneywellMCDU.ttf", 16)
    title = font.render(altncorte, True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (90, 155)
    screen.blit(title, title_rect)
    title = font.render("CO RTE", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (113, 86)
    screen.blit(title, title_rect)
    title = font.render("FROM/TO", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (312, 86)
    screen.blit(title, title_rect)
    title = font.render("ALTN/CO RTE", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (91, 135)
    screen.blit(title, title_rect)
    title = font.render("FLT NBR", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (91, 177)
    screen.blit(title, title_rect)
    title = font.render("COST INDEX", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (91, 268)
    screen.blit(title, title_rect)
    title = font.render("TROPO", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (363, 268)
    screen.blit(title, title_rect)
    title = font.render(tropo, True, cyan)
    title_rect = title.get_rect()
    title_rect.topleft = (363, 290)
    screen.blit(title, title_rect)
    title = font.render("CRZ FL/TEMP", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (91, 314)
    screen.blit(title, title_rect)
    title = font.render("GND TEMP", True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (326, 314)
    screen.blit(title, title_rect)
    title = font.render(gtemp, True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (376, 337)
    screen.blit(title, title_rect)
    if initrqvis == True:
      title = font.render("INIT", True, orange)
      title_rect = title.get_rect()
      title_rect.topleft = (369, 140)
      screen.blit(title, title_rect)
      font = pygame.font.Font("HoneywellMCDU.ttf", 21)
      title = font.render("REQUEST*", True, orange)
      title_rect = title.get_rect()
      title_rect.topleft = (308, 158)
      screen.blit(title, title_rect)
    scrtchpd.pad("")
    return
    
  def acftdata(self):
    global currPage
    currPage = "acftdata"
    scrtchpd.pad("")
    font = pygame.font.Font("HoneywellMCDU.ttf", 21)
    title = font.render('A3XX-200', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (187,61)
    screen.blit(title, title_rect)
    title = font.render('LEAP-1AXX', True, green)
    title_rect = title.get_rect()
    title_rect.topleft = (96,108)
    screen.blit(title, title_rect)
    title = font.render('AIRAC 2209', True, cyan)
    title_rect = title.get_rect()
    title_rect.topleft = (255,155)
    screen.blit(title, title_rect)
    title = font.render('AIRAC 2210', True, grey)
    title_rect = title.get_rect()
    title_rect.topleft = (95,198)
    screen.blit(title, title_rect)
    title = font.render('[   ]', True, grey)
    title_rect = title.get_rect()
    title_rect.topleft = (95,288)
    screen.blit(title, title_rect)
    font = pygame.font.Font("HoneywellMCDU.ttf", 16)
    title = font.render('ENG', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (123,91)
    screen.blit(title, title_rect)
    title = font.render('ACTIVE NAV DATA BASE', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (114,134)
    screen.blit(title, title_rect)
    title = font.render('SECOND NAV DATA BASE', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (114,179)
    screen.blit(title, title_rect)
    title = font.render('CHG CODE', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (94,270)
    screen.blit(title, title_rect)
    title = font.render('IDLE/PERF', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (94, 314)
    screen.blit(title, title_rect)
    title = font.render('+0.0/+0.0', True, green)
    title_rect = title.get_rect()
    title_rect.topleft = (89, 336)
    screen.blit(title, title_rect)
    title = font.render('MADE WITH', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (318,325)
    screen.blit(title, title_rect)
    title = font.render('PYGAME ON REPLIT', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (238, 344)
    screen.blit(title, title_rect)
  def mcdumenu(self):
    global currPage
    currPage = "mcdumenu"
    scrtchpd.pad("")
    font = pygame.font.Font("HoneywellMCDU.ttf", 21)
    title = font.render('MCDU MENU', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (187,61)
    screen.blit(title, title_rect)

class Scratchpad():
  def __init__(self):
    self.rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(82, 360, 350, 29))
    blocker = pygame.Surface((350, 29))
    blocker.fill((0, 0, 0))
    screen.blit(blocker, self.rect)

  def pad(self, inpt):
    global scratch
    global scratchpadact
    font = pygame.font.Font("HoneywellMCDU.ttf", 21)
    if inpt == "CLR":
      if scratch == "":
        scratch = "     CLR"
        scratchpadact = False
      elif scratch == "     CLR":
        scratch = ""
        scratchpadact = True
      else:
        scratch = scratch[:-1]
    elif scratchpadact == True:
      if len(scratch) >= 23 and inpt != "CLR":
        self.invalidinpt("TOO LONG")
        return
      elif inpt == "+":
        if len(scratch) != 0:
          if scratch[-1] == "+":
            scratch = scratch[:-1] + "-"
          elif scratch[-1] == "-":
            scratch = scratch[:-1] + "+"
          else:
            scratch = str(scratch) + inpt
        else:
          scratch = str(scratch) + inpt
      else:
        scratch = str(scratch) + inpt
    blocker = pygame.Surface((350, 29))
    blocker.fill((0, 0, 0))
    screen.blit(blocker, self.rect)
    text = font.render(scratch, True, white)
    text_rect = text.get_rect()
    text_rect.topleft = (87, 363)
    screen.blit(text, text_rect)
    return scratch
      
  def invalidinpt(self, text):
    global scratch
    font = pygame.font.Font("HoneywellMCDU.ttf", 21)
    text = font.render(text, True, orange)
    text_rect = text.get_rect()
    text_rect.topleft = (87, 363)
    blocker = pygame.Surface((350, 29))
    blocker.fill((0, 0, 0))
    screen.blit(blocker, self.rect)
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(2)
    screen.blit(blocker, self.rect)
    text = font.render(scratch, True, white)
    text_rect = text.get_rect()
    text_rect.topleft = (87, 363)
    screen.blit(text, text_rect)
    pygame.display.flip()

  def clear(self):
    global scratch
    scratch = ""
    font = pygame.font.Font("HoneywellMCDU.ttf", 21)
    text = font.render(scratch, True, white)
    text_rect = text.get_rect()
    text_rect.topleft = (87, 363)
    blocker = pygame.Surface((350, 29))
    blocker.fill((0, 0, 0))
    screen.blit(blocker, self.rect)
    screen.blit(text, text_rect)
    
#line select keys
l1sk = Button(10 , 103, mcdubutton)
l2sk = Button(10 , 148, mcdubutton)
l3sk = Button(10 , 195, mcdubutton)
l4sk = Button(10 , 239, mcdubutton)
l5sk = Button(10 , 284, mcdubutton)
l6sk = Button(10 , 330, mcdubutton) 

r1sk = Button(470 , 103, mcdubutton)
r2sk = Button(470 , 148, mcdubutton)
r3sk = Button(470 , 195, mcdubutton)
r4sk = Button(470 , 239, mcdubutton)
r5sk = Button(470 , 284, mcdubutton)
r6sk = Button(470 , 330, mcdubutton)

#keyboard
k_a =  Button(206 , 500, akey)
k_b =  Button(260 , 500, bkey)
k_c =  Button(312 , 500, ckey)
k_d =  Button(366 , 500, dkey)
k_e =  Button(420 , 500, ekey)
k_f =  Button(206 , 548, fkey)
k_g =  Button(260 , 548, gkey)
k_h =  Button(312 , 548, hkey)
k_i =  Button(366 , 548, ikey)
k_j =  Button(420 , 548, jkey)
k_k =  Button(206 , 596, kkey)
k_l =  Button(260 , 596, lkey)
k_m =  Button(312 , 596, mkey)
k_n =  Button(366 , 596, nkey)
k_o =  Button(420 , 596, okey)
k_p =  Button(206 , 644, pkey)
k_q =  Button(260 , 644, qkey)
k_r =  Button(312 , 644, rkey)
k_s =  Button(366 , 644, skey)
k_t =  Button(420 , 644, tkey)
k_u =  Button(206 , 692, ukey)
k_v =  Button(260 , 692, vkey)
k_w =  Button(312 , 692, wkey)
k_x =  Button(366 , 692, ykey)
k_y =  Button(420 , 692, xkey)
k_z =  Button(206 , 740, zkey)
k_slant =  Button(260 , 740, slashkey)
k_sp =  Button(312 , 740, spkey)
k_ovfy =  Button(366 , 740, ovfykey)
k_clr = Button(420 , 740, clrkey)
k_1 = Button(55, 618, key1)
k_2 = Button(105, 618, key2)
k_3 = Button(156, 618, key3)
k_4 = Button(55, 660, key4)
k_5 = Button(105, 660, key5)
k_6 = Button(156, 660, key6)
k_7 = Button(55, 701, key7)
k_8 = Button(105, 701, key8)
k_9 = Button(156, 701, key9)
k_0 = Button(105, 742, key0)
k_dot = Button(55, 742, keydot)
k_plusminus = Button(156, 742, keyplus)

#page select keys
blank = Button(370, 421, blankbtn)
init = Button(245, 421, initbtn)
data = Button(308, 421, inopbtn)
perf = Button(181, 421, inopbtn)
prog = Button(118, 421, inopbtn)
dir = Button(56, 421, inopbtn)
mcdumenu = Button(370, 459, mcdumenu)
secfpln = Button(245, 459, inopbtn)
atccomm = Button(308, 459, inopbtn)
fuelpred = Button(181, 459, inopbtn)
radnav = Button(118, 459, inopbtn)
fpln = Button(56, 459, inopbtn)
blank2 = Button(118, 497, blankbtn)
airport = Button(56, 497, inopbtn)
up = Button(118, 535, inopbtn)
left = Button(56, 535, inopbtn)
down = Button(118, 573, inopbtn)
right = Button(56, 573, inopbtn)
#screens
sinita = fmgc()
sinitb = fmgc()
sdir = fmgc() #dit-to inop
sprog = fmgc() #gnd only
stoperf = fmgc() #to perf only
sdata = fmgc() #data inop
sfpln = fmgc() #vhhh-rctp only
sradnav = fmgc() #vhhh only
sfuelpred = fmgc() #fuelpred to
ssecfpln = fmgc() #inop
satccomm = fmgc() #pdc only
smcdumenu = fmgc() #atsu gen only
sairprt = fmgc() #inop
sdep = fmgc() #dep
sarr = fmgc() #arr
slatrev = fmgc() #inop
svertrev = fmgc() #alt+spd ctsr only
sacftmnu = fmgc() #fmgcmenu
sinop = fmgc()
reset = fmgc()
scrtchpd = Scratchpad()


screen.fill(backgroundColor)
screen.blit(mcduframe, framerect)
sacftmnu.acftdata()

#temp implementation of keyboard input
events = pygame.event.get()
clock = pygame.time.Clock()
    
while True:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        scrtchpd.pad("A")
      elif event.key == pygame.K_b:
        scrtchpd.pad("B")
      elif event.key == pygame.K_c:
        scrtchpd.pad("C")
      elif event.key == pygame.K_d:
        scrtchpd.pad("D")
      elif event.key == pygame.K_e:
        scrtchpd.pad("E")
      elif event.key == pygame.K_f:
        scrtchpd.pad("F")
      elif event.key == pygame.K_g:
        scrtchpd.pad("G")
      elif event.key == pygame.K_h:
        scrtchpd.pad("H")
      elif event.key == pygame.K_i:
        scrtchpd.pad("I")
      elif event.key == pygame.K_j:
        scrtchpd.pad("J")
      elif event.key == pygame.K_k:
        scrtchpd.pad("K")
      elif event.key == pygame.K_l:
        scrtchpd.pad("L")
      elif event.key == pygame.K_m:
        scrtchpd.pad("M")
      elif event.key == pygame.K_n:
        scrtchpd.pad("N")
      elif event.key == pygame.K_o:
        scrtchpd.pad("O")
      elif event.key == pygame.K_p:
        scrtchpd.pad("P")
      elif event.key == pygame.K_q:
        scrtchpd.pad("Q")
      elif event.key == pygame.K_r:
        scrtchpd.pad("R")
      elif event.key == pygame.K_s:
        scrtchpd.pad("S")
      elif event.key == pygame.K_t:
        scrtchpd.pad("T")
      elif event.key == pygame.K_u:
        scrtchpd.pad("U")
      elif event.key == pygame.K_v:
        scrtchpd.pad("V")
      elif event.key == pygame.K_w:
        scrtchpd.pad("W")
      elif event.key == pygame.K_x:
        scrtchpd.pad("X")
      elif event.key == pygame.K_y:
        scrtchpd.pad("Y")
      elif event.key == pygame.K_z:
        scrtchpd.pad("Z")
      elif event.key == pygame.K_BACKSPACE:
        scrtchpd.pad("CLR")
      elif event.key == pygame.K_SPACE:
        scrtchpd.pad(" ")
      elif event.unicode == "+" or event.unicode == "-":
        scrtchpd.pad("+")
      elif event.key == pygame.K_SLASH:
        scrtchpd.pad("/")
      elif event.key == pygame.K_0:
        scrtchpd.pad("0")
      elif event.key == pygame.K_1:
        scrtchpd.pad("1")
      elif event.key == pygame.K_2:
        scrtchpd.pad("2")
      elif event.key == pygame.K_3:
        scrtchpd.pad("3")
      elif event.key == pygame.K_4:
        scrtchpd.pad("4")
      elif event.key == pygame.K_5:
        scrtchpd.pad("5")
      elif event.key == pygame.K_6:
        scrtchpd.pad("6")
      elif event.key == pygame.K_7:
        scrtchpd.pad("7")
      elif event.key == pygame.K_8:
        scrtchpd.pad("8")
      elif event.key == pygame.K_9:
        scrtchpd.pad("9")
      elif event.key == pygame.K_PERIOD:
        scrtchpd.pad(".")
  l1sk.draw()
  l2sk.draw()
  l3sk.draw()
  l4sk.draw()
  l5sk.draw()
  l6sk.draw()
  r1sk.draw()
  r2sk.draw()
  r3sk.draw()
  r4sk.draw()
  r5sk.draw()
  r6sk.draw()
  if blank.draw() == True:
    reset.resetdispl()
    sacftmnu.acftdata()
  if init.draw() == True:
    reset.resetdispl()
    sinita.InitA()
  if mcdumenu.draw() == True:
    reset.resetdispl()
    smcdumenu.mcdumenu()
  dir.draw()
  perf.draw()
  prog.draw()
  data.draw()
  fpln.draw()
  atccomm.draw()
  secfpln.draw()
  radnav.draw()
  fuelpred.draw()
  blank2.draw()
  airport.draw()
  up.draw()
  down.draw()
  left.draw()
  right.draw()
  if k_a.draw() == True:
    scrtchpd.pad("A")
  if k_b.draw() == True:
    scrtchpd.pad("B")
  if k_c.draw() == True:
    scrtchpd.pad("C")
  if k_d.draw() == True:
    scrtchpd.pad("D")
  if k_e.draw() == True:
    scrtchpd.pad("E")
  if k_f.draw() == True:
    scrtchpd.pad("F")
  if k_g.draw() == True:
    scrtchpd.pad("G")
  if k_h.draw() == True:
    scrtchpd.pad("H")
  if k_i.draw() == True:
    scrtchpd.pad("I")
  if k_j.draw() == True:
    scrtchpd.pad("J")
  if k_k.draw() == True:
    scrtchpd.pad("K")
  if k_l.draw() == True:
    scrtchpd.pad("L")
  if k_m.draw() == True:
    scrtchpd.pad("M")
  if k_n.draw() == True:
    scrtchpd.pad("N")
  if k_o.draw() == True:
    scrtchpd.pad("O")
  if k_p.draw() == True:
    scrtchpd.pad("P")
  if k_q.draw() == True:
    scrtchpd.pad("Q")
  if k_r.draw() == True:
    scrtchpd.pad("R")
  if k_s.draw() == True:
    scrtchpd.pad("S")
  if k_t.draw() == True:
    scrtchpd.pad("T")
  if k_u.draw() == True:
    scrtchpd.pad("U")
  if k_v.draw() == True:
    scrtchpd.pad("V")
  if k_w.draw() == True:
    scrtchpd.pad("W")
  if k_y.draw() == True:
    scrtchpd.pad("Y")
  if k_x.draw() == True:
    scrtchpd.pad("X")
  if k_z.draw() == True:
    scrtchpd.pad("Z")
  if k_slant.draw() == True:
    scrtchpd.pad("/")
  if k_sp.draw() == True:
    scrtchpd.pad(" ")
  if k_ovfy.draw() == True:
    scrtchpd.pad("Δ")
  if k_clr.draw() == True:
    scrtchpd.pad("CLR")
  if k_1.draw() == True:
    scrtchpd.pad("1")
  if k_2.draw() == True:
    scrtchpd.pad("2")
  if k_3.draw() == True:
    scrtchpd.pad("3")
  if k_4.draw() == True:
    scrtchpd.pad("4")
  if k_5.draw() == True:
    scrtchpd.pad("5")
  if k_6.draw() == True:
    scrtchpd.pad("6")
  if k_7.draw() == True:
    scrtchpd.pad("7")
  if k_8.draw() == True:
    scrtchpd.pad("8")
  if k_9.draw() == True:
    scrtchpd.pad("9")
  if k_0.draw() == True:
    scrtchpd.pad("0")
  if k_dot.draw() == True:
    scrtchpd.pad(".")
  if k_plusminus.draw() == True:
    scrtchpd.pad("+")

  #softkeys - INIT A
  if currPage == "initA":
    if l1sk.draw() == True:
      if scrtchpd.pad("") == "VHHHRCTP01":
        corte = "VHHHRCTP01"
        depdest = "VHHH/RCTP"
        depdestclr = cyan
        corteclr = cyan
        initrqvis = False
        reset.resetdispl()
        scrtchpd.clear()
        sinita.InitA()
      elif scrtchpd.pad("") == "     CLR":
        corte = "__________"
        depdest = "____/____"
        depdestclr = orange
        corteclr = orange
        initrqvis = True
        reset.resetdispl()
        scrtchpd.clear()
        sinita.InitA()
      else:
        scrtchpd.invalidinpt("INVALID CO RTE")
        time.sleep(2.1)         
    if l2sk.draw() == True:
      if scrtchpd.pad("") == "RCKH/RCTPRCKH01":
        altncorte = "RCKH/RCTPRCKH01"
        reset.resetdispl()
        scrtchpd.clear()
        sinita.InitA()
      elif scrtchpd.pad("") == "     CLR":
        depdest = "____/__________"
        reset.resetdispl()
        scrtchpd.clear()
        sinita.InitA()
      else:
        scrtchpd.invalidinpt("INVALID ALTN")
        time.sleep(2.1)      
    if l3sk.draw() == True:
      if scrtchpd.pad("").isalnum() == True:
        fltnbr = scrtchpd.pad("")
        fltnbrclr = cyan
        reset.resetdispl()
        scrtchpd.clear()
        sinita.InitA()
      elif scrtchpd.pad("") == "     CLR":
        fltnbr = "________"
        fltnbrclr = orange
        reset.resetdispl()
        scrtchpd.clear()
        sinita.InitA()
      else:
        scrtchpd.invalidinpt("INVALID INPUT")
        time.sleep(2.1)      
    if l4sk.draw() == True:
      reset.resetdispl()
      sinop.inopPages()
    if l5sk.draw() == True:
      if scrtchpd.pad("").isdecimal() == True and int(scrtchpd.pad("")) <= 150:
        costi = scrtchpd.pad("")
        ciclr = cyan
        reset.resetdispl()
        scrtchpd.clear()
        sinita.InitA()
      elif scrtchpd.pad("") == "     CLR":
        costi = "---"
        ciclr = cyan
        reset.resetdispl()
        scrtchpd.clear()
        sinita.InitA()
      else:
        scrtchpd.invalidinpt("INVALID COST INDEX")
        time.sleep(2.1)      
    if l6sk.draw() == True:
      if scrtchpd.pad("").isdecimal() == True:
        if int(scrtchpd.pad("")) >= 2000 and int(scrtchpd.pad("")) % 100 == 0 and int(scrtchpd.pad("")) <= 39500:
          crzalt = int(scrtchpd.pad(""))   
          flclr = cyan
          reset.resetdispl()
          scrtchpd.clear()
          sinita.InitA()
        elif len(scrtchpd.pad("")) <= 3 and int(scrtchpd.pad("")) in range(20, 391):
          crzalt = int(scrtchpd.pad("")) * 100
          flclr = cyan
          reset.resetdispl()
          scrtchpd.clear()
          sinita.InitA()
        else:
          scrtchpd.invalidinpt("INVALID CRZ ALT")
          time.sleep(2.1)
      elif len(scrtchpd.pad("")) == 5 and scrtchpd.pad("").isalnum() == True:
        if scrtchpd.pad("")[0] + scrtchpd.pad("")[1] == "FL": 
          crzalt = int(scrtchpd.pad("")[2] + scrtchpd.pad("")[3] + scrtchpd.pad("")[4])*100
          flclr = cyan
          reset.resetdispl()
          scrtchpd.clear()
          sinita.InitA()
        else:
          scrtchpd.invalidinpt("INVALID CRZ ALT")
          time.sleep(2.1)
      elif len(scrtchpd.pad("")) == 4 and scrtchpd.pad("").isalnum() == True:
        if scrtchpd.pad("")[0] + scrtchpd.pad("")[1] == "FL": 
          crzalt = int(scrtchpd.pad("")[2] + scrtchpd.pad("")[3])*100
          flclr = cyan
          reset.resetdispl()
          scrtchpd.clear()
          sinita.InitA()
        else:
          scrtchpd.invalidinpt("INVALID CRZ ALT")
          time.sleep(2.1)
      elif scrtchpd.pad("") == "     CLR":
        crzalt = "-----"
        flclr = white
        reset.resetdispl()
        scrtchpd.clear()
        sinita.InitA()
      else:
        scrtchpd.invalidinpt("INVALID CRZ ALT")
        time.sleep(2.1)  
        
    if r1sk.draw() == True:
      if scrtchpd.pad("") == "VHHH/RCTP":
        depdest = "VHHH/RCTP"
        depdestclr = cyan
        initrqvis = False
        reset.resetdispl()
        print(depdest)
        scrtchpd.clear()
        sinita.InitA()
      elif scrtchpd.pad("") == "     CLR":
        depdest = "____/____"
        depdestclr = orange
        reset.resetdispl()
        initrqvis = True
        scrtchpd.clear()
        sinita.InitA()
      else:
        scrtchpd.invalidinpt("INVALID INPUT")
        time.sleep(2.1)
    if r2sk.draw() == True:
      reset.resetdispl()
      sinop.inopPages()
    if r3sk.draw() == True:
      reset.resetdispl()
      sinop.inopPages()
    if r4sk.draw() == True:
      reset.resetdispl()
      sinop.inopPages()
    if r5sk.draw() == True:
      reset.resetdispl()
      sinop.inopPages()
    if r6sk.draw() == True:
      reset.resetdispl()
      sinop.inopPages()
  pygame.display.flip()


