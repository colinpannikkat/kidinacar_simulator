import easygui as eg, time, sys
loop = 0
while True:
    def loop1():
        if loop == 20:
            eg.msgbox("We are here.", ok_button="Exit")
            sys.exit()
    a = eg.buttonbox("Are we there yet?", choices=("Yes", "No"), title="Kid in a Car Simulator")
    if a != "No":
        i = eg.msgbox("Really!?", ok_button="No.")
        time.sleep(.5)
        loop = loop+1
        loop1()
        print loop
        continue
    else:
        eg.msgbox("Aw...", ok_button="Drive on.")
        time.sleep(.5)
        loop = loop+1
        loop1()
        print loop
        continue
