"""Generate a save an image of a QR code, generated from text input"""

from __future__ import print_function

import fileinput
from os import unlink
from os.path import expanduser
import qrcode
import tempfile
from time import sleep

def generate_qr(text):
    img = qrcode.make(text)
    output = tempfile.NamedTemporaryFile(dir=expanduser("~"), delete=False)
    img.save(output.name)
    return output.name

def main():
    lines = fileinput.input()
    text = "".join(lines)
    rendered_image = generate_qr(text)
    print(rendered_image)

if __name__ == "__main__":
    main()
