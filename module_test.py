
#subprogramm or main programm,
import webbrowser

default = 'www.google.com'
default_index = 0

#depended function, class NoteMaster
class NoteMaster(object):
    def __init__(self,filename,pos):
        self.filename=filename
        self.pos = pos
        self.fp=None    
    def __enter__(self):
        print("__enter__")
        self.fp=open(self.filename,'r')
        return self    
    def f_collection(self):
        for row in enumerate(self.fp,start = 1):
            data = list(row)
            if data[0] == self.pos: 
                return data[1]
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.fp.close()

#main function, potential class BrowserMaster
def opensite(pos): 
    if pos == 0:
        global default
        site = default
    else:
        with NoteMaster("urls.txt",pos) as url_file:
            url_record = url_file.f_collection()
            url_list = url_record.split()
            site = url_list[1]
    webbrowser.open(site)

if __name__ == "__main__":
    print("hello there",__name__)
    opensite(default_index)
elif __name__ != "__main__":
    print(("This file was been used as %s") % (__name__) )
