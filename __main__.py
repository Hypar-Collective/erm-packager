import shutil
import PySimpleGUI as sg
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Google Drive Authentication
gauth = GoogleAuth()
drive = GoogleDrive(gauth)


OUT_FOLDER = "out"

TEMPLATE_CONFIG = "template.config.json"


def package():
    print(values["-IN-"])
    shutil.copyfile(TEMPLATE_CONFIG, os.path.join(OUT_FOLDER, "config.json"))


def list_files():
    file_list = drive.ListFile(
        {'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))


sg.theme("DarkAmber")


layout = [
    [sg.Text("Collect all the files and installers and put them in the 'files' folder.")],
    [sg.Text("Controller Installer"), sg.Input(), sg.FileBrowse(key="-IN-")],
    [sg.Text("Designer Installer"), sg.Input(), sg.FileBrowse()],
    [sg.Text("Ableton Project"), sg.Input(), sg.FileBrowse()],
    [sg.Text("Current date: "), sg.InputText("dd-mm-yyyy")],
    [sg.Text("Version: "), sg.InputText("1.0.0")],
    [sg.Button("Package"), sg.Button("Get ERMs")]
]

window = sg.Window('ERM Packager', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Package":
        package()

    if event == "Get ERMs":
        list_files()


window.close()
