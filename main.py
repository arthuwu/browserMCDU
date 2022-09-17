import pygame
import pygame.font

pygame.init()
width, height = 514, 800
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Airbus MCDU")

mcduframe = pygame.image.load("mcduframe.png").convert()
framerect = mcduframe.get_rect()
mcdubutton = pygame.image.load("mcdubutton.png").convert()
plankbtntemp = pygame.image.load("plankbtntemp.png").convert()
akey = pygame.image.load("transparenta.png").convert()

#logic vars
currPage = "menu1"
scratch = ""

#colour vars
red = (255, 0, 0)
green = (0, 255, 0)
cyan = (94, 198, 255)
grey = (70, 70, 70)
white = (255, 255, 255)

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

  def InitA(self):
    font = pygame.font.Font("HoneywellMCDU.ttf", 30)
    text_surface = font.render('PAGE INOP', True, red)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (165,188)
    screen.blit(text_surface, text_rect)
  def StartMenu(self):
    font = pygame.font.Font("HoneywellMCDU.ttf", 23)
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
    title_rect.topleft = (255,156)
    screen.blit(title, title_rect)
    title = font.render('AIRAC 2210', True, grey)
    title_rect = title.get_rect()
    title_rect.topleft = (95,200)
    screen.blit(title, title_rect)
    title = font.render('[   ]', True, grey)
    title_rect = title.get_rect()
    title_rect.topleft = (95,289)
    screen.blit(title, title_rect)
    font = pygame.font.Font("HoneywellMCDU.ttf", 16)
    title = font.render('ENG', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (123,91)
    screen.blit(title, title_rect)
    title = font.render('ACTIVE NAV DATA BASE', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (114,138)
    screen.blit(title, title_rect)
    title = font.render('SECOND NAV DATA BASE', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (114,182)
    screen.blit(title, title_rect)
    title = font.render('CHG CODE', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (94,270)
    screen.blit(title, title_rect)
    title = font.render('IDLE/PERF', True, white)
    title_rect = title.get_rect()
    title_rect.topleft = (94, 319)
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
    self.rect = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(78, 347, 358, 29))

  def pad(self, inpt):
    global scratch
    act = True
    if act == True:
      font = pygame.font.Font("HoneywellMCDU.ttf", 23)
      if inpt == "CLR":
        if scratch == "":
          scratch = "     CLR"
        elif scratch == "     CLR":
          scratch = ""
        else:
          scratch = scratch[:-1]
      elif input == "":
        text = font.render(scratch, True, white)
        return 
      else:
        scratch = str(scratch) + inpt
        
      screen.fill(backgroundColor)
      screen.blit(mcduframe, framerect)
      text = font.render(scratch, True, white)
      text_rect = text.get_rect()
      text_rect.topleft = (87, 350)
      screen.blit(text, text_rect)
      return text
      
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
k_clr = Button(420 , 740, akey)


#page select keys
blank = Button(370, 406, plankbtntemp)
init = Button(180, 406, plankbtntemp)

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
scrtchpd = Scratchpad()

screen.fill(backgroundColor)
screen.blit(mcduframe, framerect)

while True:
  if l1sk.draw() == True:
    screen.fill(backgroundColor)
    screen.blit(mcduframe, framerect)
    sinita.InitA()
  if l2sk.draw() == True:
    screen.fill(backgroundColor)
    screen.blit(mcduframe, framerect)
    scrtchpd.pad("")
  if l3sk.draw() == True:
    print(pygame.font.get_fonts())
  if l4sk.draw() == True:
    print(pygame.font.get_fonts())
  if l5sk.draw() == True:
    print(pygame.font.get_fonts())
  if l6sk.draw() == True:
    print(pygame.font.get_fonts())
  if r1sk.draw() == True:
    print(pygame.font.get_fonts())
  if r2sk.draw() == True:
    print(pygame.font.get_fonts())
  if r3sk.draw() == True:
    print(pygame.font.get_fonts())
  if r4sk.draw() == True:
    print(pygame.font.get_fonts())
  if r5sk.draw() == True:
    print(pygame.font.get_fonts())
  if r6sk.draw() == True:
    print(pygame.font.get_fonts())
  if blank.draw() == True:
    screen.fill(backgroundColor)
    screen.blit(mcduframe, framerect)
    sfmgcmnu.StartMenu()
  if blank.draw() == True:
    screen.fill(backgroundColor)
    screen.blit(mcduframe, framerect)
    sfmgcmnu.StartMenu()
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
  if k_clr.draw() == True:
    scrtchpd.pad("CLR")
  pygame.display.flip()


