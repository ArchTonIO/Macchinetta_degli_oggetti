"""
This module contains a collection of useful functions
to track the progress of a long running process.
"""


def print_progress_bar(
    iteration,
    total,
    decimals=1,
    length=71,
    fill="#"
) -> None:
    """
    Call in a loop to create terminal progress bar.
    - Args:
        - iteration: current iteration.
        - total: total iterations.
        - decimals: positive number of decimals.
        - length: character length of bar.
        - fill: bar fill character.
    """
    percent = (
        "{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    n_bar = fill * filled_length + '-' * (length - filled_length)
    print(f"|{n_bar}| {percent}%", end="\r")
    if iteration == total:
        print("----------> DONE! <")
