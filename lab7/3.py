import pygame
import os

pygame.init()

playlist = []
music_folder = "/Users/dautkhan/Documents/new_folder_3/lab7/musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Musics")
clock = pygame.time.Clock()

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 20)

# Путь к кнопкам
playb = pygame.image.load("/Users/dautkhan/Documents/new_folder_3/lab7/music-elements/play.png")
pausb = pygame.image.load("/Users/dautkhan/Documents/new_folder_3/lab7/music-elements/pause.png")
nextb = pygame.image.load("/Users/dautkhan/Documents/new_folder_3/lab7/music-elements/next.png")
prevb = pygame.image.load("/Users/dautkhan/Documents/new_folder_3/lab7/music-elements/back.png")

index = 0
aplay = False

try:
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play(1)
    aplay = True
except pygame.error as e:
    print(f"Error loading {playlist[index]}: {e}")
    index += 1  # Пропускаем проблемный трек

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                try:
                    pygame.mixer.music.load(playlist[index])
                    pygame.mixer.music.play()
                except pygame.error as e:
                    print(f"Error loading {playlist[index]}: {e}")
                    index = (index + 1) % len(playlist)

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                try:
                    pygame.mixer.music.load(playlist[index])
                    pygame.mixer.music.play()
                except pygame.error as e:
                    print(f"Error loading {playlist[index]}: {e}")
                    index = (index - 1) % len(playlist)

    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))

    screen.fill((0, 0, 0))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (365, 520))
    playb = pygame.transform.scale(playb, (70, 70))
    pausb = pygame.transform.scale(pausb, (70, 70))
    if aplay:
        screen.blit(pausb, (370, 590))
    else:
        screen.blit(playb, (370, 590))
    nextb = pygame.transform.scale(nextb, (70, 70))
    screen.blit(nextb, (460, 587))
    prevb = pygame.transform.scale(prevb, (75, 75))
    screen.blit(prevb, (273, 585))

    clock.tick(24)
    pygame.display.update()
