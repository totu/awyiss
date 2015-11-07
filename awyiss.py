# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from sys import argv

class Awyiss(object):
    """This class is used to create awesome Aw Yiss duck images"""
    def __init__(self, font="Tahoma", font_type="ttf", font_path="/Library/Fonts/"):
        """Initialization method.

        Args:
            font (string):         Indicates which font you want to use. Default "Tahoma".
            font_type (string):    File type of the font. Default "tff".
            font_path (string):    Path where your fonts live. Default "/Library/Fonts" (OS X).
        """
        self.font_face = (font, font_type)
        self.font = ImageFont.truetype(font_path + "%s.%s" % self.font_face, 50)
        self.template = Image.open("temp.png")

    def _set_custom_template(self, path):
        """This method can be used to setup custom template,
        which is fine, but it might not work as well

        Args:
            path (string):    Path to the template image
        """
        self.template = Image.open(path)

    def draw(self, string, output="output.png"):
        """This method is the main usage for the class. It is used to draw
        the actual image. Descriptive names are funny, aren't they?

        Args:
            string (string):    The string you want the funny duck to say.
                                String should preferably be shorter than 15
                                characters, because the speech bubble is finite.
            output (string):    Name of the output file. Default "output.png".
        """
        draw = ImageDraw.Draw(self.template)
        draw.text((1190, 328), string, (0, 0, 0), font=self.font)
        draw = ImageDraw.Draw(self.template)
        self.template.save(output)


"""This is the dumb part which allows CLI execution non-sense"""
def main(string):
    awyiss = Awyiss()
    awyiss.draw(string)

if __name__ == "__main__":
    string = argv[1]
    main(string)
