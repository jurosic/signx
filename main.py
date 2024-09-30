import signx, time

win = signx.SignatureWindow()
win.run()

while win.running():
    if win.finished():
        sig = win.get_signature()
        sig = signx.filters.remove_leading_duplicates(sig)
        sig = signx.filters.crop_to_content(sig)
        print(sig)
        win.reset()