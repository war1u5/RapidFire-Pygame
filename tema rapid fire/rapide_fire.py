import pygame
import sys
import random
import time

############################ init visual stuff ###############################
pygame.init()
(6, 0)
pygame.font.init()
pygame.mixer.init()


################################# Classes ####################################
################################# Worlds #####################################

################################# Helios #####################################

#cursor
class Player( pygame.sprite.Sprite ):
    def __init__( self ):
        pygame.sprite.Sprite.__init__( self )
        self.image = crosshair_img
        self.rect = self.image.get_rect()
        
    def update( self ):
        self.rect.center = pygame.mouse.get_pos()
        
#planet
class Target( pygame.sprite.Sprite ):
    def __init__( self ):
        pygame.sprite.Sprite.__init__( self )
        self.image = target_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint( 0, wn_width - self.rect.width )
        self.rect.y = random.randint( -100, -40 )
        self.speedy = 2
        self.speedx = 2
        
    def update( self ):
        #self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        
        #check boundaries
        if self.rect.right < 0 or self.rect.left > wn_width:
            self.rect.x = random.randint( 0, wn_width - self.rect.width )
            self.rect.y = random.randint( -100, -40 )
            #self.speedy = random.randint( 1, 3 )
            #self.speedx = random.randint( -1, 1 )
            
        #check the buttom
        if self.rect.top > wn_height:
            with open( "players.txt", "a" ) as f:
                        f.write( " Level 1 not completed." )
                        f.write( "\n" )
                        f.close()
            font = pygame.font.SysFont( "ocr a extended" , 40 )
            text = font.render( "Game Over!", True, red )
            wn.blit( text, ( 110 , wn_height / 2 ) )
            pygame.display.flip()
            time.sleep(3)
            game_intro2()
            

################################### Venice ###################################

#cursor          
class Player2( pygame.sprite.Sprite ):
    def __init__( self ):
        pygame.sprite.Sprite.__init__( self )
        self.image = crosshair_img2
        self.rect = self.image.get_rect()
        
    def update( self ):
        self.rect.center = pygame.mouse.get_pos()
        
#pizza
class Target2( pygame.sprite.Sprite ):
    def __init__( self ):
        pygame.sprite.Sprite.__init__( self )
        self.image = target_img2
        self.rect = self.image.get_rect()
        self.rect.x = random.randint( 0, wn_width - self.rect.width )
        self.rect.y = random.randint( -100, -40 )
        self.speedy = 3
        self.speedx = 3
        
    def update( self ):
        #self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        
        #check boundaries
        if self.rect.right < 0 or self.rect.left > wn_width:
            self.rect.x = random.randint( 0, wn_width - self.rect.width )
            self.rect.y = random.randint( -100, -40 )
            #self.speedy = random.randint( 1, 3 )
            #self.speedx = random.randint( -1, 1 )
        
        if self.rect.top > wn_height: #check the bottom
            with open( "players.txt", "a" ) as f:
                        f.write( " Level 2 not completed." )
                        f.write( "\n" )
                        f.close()
            font = pygame.font.SysFont( "ocr a extended" , 40 )
            text = font.render( "Game Over!", True, red )
            wn.blit( text, ( 115, wn_height / 2 ) )
            pygame.display.flip()
            time.sleep(3)
            game_intro2()
            
            
################################ Dynasty #####################################

#cursor
class Player3( pygame.sprite.Sprite ):
    def __init__( self ):
        pygame.sprite.Sprite.__init__( self )
        self.image = crosshair_img3
        self.rect = self.image.get_rect()
        
    def update( self ):
        self.rect.center = pygame.mouse.get_pos()
        
#noodles   
class Target3( pygame.sprite.Sprite ):
    def __init__( self ):
        pygame.sprite.Sprite.__init__( self )
        self.image = target_img3
        self.rect = self.image.get_rect()
        self.rect.x = random.randint( 0, wn_width - self.rect.width )
        self.rect.y = random.randint( -100, -40 )
        self.speedy = 3 #random.randint( 1, 3 )
        self.speedx = 3 #random.randint( -1, 1 )
        
    def update( self ):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        
        #check boundaries
        if self.rect.right < 0 or self.rect.left > wn_width:
            self.rect.x = random.randint( 0, wn_width - self.rect.width )
            self.rect.y = random.randint( -100, -40 )
            self.speedy = random.randint( 1, 3 )
            self.speedx = random.randint( -1, 1 )
            
        #check the bottom
        if self.rect.top > wn_height:
            with open( "players.txt", "a" ) as f:
                        f.write( " Level 3 not completed." )
                        f.write( "\n" )
                        f.close()
            font = pygame.font.SysFont( "ocr a extended" , 50 )
            text = font.render( "Game Over!", True, (255, 255, 255 ) )
            wn.blit( text, ( 80, wn_height / 2 - 180 ) )
            pygame.display.flip()
            time.sleep(3)
            game_intro2()

