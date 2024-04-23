from advertisement import Advertisement

class Display(Advertisement):
    # Class attributes defining the format and subtypes of the Display advertisement
    FORMAT = "Display"
    SUBTYPES = ("traditional", "native")
    
    def __init__(self, width: int, height: int, file_url: str, click_url: str, sub_type: str):
        # Initialize the Display advertisement with provided attributes
        super().__init__(width, height, file_url, click_url, sub_type)

    def compress_ads(self):
        # Method to compress Display advertisements
        print("DISPLAY ADS COMPRESSION NOT YET IMPLEMENTED")

    def resize_advertisement(self):
        # Method to resize Display advertisements
        print("DISPLAY ADS RESIZING NOT YET IMPLEMENTED")
