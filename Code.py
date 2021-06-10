from microbit import *

hi = Image("90009:90009:99999:90009:90009")
hi2 = Image("90009:90009:99999:90009:00000")
hi3 = Image("90009:90009:99999:00000:00000")
hi4 = Image("90009:90009:00000:00000:00000")
hi5 = Image("90009:00000:00000:00000:00000")
hi6 = Image("90009:90009:00000:00000:00000")
hi7 = Image("90009:90009:99999:00000:00000")
hi8 = Image("90009:90009:99999:90009:00000")
hi9 = Image("90009:90009:99999:90009:90009")

all_hi = [hi,hi2,hi3,hi4,hi5,hi6,hi7,hi8,hi9]
while True:
    if button_a.was_pressed:
        display.show(all_hi, loop = True, delay = 100)
    else:
        display.scroll(Image.ASLEEP)
