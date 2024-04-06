from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
from datetime import datetime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 0
            print(filename)
            if filename != 'newDesktop':
                new_name = filename # f1.jpg and f2.jpg
                extension = 'noname' # noname
                # print(new_name,extension)
                try:
                    extension = str(os.path.splitext(folder_to_track + '/' + filename)[1]) # .jpg
                    path = extensions_folders[extension] # C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images path of newDesktop where file is to be sent
                    # print(extension,path)
                except Exception:
                    extension = 'noname'
                dir_present = extensions_folders[extension].split("/")
                main = "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop"
                for i in range(len(dir_present) - 6):
                    if not os.path.exists(extensions_folders[extension]):
                        os.makedirs(extensions_folders[extension])
                        main += "/" + dir_present[6+i]
                now = datetime.now() # date + time
                year = now.strftime("%Y") # year in 200x format
                month = now.strftime("%m") # month in 01 to 12
                # print(now,year,month)
                folder_destination_path = extensions_folders[extension] # C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images

                year_exists = False
                month_exists = False
                for folder_name in os.listdir(extensions_folders[extension]): # returns directories in newDesktop of extension type and check for year and month
                    if folder_name == year:
                        folder_destination_path = extensions_folders[extension] + "/" + year
                        year_exists = True
                        for folder_month in os.listdir(folder_destination_path):
                            if month == folder_month:
                                folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                month_exists = True
                if not year_exists: # if folders of year nd month are not present than it will create months and years folders
                    os.mkdir(extensions_folders[extension] + "/" + year)
                    folder_destination_path = extensions_folders[extension] + "/" + year
                    # print("Made folder",year)
                if not month_exists:
                    os.mkdir(folder_destination_path + "/" + month)
                    folder_destination_path = folder_destination_path + "/" + month
                    # print("Made folder",month)
                file_exists = os.path.isfile(folder_destination_path + "/" + new_name) # false if files are not present in newDesktop
                # print(new_name,file_exists) 
                while file_exists:
                    i += 1
                    # splitext splits the path into filename + extension of it
                    # splitext[0] = path + filename and splitext[1] = extension of file
                    new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + ("("+str(i)+")") + os.path.splitext(folder_to_track + '/' + filename)[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    print(new_name,file_exists)
                src = folder_to_track + "/" + filename
                new_name = folder_destination_path + "/" + new_name
                print(src,new_name)
                # os.rename(src, new_name)
extensions_folders = {
# noname or other type of files
    'noname': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other",
# Audio
    '.aif' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.cda' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.mid' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.midi' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.mp3' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.mpa' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.ogg' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.wav' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.wma' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.wpl' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
    '.m3u' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Audio",
#Text
    '.txt' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.doc' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Microsoft/Word",
    '.docx' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Microsoft/Word",
    '.odt ' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.pdf': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/PDF",
    '.rtf': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.tex': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.wks ': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.wps': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/TextFiles",
    '.wpd': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/TextFiles",
#Video
    '.3g2': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.3gp': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.avi': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.flv': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.h264': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.m4v': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.mkv': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.mov': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.mp4': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.mpg': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.mpeg': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.rm': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.swf': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.vob': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
    '.wmv': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Video",
#Images
    '.ai': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.bmp': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.gif': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.ico': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.jpg': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.jpeg': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.png': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.ps': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.psd': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.svg': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.tif': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.tiff': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.CR2': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
    '.webp': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Media/Images",
# Internet
    '.asp': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.aspx': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.cer': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.cfm': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.cgi': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.pl': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.css': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.htm': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.js': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.jsp': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.part': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.php': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.rss': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
    '.xhtml': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Internet",
# Compressed
    '.7z': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.arj': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.deb': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.pkg': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.rar': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.rpm': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.tar.gz': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.z': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Compressed",
    '.zip': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Compressed",
# Disc
    '.bin': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Disc",
    '.dmg': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Disc",
    '.iso': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Disc",
    '.toast': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Disc",
    '.vcd': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Disc",
# Data
    '.csv': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.dat': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.db': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.dbf': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.log': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.mdb': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.sav': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.sql': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.tar': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.xml': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
    '.json': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Database",
# Executables
    '.apk': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Executables",
    '.bat': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Executables",
    '.com': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Executables",
    '.exe': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Executables",
    '.gadget': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Executables",
    '.jar': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Executables",
    '.wsf': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Executables",
# Fonts
    '.fnt': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Fonts",
    '.fon': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Fonts",
    '.otf': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Fonts",
    '.ttf': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Other/Fonts",
# Presentations
    '.key': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Presentations",
    '.odp': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Presentations",
    '.pps': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Presentations",
    '.ppt': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Presentations",
    '.pptx': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Presentations",
# Programming
    '.c': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/C&C++",
    '.class': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Java",
    '.dart': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Dart",
    '.py': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Python",
    '.sh': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Shell",
    '.swift': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/Swift",
    '.html': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/html",
    '.h': "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Programming/html",
# Spreadsheets
    '.ods' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlr' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xls' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlsx' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Microsoft/Excel",
    '.csv' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Microsoft/Excel",
# System
    '.bak' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.cab' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.cfg' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.cpl' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.cur' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.dll' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.dmp' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.drv' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.icns' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.ico' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.ini' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.lnk' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.msi' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.sys' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
    '.tmp' : "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop/Text/Other/System",
}
folder_to_track = "C:/Users/Dhrumil/OneDrive/Desktop/oldDesktop"
folder_destination = "C:/Users/Dhrumil/OneDrive/Desktop/newDesktop"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()