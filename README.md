# WordTime
A macOS menu bar item which tells the time in words.

Install dependencies and package with:
<br />`python setup.py install`

Dependencies:
<br />`pyobjc` & `rumps`
for macOS menubar interaction.

![Image of menubar](https://cloud.githubusercontent.com/assets/26842759/24832420/dd17b148-1ca7-11e7-84c0-f1acb231665a.png)


Do not use standard python that comes with macOS, install python ~2.7 with pip usually in `/usr/local/bin/python`, for example python from the brew package manager, e.g. `brew install python`

To stop `wordtime` press the item and press 'Quit', if not, then unload `wordtime` by using: <br />
`launchctl unload ~/Library/LaunchAgents/com.wordtime.autorun.plist`

To start the menu bar item from the terminal simply write `wordtime` or `wordtime &` to run it int the background in your terminal, make sure to have `/usr/local/bin/` in your `PATH`, This is only for macOS, if you installed it wordtime on another OS, remove `/usr/local/bin/wordtime` as this executable will only work on macOS.

If you are using another OS, to run it in the terminal run `python terminal.py` this doesn't need any of the dependencies and works only when in the same directory as the `wordtime` folder or you have installed it through `python setup.py install`.
