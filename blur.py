from PIL import Image
import time
import os
import datetime
from file_processors import json_processor

def format_step_number(number : str) -> str:
    if number[-1] == '1' and number != "11":
        return number + "st"
    elif number[-1] == '2' and number != "12":
        return number + "nd"
    elif number[-1] == '3' and number != "13":
        return number + "rd"
    else:
        return number + "th"

def blur(path_to_image : str, where_to_write: str) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

    input_file_name = os.path.basename(path_to_image)

    print("Processed image:", input_file_name)

    start_time_of_blur = time.time()

    input_image = Image.open(path_to_image)
    input_pixel_map = input_image.load()

    width, height = input_image.size
    mode = input_image.mode

    output_image = Image.new(mode, (width, height))
    output_pixel_map = output_image.load()

    intensity = os.getenv("INTENSITY")

    time_of_every_step = {}
    for step in range(int(intensity)):
        start_time_of_step = time.time()
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

        end_time_of_step = time.time()

        print(format_step_number(str(step + 1)) + " step", end=' | ')

        time_of_step = f"{end_time_of_step - start_time_of_step:.2f} seconds"
        time_of_every_step["Step " + str(step)] = time_of_step

        print("Time of step:" + time_of_step)

    output_file_name = (
            where_to_write +
            "/output." +
            os.getenv("OUTPUT_FORMAT")
    )
    output_image.save(output_file_name)

    datetime_of_mod = datetime.datetime.now()
    time_of_modification = datetime_of_mod.strftime("%H:%M:%S")
    date_of_modification = datetime_of_mod.strftime("%d-%m-%Y")

    end_time_of_blur = time.time()
    total_time = f"{end_time_of_blur - start_time_of_blur:.2f} seconds"
    print("Total time: " + total_time)

    statistics = {
        "Input filename": input_file_name,
        "Intensity": intensity,
        "Date of modification": date_of_modification,
        "Time of modification":time_of_modification,
        "Total time:": total_time,
        "Time of every step": time_of_every_step
    }

    json_processor.write(where_to_write + "data.json", statistics)

    time.sleep(2)