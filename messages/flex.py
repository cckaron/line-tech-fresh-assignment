import os
import json

project_folder = os.path.dirname(os.path.abspath(__file__))

class flex:
    def __init__(self, fileName):
        self.project_folder = project_folder
        self.fileName = fileName

    def readFile(self):
        filePath = os.path.join(os.path.join(project_folder, 'templates'), self.fileName+".json")
        with open(filePath, 'r') as file:
            data = json.load(file)
            return data

