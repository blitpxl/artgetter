from concurrent.futures import ThreadPoolExecutor
from coverpy import CoverPy, NoResultsException
from natsort import os_sorted
import requests
import os
import sys


class AlbumArtGetter:
    def __init__(self, path: str = None):
        """
        This class can either accept the image output path or leave it empty.

        :param path: image output path or none.
        """

        self.finder = CoverPy()
        self.track_list = None
        self.output_path = path
        self.path_to_arts = set()

    @staticmethod
    def _check_exist(path):
        return os.path.isfile(path)

    def _download(self, link, track_name):
        try:
            response = requests.get(link)
            with open(self.output_path + str(self.track_list.index(track_name)) + ".jpg", 'wb') as imageFile:
                imageFile.write(response.content)
                set.add(self.path_to_arts, self.output_path + str(self.track_list.index(track_name)) + ".jpg")
        except requests.exceptions:
            set.add(self.path_to_arts, self.output_path + str(self.track_list.index(track_name)) + " null")

    def _search(self, term, image_size, track_name):
        try:
            if not self._check_exist(self.output_path + str(self.track_list.index(track_name)) + ".jpg"):
                result = self.finder.get_cover(term)
                self._download(result.artwork(image_size), track_name)
                print(f"Found result for: {term}")
            else:
                print(f"image file of {term} already exist, skipped")
                set.add(self.path_to_arts, self.output_path + str(self.track_list.index(track_name)) + ".jpg")
        except NoResultsException:
            print(f"No result for: {term}")
            set.add(self.path_to_arts, self.output_path + str(self.track_list.index(track_name)) + " null")
        except requests.exceptions.ConnectionError:
            sys.stderr.write(f"Couldn't search for {term}: Connection Error\n")

    def set_output_path(self, output_path: str):
        """
        Set the images output path
        \n**Note:** always put slash at the end of the directory, example: (path/to/output/).

        :param output_path:
        :return: output_path
        """
        self.output_path = output_path

    def get_art(self, track_library, image_size: int, attempts: int = 5, worker_limit: int = 50, folder_mode=True):
        """
        Search and batch download all the Album arts

        :param track_library: path to music folder (if folder mode enabled), list of path to each of your track
         (if folder mode disabled).
        :param image_size: the size of the image that will be downloaded.
        :param attempts: number of attempts allowed, if failed to found image, the script will re-attempt to search it.
        :param worker_limit: set the limit of thread spawning.
        :param folder_mode: If enabled artgetter will scan a music folder that passed in from the
         parameter 'track_library'. otherwise you have to pass a list of the path of each of your track.

        :return: None
        """

        if folder_mode:
            folder = os.listdir(track_library)
            track_library = os_sorted(folder)

        else:
            track_library = os_sorted(track_library)

        self.track_list = track_library
        for attempt in range(attempts):
            with ThreadPoolExecutor(max_workers=worker_limit) as executor:
                for track in track_library:
                    executor.submit(self._search, os.path.splitext(os.path.basename(track))[0], image_size, track)

    def get_arts_path(self, return_sorted: bool = True):
        """
        Get the path of each image

        :param return_sorted: return sorted list of image paths (Enabled by default)
        :return: list of image paths
        """

        if return_sorted:
            return os_sorted(list(self.path_to_arts))
        else:
            list(self.path_to_arts)
