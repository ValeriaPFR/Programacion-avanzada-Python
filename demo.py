from advertisement import Advertisement, Video, Display, Social
from campaign import Campaign
from datetime import datetime, timedelta
from error import InvalidSubtypeError


def request_type_and_subtype(advertisement_class):
    """
    Prompts the user for the type and subtype of advertisement and validates the input.

    Args:
        advertisement_class (type): The class of the advertisement (Video, Display, or Social).

    Returns:
        tuple: A tuple containing the type and subtype of the advertisement entered.
    """
    valid_types = {
        "video": Video,
        "display": Display,
        "social": Social,
    }

    while True:
        entered_type = (
            input(f"Enter the type of advertisement ({', '.join(valid_types.keys())}): ")
            .lower()
            .strip()
        )
        if entered_type in valid_types:
            advertisement_class = valid_types[entered_type]
            entered_subtype = request_advertisement_subtype(advertisement_class)
            return entered_type, entered_subtype
        else:
            print(
                f"Error: The advertisement type '{entered_type}' is not valid. Valid types are: {', '.join(valid_types.keys())}"
            )


def request_advertisement_subtype(advertisement_class):
    """
    Prompts the user for a valid subtype for the advertisement of the specified class.

    Args:
        advertisement_class (type): The class of the advertisement (Video, Display, or Social).

    Returns:
        str: The advertisement subtype entered by the user.
    """
    valid_subtypes = (
        advertisement_class.SUBTYPES
    )  # Get valid subtypes from the class
    while True:
        entered_subtype = (
            input(f"Enter a valid subtype for {advertisement_class.FORMAT.lower()}: ")
            .lower()
            .strip()
        )  # Normalize input
        if entered_subtype in valid_subtypes:
            return entered_subtype
        else:
            print(
                f"Error: The subtype '{entered_subtype}' is not valid. Valid subtypes are: {valid_subtypes}"
            )


def request_campaign_name():
    """
    Prompts the user for a new name for the campaign and performs validation.

    Returns:
        str: The new campaign name entered by the user.
    """
    while True:
        new_name = input("Enter a new name for the campaign: ")
        if len(new_name) <= 250:
            return new_name
        else:
            print("Error: The campaign name cannot exceed 250 characters.")


def create_advertisement(type, subtype):
    """
    Creates an advertisement based on the selected type and subtype.

    Args:
        type (str): The type of advertisement (video, display, social).
        subtype (str): The advertisement subtype.

    Returns:
        Advertisement: Created Advertisement object.
    """
    try:
        if type == "video":
            width = int(input("Enter the width of the video: "))
            height = int(input("Enter the height of the video: "))
            #file_url = input("Enter the video file URL: ")
            #click_url = input("Enter the video click URL: ")
            duration = int(input("Enter the duration of the video (in seconds): "))
            advertisement = Video(width, height, file_url, click_url, subtype, duration)
        elif type == "display":
            width = int(input("Enter the width of the display advertisement: "))
            height = int(input("Enter the height of the display advertisement: "))
            #file_url = input("Enter the image file URL: ")
            #click_url = input("Enter the display advertisement click URL: ")
            advertisement = Display(width, height, file_url, click_url, subtype)
        elif type == "social":
            width = int(input("Enter the width of the social advertisement: "))
            height = int(input("Enter the height of the social advertisement: "))
            #file_url = input("Enter the social advertisement URL: ")
        else:
            raise ValueError(f"Invalid advertisement type: '{type}'")
    except ValueError as e:
        print(f"Error: {e}")
        return None


def handle_error(e):
    """
    Handles exceptions and writes the error message to the "error.log" file.

    Args:
        e (Exception): The exception that occurred.
    """
    with open("error.log", "a+") as log:
        log.write(f"{e}\n")
    print("An error occurred. Check the 'error.log' file for more details.")


def main():
    new_video = [
        Video(640, 480, "video.mp4", "http://example.com", "Video_campaign", 60)
    ]
    start_date = datetime.now()
    end_date = start_date + timedelta(days=2)
    new_campaign = Campaign("Campaign1", start_date, end_date, new_video)

    try:
        new_name = request_campaign_name()
        new_campaign.name = new_name

        type_advertisement, subtype_advertisement = request_type_and_subtype(Video)
        new_advertisement = create_advertisement(type_advertisement, subtype_advertisement)
        if new_advertisement:
            new_campaign.add_advertisement(new_advertisement)

    except Exception as e:
        handle_error(e)


if __name__ == "__main__":
    main()
