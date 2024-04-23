from abc import ABC, abstractmethod

class Advertisement(ABC):
    # Constructor method for Advertisement class
    def __init__(self, width: int, height: int, file_url: str, click_url: str, sub_type: str):
        # Initialize attributes for width, height, file_url, click_url, and sub_type
        self.__width = width
        self.__height = height
        self.__file_url = file_url
        self.__click_url = click_url
        self.__sub_type = sub_type

    @property
    def width(self):
        # Getter method for width attribute
        return self.__width

    @width.setter
    def width(self, new_width):
        # Setter method for width attribute
        if new_width > 0:
            self.__width = new_width
        else:
            raise ValueError("Width must be a positive value.")

    @property
    def height(self):
        # Getter method for height attribute
        return self.__height

    @height.setter
    def height(self, new_height):
        # Setter method for height attribute
        if new_height > 0:
            self.__height = new_height
        else:
            raise ValueError("Height must be a positive value.")

    @property
    def file_url(self):
        # Getter method for file_url attribute
        return self.__file_url

    @file_url.setter
    def file_url(self, new_url):
        # Setter method for file_url attribute
        self.__file_url = new_url

    @property
    def click_url(self):
        # Getter method for click_url attribute
        return self.__click_url

    @click_url.setter
    def click_url(self, new_url):
        # Setter method for click_url attribute
        self.__click_url = new_url

    @abstractmethod
    def format(self):
        # Abstract method for determining format of advertisement
        pass

    @staticmethod
    def show_formats(format: str, sub_types: tuple):
        # Static method to display available formats
        print(f"""
FORMAT {format}
==========
- {sub_types[0]}
- {sub_types[1]}
==========
""")

class VideoAdvertisement(Advertisement):
    # Define format and subtypes for VideoAdvertisement
    FORMAT = "Video"
    SUBTYPES = ("instream", "outstream")

    def __init__(self, width: int, height: int, file_url: str, click_url: str, sub_type: str, duration: int):
        super().__init__(width, height, file_url, click_url, sub_type)
        # Initialize duration attribute and ensure it's at least 1
        self.duration = max(duration, 1)

    @property
    def format(self):
        # Getter method for advertisement format
        return self.FORMAT

    def compress_ads(self):
        # Method to compress video advertisements
        print("VIDEO COMPRESSION IMPLEMENTED")

    def resize_advertisement(self):
        # Method to resize video advertisements
        print("VIDEO RESIZING IMPLEMENTED")

class DisplayAdvertisement(Advertisement):
    # Define format and subtypes for DisplayAdvertisement
    FORMAT = "Display"
    SUBTYPES = ("traditional", "native")

    def compress_ads(self):
        # Method to compress display advertisements
        print("DISPLAY ADS COMPRESSION IMPLEMENTED")

    def resize_advertisement(self):
        # Method to resize display advertisements
        print("DISPLAY ADS RESIZING IMPLEMENTED")

class SocialAdvertisement(Advertisement):
    # Define format and subtypes for SocialAdvertisement
    FORMAT = "Social"
    SUBTYPES = ("facebook", "linkedin")

    def compress_ads(self):
        # Method to compress social advertisements
        print("SOCIAL ADS COMPRESSION IMPLEMENTED")

    def resize_advertisement(self):
        # Method to resize social advertisements
        print("SOCIAL ADS RESIZING IMPLEMENTED")
