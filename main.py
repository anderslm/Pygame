import pygame
import time

def main():
	pygame.init()
	
	pygame.display.set_caption("Hello Pygame")
	
	man = pygame.image.load("face-open.png")
	position = 50
	move_speed = 0.001
	screen = pygame.display.set_mode((600, 400))
	
	screen.blit(man, (position, 50))
	pygame.display.flip()
	
	move_right = False
	move_left = False
	
	running = True
	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					move_right = True
					move_left = False
				if event.key == pygame.K_LEFT:
					move_left = True
					move_right = False
			if event.type == pygame.KEYUP:
				move_left = False
				move_right = False
		if move_right:
			position += 1
			time.sleep(move_speed)
		if move_left:
			position -= 1
			time.sleep(move_speed)
			
		screen.blit(man, (position, 50))
		pygame.display.flip()
				
if __name__=="__main__":
	main()