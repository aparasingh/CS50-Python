import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Use regex to extract the src attribute value from iframe tags
    # This pattern looks for iframe tags and captures the src attribute value
    pattern = r'<iframe[^>]*\ssrc="([^"]*)"[^>]*>'
    match = re.search(pattern, s, re.IGNORECASE)

    if match:
        url = match.group(1)
        # Check if it's a YouTube embed URL
        youtube_pattern = r"^https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"
        youtube_match = re.search(youtube_pattern, url)

        if youtube_match:
            video_id = youtube_match.group(1)
            return f"https://youtu.be/{video_id}"

    return None


if __name__ == "__main__":
    main()
