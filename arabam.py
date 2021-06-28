import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def my_function():
    soup=BeautifulSoup(r.content,"html.parser")
    gelen_veri=soup.find_all("table",{"class":"table listing-table w100 border-grey2"})
    deneme= (gelen_veri[0].contents)[len(gelen_veri[0].contents)-1]
    deneme= deneme.find_all("tr",{"class":"listing-list-item pr should-hover bg-white"})
    wb = Workbook()
    ws = wb.active
    for acaba in deneme:
        aaaa = acaba.find_all("h3",{"class":"crop-after"})
        bbbb = acaba.find_all("td",{"class":"pl8 pr8 tac pr"})
        cccc = acaba.find_all("td",{"class":"listing-text pl8 pr8 tac pr"})    
        adi=aaaa[0]
        para=bbbb[0]
        yil=cccc[0]  
        print(adi.text)
        print(para.text[1:-4]+" TL")
        print(yil.text)
        print("*******************")
        ws.append([adi.text,para.text[1:-1],yil.text])
    wb.save("dosya.xlsx")

inp = input("Link: ")
if inp[0:5]=="https":
    url=inp
    r=requests.get(url)
    my_function()
elif inp[0:3]=="www":
    url=inp
    url2="https://"+url
    r=requests.get(url2)
    my_function()
elif inp[0:6]=="arabam":
    url=inp
    url3="https://www."+url
    r=requests.get(url3)
    my_function()    
else:
    print("Linkinizi Kontrol Ediniz")































