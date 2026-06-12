import pyperclip
from tkinter import *
from deep_translator import GoogleTranslator

def copy_text():
    pyperclip.copy(output_text.get("1.0", END))

def translate_text():
    text = input_text.get("1.0", END)

    translated = GoogleTranslator(
        source=source_lang.get(),
        target=target_lang.get()
    ).translate(text)

    output_text.delete("1.0", END)
    output_text.insert(END, translated)

root = Tk()
root.title("Language Translator")
root.geometry("500x500")

languages = ["english", "hindi", "telugu", "tamil"]

source_lang = StringVar()
source_lang.set("english")

target_lang = StringVar()
target_lang.set("hindi")

Label(root, text="Source Language").pack()
OptionMenu(root, source_lang, *languages).pack()

Label(root, text="Target Language").pack()
OptionMenu(root, target_lang, *languages).pack()

Label(root, text="Enter Text").pack()

input_text = Text(root, height=5, width=40)
input_text.pack()

Button(root, text="Translate", command=translate_text).pack(pady=10)

Button(root, text="Copy", command=copy_text).pack(pady=5)

Label(root, text="Translated Text").pack()

output_text = Text(root, height=5, width=40)
output_text.pack()

root.mainloop()