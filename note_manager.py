class NoteManager():
    def __init__(self):
        self.__notes = []
        
    def __findNoteIndex(self,id):
        for i in range(len(self.__notes)):
            if(self.__notes[id].getId() == id):
                self.__notes.pop(i)
                return i
        return False

    def getAllNotes(self):
        return self.__notes

    def getNoteById(self,id):
        neededNoteIndex = self.__findNoteIndex(id)
        return self.__notes[neededNoteIndex]
    
    def addNote(self,note):

        neededNoteIndex = self.__findNoteIndex(note.getId())

        if neededNoteIndex():
            print("This ID is already taken")
            return False 
        
        try:
            self.__notes.append(note)
            return True
        
        except Exception as e:
            print(str(e))
            return False
    
    def DeleteNote(self,id):
        neededNoteIndex = self.__findNoteIndex(id)

        if(not neededNoteIndex):
            return False
        
        self.__notes.pop[neededNoteIndex]
        return True
        
    def UpdateNote(self,id,**kwargs):
        neededNoteIndex = self.__findNoteIndex(id)

        if (not neededNoteIndex):
            return False
        
        self.__notes[neededNoteIndex].updateNote(kwargs)
        return True