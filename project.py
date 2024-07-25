import customtkinter as cTk

from pytube import YouTube
def video_download():
        try: 

            yt_link = YouTube(link.get())
            title = yt_link.title
            info.configure(text = f"The title of the video that you are downloading is\n {title}.", font = ("Helvetica", 15, "bold"))
            yt_link.streams.get_highest_resolution().download()
            status.configure(text= "Download Completed")

        except:
            status.configure(text = "Download Error", font = ("Helvetica", 18),text_color  = "red" )

        
        
def clear():
    var.set(" ")
    info.configure(text = "Insert the link", font=("Helvetica", 20))
    status.configure(text = " ")
    

# def progress(size , bytes_reamaining):
#      video_size = size.filesize
#      bytes_downloaded = video_size-bytes_reamaining
#      percentage_of_completion = bytes_downloaded/video_size*100
#      per =str(int(percentage_of_completion))
#      pPercenttage.configure(text = per + "%")
#      pPercenttage.update()

#      progress_bar.set(float(percentage_of_completion))




        
        
        
root = cTk.CTk()
root.geometry('500x250')
root.maxsize(500, 300)
root.title("Download YouTube Videos")
var  = cTk.StringVar()
window = cTk.CTkFrame(root, fg_color="transparent")
info = cTk.CTkLabel(window, text = "Insert the link", font=("Helvetica", 20))
info.pack(padx = 10, pady =10)
link = cTk.CTkEntry(window , textvariable=var)
link.pack(padx = 10, pady =10)
status = cTk.CTkLabel(window, text = "", font = ("Helvetica",18), text_color="white" )
status.pack()
btn_download = cTk.CTkButton(window, text="Download", width= 100, command=video_download, corner_radius=20)
btn_download.pack(padx = 10, pady =10)
btn_clear  = cTk.CTkButton(window, text = "clear",width = 70, command= clear, corner_radius=60 )
btn_clear.pack()
# pPercenttage = cTk.CTkLabel(window, text  = "0%")
# pPercenttage.pack()
# progress_bar = cTk.CTkProgressBar(window)
# progress_bar.set(0)
# progress_bar.pack()

window.pack()
root.mainloop()