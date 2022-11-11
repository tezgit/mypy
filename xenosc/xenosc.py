

#########################################
## OSC INIT section
import argparse
import random
import time
# from pythonosc import osc_message_builder
# from pythonosc import udp_client

from pythonosc.udp_client import SimpleUDPClient

oscdestIP = "192.168.0.170"
port = 54321
client = SimpleUDPClient(oscdestIP, port)  # Create client
# test send
client.send_message("/test/floatparam", 123)   # Send float message
client.send_message("/test/moreparams", [1, 2., "hello"])  # Send message with int, float and string

        
#########################################
## GUI INIT section
import PySimpleGUI as sg

sg.theme('dark grey 9')

linespace = 12
down = False 

layout=[
        
    [sg.Text('XENOLALIA OSC KONTROL',text_color='gray', font=("Helvetica", 24))],
    [sg.Text(' ',text_color='gray', font=("Helvetica", linespace))], # EMPTY LINE
    
    [sg.Text('IP address',text_color='white', font=("Helvetica", 10)),
    sg.InputText('192.168.0.170', text_color='white', background_color='#002233',size=(24,20),
                 font=("Helvetica", 14), key="destIP"),
     sg.Button('reConnect', button_color="white on black", key='reconnect')],
     [sg.Text(' ',text_color='gray', font=("Helvetica", linespace))], # EMPTY LINE
           
    [sg.Text('         ',text_color='gray', font=("Helvetica", linespace)),
    sg.Button('PumpTest', button_color="white on red", key='pumptest', size=(30,3))],
    [sg.Text(' ',text_color='gray', font=("Helvetica", linespace))], # EMPTY LINE
           
    [sg.Text('SERVO ANGLE',text_color='white', font=("Helvetica", 10)),
	sg.Slider(range=(0,99), orientation='h', size=(40,20),background_color='#002233', key="servoangle", enable_events=True)], #ROW 2 : SLIDER
    [sg.Text(' ',text_color='gray', font=("Helvetica", linespace))], # EMPTY LINE
    
      [sg.CBox('P1', size=(10, 30), key="p1", enable_events=True, default=False, font=("Helvetica", 24)),
         sg.CBox('P2', key="p2", enable_events=True, default=False, font=("Helvetica", 24))],
      [sg.Text(' ',text_color='gray', font=("Helvetica", linespace))], # EMPTY LINE
      

     
    [sg.Exit()] #ROW 3 : Exit BUTTON
]

window = sg.Window('XENO-OSC-CONTROLS', layout, size=(600,600), element_justification="left", finalize=True)

#########################################
## LOOP
while True:
    event, values = window.read()
    print (event, values) 
    
       
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    
    elif event == "reconnect":
       print("EKKICE")
       client = SimpleUDPClient(values['destIP'], port)
    
    
    elif event == "servoangle":
        # print("slider value", values['servoangle'])
        angle = values['servoangle']
        client.send_message("/xeno/servo", angle)
    elif event == "p1":
        var = int(values['p1'])
        client.send_message("/xeno/p1", var)
    elif event == "p2":
        var = int(values['p2'])
        client.send_message("/xeno/p2", var)
    elif event == "pumptest":
        down = not down
        window['pumptest'].update(button_color="white on green" if down else "white on red")
        if down:
            client.send_message("/xeno/pumptest", 1)
        else:
            client.send_message("/xeno/pumptest", 0)
     
    
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    

#########################################
## EXIT
window.close()
    






