import json

from note_manager import NoteManager

class ExtendetNoteManager(NoteManager):
    def __init__(self):
        super().__init__()

    def __getIds(self,notes):
        ids = []
        for note in notes:
            ids.append(note["id"])
        return ids
    
    def __filterNotesForSaving(self,oldNotesIds=[]):
        notesAbleToSave = []

        for note in self._notes:
            if note.getId() not in oldNotesIds:
                notesAbleToSave.append(note.getDictionary())

        return notesAbleToSave

    def saveNotes(self, fileName):
        file_path = f"{fileName}.json"

        with open(file_path, "r+") as fileHandler:
            try:
                savedNotes = json.load(fileHandler) 
                print(savedNotes) 
            except Exception as e:
                print(str(e))
                savedNotes = [] 

            oldNoteIds = self.__getIds(savedNotes)  
            notesAbleToSave = self.__filterNotesForSaving(oldNoteIds) 

            if notesAbleToSave:  
                savedNotes.extend(notesAbleToSave) 
                
                fileHandler.seek(0)  
                json.dump(savedNotes, fileHandler, indent=4)  

                return True
            return False



