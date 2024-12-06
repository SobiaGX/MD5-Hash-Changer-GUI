import os
import random
import hashlib
from tkinter import Tk, Label, Button, filedialog, messagebox


def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def append_random_data(file_path):
    """Append random data to a file to change its MD5 hash."""
    with open(file_path, "ab") as f:
        random_data = os.urandom(16)  # 16 random bytes
        f.write(random_data)


class MD5HashChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MD5 Hash Changer")
        self.root.geometry("400x200")
        self.file_path = None

        # File Label
        self.file_label = Label(root, text="No file selected", wraplength=300)
        self.file_label.pack(pady=10)

        # Add File Button
        self.add_file_button = Button(root, text="Add File", command=self.add_file)
        self.add_file_button.pack(pady=5)

        # Change Hash Button
        self.change_hash_button = Button(root, text="Change Hash", command=self.change_hash, state="disabled")
        self.change_hash_button.pack(pady=5)

    def add_file(self):
        """Open file dialog to select a file."""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            self.file_label.config(text=f"Selected: {os.path.basename(file_path)}")
            self.change_hash_button.config(state="normal")

    def change_hash(self):
        """Modify the file to change its MD5 hash."""
        if not self.file_path:
            messagebox.showerror("Error", "No file selected!")
            return

        try:
            original_md5 = calculate_md5(self.file_path)
            append_random_data(self.file_path)
            modified_md5 = calculate_md5(self.file_path)

            messagebox.showinfo(
                "Hash Changed",
                f"Original MD5: {original_md5}\nModified MD5: {modified_md5}\nHash successfully changed!",
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to change hash: {str(e)}")


# Run the application
if __name__ == "__main__":
    root = Tk()
    app = MD5HashChangerApp(root)
    root.mainloop()
