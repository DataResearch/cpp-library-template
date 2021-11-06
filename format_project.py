import os
import errno
import platform
from pathlib import Path

filename_pattern = ["*.cpp", "*.h", "*.hpp", "*.inc", "*.hxx", "*.cxx", "*.c"]
folder_pattern = ["tests", "src"]
command_template = "clang-format -i -style=file "

def system_error(value):

    # this may need to be changed depending on the system you are running on
    # this version was written for linux ubuntu
    if platform.system() != 'Linux':
        raise RuntimeError("Executed on", platform.system(), "Expected 'Linux'")

    exitcode = (0xFF00 & value) >> 8
    signalcode = (0xFF & value)

    if value != 0:
        print("Error while processing command with os.system.", "Exitcode:", exitcode, "Systemsignal:", signalcode)
        raise RuntimeError("Failed to run command.")


def run_formatter(filepath):
    if os.path.isfile(filepath):
        command = command_template + filepath.__str__()
        print("Running Command:", command) 
        error = os.system(command)
        system_error(error)
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filepath)

if __name__ == "__main__":
    for folder in folder_pattern:
        for filename in filename_pattern:
            for path in Path(folder).rglob(filename):
                relative_path = path.relative_to(".")
                print("Found file:", relative_path)
                run_formatter(relative_path)
else:
    raise RuntimeError("This script is not intended to be used as a library. This script merely executes formatting for this project.")