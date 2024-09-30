import signx, time

win = signx.SignatureWindow()
win.run()

while win.running():
    if win.finished():
        print(signx.filters.remove_leading_duplicates(win.get_signature()))
        win.reset()