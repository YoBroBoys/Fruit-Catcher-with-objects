import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fruit Catcher")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255,255,0)
blue = (0,0,255)
# Basket dimensions and initial position
basket_width, basket_height = 100, 50
basket_x = (width - basket_width) // 2
basket_y = height - basket_height -20
basket_speed = 10

# Fruit dimensions and initial position
fruit_width, fruit_height = 30, 30
fruit_speed = 5
fruits=[]
# fruit_image = pygame.image.load("apple.jpg")
# fruit_image = pygame.transform.scale(fruit_image, [fruit_width,fruit_height])

# Clock to control frame rate
clock = pygame.time.Clock()
def fruite():
    type = random.choice(['apple','pineapple','pinecone'])
    fruit_x = random.randint(0, width - fruit_width)
    fruit_y = 0
    return {'t':type,'x': fruit_x,'y':fruit_y}

def display_score(score):
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

# Main game loop
score = 0

# Initial position for the fruit

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # move the basket
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and basket_x > 0:
                basket_x -= basket_speed
            if event.key == pygame.K_RIGHT  and basket_x < width - basket_width:
                basket_x += basket_speed
    if random.random() < 0.02:
        fruits.append(fruite())
    screen.fill(black)
    for fruit in fruits:
        fruit['y'] += fruit_speed

        if (basket_x < fruit['x'] < basket_x + basket_width and basket_y < fruit['y'] < basket_y + basket_width):
            fruit['x'] = random.randint(0,width - fruit_width)
            fruit['y'] = 0
            score += 1

        elif fruit['y'] > height:
            fruit['x'] = random.randint(0, width - fruit_width)
            fruit['y'] = 0
            score -= 1

        if fruit['t'] == 'apple':
            pygame.draw.circle(screen,red,(fruit['x'],fruit['y']),fruit_width//2)
        elif fruit['t'] == 'pineapple':
            pygame.draw.rect(screen,yellow,(fruit['x'],fruit['y'],20,40))
        elif fruit['t'] == 'pinecone':
            pygame.draw.ellipse(screen,blue,(fruit['x'],fruit['y'],20,40))





    pygame.draw.rect(screen,white,(basket_x,basket_y,basket_width,basket_height,))
    display_score(score)
    pygame.display.flip()
    clock.tick(30)