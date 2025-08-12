import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    out_ext = sys.argv[2].split(".")
    in_ext = sys.argv[1].split(".")
    if len(out_ext) != 2 or out_ext[1] not in ("jpg", "jpeg", "png"):
        sys.exit("Invalid output")
    elif out_ext[1] != in_ext[1]:
        sys.exit("Input and output have different extensions")
    else:
        size = (600, 600)
        try:
            # Open and resize the input image (person)
            with Image.open(sys.argv[1]) as file:
                person_image = ImageOps.fit(file, size)

            # Open the shirt image
            with Image.open('shirt.png') as shirt_file:
                shirt_image = shirt_file.copy()

            # Resize shirt to match person image size
            shirt_image = shirt_image.resize(size, Image.Resampling.LANCZOS)

            # Convert person image to RGBA if it isn't already
            if person_image.mode != 'RGBA':
                person_image = person_image.convert('RGBA')

            # Convert shirt to RGBA if it isn't already
            if shirt_image.mode != 'RGBA':
                shirt_image = shirt_image.convert('RGBA')

            # Create the final result by compositing
            # This will put the shirt over the person, respecting transparency
            result = Image.alpha_composite(person_image, shirt_image)

            # Convert back to RGB if saving as JPEG
            if out_ext[1].lower() in ('jpg', 'jpeg'):
                # Create white background for JPEG
                white_bg = Image.new('RGB', size, (255, 255, 255))
                white_bg.paste(result, mask=result.split()[-1])  # Use alpha as mask
                result = white_bg

            # Save the result
            result.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Input does not exist")
