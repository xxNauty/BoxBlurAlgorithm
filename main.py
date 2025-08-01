from dotenv import load_dotenv
from pathlib import Path
from shutil import copy
from blur import blur
import os
from file_processors import json_processor


def list_files_in_dir(directory) -> list[str]:
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))]

load_dotenv()

files = list_files_in_dir(os.getenv("INPUT_PATH"))
files.remove("input/.gitkeep")

for file in files:
    working_dir = "output/" + Path(file).stem + "/"

    if os.path.isdir(working_dir):
        os.rmdir(working_dir)

    os.mkdir(working_dir)

    copy(file, working_dir + os.path.basename(file))

    json_processor.create_file(working_dir + "data")

    blur(file, working_dir)