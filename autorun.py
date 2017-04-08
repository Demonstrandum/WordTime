import os, subprocess
import stat

plistLabel = 'com.wordtime.autorun'
plistName  = 'com.wordtime.autorun.plist'

plistCont = '''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.wordtime.autorun</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/wordtime</string>
    </array>
    <key>StandardErrorPath</key>
    <string>/Users/pink/launchctlERR.log</string>

    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
'''

print("Making and writing to .plist file '" + plistName + "'...\n")
plistFile = open(plistName, 'w')
plistFile.write(plistCont)
plistFile.close()

plistNewPath = os.path.expanduser('~') + '/Library/LaunchAgents/com.wordtime.autorun.plist'
print("Moving plist file to new directory with name: " + plistNewPath + "'...\n")
os.rename(plistName, plistNewPath)

print("Running command 'launchctl load -w " + plistNewPath + "' to enable the wordtime on login.\n")
subprocess.call(["launchctl", "load", "-w", plistNewPath])

# print("Starting programme now... ('launchctl start " + plistName + "')\n")
# subprocess.call(["launchctl", "start", plistName])
