from pypresence import Presence
import time
import psutil

PROCNAME = ["java", "VirtualBoxVM", "citra-qt",]

CLIENT_ID = ["941980247774101584", "942656248044728331", "944460758970941480",]

IMAGE = ["minecraft", "virtualbox_logo", "citra",]

STATES = ["Java Edition", "Running", "Running",]

print("Share Activity to Discord --ver.1.0--\nIf you want to turn off this program, press Ctrl+C.")
status = 0

while True:
    NamesList = []    # 実行中全プロセス名
    if status == 0:
        print("Waiting for starting process",PROCNAME)
        status = 1

    for procs in psutil.process_iter():
        NamesList.append(procs.name())
    
    for name in PROCNAME:
        
        if name in NamesList:
            print(name,"start playing")
            number = PROCNAME.index(name)
            
            RPC = Presence(CLIENT_ID[number])
            RPC.connect()
            
            RPC.update(large_image = IMAGE[number], state = STATES[number], start = time.mktime(time.localtime()))

            print("Start sharing.")

            while True:
                NameList = []

                for proc in psutil.process_iter():
                    NameList.append(proc.name())

                if not (name in NameList):
                    break

                time.sleep(5)

            print(name, "turned off.")
            RPC.clear()
            print("Stop sharing.")
            status = 0
                
        else:
            #print(name,"not running...")
            pass
    
    time.sleep(5)

