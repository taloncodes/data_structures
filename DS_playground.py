# =======================
# Arrays Section
# =======================

array = [1, 2, 3, 4, 5]  # create an array of ints

first = array[0]  # access index 0 (first element)

array[4] = 10  # edit index 4 (fifth element)

array_length = len(array)  # len() func returns number of elements

for element in array:
    print(element)

array.append(20)  # append an element to the end of the array
print(array)

del array[5]  # delete element at index 6
print(array)

sub_array = array[1:4]  # Extract elements from index 1 to 3
print(sub_array)


# =======================
# Linked Lists Section
# =======================

class Song:  # Song node class
    def __init__(self, title=None, artist=None):
        self.title = title
        self.artist = artist
        self.next = None


class Playlist:  # Head of list
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):  # Add song to end of playlist
        new_song = Song(title, artist)
        if self.head is None: # If first song, add to head of list
            self.head = new_song
        else:
            current_song = self.head    # append
            while current_song.next:
                current_song = current_song.next
            current_song.next = new_song

    def display_playlist(self):
        current_song = self.head
        while current_song:  # loops while current song is not None (end of list):
            print(f"{current_song.title} by {current_song.artist}")
            current_song = current_song.next
        print()


my_playlist = Playlist()

my_playlist.add_song("Dancing is healing", "Rudimental")
my_playlist.add_song("San_Francisco", "Dom Dolla")
my_playlist.add_song("Delilah", "Fred Again")

my_playlist.display_playlist()


