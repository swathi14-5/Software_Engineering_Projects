from Playlist import PlaylistQueue
from Songs_backStack import Songs_BackStack

# This method add songs to playlist which is implemented as a queue.
def add_to_playlist(song):
    playlist_queue.append(song)
    print(str(song) + " added to queue!")


# This method pops a song from the queue and starts playing it.
def play_song():
    song = playlist_queue.pop()
    back_stack.append(song)
    print("Playing " + song)

# This method pops next song from the queue and plays it.
def next_song():
    song = playlist_queue.pop()
    back_stack.append(song)
    print("Playing " + song)

# This method pops a song from the back stack and plays it.
def go_back():
    current = back_stack.pop()
    previous_song = back_stack.pop()
    print("Playing " + str(previous_song))


if __name__ == '__main__':
    # Instantiating the playlist and Backstack objects.
    playlist_queue = PlaylistQueue()
    back_stack = Songs_BackStack()

    # Building a playlist
    add_to_playlist("Stairway to Heaven - Led Zepplin")
    add_to_playlist("Bohemian Rhapsody - Queen")
    add_to_playlist("We will rock you - Queen")
    add_to_playlist("Back in Black - AC/DC")
    add_to_playlist("Chop Suey - System of a down")

    # Start playing
    play_song()

    # Play next and previous songs
    next_song()
    next_song()
    next_song()
    go_back()
    go_back()

