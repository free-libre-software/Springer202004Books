#############################################
###
### Download Springer Books
### Corona Virus Time
###
### carlos@cardenas.pe
###
###  GPL 3.0 v
###
### 27/04/2020
###
#############################################
import PyPDF2
import urllib3
import wget

def foo(m):
    http =urllib3.PoolManager()

    n="ht"+m

    res =http.request('GET',n)    

    title=''.join(res.data.decode('utf-8').split('h1')[1].split('>')[1].split('<')[0].split('/')[0])+".pdf"

    uld="http://link.springer.com/content/"+res.data.decode('utf-8').split('Download book PDF')[0].split('content/')[1].split('title')[0].split('.pdf')[0]+".pdf"

    wget.download(uld,title)


file =open('Spring.pdf','rb')

f= PyPDF2.PdfFileReader(file)


for i in range(0,f.numPages):

    if i ==0:

        for j in range (0, len(f.getPage(i).extractText().split('OpenURL')[1].split('ht'))):
            if f.getPage(i).extractText().split('OpenURL')[1].split('ht')[j].split('\n')[0] != '':
                print(f.getPage(i).extractText().split('OpenURL')[1].split('ht')[j].split('\n')[0])
                foo(f.getPage(i).extractText().split('OpenURL')[1].split('ht')[j].split('\n')[0])

    else:
        for j in range (0, len(f.getPage(i).extractText().split('ht'))):
            if f.getPage(i).extractText().split('ht')[j].split('\n')[0] !='':
                if len(f.getPage(i).extractText().split('ht')[j].split('\n')[0])==64:
                    print(f.getPage(i).extractText().split('ht')[j].split('\n')[0])
                    foo(f.getPage(i).extractText().split('ht')[j].split('\n')[0])

