# -*- coding: utf-8 -*-
# Copyright (c) 2018 Jan Ferko <julyloov@gmail.com>
#
# this file is part of the project "Http Dustman" released under the "MIT" open-source license

"""iref-dustman's command-line utility

Ideally use a tool such as `click <http://click.pocoo.org/5/>`_

For more information check py:func:`click.command` and py:class:`click.Command`
"""
from dustman import HttpBinClient


def entrypoint():
    client = HttpBinClient()
    print("your ip is: {}".format(client.ip()))


if __name__ == '__main__':
    # this makes the script executable without needing to install
    # the iref-dustman package
    entrypoint()
