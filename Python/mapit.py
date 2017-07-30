import webbrowser, sys, pyperclip
import pyautogui
# passing command line arguments
#sys.argv # = ['mapit.py', '870' 'Valencia', 'St.']

#Check if command line argument(s) passed

if len(sys.argv) > 1:
    #'mapit.py', '870' 'Valencia', 'St.'] -> '870 Valencia St.']
    address = ' '.join(sys.argv[1:])
    
else:
    address = pyperclip.paste()
 #   https://www.google.com/maps/place/<ADDRESS>
   # webbrowser.open('https://www.google.com/maps/place/73 Greylynne Drive')  # Working webbrowser.ope()
   # webbrowser.open('https://www.google.com/maps/place/' + address)
    
pyautogui.size()
