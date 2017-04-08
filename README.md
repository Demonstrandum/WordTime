# WordTime
A macOS menu bar item which tells the time in words.

Install dependencies and package with:
<br />`python setup.py install`

Dependencies:
<br />`pyobjc` & `rumps`

Do not use standard python that comes with the OS, install python ~2.7 with pip usually in `/usr/local/bin/python`, for example python from the brew package manager, e.g. `brew install python`

To stop `wordtime` press the item and press 'Quit', if not to unload `wordtime` use `launchctl unload ~/Library/LaunchAgents/com.wordtime.autorun.plist`

To start the menu bar item from the terminal simply write `wordtime` in your terminal, make sure to have `/usr/local/bin/` in your `PATH`

To run it in the terminal run `python terminal.py` this doesn't need any of the dependencies.
