import pygame  #importing from the pygame
import os #imporitng OS to help define path to the image 
pygame.font.init()#initilize pygame font library
pygame.mixer.init()#inititlize the pygame library as mixer for sound effect

def start_game():
   WIDTH, HEIGHT = 900, 500#variable for the measurement of window
   WIN = pygame.display.set_mode((WIDTH, HEIGHT))# setting display
   pygame.display.set_caption("Antarikshya")# captioning the game name in the left upper corner
   #colour
   WHITE = (255, 255, 255)
   BLACK = (0, 0, 0)
   RED = (255, 0, 0)
   YELLOW = (255, 255, 0)

   BORDER = pygame.Rect(WIDTH//2 - 5, 0,0.5 , HEIGHT)#rectangle at the middle as the boarder

   BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3') #loading the sound first
   BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

   HEALTH_FONT = pygame.font.SysFont('comicsans', 40)# font of health 
   WINNER_FONT = pygame.font.SysFont('comicsans', 100)# font for the win 

   FPS = 60#variable for the frames for seconds
   VEL = 5#velocity variable for movement of spaceship
   BULLET_VEL = 7#velocity for the bullets
   MAX_BULLETS = 5#number of bullets can be fired at a time
   SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 65, 50

   YELLOW_HIT = pygame.USEREVENT + 1
   RED_HIT = pygame.USEREVENT + 2#adding unique number for the making unique userevent

   YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))#calling and storing in variable of  the spaceship image with path to it
   YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
  YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)# resizing the image in (55,40) and rotating to 90 degree

   RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))#calling for the spaceship image with path to it
   RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)# resizing the image in (55,40) and rotating to 270 degree

   SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT)) #Setting the image in the background and transforming it to size 


   def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):# defining function and parameters
    WIN.blit(SPACE, (0, 0))#painting the image to background starting from the location 0,0
    pygame.draw.rect(WIN, BLACK, BORDER) # in window painting the border in middle
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)#customizing the for the health font for red in white colour with position and size also
                                                                                 #conveting the health number into string to show
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)# writing "health" in the font and colour white in given posiotin
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))# painting the text in window
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #draw the resized and rotated yellow spaceship in yellow rectangle x-axis and  y-axis position 
    WIN.blit(RED_SPACESHIP, (red.x, red.y))#draw the resized and rotated red spaceship in red rectangle x-axis and y-axis position.

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet) #drawing bullets as rectangle in red coloure

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)#drawing bullets as rectangle in yellow coloure

    pygame.display.update() # manually updating screen


   def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:# condition if key  a is pressed and the yellow.x is with the boarder area
        yellow.x -= VEL # move spaceship to left
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # condition if key  d is pressed and the yellow.x is with the boarder area
        yellow.x += VEL#Left
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:#condtion if key w is  spaceship within the boarder only
        yellow.y -= VEL#up
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  #condition if key s is pressed and shapeship is within the area
        yellow.y += VEL#down 


   def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:# condition if key  left arrow is pressed and the red.x is with the boarder area
        red.x -= VEL #Left
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:# condition if key  right arrow is pressed and the red.x is with the boarder area
        red.x += VEL#right
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:# condition if key  up arrow is pressed and the red spaceship is with the boarder area
        red.y -= VEL#up 
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:# condition if key  doen arrow is pressed and the red sapceship is with the boarder area
        red.y += VEL#down


   def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL#move the bullet to right with adding to velocity
        if red.colliderect(bullet):#if there is collision in rectangle only works for the rectangle
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)#ramoving the bullets if the event of collision take place
        elif bullet.x > WIDTH: #condtion if the bullets are out of width
            yellow_bullets.remove(bullet)#remove bullets if the above condition is fulfilled

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL#subtraction from the 
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


   def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


   def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #pygame rectangle around the spaceship
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10    #initilizing the total number of health for each
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:#condition that ensure bullets are only fired when the key is pressed and the bullets in screee is less then maximum bullets
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)#bullets as the rectangle in pygame in given position as we want them be coming from the spaceship in size 10 ,5
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()#sound play if the event takes place

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()#sound play if the vent takes place

            if event.type == RED_HIT:# if the red hit event takes place 
                red_health -= 1# the red health decrease by 1
                BULLET_HIT_SOUND.play()#plays sound

            if event.type == YELLOW_HIT:#if the yellow hit event takes place the 
                yellow_health -= 1#then yellow health decresae by one
                BULLET_HIT_SOUND.play()

        winner_text = "" #condition for the decision of
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)

    main()

   
   if __name__ == "__main__":
    main() # type: ignore
    
start_game()