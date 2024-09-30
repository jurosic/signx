import signx, time

win = signx.SignatureWindow()
win.run()

while win.running():
    if win.finished():
        print(win.get_signature())
        win.reset()