from dotenv import load_dotenv
from blur import blur
import os
import uuid

def list_files_in_dir(directory) -> list[str]:
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))]

load_dotenv()

files = list_files_in_dir("input/")
files.remove("input/.gitkeep")

for file in files:

    dir_name = str(uuid.uuid4()).split("-")[0]
    working_dir = "output/" + dir_name + "/"

    os.mkdir(working_dir)
    blur(file, working_dir)