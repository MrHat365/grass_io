"""
  @ Author:   Mr.Hat
  @ Date:     2024/3/30 14:05
  @ Description:
  @ History:
"""

from typing import Optional


def file_to_list(
        filename: str
):
    with open(filename, 'r+') as f:
        return list(filter(bool, f.read().splitlines()))


def str_to_file(file_name: str, msg: str, mode: Optional[str] = "a"):
    with open(
            file_name,
            mode
    ) as text_file:
        text_file.write(f"{msg}\n")


def shift_file(file):
    with open(file, 'r+') as f:  # open file in read / write mode
        first_line = f.readline()  # read the first line and throw it out
        data = f.read()  # read the rest
        f.seek(0)  # set the cursor to the top of the file
        f.write(data)  # write the data back
        f.truncate()  # set the file size to the current size
        return first_line.strip()
