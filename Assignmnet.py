import PySimpleGUI as sg
from PIL import Image,ImageTk,ImageDraw,ImageFont

sg.theme('BlueMono')
layout_1 =[        
        [sg.FileBrowse('Load', enable_events=True,size=(10, 1),tooltip="Helps you to load a new image every time.",key='browse')],
        [sg.Image(filename="",size=(400,400), key='Imag')],               
        [sg.Text("Enter width:",size=(9, 1)),sg.Input(key='wid_input'),sg.Text("Enter Degrees of rotation:",size=(20, 1)),sg.Input(key='dor_input', size=(7,1)),
        sg.Text("Enter your text here:",size=(15, 1)),sg.Input(key='text', size=(20,10))
        ],
        [sg.Text("Enter height:",size=(9, 1)),sg.Input(key='heig_input'),sg.Text("",size=(20, 1)),sg.Button("Rotate",key = "rot"),
        sg.Text("",size=(16, 1)),sg.Button("Apply Text",key = "applytxt")
        ],
        [sg.Button("Resize",key = "rs"),sg.Text("",size=(20, 1)),sg.Button("Transpose",key = "transpose")],
        [sg.Text("",size=(55, 1)),sg.Button("SAVE",size =(20,1),key = "save",tooltip="Save your final Image")]
        ]
window = sg.Window('Image Editor', layout_1)
filename = ''
while True:
    event, values = window.read()
    print(event, values)    
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'browse' and filename != values['browse']:  
        filename = values['browse']
        img = Image.open(values['browse']).resize((600,600))
        width, height = img.size       
        window['Imag'].Update(data= ImageTk.PhotoImage(img)) 
        img

    else:        
        if  event: 
            if event == 'rs':
                if values['wid_input'] != '' and   values['heig_input'] != '':            
                    width, height = img.size
                    img = img.resize((int(values['wid_input']),int(values['heig_input'])))                                                              
                    window['Imag'].Update(data= ImageTk.PhotoImage(img))   
                else:
                    sg.popup('Please Enter both Width and Height values')             
                
            elif event == 'rot':
                if values['dor_input'] != '':                
                    img = img.rotate((int(values['dor_input'])))                              
                    window['Imag'].Update(data= ImageTk.PhotoImage(img))  
                else:
                    sg.popup('Please Enter degree of rotation')             
               
            elif event == 'transpose':
                if img:              
                    img = img.transpose(Image.FLIP_LEFT_RIGHT)                
                    window['Imag'].Update(data= ImageTk.PhotoImage(img))  
                else:
                    sg.popup('Please Enter degree of rotation')

            elif event == 'applytxt':
                draw = ImageDraw.Draw(img)
                myFont = ImageFont.truetype('C:/ProgramData/Anaconda3/pkgs/werkzeug-1.0.1-py_0/site-packages/werkzeug/debug/shared/ubuntu.ttf', 40)
                draw.text((0, 0), values['text'], font=myFont, fill =(300, 0, 0))
                window['Imag'].Update(data= ImageTk.PhotoImage(img))            

            elif event == "save":
                img                
                img.save("Edited_Image.PNG")
                sg.popup('Thankyou for saving the image')
                break

            else:
                break
    
window.close()