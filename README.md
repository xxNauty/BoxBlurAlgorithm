# BoxBlurAlgorithm

[![Python](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/)

## Overview

**BoxBlurAlgorithm** is a Python implementation of the box blur algorithm, a simple and efficient technique used for 
image blurring. This repository provides an easy-to-use interface for applying the box blur effect to images, making it 
suitable for beginners and those interested in basic image processing. This implementation has also few quite useful 
features, like for example information about how long took the algorithm to blur image.

## Features

- Easily customizable blur intensity (most useful values are under 50, above is mostly useless and time-consuming)
- Time measurement (now only the whole run, but in future there will be more detailed information for every run)
- Customisation based on `.env` file


## What is Box Blur?

Box blur is a type of image-blurring filter that uses a square box-shaped kernel. Each pixel in the output image is 
set to the average of its neighboring pixels in the input image. It's one of the simplest forms of blurring and is
often used as a building block for more complex filters.

## Example Images

| Original                        | Blurred (intensity = 10)        |
|---------------------------------|---------------------------------|
| ![Original](examples/input.jpg) | ![Blurred](examples/output.jpg) |

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## Acknowledgments

- [Pillow](https://python-pillow.org/)

---

*Implementation of blurring algorithm in Python.*