from datetime import datetime
from advertisement import Video, Display, Social  # Import datetime to work with dates

class Campaign:
    def __init__(self, name: str, start_date: datetime, end_date: datetime, ads: list):
        # Constructor of the 'Campaign' class, initializes superclass attributes
        self.__name = name  # Assign the campaign name
        self.__start_date = start_date  # Assign the campaign start date
        self.__end_date = end_date  # Assign the campaign end date
        self.__ads = ads  # Assign the list of advertisements associated with the campaign

    @property
    def name(self):
        # Getter for the campaign name
        return self.__name

    @name.setter
    def name(self, new_name):
        # Setter for the campaign name
        if len(new_name) > 250:  # Check that the new name does not exceed 250 characters
            raise ValueError(f"The name cannot exceed 250 characters. You entered {len(new_name)} characters.")
        else:
            self.__name = new_name  # Update the campaign name if valid

    @property
    def start_date(self):
        # Getter for the campaign start date
        return self.__start_date

    @start_date.setter
    def start_date(self, new_start_date):
        # Setter for the campaign start date
        self.__start_date = new_start_date  # Update the campaign start date

    @property
    def end_date(self):
        # Getter for the campaign end date
        return self.__end_date

    @end_date.setter
    def end_date(self, new_end_date):
        # Setter for the campaign end date
        self.__end_date = new_end_date  # Update the campaign end date

    @property
    def ads(self):
        # Getter to obtain the list of advertisements associated with the campaign
        return self.__ads

    def __str__(self):
        # Initialize counters for each type of advertisement
        video_count = 0  # Counter for 'Video' type advertisements
        display_count = 0  # Counter for 'Display' type advertisements
        social_count = 0  # Counter for 'Social' type advertisements

        # Iterate over the list of advertisements
        for item in self.__ads:
            # Check the type of each item
            if isinstance(item, Video):  # If the item is of type 'Video'
                video_count += 1  # Increment the 'Video' counter
            elif isinstance(item, Display):  # If the item is of type 'Display'
                display_count += 1  # Increment the 'Display' counter
            elif isinstance(item, Social):  # If the item is of type 'Social'
                social_count += 1  # Increment the 'Social' counter
        
        # Create the output text string, with the counts of each type of advertisement
        return f"""
    Campaign Name: {self.__name}
    Advertisements: {video_count} Video, {display_count} Display, {social_count} Social
    """
