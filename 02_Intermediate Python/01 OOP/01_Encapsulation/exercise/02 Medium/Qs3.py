"""
Question 3:
Create a Playlist class with private attributes
 __songs (a list of song titles)
and
__current_song (index of the current song).
Implement methods to
add a song,
remove a song,
play the next song,
and play the previous song.
"""


class PlayList:
    def __init__(self, songs_list):
        self.__songs = songs_list
        self.__current_song_index = 0

    def add_song(self, new_song):
        self.__songs.append(new_song)
        print(f"New song '{new_song}' is added")
        print(self.__songs)

    def remove_song(self, remove_song_name):
        if remove_song_name in self.__songs:
            self.__songs.remove(remove_song_name)
            print(f"The song '{remove_song_name}' has been deleted.")
            print(self.__songs)
        else:
            print(f"There is no such a song named '{remove_song_name}'.")

    def play_next_song(self):
        if self.__current_song_index < len(self.__songs) - 1:
            self.__current_song_index += 1
            return self.__songs[self.__current_song_index]
        else:
            print("End of playlist reached.")
            return None

    def play_previous_song(self):
        if self.__current_song_index > 0:
            self.__current_song_index -= 1
            return self.__songs[self.__current_song_index]
        else:
            print("Beginning of playlist reached.")
            return None


# Test the Playlist class
song_list = ['song1', 'song2', 'song3', 'song4', 'song5']
playlist = PlayList(song_list)
playlist.add_song("song6")
playlist.remove_song("song4")
print("Playing next song:", playlist.play_next_song())
print("Playing next song:", playlist.play_next_song())
print("Playing next song:", playlist.play_next_song())
print("Playing previous song:", playlist.play_previous_song())
print("Playing previous song:", playlist.play_previous_song())
print("Playing previous song:", playlist.play_previous_song())
