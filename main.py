import pygame
import time

def main():
	pygame.init()
	
	pygame.display.set_caption("Hello Pygame")
	
	man = pygame.image.load("man100x100.png")
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
				if event.key == pygame.K_LEFT:
					move_left = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					move_right = False
				if event.key == pygame.K_LEFT:
					move_left = False
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