#building
class Target4( pygame.sprite.Sprite ):
    def __init__( self ):
        pygame.sprite.Sprite.__init__( self )
        self.image = target_img4
        self.rect = self.image.get_rect()
        self.rect.x = random.randint( 0, wn_width - self.rect.width )
        self.rect.y = random.randint( -100, -40 )
        self.speedy = 3 #random.randint( 1, 3 )
        self.speedx = 3 #random.randint( -1, 1 )
        
    def update( self ):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        
        #check boundaries
        if self.rect.right < 0 or self.rect.left > wn_width:
            self.rect.x = random.randint( 0, wn_width - self.rect.width )
            self.rect.y = random.randint( -100, -40 )
            self.speedy = random.randint( 1, 3 )
            self.speedx = random.randint( -1, 1 )
            
        #check the bottom
        if self.rect.top > wn_height: 
            with open( "players.txt", "a" ) as f:
                        f.write( " Level 3 not completed." )
                        f.write( "\n" )
                        f.close()
            font = pygame.font.SysFont( "ocr a extended" , 50 )
            text = font.render( "Game Over!", True, (255, 255, 255) )
            wn.blit( text, ( 80, wn_height / 2 - 180 ) )
            pygame.display.flip()
            time.sleep(3)
            game_intro2()
            
##############################################################################
############################## END OF CLASSES ################################
##############################################################################

#clock (fps related)
clock = pygame.time.Clock()
fps = 60


################################# colors #####################################

white = ( 255, 255, 255 )
blue = ( 0, 0, 255 )
black = ( 0, 0, 0 )
red = ( 200, 0, 0 )
bright_red = ( 255, 0, 0 )
green = ( 0, 200, 0 )
bright_green = ( 0, 255, 0 )
pink = ( 255, 0, 205 )
bright_pink = ( 255, 100, 225 )

ic = ( 255, 100, 225 ) #inactive color
ac = ( 0, 255, 0 ) #active color
color = ( 255, 100, 225 )

##############################################################################


################################ game wn #####################################

wn_width = 450
wn_height = 650
wn = pygame.display.set_mode( ( wn_width, wn_height ) ) 
pygame.display.set_caption( "Rapid Fire (Retro Edition)" )
icon = pygame.image.load( "joypad.png" )
pygame.display.set_icon( icon )

##############################################################################


#text pentru paginile cu Worlds atunci cand Game over (tho am facut niste
#schimbari si functioneaza independent -- TODO: check if redundant)
font = pygame.font.SysFont( "ocr a extended", 20 )
text = font.render( "Game Over!", True, red )


##############################################################################
############################# PAGINILE JOCULUI ###############################
##############################################################################

################################# MAIN MENU ##################################

bg_img = pygame.image.load( "bg.png" )
bg_img = pygame.transform.scale( bg_img, (450,660) )


############################### levels menu ##################################

menu_img = pygame.image.load( "menu.png" )
menu_img = pygame.transform.scale( menu_img, (450,660) )


################################# HELIOS #####################################

bg_img1 = pygame.image.load( "1.png" )
bg_img1 = pygame.transform.scale( bg_img1, (450,760) )
crosshair_img = pygame.image.load( "crosshair.png" )
target_img = pygame.image.load( "neptune.png" )
hit_sound = pygame.mixer.Sound( "saber.wav" )


################################## VENICE ####################################

bg_img2 = pygame.image.load( "2.png" )
bg_img2 = pygame.transform.scale( bg_img2, (450,760) )
venice = pygame.image.load( "venice.png" ) 
venice = pygame.transform.scale( venice, (450,760) )
crosshair_img2 = pygame.image.load( "knife.png" )
target_img2 = pygame.image.load( "pizza.png" )
hit_sound2 = pygame.mixer.Sound( "slash.wav" )


################################## Dynasty ###################################

bg_img3 = pygame.image.load( "3.png" )
bg_img3 = pygame.transform.scale( bg_img3, (450,760) )
crosshair_img3 = pygame.image.load( "axe.png" )
target_img3 = pygame.image.load( "noodles.png" )
target_img4 = pygame.image.load( "china.png" )
hit_sound3 = pygame.mixer.Sound( "slash.wav" )


################################# redundant! #################################

