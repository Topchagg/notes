class BaseNote():
    def __init__(self,title,text,id):
        self.__id = id
        self.__title = title
        self.__text = text

    def getInfo(self):
        return f"ID: {self.__id}\nTitle: {self.__title}\nText: {self.__text}"
        
    def updateNote(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, f"_{self.__class__.__name__}__{key}"):
                setattr(self, f"_{self.__class__.__name__}__{key}", value)  

    def getId(self):
        return self.__id                      