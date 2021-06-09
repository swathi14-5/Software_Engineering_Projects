class PlaylistQueue:

    queue = None

    def __init__(self):
        self.queue = []

    # This method appends songs to the Playlist queue
    def append(self, url):
        """Write your code here to append the song to queue."""
        self.queue.append(url)

    # This method pops the song from Playlist queue
    def pop(self):
        """Write your code here to pop the song from queue."""
        if len(self.queue) < 1:
            return None
        return  self.queue.pop(0)