bg_img4 = pygame.image.load( "chill.png" )
bg_img4 = pygame.transform.scale( bg_img4, (450,760) )


##############################################################################
################ face cursorul ala basic de windows invizibil ################

pygame.mouse.set_visible( False )


############################# func pentru scor ###############################
 
def score_board( score ):
    
    font = pygame.font.SysFont( "ocr a extended", 20 )
    text = font.render( "Score: " + str( score ), True, white )
    pygame.draw.rect(wn, black, (600, 450, 100, 50))
    wn.blit( text, ( 10, 10 ) )


################### pentru timer (acelasi concept ca mai sus) ################

def timer_board( seconds ):
    
    font = pygame.font.SysFont( "ocr a extended", 20 )
    text = font.render( "Seconds: " + str( seconds ), True, white )
    pygame.draw.rect(wn, black, (600, 450, 100, 50))
    wn.blit( text, ( 310, 10 ) )
    

######################## text pentru main menu text ##########################

def text_objects( text, font ): 
    
    textSurface = font.render( text, True, ( random.randint(135,240), 30, random.randint(75,225) ) )
    return textSurface, textSurface.get_rect()


##### text pentru butoane (ulterior si alte lucruri ie. func intro_helios)####

def text_objects1( text, font ): 
    
    textSurface = font.render( text, True, ( 255, 255, 255 ) )
    return textSurface, textSurface.get_rect()


####################### text pentru func intro_venice ########################

def text_objects2( text, font ): 
    
    textSurface = font.render( text, True, ( 255, 94, 0 ) )
    return textSurface, textSurface.get_rect()


################## func pentru blit text anywhere pretty much ################

def message_display( text ):
    
    largeText = pygame.font.SysFont( 'ocr a extended', 115 )
    TextSurf, TextRect = text_objects( text, largeText )
    TextRect.center = ( ( wn_width/2),( wn_height/2 ) )
    wn.blit( TextSurf, TextRect )
    
    
######################## pentru creare de butoane ############################

def button( msg, x, y, w, h, ic, ac, action = None ):
    
    #msg -> ce vrei sa scrie pe buton
    #x -> x location of the top left coordinate of the button box
    #y -> y location of the top left coordinate of the button box
    #w -> button width
    #h -> button height
    #ic -> inactive color
    #ac -> active color (when hovering over it)
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(wn, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            action()
            
    else:
        pygame.draw.rect( wn, ic, (x,y,w,h) )

    smallText = pygame.font.SysFont( "ocr a extended",20 )
    textSurf, textRect = text_objects1( msg, smallText )
    textRect.center = ( (x + (w/2) ), ( y + (h/2) ) )
    wn.blit( textSurf, textRect )
    
    
##### when called it helps u quit the game at any point in time n space ######

def quit_game():
    
    pygame.quit()
    sys.exit()


################################## Main Menu #################################

def game_intro(): 
    
    check = False
    
    intro = True
    
    #cursor
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    #pt a se inchide de la "x"
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #quit()
        
        #print bg onto page
        wn.blit( bg_img, (0,0) )
        
        #titlu main page
        largeText = pygame.font.SysFont( "ocr a extended", 50 )
        TextSurf, TextRect = text_objects( "RAPID FIRE", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 190 ) )
        wn.blit( TextSurf, TextRect )
        
        #subtitlu main page
        largeText = pygame.font.SysFont( "ocr a extended", 20 ) 
        TextSurf, TextRect = text_objects( "RETRO EDITION", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 150 ) )
        wn.blit( TextSurf, TextRect )
        
        #butoanele de pe main page
        if check == False:
            button( "GO!", 50,450,100,50, green, bright_green, username_page )
            button( "Worlds", 175,450,100,50, pink, bright_pink, levels_menu )
            button( "Quit", 300,450,100,50, red, bright_red, quit_intrebare )
            check == True
            
        #score page
        if check == True:
            button( "Score History", 135,350,180,50, pink, bright_pink, score_page )
         
        #cursor related
        player_group.update()
        player_group.draw( wn )
        
        pygame.display.update()
        clock.tick( fps )
        
        

