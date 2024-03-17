from llama_index.tools import FunctionTool
import os

note_file = os.path.join("data", "notes.txt")
# function below will save note

def save_note(note): #note is piece of text you want to add to a file
    if not os.path.exists(note_file):
        open(note_file, "w") #if not, we create new file
    
    with open (note_file, "a") as f: #opens a file in append mode
        f.writelines([note + "\n"]) 
        #writes the given 'note' to the file adding a newline character '\n' at the end
    
    return "note saved "

note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name='note_saver',
    description = 'this tool can save a text bsed note to a file for a user'
)

