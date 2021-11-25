import os
import sys


def change_exten(directory, old_exten, new_exten, divider="/"):
    """recursively the extension of all files with old_exe to new_exten
    :param directory: string - path to root of recursive search
    :param old_exten: the extension to replace
    :param new_exten: all files with old_exten are replaced with new_exten
    :param divider: default of '/' for Linux and OS, use '\\' for windows
    :return: None
    """
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.find(old_exten) > 0 and filename.endswith(old_exten):
                name = filename.rsplit(".", 1)[0]
                print(subdir + divider + filename, subdir + divider + name + new_exten)
                os.rename(subdir + divider + filename, subdir + divider + name + new_exten)


if __name__ == '__main__':
    folder = "C:\\Users\\bjrat\\WebstormProjects\\ChessKingsCouncil\\app\\src\\game_logic"
    change_exten(folder, ".js", ".ts", "\\")

