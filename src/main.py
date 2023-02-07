# Complete your game here
import random
import pygame

class RainOfCoins:
    def __init__(self):
        pygame.init()

        self.load_img()
        self.game_font = pygame.font.SysFont("Arial", 24)


        self.window = pygame.display.set_mode((800,600))
        pygame.display.set_caption("A rain of coins!!")

        
        self.points = 0
        self.highscore = 1
        self.clock = pygame.time.Clock()
        self.started = False
        self.player_x = 0
        self.to_left = False
        self.to_right = False
        self.game_over = False
        self.load_text()
        self.new_game()

    
    def load_img(self):
        self.img = []
        for name in ["coin", "monster", "robot"]:
            self.img.append(pygame.image.load(name+".png"))

    def load_text(self):
        self.line1 = self.game_font.render("Welcome to Rain Of Coins!", True, (255, 255, 255))
        self.line2 = self.game_font.render("Use arrows to control your robot", True, (255, 255, 255))
        self.line3 = self.game_font.render("Collect coins falling from the sky", True, (255, 255, 255))
        self.line4 = self.game_font.render("Avoid monsters - 'The Groke' like creatures", True, (255, 255, 255))
        self.line5 = self.game_font.render("Press ENTER to start, Have fun!", True, (255, 255, 255))
        self.current_hs = self.game_font.render(f"Highscore: {self.highscore}", True, (208, 255, 0))
        self.current_points = self.game_font.render(f"Points: {self.points}", True, (208, 255, 0))
        self.texts = [self.current_points, self.line1, self.line2, self.line3, self.line4, self.line5, self.current_hs]
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_RETURN and self.started == False:
                    self.started = True
                if event.key == pygame.K_RETURN and self.game_over == True:
                    
                    self.game_over = False
                    self.new_game()
                    
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_ESCAPE:
                    exit()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False  
            if event.type ==  pygame.QUIT:
                exit()    

    def new_game(self):
        self.window.fill((65,65,65))
        from_top = 50
        num_mon = 3
        

        mon_x = random.sample(range(0,750),50)
        mon_y = random.sample(range(-800,-100),50)
        points_counter = self.game_font.render(f"Points: {self.points}", True, (208, 255, 0))
        

        num_coin = 5
        coin_x = random.sample(range(0,750),50)
        coin_y = random.sample(range(-800,-100),50)
        for el in range (1,7):
            self.window.blit(self.texts[el], (400 - self.texts[el].get_width()/2, from_top))
            from_top += 70
            if el == 5:
                from_top += 70
        
        self.player_x = 400 - self.img[2].get_width()
        player_y = 600 - self.img[2].get_height()
        self.points = 0
        
        while True:
            if self.started:
                if self.points > 10:
                    num_mon = 5
                    num_coin = 6
                if self.points > 30:
                    num_mon = 7
                    num_coin = 8
                if self.points > 75:
                    num_coin = 10
                    num_mon = 35
                self.window.fill((65,65,65))
                self.window.blit(self.img[2],(self.player_x, player_y))
                self.window.blit(points_counter, (650,50))

                #ADDING COINS
                for coin in range(num_coin):
                    self.window.blit(self.img[0],(coin_x[coin], coin_y[coin]))
                    coin_y[coin] += 2

                    if coin_y[coin] >= 600:
                        coin_x[coin] = random.randint(0,750)
                        coin_y[coin] = random.randint(-800,-100)

                    if coin_x[coin] <= self.player_x + self.img[2].get_width()/2 and coin_x[coin] >= self.player_x - self.img[2].get_width()/ 2:
                        if coin_y[coin] <= player_y + self.img[2].get_height()/2 and coin_y[coin] >= player_y - self.img[2].get_height()/ 2:
                            self.points += 1
                            points_counter = self.game_font.render(f"Points: {self.points}", True, (208, 255, 0))
                            coin_x[coin] = random.randint(0,750)
                            coin_y[coin] = random.randint(-800,-100)

                #ADDING MONSTERS:
                for mon in range(num_mon):
                    self.window.blit(self.img[1],(mon_x[mon], mon_y[mon]))
                    mon_y[mon] += 2
                    if self.points > 10:
                        mon_y[mon] += 1
                    if self.points > 25:
                        mon_y[mon] += 1

                    if mon_y[mon] >= 600:
                        mon_x[mon] = random.randint(0,750)
                        mon_y[mon] = random.randint(-800,-100)

                    if mon_x[mon] <= self.player_x + self.img[2].get_width()/2 and mon_x[mon] >= self.player_x - self.img[2].get_width()/ 2:
                        if mon_y[mon] <= player_y + self.img[2].get_height()/2 and mon_y[mon] >= player_y - self.img[2].get_height()/ 2:
                            
                            current = self.points
                            if self.points > self.highscore:
                                self.highscore = self.points
                            self.started = False
                            self.game_over = True

                if self.to_left:
                    self.player_x -= 3
                if self.to_right:
                    self.player_x +=3
                if self.player_x <= 0:
                    self.to_left = False
                if self.player_x >= 800 - self.img[2].get_width():
                    self.to_right = False

            if self.game_over:
                self.window.fill((65,65,65))
                text = self.game_font.render(f"Game Over!", True, (255, 255, 255))
                self.window.blit(text,(400 - text.get_width()/2, 50))
                text = self.game_font.render(f"Your score is: {current}", True, (255, 255, 255))
                self.window.blit(text,(400 - text.get_width()/2, 120))
                if current == self.highscore:
                    text = self.game_font.render(f"High Score! Congrats!", True, (208, 255, 0))
                    self.window.blit(text,(400 - text.get_width()/2, 200))
                    self.points = 0
                else:
                    text = self.game_font.render(f"Current High Score: {self.highscore}", True, (208, 255, 0))
                    self.window.blit(text,(400 - text.get_width()/2, 200))
                    self.points = 0
                text = self.game_font.render(f"Press ENTER to play agian!", True, (255, 255, 255))
                self.window.blit(text,(400 - text.get_width()/2, 300))
                text = self.game_font.render(f"Press ESC to quit", True, (255, 255, 255))
                self.window.blit(text,(400 - text.get_width()/2, 400))
                

            
            
            self.check_events()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    RainOfCoins()