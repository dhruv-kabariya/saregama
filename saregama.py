import PyPDF2 
import re
import csv
import datetime


song = []
fault = []
# creating a pdf file object 
pdfFileObj = open('Saregama.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
pl = pdfReader.numPages
t1 = datetime.datetime.now()
for i in range(2,112):

# creating a page object 
    pageObj = pdfReader.getPage(i) 
  
# extracting text from page
    x = pageObj.extractText()

    xn=re.split('(\d*\D+)',x)
    l = len(xn)
    for j in range(1,l):
        if(len(xn[j]) > 1):
            
            if(("Album" in xn[j]) and (("Artistes" in xn[j])  or ("Artiste" in xn[j]))):
                
                
                mix = xn[j]
                st = mix.split("Album:")
                songname = st[0]
                if("Artistes:" in st[1]):
                    fa = st[1].split("Artistes:")
                else:
                # print(st[1])
                    fa = st[1].split("Artiste:")
                # print(fa)
                film = fa[0]
                artist = fa[1]
                song.append(
                    {
                        "Song" : songname,
                        "Film" : film,
                        "Artistes" : artist,
                    }
                )   
            elif(("Film" in xn[j]) and (("Artistes" in xn[j])  or ("Artiste" in xn[j]))):
                
                
                mix = xn[j]
                st = mix.split("Film:")
                songname = st[0]
                if("Artistes:" in st[1]):
                    fa = st[1].split("Artistes:")
                else:
                # print(st[1])
                    fa = st[1].split("Artiste:")
                # print(fa)
                film = fa[0]
                artist = fa[1]
                song.append(
                    {
                        "Song" : songname,
                        "Film" : film,
                        "Artistes" : artist,
                    }
                ) 
            else:
                fault.append(xn[j])
t2 = datetime.datetime.now()
print(t2-t1)
# closing the pdf file object 
pdfFileObj.close() 
fileds = ["Song","Film","Artistes"]
file_name = "detail.csv"
print(len(song))
with open(file_name,"w") as f:
    writer = csv.DictWriter(f,fieldnames = fileds)
    writer.writeheader()
    writer.writerows(song)

t1 = datetime.datetime.now()
print(t1-t2)
print(len(fault))
print(fault)