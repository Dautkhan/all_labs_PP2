import pygame
import os

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

MUSIC_DIR = "music/"
songs = [f for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
current_song_index = 0
pygame.mixer.music.load(os.path.join(MUSIC_DIR, songs[current_song_index]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_n:
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(os.path.join(MUSIC_DIR, songs[current_song_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                current_song_index = (current_song_index - 1) % len(songs)
                pygame.mixer.music.load(os.path.join(MUSIC_DIR, songs[current_song_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
pygame.quit()
