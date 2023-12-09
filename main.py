import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import filedialog

def speech_to_text_and_speak():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Speak something:")
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        print("Recognized Text: " + recognized_text)
        engine.say(recognized_text)
        engine.runAndWait()
        text_canvas.delete("1.0", tk.END)  # Clear previous text
        text_canvas.insert(tk.END, recognized_text)  # Display recognized text in the canvas box
        save_button.config(state=tk.NORMAL)  # Enable the save button
        save_text = recognized_text  # Assign the recognized text to a global variable for saving
    except sr.UnknownValueError:
        print("Speech not recognized")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def save_text_as_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(save_text)
        print("Text saved as file:", file_path)

def start_conversion():
    button.config(state=tk.DISABLED)  # Disable the button during conversion
    save_button.config(state=tk.DISABLED)  # Disable the save button during conversion
    speech_to_text_and_speak()
    button.config(state=tk.NORMAL)  # Enable the button after conversion

# Create the GUI window
window = tk.Tk()

# Create a canvas box to display recognized text
text_canvas = tk.Text(window, height=10, width=50)
text_canvas.pack()

# Create a button to start the speech-to-text conversion
button = tk.Button(window, text="Start Conversion", command=start_conversion, bg="blue", fg="white")
button.pack()

# Create a save button to save the recognized text
save_button = tk.Button(window, text="Save", command=save_text_as_file, bg="yellow", fg="white", state=tk.DISABLED)
save_button.pack()

# Run the GUI window
window.mainloop()
