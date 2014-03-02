#main.py
#By Tyler Spadgenske
DEBUG = True

import getcmd, cmds, sttwin

def Cyclops(DEBUG=False):
    THRESHOLD = sttwin.audio_int()
    #Main loop
    while True:
        print
        #Get the command and convert it to a list
        cmd = getcmd.get(THRESHOLD, True)
        if DEBUG: print 'COMMAND:', cmd

        cmd.pop(0)
        num = 0
        for word in cmd:
            cmd[num] = word.lower()
            num += 1
        if len(cmd) == 0:
            cmd.append('')
            if DEBUG: print 'Not complete command'
        #Determin master command
        if cmd[0] == 'what':
            cmds.What(cmd, DEBUG)
        elif cmd[0] == 'walk' or cmd[0] == 'turn':
            cmds.Walk(cmd, DEBUG)
        elif cmd[0] == 'stop':
            cmds.Walk(cmd, DEBUG).stop()
        elif cmd[0] == 'pickup' or cmd[0] == 'pick' and cmd[1] == 'up':
            master_cmd = 'pickup'
        elif cmd[0] == 'set' and cmd[1] == 'down':
            master_cmd = 'set down'
        elif cmd[0] == 'where':
            master_cmd = 'where'
        elif cmd[0] == 'take':
            master_cmd = 'take'
        elif cmd[0] == 'set':
            master_cmd = 'set'
        elif cmd[0] == 'tell':
            master_cmd = 'tell'
        elif cmd[0] == 'who':
            master_cmd = 'who'
        else:
            if DEBUG: print 'Not valid command'
            
            
Cyclops(DEBUG=DEBUG)
