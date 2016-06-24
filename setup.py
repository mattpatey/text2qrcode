from setuptools import (
    find_packages,
    setup,
    )

setup(
    name="text2qrcode",
    version="1.0-a1",
    description="Render a QR code image from input text",
    author="Matt Patey",
    packages=find_packages(),
    install_requires=["qrcode", "pillow"],
    entry_points={
        "console_scripts": [
            "t2qr=text2qrcode.main:main"
        ]
    }
)
