import pygame

pygame.init()
print('Setup Started')
screen = pygame.display.set_mode((800, 600))
window = pygame.display.set_mode(size=(600, 480))

print('Loop Started')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            quit() # end paygame