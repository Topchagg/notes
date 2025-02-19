class BaseNote():
    def __init__(self,title,text,id):
        self._id = id
        self._title = title
        self._text = text

    def getInfo(self):
        return f"ID: {self._id}\nTitle: {self._title}\nText: {self._text}"
        
    def updateNote(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, f"_{self.__class__.__name__}__{key}"):
                setattr(self, f"_{self.__class__.__name__}__{key}", value)  

    def getId(self):
        return self._id  

    def getDictionary(self):
        newDict = {}
        
        for key, value in vars(self):
            newDict[key.lstrip('_')] = value

        return newDict
