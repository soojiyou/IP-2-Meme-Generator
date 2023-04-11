
from PIL import Image, ImageDraw
import random
import os


class MemeEngine():
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):  # Check if the output directory exists
            # Create the output directory if it doesn't exist
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500):
        out_file = f"{self.output_dir}/{str(random.randint(0, 10000))}.jpg"
        try:
            with Image.open(img_path) as img:
                ratio = img.height / img.width
                height = int(width * ratio)
                img = img.resize((width, height), Image.NEAREST)

                text = text.replace("\u2019", "")
                author = author.replace("\u2019", "")

                rand_x = random.randint(0, int(width))
                rand_y = random.randint(0, int(height))

                draw = ImageDraw.Draw(img)
                draw.text((rand_x, rand_y), text, fill='white')
                draw.text(((rand_x), (rand_y+25)),
                          ('  - '+author), fill='white')

                img.save(out_file, "JPEG")
        except Exception as e:
            print(f"Error saving image: {e}")
            raise Exception("Invalid image path")
        return out_file
