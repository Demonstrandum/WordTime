# WordTime
A macOS menu bar item which tells the time in words.

Download with `git` using:
<br />`git clone https://github.com/Demonstrandum/WordTime && cd ./WordTime`
<br />Then, install dependencies and the package with:
<br />`python setup.py install`
<br />Now you can <a href="#terminal">start it from the terminal</a>
<br />or <a href="#autorun">enable it on login using autorun.py</a>

Dependencies:
<br />`pyobjc` & `rumps`
for macOS menubar interaction.

![Image of menubar](https://cloud.githubusercontent.com/assets/26842759/24832420/dd17b148-1ca7-11e7-84c0-f1acb231665a.png)

<div id="autorun"></div>
## Start on login (autorun)
Use `autorun.py` after having installed through  `setup.py` to enable the automatic start of WordTime. Run the command `python autorun.py enable` in your terminal to enable WordTime on login. To disable WordTime autorun, run `python autorun.py disable`, then you can always reenable it again.

## Notice
Do not use standard python that comes with macOS, install python ~2.7 with pip usually in `/usr/local/bin/python`, for example python from the brew package manager, e.g. `brew install python`

To stop `wordtime` press the item and press 'Quit'.

#### Start from terminal or use in terminal
<div id="terminal"></div>
To start the menu bar item from the terminal simply write `wordtime` or `wordtime &` to run it int the background in your terminal, make sure to have `/usr/local/bin/` in your `PATH`, This is only for macOS, if you installed it wordtime on another OS, remove `/usr/local/bin/wordtime` as this executable will only work on macOS.

##### Other OS
If you are using another OS, to run it in the terminal run `python terminal.py` this doesn't need any of the dependencies and works only when in the same directory as the `wordtime` folder or you have installed it through `python setup.py install`.
