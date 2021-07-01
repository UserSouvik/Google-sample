"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.isPaused = False
        self.isPlaying = False
        self._current_video = None
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()  # Fetch all the videos, based off above function
        all_videos.sort(key=lambda x: x.title)  # Use key with lambda to dictate sort to only go through video title
        print("Here's a list of all available videos:")

        for video in all_videos:  # Loop through txt file, reading each video line by line
            tagString = str(video.tags)  # Convert to string to allow stripping of brackets
            # tagStrip.strip("()") # Old code - this didn't make a difference with this line placement
            print(f'{video.title} ({video.video_id}) [{tagString}]')
            #print(video.title, "(", video.video_id, ")", "[", tagString.strip("()"), "]") #alternative

    def play_video(self, video_id):
        # self._current_video = None
        vidPlay = self._video_library.get_video(video_id)  # Start playing the chosen video

        try:  # Check if the video exists
            vidPlay.video_id
        except AttributeError:  # If video doesn't exist, don't bother with the rest of the code
            print("Cannot play video: Video does not exist")
        else:  # Continue as normal if the video exists
            # print("Current ID:", vidPlay.video_id) # Debug
            # currentVideo = vidPlay  # Old code with local currentVideo variable. Caused too much headaches to work
            if self.isPlaying:  # Don't this message on first run of function
                print("Stopping video:", self.currentVideo.title)  # Stop the previous video if any
                self.isPaused = False
            print("Playing video:", vidPlay.title)
            self.isPlaying = True
            self.currentVideo = vidPlay  # Store the video currently playing in a variable

    '''
    def play_video(self, video_id):
        if video_id =="amazing_cats_video_id":
            print("Playing video: Amazing Cats")
        elif video_id =="funny_dogs_video_id":
            print("Playing video: Funny Dogs")
        elif video_id =="another_cat_video_id":
            print("Playing video: Another Cat Video")
        elif video_id =="life_at_google_video":
            print("Playing video: Life at Google")
        elif video_id =="nothing_video_id":
            print("Playing video: video about nothing")
        else:
            print("Cannot play video: video does not exist")
    '''
    def stop_video(self):
        """Stops the current video."""
        if self.isPlaying is True:
            print("Stopping video:", self.currentVideo.title)
            self.isPlaying = False
            self.isPaused = False
        else:
            print("Cannot stop video: No video is currently playing")

    def pause_video(self):
        """Pauses the current video."""
        if not self.isPaused:
            print(f"Pausing video : {self._current_video.title}")
            self.isPaused = True
        else:
            print(f"Video already paused: {self._current_video.title}")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.isPaused == True:
            print(f'Continuing video : {self.currentVideo.title}')
        if self._current_video == None
            print("Cannot continue video: no video is playing")
        if self.isPaused == False and self.currentVideo != None:
            print("Cannot continue video: video is not paused")
        self.isPaused = False


    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() != self.playlist:
            print(f" Successfully created new playlist: {playlist_name}")
        else:
            print('Cannot create playlist: playlist with the same name already exist')

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        video_term = self._video_library.get_video(search_term)
        if video_term:
            print(f"Here are the results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        video_tag_search = self._video_library.get_video(video_tag)
        if video_tag_search:
            print(f"Here are the results for {video_tag}")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
