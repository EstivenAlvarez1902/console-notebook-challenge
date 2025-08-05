



class Note:
    High: str = ("HIGH")
    Medium: str = ("MEDIUM")
    Low: str = ("LOW")


    def __init__(self, code: str, tittle: str,text: str,importance: str):
        self.code = code
        self.tittle = tittle
        self.importance = importance



class Notebook:
    Notes = []


    def add_note(self, tittle: str, text: str, importance: str,):





