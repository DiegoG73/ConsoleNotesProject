# Importing the note module:
import notes.note as model

class Actions:
    
    def create(self, user):
        print(f"Ok {user[1]}, let's create a new note")
        
        
        title = input("\nIntroduce a title: ")
        description = input("Introduce a description: ")
        
        note = model.Note(user[0], title, description)
        save = note.save()
        
        
        if save[0] >= 1:
            print(f"\nPerfect, the note has been saved: {note.title}")
            
        else:
            print(f"This note has not saved: {note.title}")


    def show(self, user):
        print(f"\nOk {user[1]}, here are your notes: ")
        
        note = model.Note(user[0])
        notes = note.list()
        
        for note in notes:
            print("\n---------------------------------------------------------")
            print(note[2])
            print(note[3])
            print("---------------------------------------------------------")
            
            
            
    def delete(self, user):
        print(f"\nOk, {user[1]} Let's delete some notes: ")
        
        title = input("Please, introduce the title of the note that you want to delete: ")
        
        note = model.Note(user[0], title, "")
        delete = note.delete()
        
        if delete[0] >= 1:
            print(f"We've been deleted the note: {note.title}")
        else:
            print("Sorry, we couldn't delete your note, try again later")