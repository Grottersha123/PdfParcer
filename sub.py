import subprocess,os
import Con
path = '/home/grotter/Downloads/ab.pdf'
def pdfpar(path,form):
    
    t = os.path.splitext(path)[0]
    try:
        os.makedirs(t)
        os.chdir(t)
        try:
            subprocess.check_output(['pdfimages','-png',path,'nes'])
            Con.convert(t+'/',form)
            print('Your pictures in '+ t)
        except:
            print('You should input correct format .format')
    except:
        print('The directory is ready '+ t)


