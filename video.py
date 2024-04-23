from advertisement import Advertisement

class Video(Advertisement):
    # Constants for the video advertisement format and subtypes
    FORMAT = "Video"
    SUBTYPES = ("instream", "outstream")
    
    def __init__(self, width: int, height: int, file_url: str, click_url: str, sub_type: str, duration: int):
        # Initialize the Video advertisement with width, height, file URL, click URL, subtype, and duration
        super().__init__(width, height, file_url, click_url, sub_type)
        self.__duration = max(duration, 1)  # Video duration validation
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, new_width):
        pass
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        pass
    
    def compress_advertisement(self):
        # Method to compress video advertisement
        print("Video compression not yet implemented")

    def resize_advertisement(self):
        # Method to resize video advertisement
        print("Video resizing not yet implemented")
