import tkinter as tk
from tkinter import Label, ttk, Text, messagebox, filedialog
import os
from pytubefix import YouTube, captions
from pytubefix.cli import on_progress


# WINDOW
def create_window() -> tk.Tk:
    window = tk.Tk()
    window.title('YouDL')
    window.geometry("620x350")

    l = Label(window, text="Download Audio, Video and Subtitles.", font=('Helvetica 15 bold'), bg='indianred', fg='bisque')
    l.pack(pady=(100, 10))
    window.configure(bg='indianred')
    return window

# HANDLE RADIO BUTTON
def handle_radio_button(v: tk.StringVar, entry: tk.Entry) -> None:
    selected_button = v.get()
    entry_value = entry.get()
    try:
        if selected_button == 'mp3':
                yt = YouTube(entry_value, on_progress_callback=on_progress)
                video = yt.streams.filter(only_audio=True).first()
                if video is not None:
                    destination = filedialog.askdirectory()
                    out_file = video.download(output_path=destination)
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    messagebox.showinfo('Success', 'Installation was completed.')
                else:
                    messagebox.showwarning('Warning', 'No audio stream found')


        elif selected_button == 'mp4':
            yt = YouTube(entry_value, on_progress_callback = on_progress)
            video = yt.streams.get_highest_resolution()
            if video is not None: 
                destination = filedialog.askdirectory()
                out_file = video.download(output_path=destination)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp4'
                os.rename(out_file, new_file)
                messagebox.showinfo('Success', 'Installation was completed')
            else:
                messagebox.showwarning('Warning', 'No video stream found')
        elif selected_button == 'subtitles':
            yt = YouTube(entry_value, on_progress_callback= on_progress)
            captions = yt.captions
            if captions:
                caption = yt.captions['en']                
                xml_caption = caption.xml_captions

                with open('output.txt', 'w', encoding='utf-8') as f:
                    f.write(xml_caption)
                messagebox.showinfo('Success', 'Installation was completed')
            else:
                messagebox.showwarning('Warning', 'No subtitles.')
    except Exception as e:
        messagebox.showerror('error' , f'An error occured: {e}')

# ENTRY
def add_button(window: tk.Tk, v: tk.StringVar, entry: tk.Entry) -> None:
    style = ttk.Style()
    
    style.configure('TButton', 
                    font=('Helvetica', 12, 'bold'), 
                    background='bisque', 
                    bordercolor='black',
                    relief='solid',
                    borderwidth=2,
                    highlightthickness=2)
    
    button = ttk.Button(window, text='Download', style='TButton', command=lambda: handle_radio_button(v, entry))
    button.pack(pady=(10, 10))

# RADIO BUTTON
def radio_button(window: tk.Tk) -> tk.StringVar:
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
    return v

# ADD ENTRY
def add_entry(window: tk.Tk) -> tk.Entry:
    entry = tk.Entry(window, justify=tk.LEFT, width=60)
    entry.pack(pady=(10, 10))
    entry.configure(highlightthickness=2,borderwidth=1,highlightbackground='black') 
    return entry

# MAIN
def main():
    window = create_window()
    entry = add_entry(window)
    v = radio_button(window)
    add_button(window, v, entry)
    window.mainloop()

if __name__ == "__main__":
    main()