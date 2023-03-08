#n=input( "masukkan asal mobil (ketik 'done'untuk keluar):").lower

def hitung_mobil():
     
    mobil = 0
while True:
        mobil =input( "masukkan asal mobil (ketik 'done'untuk keluar):").lower().split(" ")
        n =str(mobil)
        if  n[0] == "done" :
            break
        else:
             
            if n[0] == "solo" :
                mobil += n 
                print("Jumlah mobil Solo :", mobil)
            elif n[0] == "surabaya":
                mobil += n 
                print("Jumlah Mobil Surabaya :", mobil)
            elif n [0]== "jogja":
                mobil += n 
                print("Jumlah Mobil Jogja :", mobil)
            elif n[0]== "magelang":
                mobil += n 
            print("Jumlah Mobil Magelang:", mobil)

    


