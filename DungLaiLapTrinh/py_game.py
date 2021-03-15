import pygame 

pygame.init()

sceen = pygame.display.set_mode((500,600))

GREY = (150,150,150)
WHITE = (255,255,255)

running = True
while running:
	sceen.fill(GREY)

	pygame.draw.rect(sceen,WHITE,(100,50,50,50))
	pygame.draw.rect(sceen,WHITE,(100,50,50,50))
	pygame.draw.rect(sceen,WHITE,(100,50,50,50))
	pygame.draw.rect(sceen,WHITE,(100,50,50,50))
	pygame.draw.rect(sceen,WHITE,(100,50,50,50))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("XXX")

	pygame.display.flip()

pygame.quit()