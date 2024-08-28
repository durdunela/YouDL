from pytube import YouTube
import tkinter as tk
from tkinter import Label, ttk, Text

def create_window() -> tk.Tk:
    window = tk.Tk()
    window.title('YouDL')
    window.geometry("620x350")

    l = Label(window, text="Download Audio, Video and Subtitles.", font=('Helvetica 15 bold'), bg='indianred', fg='bisque')
    l.pack(pady=(100, 10))
    window.configure(bg='indianred')
    return window

def add_button(window: tk.Tk) -> None:
    style = ttk.Style()
    
    style.configure('TButton', 
                    font=('Helvetica', 12, 'bold'), 
                    background='bisque', 
                    bordercolor='black',
                    relief='solid',
                    borderwidth=2,
                    highlightthickness=2)
    
    button = ttk.Button(window, text='Download', style='TButton')
    button.pack(pady=(10, 10))

def radio_button(window: tk.Tk) -> None:
    v = tk.StringVar()
    v.set("mp3")

    frame = tk.Frame(window, bg='indianred')
    frame.pack(pady=(5, 10))    

    mp3_button = tk.Radiobutton(frame, text="MP3", variable=v, value="mp3", bg='indianred', fg='black', font=('Helvetica', 12))
    mp3_button.pack(side=tk.LEFT, padx=(0, 5))

    mp4_button = tk.Radiobutton(frame, text="MP4", variable=v, value="mp4", bg='indianred', fg='black', font=('Helvetica', 12))
    mp4_button.pack(side=tk.LEFT, padx=(5, 0))

    subtitles_button = tk.Radiobutton(frame, text="Subtitles", variable=v, value="subtitles", bg='indianred', fg='black', font=('Helvetica', 12))
    subtitles_button.pack(side=tk.LEFT, padx=(5, 5))

def add_entry(window: tk.Tk) -> None:
    entry = tk.Entry(window, justify=tk.LEFT, width=60)
    entry.pack(pady=(10, 10))
    entry.configure(highlightthickness=2,borderwidth=1,highlightbackground='black') 

def main():
    window = create_window()
    add_entry(window)
    radio_button(window)
    add_button(window)
    window.mainloop()

if __name__ == "__main__":
    main()