import PySimpleGUI as sg
sg.theme("BlueMono")
sg.theme_text_color("#00FFFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                           [sg.Text("NPM   : 2210010115 ")],
                           [sg.Text("Nama  : Adiyatma saputra ")],
                           [sg.Text("Kelas : 5B NonReg Banjarmasin ")]
                           ],
                   size=(510,200),
                   font=("Times", 18))
window()
window.close()