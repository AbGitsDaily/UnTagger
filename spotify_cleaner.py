import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Appearance and Theme Configs
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")  # Will be changed dynamically via dropdown

class SpotifyRenamerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App Settings
        self.title("🎵 Spotify Filename Cleaner Pro")
        self.geometry("650x600")
        self.resizable(False, False)
        import customtkinter as ctk
import sys

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

class SpotifyRenamerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Spotify Cleaner")
        self.geometry("600x400")

        # Correct icon setting
        try:
            self.iconbitmap(resource_path("icon.ico"))
        except Exception as e:
            print("⚠️ Icon not loaded:", e)

        # Your UI setup continues...


        self.selected_folder = ""
        self.rename_preview = []

        # Title
        self.title_label = ctk.CTkLabel(self, text="Spotify Filename Cleaner", font=ctk.CTkFont(size=22, weight="bold"))
        self.title_label.pack(pady=(20, 5))

        # Theme + Mode Selector
        selector_frame = ctk.CTkFrame(self)
        selector_frame.pack(pady=10)

        ctk.CTkLabel(selector_frame, text="🌓 Appearance:").grid(row=0, column=0, padx=5)
        self.appearance_option = ctk.CTkOptionMenu(selector_frame, values=["System", "Dark", "Light"], command=self.set_mode)
        self.appearance_option.grid(row=0, column=1, padx=10)

        ctk.CTkLabel(selector_frame, text="🎨 Theme:").grid(row=0, column=2, padx=5)
        self.theme_option = ctk.CTkOptionMenu(selector_frame, values=["blue", "green", "dark-blue", "beige", "glass"], command=self.set_theme)
        self.theme_option.grid(row=0, column=3, padx=10)

        # Folder Preview Button
        self.preview_btn = ctk.CTkButton(self, text="📂 Select Folder & Preview", command=self.preview_renames, width=400)
        self.preview_btn.pack(pady=10)

        # Rename Button
        self.rename_btn = ctk.CTkButton(self, text="✅ Apply Rename", command=self.apply_renames, width=400)
        self.rename_btn.pack(pady=10)

        # Progress Bar
        self.progress_bar = ctk.CTkProgressBar(self, width=500)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        # Output Log
        self.output_box = ctk.CTkTextbox(self, width=580, height=280, font=("Courier", 12))
        self.output_box.pack(pady=10)
        self.output_box.insert("0.0", "No files previewed yet.\n")

    def set_mode(self, mode):
        ctk.set_appearance_mode(mode)

    def set_theme(self, theme):
        try:
            if theme in ["blue", "green", "dark-blue"]:
                ctk.set_default_color_theme(theme)
            elif theme == "beige":
                ctk.set_default_color_theme("green")  # Simulate beige
            elif theme == "glass":
                ctk.set_default_color_theme("dark-blue")  # Simulate glassy look
        except Exception as e:
            messagebox.showerror("Theme Error", f"Could not apply theme: {str(e)}")

    def get_all_files(self, folder):
        all_files = []
        for root, _, files in os.walk(folder):
            for file in files:
                if "spotifydown - " in file:
                    old_path = os.path.join(root, file)
                    new_filename = file.replace("spotifydown - ", "")
                    new_path = os.path.join(root, new_filename)
                    all_files.append((old_path, new_path))
        return all_files

    def preview_renames(self):
        self.selected_folder = filedialog.askdirectory(title="Select Folder with Music Files")
        if not self.selected_folder:
            return

        self.rename_preview = self.get_all_files(self.selected_folder)
        self.output_box.delete("0.0", "end")
        self.progress_bar.set(0)

        if self.rename_preview:
            for old, new in self.rename_preview:
                self.output_box.insert("end", f"{os.path.basename(old)} ➡️ {os.path.basename(new)}\n")
            messagebox.showinfo("Preview Ready", f"Found {len(self.rename_preview)} files to rename.")
        else:
            self.output_box.insert("0.0", "No files found with 'spotifydown - ' in the name.")
            messagebox.showinfo("Nothing Found", "No files to rename.")

    def apply_renames(self):
        if not self.selected_folder or not self.rename_preview:
            messagebox.showwarning("No Folder or Preview", "Please preview first by selecting a folder.")
            return

        total = len(self.rename_preview)
        for i, (old_path, new_path) in enumerate(self.rename_preview):
            os.rename(old_path, new_path)
            self.progress_bar.set((i + 1) / total)
            self.update_idletasks()

        self.output_box.delete("0.0", "end")
        self.output_box.insert("0.0", f"✅ Renamed {total} files successfully.\n")
        messagebox.showinfo("Done", f"Renamed {total} files.")
        self.rename_preview = []
        self.progress_bar.set(0)

# Launch the app
if __name__ == "__main__":
    app = SpotifyRenamerApp()
    app.mainloop()