def game_intro2(): 
    
    intro = True
    
    #cursor
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    #pt a se inchide de la "x"
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #quit()
        
        #print bg onto page
        wn.blit( bg_img, (0,0) )
        
        #titlu main page
        largeText = pygame.font.SysFont( "ocr a extended", 50 )
        TextSurf, TextRect = text_objects( "RAPID FIRE", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 190 ) )
        wn.blit( TextSurf, TextRect )
        
        #subtitlu main page
        largeText = pygame.font.SysFont( "ocr a extended", 20 ) 
        TextSurf, TextRect = text_objects( "RETRO EDITION", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 150 ) )
        wn.blit( TextSurf, TextRect )
        
        #butoanele de pe main page
        button( "GO!", 50,450,100,50, green, bright_green, username_page )
        button( "Worlds", 175,450,100,50, pink, bright_pink, levels_menu )
        button( "Quit", 300,450,100,50, red, bright_red, quit_intrebare )

        #score page
        button( "Score History", 135,350,180,50, pink, bright_pink, score_page )
         
        #cursor related
        player_group.update()
        player_group.draw( wn )
        
        pygame.display.update()
        clock.tick( fps )
        
        
############### tab care te mai pune o data sa dai exit ######################

def quit_intrebare(): 
    
    sure = True
    
    #cursor
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    #pt a se inchide de la "x"
    while sure:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #quit()
        
        #print bg onto page
        wn.fill( black )
        
        #titlu (intrebare)
        largeText = pygame.font.SysFont( "ocr a extended", 50 )
        TextSurf, TextRect = text_objects( "EXIT GAME", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 70) )
        wn.blit( TextSurf, TextRect )
        
        #butoanele de pe main page
        button( "Go back", 95,300,100,50, pink, bright_pink, game_intro2 )
        button( "EXIT", 255,300,100,50, red, bright_red, quit_game )
        
         
        #cursor related
        player_group.update()
        player_group.draw( wn )
        
        pygame.display.update()
        clock.tick( fps )


############################### pt username ##################################

def username_page(): 
    
    #pt limìta de caractere
    count = 0
    
    #pt limita de players
    players = 0
    
    #cursor
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    #user settings
    user_text = ""
    user_font = pygame.font.SysFont( "ocr a extended", 20 )
    user_rect = pygame.Rect( ( wn_width/2 - 90 ), ( wn_height/2 - 92 ) , 181, 28 )
    
    
    #to check whether the text box is selected or not
    active = False 
    
    running = True
    
    while running:
        
        #print bg onto page
        wn.blit( bg_img, (0,0) )
        
        #culoare text box
        if active == True:
            color = ac
        
        #culoare text box
        if active == False:
            color = ic
            
        #pt a se inchide de la "x"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #quit()
                
            #if clicked by mouse it becomes active
            if event.type == pygame.MOUSEBUTTONDOWN:
                if user_rect.collidepoint( event.pos ):
                    active = True
                else: 
                    active = False
            
            #daca e activ text box, ENTER il dezactiveaza
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_RETURN:
                        active == False
                     
                #rezolvare bug counter negativ
                if count < 0:
                    count = 1
                    
                #aici am scos toate caracterele pe care le am considerat eu nepermise si care ar putea fi scrise in text box atunci cand e activ
                if active == True and count >= 0 and event.key != pygame.K_RETURN and event.key != pygame.K_ESCAPE  and event.key != pygame.K_SPACE:
                    
                    #implementarea tastei BACKSPACE
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                        count = count - 1
                    #aici efectiv se intampla scrisul in text box
                    else:
                        user_text += event.unicode
                        count = count + 1
                        #print(count)
                
                #daca dai ENTER se salveaza username ul in fisier
                if event.key == pygame.K_RETURN:
                    with open( "players.txt", "a" ) as f:
                        f.write( user_text )
                        f.close()
                    players = players + 1
                    active = False
                    intro_helios()
        
        
        #it only saves up to 1 players at once 
        if players > 1:
            largeText7 = pygame.font.SysFont( "ocr a extended", 12 )
            TextSurf7, TextRect7 = text_objects1( "Failed to save. Maximum number of players has been surpassed!", largeText7 )
            TextRect7.center = ( ( wn_width/2 ), ( wn_height/2 - 50 ) )
            wn.blit( TextSurf7, TextRect7 )
        
        #checks for username length
        if count == 9:
            largeText5 = pygame.font.SysFont( "ocr a extended", 15 )
            TextSurf5, TextRect5 = text_objects1( "character limit reached!", largeText5 )
            TextRect5.center = ( ( wn_width/2 ), ( wn_height/2 - 50 ) )
            wn.blit( TextSurf5, TextRect5 )
            active = False
            
            #scade counterul (functionalitate a lui backspace ca sa pot scrie de fiecare data dupa ce folosesc backspace )
            #also text box devine din nou activ atunci cand se foloseste backspace
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and count >= 0:
                    active = True
                    user_text = user_text[:-1]
                    count = count - 1
                else:
                    active = False
                    
                if count <= 0:
                    active = False
            
                    
        #user rect
        pygame.draw.rect( wn, color, user_rect, 2)
        
        #user text  
        text_surface = user_font.render( user_text, True, white )
        wn.blit( text_surface, ( ( user_rect.x + 12 ), ( user_rect.x + 100 ) ) )
        
        #user_rect.w = max(181, text_surface.get_width()  )
        
        #titlu main page
        largeText = pygame.font.SysFont( "ocr a extended", 30 )
        TextSurf, TextRect = text_objects( "INSERT USERNAME", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 130 ) )
        wn.blit( TextSurf, TextRect )
        
        #kinda like start game
        #button( "Done!", 175,300,100,50, pink, bright_green, intro_helios )
        button( ">", ( user_rect.x + 157 ), ( user_rect.x + 100 ), 23, 25, bright_pink, bright_green, intro_helios )
        button( "<-Main Menu", 15,592,150,50, pink, bright_pink, game_intro2 )
        
        #cursor related
        player_group.update()
        player_group.draw( wn )
        
        pygame.display.update()
        clock.tick( fps )


