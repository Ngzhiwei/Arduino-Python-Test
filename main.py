from tkinter.constants import E
import serial, time
import PySimpleGUI as sg
import serial.tools.list_ports


def OnOffLED(e_led2):
    if e_led2 == 0:
        Arduino.write(on.encode('ascii'))
        window['led'].update('ON')
        e_led2 = 1
    else:
        Arduino.write(off.encode('ascii'))
        window['led'].update('OFF')
        e_led2 = 0
    return e_led2

def Puertos():
    ports = serial.tools.list_ports.comports()
    coms = []
    for port, desc, hwid in sorted(ports):
        coms.append("{}: {} [{}]".format(port, desc, hwid))
    return coms


sg.theme('DarkPurple1')

layout =   [[sg.Text('Temperatura actual:'), sg.Text(size=(5,1), key='temperatura'), sg.Text('LED ='), sg.Text(size=(15,1), key='led')],
            [sg.Button('LED'), sg.Button('Temp'), sg.Button('Exit')],[    
            sg.Slider(range=(0, 255), orientation='v', size=(5, 20), default_value=0, enable_events=True),      
            sg.Slider(range=(0, 255), orientation='v', size=(5, 20), default_value=0, enable_events=True),      
            sg.Slider(range=(0, 255), orientation='v', size=(5, 20), default_value=0, enable_events=True),]]

coms = Puertos()
choices = (coms)
layout2 = [ [sg.Text('Elige el puerto en el que esta conectado el arduino')],
            [sg.Listbox(choices, size=(60, len(choices)), key='-COM-')],
            [sg.Button('Ok')]]

time.sleep(0.5)

# estado del led y codigos que se le pasan al arduino por el serial
e_led = 0
on = '1001'
off = '1010'
temp = '1011'

window2 = sg.Window('Elegir puerto', layout2)

while True:

    event, values = window2.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Ok':
        if values['-COM-']:    # if something is highlighted in the list
            comsel = values['-COM-'][0]
            splitter = comsel.split(':')
            Arduino = serial.Serial(splitter[0],9600)
            window = sg.Window('Arduino Control', layout)
            break

window2.close()

while True:

    event, values = window.read()
    print(event, values)

    if event == 'Temp':
            Arduino.reset_input_buffer()
            Arduino.write(temp.encode('ascii'))
            celsius = Arduino.read(size=4)
            window['temperatura'].update(float(celsius))

    if event == 'LED':
        e_led = OnOffLED(e_led)

    if event == 0 or event == 1 or event == 2:
        rgb = '2,' + str(int(values[0])) + ',' + str(int(values[1])) + ',' + str(int(values[2]))
        Arduino.write(rgb.encode('ascii'))
        time.sleep(0.07)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()