"""
random_file_generator.py

A utility script to generate random directory structures
with text files and archives for testing purposes.
"""

from pathlib import Path
from random import choices, randint, choice
import shutil


MESSAGE = "Hello World!"


def make_sure_folder(path: Path) -> None:
    """
    Ensures that the given directory exists.
    Creates it if it does not.
    :param path: Directory path for the new folder in the current directory
    :return: None
    """
    path.mkdir(parents=True, exist_ok=True)


def generate_random_filename() -> str:
    """
    The function generates a random file name using symbols, numbers, and letters from both the Latin and Cyrillic alphabets.
    :return: Random filename
    """
    random_chars = (
        "()+,-0123456789;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "[]^_`abcdefghijklmnopqrstuvwxyz{}"
        "~абвгдеєжзиіїйклмнопрстуфхцчшщьюя"
        "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
    )

    # Selects between 3 and 9 characters at random from the random_chars collection and combines them into a string.
    return "".join(choices(random_chars, k=(randint(3, 9))))


def generate_random_text_file(path: Path) -> None:
    """
    The function creates a random file by generating a file name and appending a random file extension.
    :param path: Directory path for the new folder or file in the current directory
    :return: None
    """
    documents = ("DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX")

    with open(
        path / f"{generate_random_filename()}.{choice(documents).lower()}", "wb"
    ) as file:
        file.write(MESSAGE.encode("utf-8"))


def generate_random_archive(path: Path) -> None:
    """
    The function creates an archive by internally calling the function that generates a random file name and appending a random archive extension to it.
    :param path: Directory path for the new folder or file in the current directory
    :return: None
    """
    archives = ("ZIP", "GZTAR", "TAR")

    shutil.make_archive(
        f"{path}/" + f"{generate_random_filename()}",
        f"{choice(archives).lower()}",
        path,
    )


def generate_random_structure_folder(path: Path) -> None:
    """
    Generates a directory tree with randomly chosen folder names and counts.
    :param path: Directory path for the new folder or file in the current directory
    :return: None
    """
    folder_names = [
        "temp",
        "folder",
        "dir",
        "tmp",
        "OMG",
        "is_it_true",
        "no_way",
        "find_it",
    ]

    random_path = Path(
        path
        / "/".join(
            choices(
                folder_names,
                weights=[10, 10, 1, 1, 1, 1, 1, 1],
                k=randint(3, len(folder_names) + 1),
            )
        )
    )
    random_path.mkdir(parents=True, exist_ok=True)


def generate_random_folder_forester(path: Path) -> None:
    """
    The function repeatedly calls the directory tree generation function, creating up to 4 nested directories in the current directory.
    :param path: Directory path for the new folder or file in the current directory
    :return: None
    """
    for _ in range(1, randint(4, 5)):
        generate_random_structure_folder(path)


def generate_random_files(path: Path) -> None:
    """
    The function creates 1 to 3 random files in the current directory.
    :param path: Directory path for the new folder or file in the current directory
    :return: None
    """
    for _ in range(1, randint(3, 4)):
        func_list = [generate_random_archive, generate_random_text_file]
        choice(func_list)(path)


def recursive_generate_random_files(path: Path) -> None:
    """
    Recursively processes all subdirectories of the given path.
    At each recursion level, the function generates random files
    in the current folder (path) and then calls itself for
    each subfolder, passing the new path as an argument.

    Each recursion stack handles only its local path,
    without affecting other subfolders at different levels.
    :param path: Directory path for the new folder or file in the current directory
    :return: None
    """
    for path_element in path.iterdir():
        if path_element.is_dir():
            # Randomly generates text files and archives in the currently specified directory.
            generate_random_files(path)
            # Recursively accepts a new directory path, traversing all directories and generating files in them.
            recursive_generate_random_files(path_element)


def main(path: Path) -> None:
    """
    Generates directory trees inside the given directory and randomly creates files in each directory.
    :param path: Directory path for the new folder or file in the current directory
    :return: None
    """
    make_sure_folder(path)
    generate_random_folder_forester(path)
    recursive_generate_random_files(path)


if __name__ == "__main__":
    main_path = Path("Temp")
    main(main_path)