############################ creare meniu levels #############################

def levels_menu():
    
    #cursorul
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    #pentru a inchide cu totul aplicatia de la "X"
    selected = True 
    
    while selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #quit()
        
        #printare background din meniul WORLDS
        wn.blit( menu_img, (0,0) )
        
        #titlu meniu WORLDS
        largeText = pygame.font.SysFont( "ocr a extended", 35 )
        TextSurf, TextRect = text_objects( "SELECT A WORLD", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 280 ) )
        wn.blit( TextSurf, TextRect )
        
        #butoane pentru a selecta worlds
        button( "Helios", 50,150,100,50, (195,70,165), bright_pink, intro_helios )
        button( "Venice", 50,310,100,50, (50,160,140), (45,180,180), intro_venice )
        button( "Dynasty", 50,480,100,50, (100,45,180), (170,105,245), intro_dynasty )
        
        #butoane de navigat (in meniul cu nivele)
        button( "<-Main Menu", 15,592,150,50, pink, bright_pink, game_intro2 )
        #button( "CHECK->", 285,592,150,50, pink, bright_pink, game_loop_final )
        
        #cursor related
        player_group.update()
        player_group.draw( wn )
        
        pygame.display.update()
        clock.tick( fps )
        

#################################### Helios ##################################

def intro_helios():
    
    #cursorul
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    running = True

    while ( running ):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game" )
                        f.write( "\n" )
                        f.close()
                pygame.quit()
                sys.exit()
            
            if ( event.type == pygame.QUIT ) or \
            ( event.type == pygame.KEYDOWN and \
            ( event.key == pygame.K_ESCAPE ) ):
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game" )
                        f.write( "\n" )
                        f.close()
                game_intro2()
        
        #blit background
        wn.blit( bg_img1, (0,0) )
        
        #text on page
        largeText = pygame.font.SysFont( "ocr a extended", 30 )
        
        TextSurf, TextRect = text_objects1( "Level 1 requirements:", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 250 ) )
        wn.blit( TextSurf, TextRect )
        
        TextSurf3, TextRect3 = text_objects1( "Difficulty: Easy", largeText )
        TextRect3.center = ( ( wn_width/2 ), ( wn_height/2 ) )
        wn.blit( TextSurf3, TextRect3 )
        
        
        smallText = pygame.font.SysFont( "ocr a extended", 20 )
        
        TextSurf1, TextRect1 = text_objects1( "-gather a total of 30 points-", smallText )
        TextRect1.center = ( ( wn_width/2 ), ( wn_height/2 - 150 ) )
        wn.blit( TextSurf1, TextRect1 )
        
        TextSurf2, TextRect2 = text_objects1( "-in a time span of 30 seconds-", smallText )
        TextRect2.center = ( ( wn_width/2 ), ( wn_height/2 - 110 ) )
        wn.blit( TextSurf2, TextRect2 )
        
        TextSurf2, TextRect2 = text_objects( "Press ESC to exit to Main Menu", smallText )
        TextRect2.center = ( ( wn_width/2 ), ( wn_height/2 + 250 ) )
        wn.blit( TextSurf2, TextRect2 )
        
        
        button( "<-Main Menu", 15,592,150,50, pink, bright_pink, game_intro2 )
        button( "Let's go!->", 285,592,150,50, pink, bright_green, game_loop )
    
        #cursor related
        player_group.update()
        player_group.draw( wn )
    
        pygame.display.flip()
        clock.tick( fps )
        

