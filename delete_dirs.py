import os
import shutil
import tkinter.messagebox
from tkinter import filedialog
from tkinter import *
from typing import AnyStr, Tuple
from tkinter.messagebox import askokcancel, showinfo, WARNING
import yaml

end_txt = "                   \r"


def select_dir():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory()


def enumerate_files(dir_path, recursive=False):
    for root, sub_dirs, files in os.walk(dir_path):
        for name1 in files:
            yield path_join(root, name1)
        if not recursive:
            break


def enumerate_dirs(dir_path, recursive=False):
    for root, sub_dirs, files in os.walk(dir_path):
        for sub_dir in sub_dirs:
            yield path_join(root, sub_dir), sub_dir
        if not recursive:
            break


def delete_dir(path_to_dir):
    shutil.rmtree(path_to_dir)


def path_join(a: AnyStr, *paths: AnyStr) -> AnyStr:
    return os.path.join(a, *paths).replace("/", os.path.sep)


def get_file_name_extension(file_full_name) -> Tuple[AnyStr, AnyStr, AnyStr]:
    dir_name1, file_name = os.path.split(file_full_name)
    name1, extension1 = os.path.splitext(file_name)
    return dir_name1, name1, extension1


def get_delete_dir_names(fn):
    try:
        with open(fn, "r") as stream:
            values = yaml.safe_load(stream)
            return values.get('delete_dir_names', [])
    except:
        tkinter.messagebox.showerror(message=f'Bad config file! {fn}  Example content: delete_dir_names: ["obj", "bin"]')
        return None


def run_delete_dirs():
    config_fn = path_join("config.yml")
    delete_dir_names = get_delete_dir_names(config_fn)
    if delete_dir_names is None:
        return

    dir_name = select_dir()

    delete_list = [dir_full_path for dir_full_path, dir_name in enumerate_dirs(dir_name, True) if dir_name in delete_dir_names]
    if len(delete_list) == 0:
        tkinter.messagebox.showinfo(message=f'No dir named {delete_dir_names} found in {dir_name}?')
        return

    answer = askokcancel(
        title='Warning',
        message=f'Do you want to recursively delete all directories named {delete_dir_names} in {dir_name}?',
        # message=f'Do you want to delete: {delete_list}? ',
        icon=WARNING)

    if answer:
        for dir_full_path in delete_list:
            try:
                print(f"deleting -> {dir_full_path}")
                delete_dir(dir_full_path)
            except:  # todo
                pass

        print("finished")


if __name__ == '__main__':
    run_delete_dirs()
