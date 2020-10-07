# MicroPython Applications & Games for the micro:bit

| Name | Description |
| ---  | --- |
| [Racer](src/racer.py) | A racing game |
| [Flap](src/flap.py) | A flappy game |

Read the [micro:bit MicroPython documentation](https://microbit-micropython.readthedocs.io)

## Flash an application
I prefer to use [uflash](https://github.com/ntoll/uflash) instead of
[Mu Editor](https://codewith.mu) or the graphical online editor
[Make Code](https://makecode.microbit.org/) so that I can use the code editor
I prefer, like Sublime Text.

Connect your micro:bit and type `uflash src/racer.py` once in your
Python virtual environment.

## REPL
You can flash the micro:bit with only MicroPython. For that just do `uflash`.
Then you can have access to the MicroPython shell with `screen /dev/tty.usbmodem[..] 115200`

## License
[GPL-3.0](LICENSE)

Copyright (c) 2018, Cédric Eberhardt