def game_loop():
    
    start_ticks = pygame.time.get_ticks()
    
    score = 0
    
    #player
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )

    #target
    target_group = pygame.sprite.Group()
    #generare targets
    for target in range( 3 ):
        new_target = Target()
        target_group.add( new_target )
    
    completed = False
    
    running = True

    while ( running ):
        
        seconds = ( pygame.time.get_ticks() - start_ticks ) // 1000
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game" )
                        f.write( "\n" )
                        f.close()
                pygame.quit()
                sys.exit()
            
            if ( event.type == pygame.QUIT ) or \
            ( event.type == pygame.KEYDOWN and \
            ( event.key == pygame.K_ESCAPE ) ):
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") #the game" )
                        f.write( "\n" )
                        f.close()
                game_intro2()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                hit_sound.play()
                hits = pygame.sprite.spritecollide( player, target_group, True )
                
                for hit in hits:
                    score = score + 1
                    new_target = Target()
                    target_group.add( new_target )
                    
            if score > 30:
                completed = True
                if completed == True:
                    with open( "players.txt", "a" ) as f:
                        f.write( " Level 1,") #completed," )
                        f.close()
                intro_venice()
                #game_loop.quit()
                
            if seconds > 30:
                if completed == False:
                    with open( "players.txt", "a" ) as f:
                        f.write( " -Level 1 not completed." )
                        f.write( "\n" )
                        f.close()
                game_intro2()
                
                
        #blit background
        wn.blit( bg_img1, (0,0) )
        
        
        
        #blit target (planets)
        target_group.update()
        target_group.draw( wn )
        
        #blit player (crosshair)
        player_group.update()
        player_group.draw( wn )
        
        #score board
        score_board( score )
        
        #timer board
        timer_board( seconds )
                
        pygame.display.flip()
        clock.tick( fps )
    
        
################################### Venice ###################################

def intro_venice():
    
   #cursorul
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    running = True

    while ( running ):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game." )
                        f.write( "\n" )
                        f.close()
                pygame.quit()
                sys.exit()
            
            if ( event.type == pygame.QUIT ) or \
            ( event.type == pygame.KEYDOWN and \
            ( event.key == pygame.K_ESCAPE ) ):
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game." )
                        f.write( "\n" )
                        f.close()
                game_intro2()
                
        
        #blit background
        #wn.blit( venice, (0,0) )  # nu se vede bine
        wn.fill( black )
        
        #text on page
        largeText = pygame.font.SysFont( "ocr a extended", 30 )
        
        TextSurf, TextRect = text_objects2( "Level 2 requirements:", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 250 ) )
        wn.blit( TextSurf, TextRect )
        
        TextSurf3, TextRect3 = text_objects2( "Difficulty: Medium", largeText )
        TextRect3.center = ( ( wn_width/2 ), ( wn_height/2 ) )
        wn.blit( TextSurf3, TextRect3 )
        
        
        smallText = pygame.font.SysFont( "ocr a extended", 20 )
        
        TextSurf1, TextRect1 = text_objects2( "-gather a total of 50 points-", smallText )
        TextRect1.center = ( ( wn_width/2 ), ( wn_height/2 - 150 ) )
        wn.blit( TextSurf1, TextRect1 )
        
        TextSurf2, TextRect2 = text_objects2( "-in a time span of 20 seconds-", smallText )
        TextRect2.center = ( ( wn_width/2 ), ( wn_height/2 - 110 ) )
        wn.blit( TextSurf2, TextRect2 )
        
        TextSurf2, TextRect2 = text_objects( "Press ESC to exit to Main Menu", smallText )
        TextRect2.center = ( ( wn_width/2 ), ( wn_height/2 + 250 ) )
        wn.blit( TextSurf2, TextRect2 )
        
        
        button( "<-Main Menu", 15,592,150,50, pink, bright_pink, game_intro2 )
        button( "Let's go!->", 285,592,150,50, pink, bright_green, game_loop2 )
    
        #cursor related
        player_group.update()
        player_group.draw( wn )
    
        pygame.display.flip()
        clock.tick( fps )


