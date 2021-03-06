import os, subprocess
import stat, sys

def main():
    plistLabel = 'com.wordtime.autorun'
    plistName  = plistLabel + '.plist'

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
    <string>/dev/null</string>

    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
    '''
    plistNewPath = os.path.expanduser('~') + '/Library/LaunchAgents/' + plistName
    # Sometimes the LaunchAgents dir does not already exist. If it does, this wil raise
    # an OSError error:
    try:
        os.mkdir(os.path.expanduser('~') + '/Library/LaunchAgents/')
    except OSError: pass # If it exists, good.
    
    if sys.argv[len(sys.argv) - 1].lower() == 'enable':
        print("Making and writing to .plist file '" + plistName + "'...\n")
        plistFile = open(plistName, 'w')
        plistFile.write(plistCont)
        plistFile.close()

        print("Moving plist file to new directory with name: " + plistNewPath + "'...\n")
        os.rename(plistName, plistNewPath)

        print("Running command 'launchctl load -w " + plistNewPath + "' to enable the wordtime on login.\n")
        subprocess.call(["launchctl", "load", "-w", plistNewPath])

        print("If 'service already loaded' then run the command:\n\nlaunchctl start " + plistLabel + "\n")
    elif sys.argv[len(sys.argv) - 1].lower() == 'disable':
        print("Stopping...")
        subprocess.call(["launchctl", "stop", plistLabel])
        print("Disabling .plist using 'launchctl unload " + plistNewPath + "'\n")
        subprocess.call(["launchctl", "unload", plistNewPath])
        print("Removing .plist\n")
        os.remove(plistNewPath)
    else:
        print("Please supply (valid) command line argument, such as:\n'python autorun.py enable' or 'python autorun.py disable'")

if __name__ == "__main__":
    main()
else:
    sys.argv.append("enable")
    main()
