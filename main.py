import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

pygame.init()
clock = pygame.time.Clock()
dt = 0

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while 1 == 1:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")

		player.draw(screen)

		# be sure to run this last - exception for dt
		pygame.display.flip()

		dt = clock.tick(60) / 1000
		


if __name__ == "__main__":
    main()