def game_loop2():
    
    score = 0
    
    #timer
    start_ticks = pygame.time.get_ticks()
    
    #player
    player2 = Player2()
    player_group2 = pygame.sprite.Group()
    player_group2.add( player2 )

    #target
    target_group2 = pygame.sprite.Group()
    #generare targets
    for target2 in range( 6 ):
        new_target2 = Target2()
        target_group2.add( new_target2 )
    
    completed = False
    
    running = True

    while ( running ):
        
        #timer
        seconds = ( pygame.time.get_ticks()-start_ticks ) // 1000
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game" )
                        f.write( "\n" )
                        f.close()
                pygame.quit()
                sys.exit()
            
            if ( event.type == pygame.QUIT ) or \
            ( event.type == pygame.KEYDOWN and \
            ( event.key == pygame.K_ESCAPE ) ):
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game" )
                        f.write( "\n" )
                        f.close()
                game_intro2()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                hit_sound2.play()
                hits = pygame.sprite.spritecollide( player2, target_group2, True )
                for hit in hits:
                    score = score + 1
                    new_target2 = Target2()
                    target_group2.add( new_target2 )
                    
            if score == 50:
                completed = True
                if completed == True:
                    with open( "players.txt", "a" ) as f:
                        f.write( " Level 2,") # completed" )
                        f.close()
                        
            if score == 50:
                intro_dynasty()
                
            if seconds == 20:
                if completed == False:
                    with open( "players.txt", "a" ) as f:
                        f.write( " Level 2 not completed." )
                        f.write( "\n" )
                        f.close()
                game_intro2()
                    
        
        #blit background
        wn.blit( bg_img2, (0,0) )
        
        #blit target (pizza)
        target_group2.update()
        target_group2.draw( wn )
        
        #blit player (knife)
        player_group2.update()
        player_group2.draw( wn )
        
        #score board
        score_board( score )
        
        #timer board
        timer_board( seconds )
                
        pygame.display.flip()
        clock.tick( fps )
        
     
################################## Dynasty ###################################

def intro_dynasty():
    
   #cursorul
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    running = True

    while ( running ):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game" )
                        f.write( "\n" )
                        f.close()
                pygame.quit()
                sys.exit()
            
            if ( event.type == pygame.QUIT ) or \
            ( event.type == pygame.KEYDOWN and \
            ( event.key == pygame.K_ESCAPE ) ):
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game" )
                        f.write( "\n" )
                        f.close()
                game_intro2()
                
        
        #blit background
        wn.blit( bg_img3, (0,0) )
        
        #text on page
        largeText = pygame.font.SysFont( "ocr a extended", 30 )
        
        TextSurf, TextRect = text_objects1( "Level 3 requirements:", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 250 ) )
        wn.blit( TextSurf, TextRect )
        
        TextSurf3, TextRect3 = text_objects1( "Difficulty: Hard", largeText )
        TextRect3.center = ( ( wn_width/2 ), ( wn_height/2 ) )
        wn.blit( TextSurf3, TextRect3 )
        
        
        smallText = pygame.font.SysFont( "ocr a extended", 20 )
        
        TextSurf1, TextRect1 = text_objects1( "-gather a total of 50 points-", smallText )
        TextRect1.center = ( ( wn_width/2 ), ( wn_height/2 - 150 ) )
        wn.blit( TextSurf1, TextRect1 )
        
        TextSurf2, TextRect2 = text_objects1( "-in a time span of 15 seconds-", smallText )
        TextRect2.center = ( ( wn_width/2 ), ( wn_height/2 - 110 ) )
        wn.blit( TextSurf2, TextRect2 )
        
        TextSurf2, TextRect2 = text_objects( "Press ESC to exit to Main Menu", smallText )
        TextRect2.center = ( ( wn_width/2 ), ( wn_height/2 + 250 ) )
        wn.blit( TextSurf2, TextRect2 )
        
        #buttons
        button( "<-Main Menu", 15,592,150,50, pink, bright_pink, game_intro2 )
        button( "Let's go!->", 285,592,150,50, pink, bright_green, game_loop3 )
    
        #cursor related
        player_group.update()
        player_group.draw( wn )
    
        pygame.display.flip()
        clock.tick( fps )


