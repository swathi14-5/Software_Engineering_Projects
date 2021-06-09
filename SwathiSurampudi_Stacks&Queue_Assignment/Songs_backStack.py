class Songs_BackStack:

    stack = None

    def __init__(self):
        self.stack = []

    # This method appends songs to the backstack
    def append(self, song):
        """Write your code here to append songs to backstack"""
        self.stack.append(song)

    # This method pops the song from backstack.
    def pop(self):
        """Write your code here to pop the song from the stack."""
        if len(self.stack) < 1:
            return None
        return self.stack.pop()




