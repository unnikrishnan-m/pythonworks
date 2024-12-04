from abc import ABC,abstractmethode

class Editor(ABC):

    @abstractmethode

    def open(self):

        pass

    @abstractmethode

    def write(self):
        pass

    @abstractmethode

    def debug(self):

        pass

    @abstractmethode

    def execute(selgf):
        

class Vscode(Editor):

    def open(self):

        print("vscode open methode")

vscode_instance=Vscode

vscode_instance.open()       
    

