# About
artgetter is a python module for batch searching and downloading album arts for music file
that doesn't have id3 tag or tags in general, therefore it's searching using the file name.

# How to use it
### To search and download

There are two methods for searching album arts:
* Search from folder
    * This method will scan through your music library and automatically search for each
    track and download the art (if it found any).
      

* Search from list
    * This method requires a list of each path to your tracks, and then artgetter will
    scan that list and automatically search and download it.
      

### Examples

#### Folder Mode:

```python

from artgetter import AlbumArtGetter  # import the module

music_library_path = r'C:\Users\Kevin\Music\OneDirectory'
art_size = 128

getter = AlbumArtGetter()  # instantiate the class (you can optionally pass the image output path to this class)
getter.set_output_path("D:/img/")  # set the image output path
getter.get_art(music_library_path, art_size, folder_mode=True)  # initiate search

```

#### Non Folder Mode:

```python

from artgetter import AlbumArtGetter  # import the module

music_list = [r'C:\Users\Kevin\Music\OneDirectory\Didrick - Ready To Fly (feat. Adam Young).mp3',
              r'C:\Users\Kevin\Music\OneDirectory\TheFatRat - MAYDAY feat. Laura Brehm.mp3',
              r'C:\Users\Kevin\Music\OneDirectory\AURORA - Runaway.mp3']
art_size = 128

getter = AlbumArtGetter()  # instantiate the class (you can optionally pass the image output path to this class)
getter.set_output_path("D:/img/")  # set the image output path
getter.get_art(music_list, art_size, folder_mode=False)  # initiate search

```

### To get the image path
To get the path of each downloaded image, see the code below:

```python

from artgetter import AlbumArtGetter  # import the module

music_list = [r'C:\Users\Kevin\Music\OneDirectory\Didrick - Ready To Fly (feat. Adam Young).mp3',
              r'C:\Users\Kevin\Music\OneDirectory\TheFatRat - MAYDAY feat. Laura Brehm.mp3',
              r'C:\Users\Kevin\Music\OneDirectory\AURORA - Runaway.mp3']
art_size = 128

getter = AlbumArtGetter()  # instantiate the class (you can optionally pass the image output path to this class)
getter.set_output_path("D:/img/")  # set the image output path
getter.get_art(music_list, art_size, folder_mode=False)  # initiate search

paths = getter.get_arts_path()  # get the path of each image
print(paths)

```

The function `get_arts_path()` will return a list.

```python

['D:/img/0.jpg', 'D:/img/1.jpg', 'D:/img/2.jpg']

```

if the image is not found or failed to download, the path will look like this inside the list:

```python

['D:/img/0 null', 'D:/img/1 null', 'D:/img/2 null']

```
