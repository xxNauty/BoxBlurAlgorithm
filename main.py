from PIL import Image
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
from time import time

def format_step_number(number : str) -> str:
    if number[-1] == '1' and number != "11":
        return number + "st"
    elif number[-1] == '2' and number != "12":
        return number + "nd"
    elif number[-1] == '3' and number != "13":
        return number + "rd"
    else:
        return number + "th"

start_time = time()

load_dotenv()

input_image = Image.open(getenv("INPUT_PATH") + getenv("IMAGE_NAME"))
input_pixel_map = input_image.load()

width, height = input_image.size

output_image = Image.new('RGB', (width, height))
output_pixel_map = output_image.load()

intensity = getenv("INTENSITY")

for step in range(int(intensity)):
    print(format_step_number(str(step + 1)) + " step")
    for i in range(width):
        for j in range(height):
            r_value = g_value = b_value = 0
            number_of_values = 0

            start_x = i - 1 if i - 1 >= 0 else 0
            end_x = i + 2 if i + 2 < width else width

            start_y = j - 1 if j - 1 >= 0 else 0
            end_y = j + 2 if j + 2 < height else height

            for x in range(start_x, end_x):
                for y in range(start_y, end_y):
                    r, g, b = input_pixel_map[x, y]

                    r_value += r
                    g_value += g
                    b_value += b

                    number_of_values += 1

            r_value = r_value // number_of_values
            g_value = g_value // number_of_values
            b_value = b_value // number_of_values

            output_pixel_map[i, j] = (r_value, g_value, b_value)
    input_pixel_map = output_pixel_map

date_of_blur = "_ " + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") if getenv("ADD_DATETIME_TO_FILENAME") == "True" else ""
intensity_of_blur = "_intensity-" + intensity if getenv("ADD_INTENSITY_TO_FILENAME") == "True" else ""

output_file_name = getenv("OUTPUT_PATH") + "/blurred" + date_of_blur + intensity_of_blur + "." + getenv("OUTPUT_FORMAT")
output_image.save(output_file_name)

end_time = time()
elapsed = end_time - start_time
print(f"Execution time: {elapsed:.6f} seconds")