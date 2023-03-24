import os
import sys

from pyfiglet import figlet_format
from termcolor import cprint

from mistic import prog_name
from mistic.cli import cli


def main():
    cprint(text=figlet_format(text=prog_name,
                              font='standard'),
           color='magenta',
           attrs=['bold'],
           )
    cli()


if __name__ == '__main__':
    main()
