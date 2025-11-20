import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
clock = pygame.time.Clock()

def main():
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)

	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	AsteroidField()

	while 1 == 1:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")

		for object in updatable:
			object.update(dt)
			if object == player:
				object.shot_cooldown_timer -= dt
		for object in asteroids:
			if object.collides_with(player) == True:
				log_event("player_hit")
				print("Game over!")
				sys.exit()
			for shot in shots:
				if object.collides_with(shot) == True:
					log_event("asteroid_shot")
					object.split()
					shot.kill()
		for object in drawable:
			object.draw(screen)

		# be sure to run this last - exception for dt
		pygame.display.flip()

		dt = clock.tick(60) / 1000
		


if __name__ == "__main__":
    main()

