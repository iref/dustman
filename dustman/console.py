# -*- coding: utf-8 -*-
# Copyright (c) 2018 Jan Ferko <julyloov@gmail.com>
#
# this file is part of the project "Http Dustman" released under the "MIT" open-source license

"""iref-dustman's command-line utility

Ideally use a tool such as `click <http://click.pocoo.org/5/>`_

For more information check py:func:`click.command` and py:class:`click.Command`
"""

def ansi_red(string):
    """Colorizes the given string with `ANSI escape codes <https://en.wikipedia.org/wiki/ANSI_escape_code>`_

    :param string: a py:class:`str`

    .. note:: This function is here for demo purposes, feel free to delete it.

    :returns: a string
    """

    return '\033[1;31m{}\033[0m'.format(string)


def entrypoint():
    print(ansi_red("Not implemented yet!"))
    raise SystemExit(1)


if __name__ == '__main__':
    # this makes the script executable without needing to install
    # the iref-dustman package
    entrypoint()
