Introduction
============


.. image:: https://readthedocs.org/projects/adafruit-circuitpython-ch9328/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/ch9328/en/latest/
    :alt: Documentation Status


.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/adafruit/Adafruit_CircuitPython_CH9328/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_CH9328/actions
    :alt: Build Status


.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Code Style: Ruff

CircuitPython driver for the CH9328 UART to HID keyboard breakout


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.


`Purchase one from the Adafruit shop <http://www.adafruit.com/products/5973>`_

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-ch9328/>`_.
To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-ch9328

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-ch9328

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install adafruit-circuitpython-ch9328

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install adafruit_ch9328

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    import board
    import busio
    import time
    from adafruit_ch9328.ch9328 import Adafruit_CH9328
    from adafruit_ch9328.ch9328_keymap import Keymap

    # Initialize UART for the CH9328
    uart = busio.UART(board.TX, board.RX, baudrate=9600)
    ch9328 = Adafruit_CH9328(uart)

    ch9328.send_string("Hello World!")

    # Send the backspace key 12 times to erase the string
    keys = [Keymap.BACKSPACE, 0, 0, 0, 0, 0]  # Keycode for backspace in US mapping
    no_keys_pressed = [0, 0, 0, 0, 0, 0]
    for _ in range(12):
        ch9328.send_key_press(keys, 0)  # Press
        ch9328.send_key_press(no_keys_pressed, 0)  # Release the key

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/ch9328/en/latest/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_CH9328/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
