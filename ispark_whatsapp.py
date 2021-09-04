
import pywhatkit as py
import requests


BASE="https://api.ibb.gov.tr/ispark/Park"
response=requests.get(BASE)
yanitlar=response.json()

print(len(yanitlar)) # lenght of response

bosKapasite=0

for i in range(len(yanitlar)): 

    if yanitlar[i]["parkName"]=="<ParkYeriAdi": #Onr:Florya Sosyal Tesisleri
       bosKapasite=yanitlar[i]["emptyCapacity"]
    i += 1

print(bosKapasite) #free spaces:bos kapasite


py.sendwhatmsg_instantly("+90<telefonNo>",str(bosKapasite))

print("sent")
