# QR Code Generator
![Linkdin Hamza Rafique](./hamza-rafique-linkdin.png)

A simple Python project to generate QR codes using the `qrcode` library. This project allows you to create QR codes for any input text or URL and save them as image files.

## Features
- Generate QR codes for text, URLs, or any string.
- Save the QR code as an image in PNG format.
- Customize QR code size and error correction level.

## Prerequisites

Before running this project, ensure that you have Python installed on your system. You will also need the following Python libraries:

- `qrcode`: For generating the QR codes.
- `Pillow`: For working with image files (required by `qrcode`).

Install the required libraries using the following command:

```bash
pip install qrcode[pil]
```

## Installation
 - 1.Clone the repository:
 
 ```bash
  git clone https://github.com/Hamza-Rafique/QRCodeGeneratorInPython.git
  cd qr-code-generator
```
 - 2.Install the dependencies:

 ```bash
 pip install -r requirements.txt
 ```

 ## Usage

- Open the qr_code.py file and modify the input_data variable with the text or URL you want to encode into a QR code.

- Run the Python script to generate the QR code:

```bash
python qr_code.py
```
-The QR code image will be saved as hamza-rafique-linkdin.png in the current directory.

**Contributions**

Feel free to fork this repository and submit pull requests to add more features or improve the code.