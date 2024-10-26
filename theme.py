import PySimpleGUI as sg
sg.theme("Dark")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM     : 2210010115")],
                           [sg.Text("Nama    : Adiyatma saputra")],
                           [sg.Text("Kelas   : 5B NonReg Banjarmasin")],
                           [sg.Text("Matkul  : Pemrograman Visual 3")],
                           ],
                        size=(400,200))
window()
window.close()