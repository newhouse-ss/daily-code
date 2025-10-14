#Following the requirement: play the songs in order, use List is better.
import random
song_list = ["ruchang", "taotao", "lige", "kong"]
random.shuffle(song_list)
for song in song_list:
    print(song)

song_list.append("dan")
song_list.remove("lige")
print(song_list)