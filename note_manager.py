class NoteManager():
    def __init__(self):
        self._notes = []
        
    def _findNoteIndex(self,id):
        for i in range(len(self._notes)):
            if(self._notes[id].getId() == id):
                self._notes.pop(i)
                return i
        return False

    def getAllNotes(self):
        return self._notes

    def getNoteById(self,id):
        neededNoteIndex = self._findNoteIndex(id)
        return self._notes[neededNoteIndex]
    
    def addNote(self,note):

        if self._findNoteIndex(note.getId()):
            print("This ID is already taken")
            return False 
        
        try:
            self._notes.append(note)
            return True
        
        except Exception as e:
            print(str(e))
            return False
    
    def DeleteNote(self,id):
        neededNoteIndex = self._findNoteIndex(id)

        if(not neededNoteIndex):
            return False
        
        self._notes.pop[neededNoteIndex]
        return True
        
    def UpdateNote(self,id,**kwargs):
        neededNoteIndex = self._findNoteIndex(id)

        if (not neededNoteIndex):
            return False
        
        self._notes[neededNoteIndex].updateNote(kwargs)
        return True