def game_loop3():
    
    score = 0
    
    start_ticks = pygame.time.get_ticks()
    
    #player (cursor)
    player3 = Player3()
    player_group3 = pygame.sprite.Group()
    player_group3.add( player3 )

    #targets
    target_group4 = pygame.sprite.Group()
    for target4 in range( 2 ):
        new_target4 = Target4()
        target_group4.add( new_target4 )
    
    target_group3 = pygame.sprite.Group()
    for target3 in range( 6 ):
            new_target3 = Target3()
            target_group3.add( new_target3 )
        
    completed = False
    
    running = True

    while ( running ):
        
        seconds = ( pygame.time.get_ticks()-start_ticks ) // 1000
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game" )
                        f.write( "\n" )
                        f.close()
                pygame.quit()
                sys.exit()
            
            if ( event.type == pygame.QUIT ) or \
            ( event.type == pygame.KEYDOWN and \
            ( event.key == pygame.K_ESCAPE ) ):
                with open( "players.txt", "a" ) as f:
                        f.write( " Canceled.") # the game" )
                        f.write( "\n" )
                        f.close()
                game_intro2()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                hit_sound3.play()
                hits1 = pygame.sprite.spritecollide( player3, target_group3, True )
                for hit1 in hits1:
                    score = score + 1
                    new_target3 = Target3()
                    target_group3.add( new_target3 )
                
                hits2 = pygame.sprite.spritecollide( player3, target_group4, True )
                for hit2 in hits2:
                    score = score + 5
                    new_target3 = Target3()
                    target_group3.add( new_target3 )
                  
            if seconds == 17:
                if completed == False:
                    with open( "players.txt", "a" ) as f:
                        f.write( " Level 3 not completed." )
                        f.write( "\n" )
                        f.close()
                game_intro2()  
                  
            if score > 50:
                completed = True
                if completed == True:
                    with open( "players.txt", "a" ) as f:
                        f.write( " Level 3") # completed" )
                        f.write( " => winner" )
                        f.write( "\n" )
                        f.close()
                    game_loop_final()
            
            if score > 50:
                game_loop_final()
                
            #if completed == True:
                #completed_game()
                
        #blit background
        wn.blit( bg_img3, (0,0) )
        
        #blit target (noodles)
        target_group3.update()
        target_group3.draw( wn )
        
        #blit target (building)
        target_group4.update()
        target_group4.draw( wn )
        
        #blit player (knife)
        player_group3.update()
        player_group3.draw( wn )
        
        #score board
        score_board( score )
        
        #timer board
        timer_board( seconds )
        
        pygame.display.flip()
        clock.tick( fps )


################################ end of game #################################

def game_loop_final():
    
    #cursor
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    running = True

    while ( running ):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if ( event.type == pygame.QUIT ) or \
            ( event.type == pygame.KEYDOWN and \
            ( event.key == pygame.K_ESCAPE ) ):
                game_intro2()
                
        
        #blit background
        wn.fill( black )
        
        #text on screen
        largeText = pygame.font.SysFont( "ocr a extended", 50 )
        TextSurf, TextRect = text_objects( "YOU WIN!", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 70) )
        wn.blit( TextSurf, TextRect )
        
        #to go to Main Menu
        button( "MAIN MENU", 150,550,150,50, pink, bright_pink, game_intro2 )
       
        #cursor related
        player_group.update()
        player_group.draw( wn )
       
        pygame.display.flip()
        clock.tick( fps )


################################ score menu #################################
    
def score_page():
    
    users_font = pygame.font.SysFont( "ocr a extended", 15 ) #14 sau asta for good looks
    
    #cursor
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add( player )
    
    running = True

    while ( running ):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if ( event.type == pygame.QUIT ) or \
            ( event.type == pygame.KEYDOWN and \
            ( event.key == pygame.K_ESCAPE ) ):
                game_intro2()
                
            
        #blit background
        wn.fill( black )
        
        with open( "players.txt" ) as f:
            for line in f:
                users_text = users_font.render( line, True, white )
        
        wn.blit( users_text, (20,150) )
        
        #text on screen
        largeText = pygame.font.SysFont( "ocr a extended", 40 )
        TextSurf, TextRect = text_objects( "Score history", largeText )
        TextRect.center = ( ( wn_width/2 ), ( wn_height/2 - 270) )
        wn.blit( TextSurf, TextRect )
        
        largeText21 = pygame.font.SysFont( "ocr a extended", 20 )
        TextSurf21, TextRect21 = text_objects( "Last player's score: ", largeText21 )
        TextRect21.center = ( ( wn_width/2 ), ( wn_height/2 - 220) )
        wn.blit( TextSurf21, TextRect21 )
        
        #to go to Main Menu
        button( "MAIN MENU", 150,550,150,50, pink, bright_pink, game_intro2 )
       
        #cursor related
        player_group.update()
        player_group.draw( wn )
       
        pygame.display.flip()
        clock.tick( fps )


############################## closing loops #################################

game_intro()
game_intro2()
quit_intrebare()
username_page()
levels_menu()
intro_helios()       
game_loop()
intro_venice()
game_loop2()
intro_dynasty()
game_loop3()
game_loop_final()
quit_game()


########################### closing the whole game ###########################

pygame.quit()
sys.exit()


################################# NOTES ######################################

# pygame.font.Font/SysFont().render() does not support multiple line text.
# func ponsitioning & closing loops ( order )
