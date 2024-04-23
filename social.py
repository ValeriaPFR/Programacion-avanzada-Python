from advertisement import Advertisement

class Social(Advertisement):
    # Constants for the social advertisement format and subtypes
    FORMAT = "Social"
    SUBTYPES = ("facebook", "linkedin")

    def __init__(self, width: int, height: int, file_url: str, click_url: str, sub_type: str):
        # Initialize the Social advertisement with width, height, file URL, click URL, and subtype
        super().__init__(width, height, file_url, click_url, sub_type)  
        
    def compress_ads(self):
        # Method to compress social ads
        print("Social ads compression not yet implemented")

    def resize_advertisement(self):
        # Method to resize social ads
        print("Social ads resizing not yet implemented")
