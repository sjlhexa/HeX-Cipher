import tkinter as tk
from tkinter import messagebox, BooleanVar
import argparse
import sys


ALPHABET_SIZE = 26

# My lucky number ;)
DEFAULT_SHIFT = 7

def jumble_text(text, magic_number, mode='super_secret', no_spaces=False):
    result = ""
    for char in text:
        if char.isalpha():
            # Uppercase and lowercase letters are treated differently
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            
            if mode == 'super_secret':
                new_char = chr((ord(char) - start + magic_number) % ALPHABET_SIZE + start)
            else:
                new_char = chr((ord(char) - start - magic_number) % ALPHABET_SIZE + start)
            
            result += new_char
        elif char.isspace() and no_spaces:
            result += '$@'  # Replace space with $@
        else:
            result += char
    
    return result

class SecretMsgApp:
    def __init__(self, master):
        self.master = master
        master.title("HeX Cipher")

        # Setting up the GUI
        tk.Label(master, text="Type your secret message:").pack(pady=5)
        self.msg_entry = tk.Entry(master, show="*", width=40)
        self.msg_entry.pack(pady=5)

        tk.Label(master, text="Enter your magic number:").pack(pady=5)
        self.magic_num_entry = tk.Entry(master, width=10)
        self.magic_num_entry.insert(0, str(DEFAULT_SHIFT))  # My lucky number as default
        self.magic_num_entry.pack(pady=5)

        self.sneaky_mode = BooleanVar()
        tk.Checkbutton(master, text="Super sneaky mode (replace spaces with $@)", 
                       variable=self.sneaky_mode).pack(pady=5)

        tk.Button(master, text="Hexify!", command=self.scramble).pack(pady=5)
        tk.Button(master, text="DE-Hexify!", command=self.unscramble).pack(pady=5)

        self.result_box = tk.Text(master, height=5, width=40)
        self.result_box.pack(pady=10)

    def scramble(self):
        self._do_the_thing('super_secret')

    def unscramble(self):
        self._do_the_thing('not_so_secret')

    def _do_the_thing(self, mode):
        msg = self.msg_entry.get()
        try:
            magic_num = int(self.magic_num_entry.get())
        except ValueError:
            messagebox.showerror("Oops!", "Magic number should be a whole number, silly!")
            return

        no_spaces = self.sneaky_mode.get()

        result = jumble_text(msg, magic_num, mode, no_spaces)
        
        if mode == 'not_so_secret':
            result = result.replace('$@', ' ')  # Restore spaces when decrypting
        
        self.result_box.delete('1.0', tk.END)
        self.result_box.insert(tk.END, result)

# For command line ninjas
def ninja_mode():
    parser = argparse.ArgumentParser(description="Psst... wanna encrypt a message?")
    parser.add_argument("message", help="Your super secret message")
    parser.add_argument("magic_number", type=int, help="Your magic number (sshhh)")
    parser.add_argument("-u", "--unscramble", action="store_true", help="Unscramble a message")
    parser.add_argument("-s", "--super-sneaky", action="store_true", help="Replace spaces with $@")
    
    args = parser.parse_args()

    mode = 'not_so_secret' if args.unscramble else 'super_secret'
    no_spaces = args.super_sneaky

    result = jumble_text(args.message, args.magic_number, mode, no_spaces)
    
    if mode == 'not_so_secret':
        result = result.replace('$@', ' ')  # Restore spaces when decrypting
    
    print(f"Here's your {'un' if args.unscramble else ''}scrambled message: {result}")

# The magic starts here!
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ninja_mode()
    else:
        root = tk.Tk()
        app = SecretMsgApp(root)
        root.mainloop()
