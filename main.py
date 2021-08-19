#1 import modules

import pygame,random,time,os,sys
pygame.init()
pygame.font.init() #9.2 initial the font

#6 set the screen
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) ## bisa dinamaiin juga SCREEN kaya di flappy bird :D
pygame.display.set_caption("Space Shooter!")

#2 load images. space ship
RED_SPACE_SHIP = pygame.image.load('assets/pixel_ship_red_small.png')
GREEN_SPACE_SHIP = pygame.image.load('assets/pixel_ship_green_small.png')
BLUE_SPACE_SHIP = pygame.image.load('assets/pixel_ship_blue_small.png')

#3 load images. Player player
YELLOW_SPACE_SHIP = pygame.image.load("assets/pixel_ship_yellow.png")

#4 load images. Laser
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#5 load images. background
BG = pygame.transform.scale(pygame.image.load("assets/background-black.png"),(WIDTH,HEIGHT))

#17.1 making the new laser class
class Laser:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img) #mask method -> untuk ambil objectnya ajaa tanpa backgroundnya
    
    def draw(self,window):
        window.blit(self.img, (self.x,self.y))

    def move(self,vel):
        self.y += vel # kalo benda turun ke bawah +, kalo naik - (inget sumbu x y)
    
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self,obj):
        return collide(self,obj)

#10.1 defining the ships (utk dipake berkali2) and draw it
class Ship:
    #17.4 set cooldown
    COOLDOWN = 30 #mau di set setengah fps, 1 detik = 60 fps. kalo mau 0.5 detik = 30 fps
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self,window):
        window.blit(self.ship_img, (self.x,self.y))
        #17. 7 draw the laser
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self,vel,obj): #obj disini digunaiin buat apakah laser kita kena ke musuh atau enggak
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj): #kalo udah kena object, lasernya ilang/di remove
                obj.health -= 10
                self.lasers.remove(laser)
            
    #17.5
    def cooldown(self): #bikin jeda 0.5 detik sebelum nembak lagi
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter >0:
            self.cool_down_counter += 1 

    #17.3 pesawat bisa nembak
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1  

    #13 buat pesawat ga ilang kalau di mainkan
    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

#12 Buat class untuk pesawatnya
class Player(Ship):
    def __init__(self,x,y, health=100):
        super().__init__(x,y,health) # super() -> mengkopas ship class ke player class
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img) #mask method -> untuk ambil objectnya ajaa tanpa backgroundnya
        self.max_health = health

    def move_lasers(self,vel,objs): #obj disini digunaiin buat apakah laser kita kena ke musuh atau enggak
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj): #kalo udah kena object, lasernya ilang/di remove
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    #19.2 draw the healthbar
    def draw(self,window):
        super().draw(window)
        self.healthbar(window)

    #19.1 buat healthbar
    def healthbar(self,window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10)) #(s.health/s.max_health) -> persentasi health kita berapa

#14.1 Buat class untuk pesawat musuuuh
class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP,GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP,BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    #buat bikin pesawatnya turun kebawah
    def move(self,vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1 

#17.2 buat function kalo nabrak
def collide(obj1,obj2):
    offset_x = obj2.x - obj1.x #kalo obj1 sm obj 2 nabrak
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None #-> kalo ga overlap/tabrakan berarti ga terjadi apa22 (None)


#7.1 defining main loop
def main():
    run = True
    FPS = 60
    
    #9.1 adding level, lifes, main_font
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans",50)

    #15.3 set the lost_font
    lost_font = pygame.font.SysFont("comicsans",60)

    #14.2 defining all we are need to do with enemy shippp
    enemies = []
    wave_length = 5 #total musuh
    enemy_vel = 1 #brp pixel pesawat bakal jatuh

    #11.2 
    player_vel = 5 #setiap pencet key_a maka akan bergerak 5pixel

    #17.8
    laser_vel = 5

    #10.2 calling the Player ship
    player = Player(300,630)

    #7.1 ... adding clock
    clock = pygame.time.Clock()

    #15.1 define lost variable with False
    lost = False

    #16.1 
    lost_count = 0

    #8.1 menampilkan code gambar dan update render
    def redraw_window():
        WIN.blit(BG,(0,0))

        #9.3 draw text
        level_label = main_font.render(f'Level: {level}',1,(255,255,255))
        lives_label = main_font.render(f'Lives: {lives}',1,(255,255,255))

        #9.4 blit the lives & level label
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label,(WIDTH-level_label.get_width()-10,10))

        #14.3 draw the enemy ship -- musti dimunculin duluan biar ga numpuk
        # karna di dalam function Ship yang di draw ship player bukan enemies
        for enemy in enemies:
            enemy.draw(WIN)

        #10.3 drawing the ship to the window
        player.draw(WIN)

        #15.4 munculin kata you lost di layar
        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label,(WIDTH/2 - lost_label.get_width()/2, 350))

        #8.2 update render
        pygame.display.update()

    #7.2 set the main loop
    while run:
        clock.tick(FPS)

        #8.2 caliing the redraw_window() function
        redraw_window()     

        #15.2 kalau livesnya / bar healthnya abis berarti kalah :(
        if lives <= 0 or player.health <=0:
            lost = True
            #16.2
            lost_count += 1

        #16.3
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        #7.3 set the main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        #14.4 kalau musuh sudah tida ada, maka..
        if len(enemies) == 0:
            level += 1 #level akan bertambah 1
            wave_length += 5 #musuh akan bertambah 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50,WIDTH-100), 
                        random.randrange(-1500,-100), 
                        random.choice(['red','green','blue'])) # set the enemy ship diatas layar buat turun ke bawah (enemy(x,y,sm choice (pilih salah satu warna pesawat)))
                enemies.append(enemy)

        #11.1 setiap keyboard yang dipencet maka...
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: #LEFT
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: #RIGHT
            player.x += player_vel 
        if keys[pygame.K_w] and player.y - player_vel > 0: #UP
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: #DOWN & '+ 15' untuk tambah healthbar
            player.y += player_vel

        #17.6 kalo pencet spasi, player nembak
        if keys[pygame.K_SPACE]:
            player.shoot()

        #14.5 buat enemy space ship turun ke bawah
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel,player) #cek apakah laser kena ke player

            if random.randrange(0, 2*FPS) == 1: #setiap 2 detik musuh bisa nembak
                enemy.shoot()

            #18.1 kalo misalnya enemy ship nabrak player ship, maka healthnya berkutang -10 dan enemy bakal berkurang dari list yang akan turun
            if collide(enemy,player):
                player.health -=10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies) #-> mau cek apakah laser player kena ke enemy space ship, "-vel" biar lasernya terbang keatas 

#20 BUAT MAIN SCREEN -> THEN, DONE!
def main_menu():
	title_font = pygame.font.SysFont('comicsans',70)
	run = True
	while run:
		WIN.blit(BG,(0,0))
		title_label = title_font.render('Press the mouse to begin...',1,(255,255,255))
		WIN.blit(title_label,(WIDTH/2 - title_label.get_width()/2,350))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				main()
	pygame.quit()

#7.4 calling the function
main_menu()
