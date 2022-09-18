import pygame
import pygame.font
import time

pygame.init()
width, height = 514, 800
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Airbus MCDU")

mcduframe = pygame.image.load("mcduframe.png").convert()
framerect = mcduframe.get_rect()
mcdubutton = pygame.image.load("mcdubutton.png").convert()
plankbtntemp = pygame.image.load("plankbtntemp.png").convert()
akey = pygame.image.load("akey.png").convert()
circularbutton = pygame.image.load("circularbutton.png").convert()

#logic vars
currPage = ""
scratch = ""

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
    if crzalt != 0:
      crzfl = "FL" + str(int(crzalt)/100)
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
    
  def StartMenu(self):
    global currPage
    currPage = "menu1"
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
    title_rect.topleft = (86, 339)
    screen.blit(title, title_rect)
    title = font.render('MADE WITH', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (318,325)
    screen.blit(title, title_rect)
    title = font.render('PYGAME ON REPLIT', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (238, 344)
    screen.blit(title, title_rect)

class Scratchpad():
  def __init__(self):
    self.rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(82, 360, 350, 29))
    blocker = pygame.Surface((350, 29))
    blocker.fill((0, 0, 0))
    screen.blit(blocker, self.rect)

  def pad(self, inpt):
    global scratch
    act = True
   
    if act == True:
      font = pygame.font.Font("HoneywellMCDU.ttf", 21)
      if len(scratch) >= 23 and inpt != "CLR":
        self.invalidinpt("TOO LONG")
        return
      elif inpt == "CLR":
        if scratch == "":
          scratch = "     CLR"
        elif scratch == "     CLR":
          scratch = ""
        else:
          scratch = scratch[:-1]
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
k_b =  Button(260 , 500, akey)
k_c =  Button(312 , 500, akey)
k_d =  Button(366 , 500, akey)
k_e =  Button(420 , 500, akey)
k_f =  Button(206 , 548, akey)
k_g =  Button(260 , 548, akey)
k_h =  Button(312 , 548, akey)
k_i =  Button(366 , 548, akey)
k_j =  Button(420 , 548, akey)
k_k =  Button(206 , 596, akey)
k_l =  Button(260 , 596, akey)
k_m =  Button(312 , 596, akey)
k_n =  Button(366 , 596, akey)
k_o =  Button(420 , 596, akey)
k_p =  Button(206 , 644, akey)
k_q =  Button(260 , 644, akey)
k_r =  Button(312 , 644, akey)
k_s =  Button(366 , 644, akey)
k_t =  Button(420 , 644, akey)
k_u =  Button(206 , 692, akey)
k_v =  Button(260 , 692, akey)
k_w =  Button(312 , 692, akey)
k_x =  Button(366 , 692, akey)
k_y =  Button(420 , 692, akey)
k_z =  Button(206 , 740, akey)
k_slant =  Button(260 , 740, akey)
k_sp =  Button(312 , 740, akey)
k_ovfy =  Button(366 , 740, akey)
k_clr = Button(420 , 740, akey)
k_1 = Button(55, 618, circularbutton)
k_2 = Button(105, 618, circularbutton)
k_3 = Button(156, 618, circularbutton)
k_4 = Button(55, 660, circularbutton)
k_5 = Button(105, 660, circularbutton)
k_6 = Button(156, 660, circularbutton)
k_7 = Button(55, 701, circularbutton)
k_8 = Button(105, 701, circularbutton)
k_9 = Button(156, 701, circularbutton)
k_0 = Button(105, 742, circularbutton)
k_dot = Button(55, 742, circularbutton)
k_plusminus = Button(156, 742, circularbutton)

#page select keys
blank = Button(370, 421, plankbtntemp)
init = Button(245, 421, plankbtntemp)
data = Button(308, 421, plankbtntemp)
perf = Button(181, 421, plankbtntemp)
prog = Button(118, 421, plankbtntemp)
dir = Button(56, 421, plankbtntemp)
mcdumenu = Button(370, 459, plankbtntemp)
secfpln = Button(245, 459, plankbtntemp)
atccomm = Button(308, 459, plankbtntemp)
fuelpred = Button(181, 459, plankbtntemp)
radnav = Button(118, 459, plankbtntemp)
fpln = Button(56, 459, plankbtntemp)
blank2 = Button(118, 497, plankbtntemp)
airport = Button(56, 497, plankbtntemp)
up = Button(118, 535, plankbtntemp)
left = Button(56, 535, plankbtntemp)
down = Button(118, 573, plankbtntemp)
right = Button(56, 573, plankbtntemp)
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
sfmgcmnu = fmgc() #fmgcmenu
sinop = fmgc()
reset = fmgc()
scrtchpd = Scratchpad()


screen.fill(backgroundColor)
screen.blit(mcduframe, framerect)
sfmgcmnu.StartMenu()

while True:
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
    sfmgcmnu.StartMenu()
  if init.draw() == True:
    reset.resetdispl()
    sinita.InitA()
  dir.draw()
  perf.draw()
  prog.draw()
  data.draw()
  fpln.draw()
  atccomm.draw()
  secfpln.draw()
  mcdumenu.draw()
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
    l4sk.draw()
    if l5sk.draw() == True:
      if scrtchpd.pad("").isdecimal() == True and int(scrtchpd.pad("")) <= 150:
        costi = scrtchpd.pad("")
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
      print(pygame.font.get_fonts())
    if r3sk.draw() == True:
      print(pygame.font.get_fonts())
    if r4sk.draw() == True:
      print(pygame.font.get_fonts())
    if r5sk.draw() == True:
      print(pygame.font.get_fonts())
    if r6sk.draw() == True:
      screen.fill(backgroundColor)
      screen.blit(mcduframe, framerect)
      sinop.inopPages()
  
  pygame.display.flip()


