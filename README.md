# BoxBlurAlgorithm

[![Python](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)

## Overview

**BoxBlurAlgorithm** is a Python implementation of the box blur algorithm, a simple and efficient technique used for 
image blurring. This repository provides an easy-to-use interface for applying the box blur effect to images, making it 
suitable for beginners and those interested in basic image processing. This implementation also includes several useful 
features, such as reporting how long the algorithm takes to blur an image and customizable blur intensity.

## Features

- Easily customizable blur intensity
Time measurement: while the algorithm is running, information about the duration of each step is provided. At the end 
- of the program, .json, .xml, or both files (depending on the value set in the .env file) containing more detailed information are created.
- Customisation via `.env` file


## What is Box Blur?

Box blur is a type of image-blurring filter that uses a square box-shaped kernel. Each pixel in the output image is 
set to the average of its neighboring pixels in the input image. It's one of the simplest forms of blurring and is
often used as a building block for more complex filters.

## Example Images

| Original                         | Blurred (intensity = 10)       |
|----------------------------------|--------------------------------|
| ![Original](example/input.jpg)   | ![Blurred](example/output.jpg) |

## Usage
1. Paste all images you want to blur into `input/` directory. There is no need for special filenames or any other preparation.
2. In the `.env` file set the intensity value (recommended are values under 40, above this value there are many distortions).
3. Choose which output format you want to use for blur statistics
4. Run the main.py script and wait for it to process the images.
5. When the code is done, under the output/ directory, there will be a folder for each input file. Inside each of them, 
there will be at least three files:
   1. The input image, named input with the input file extension
   2. The result, named output with the input file extension
   3. All the blurring statistics, saved as data.json and/or data.xml

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## Acknowledgments

- [Pillow](https://python-pillow.org/)

---

*Implementation of the blurring algorithm in Python.*