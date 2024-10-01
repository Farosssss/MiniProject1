print('Selamat datang di perusahaan') 
print('Masukkan data diri anda')  

username = input('username: ') 
password = input('password: ') 

print('Selamat datang')  
username2 = input('username: ') 
password2 = input('password: ') 

if username == username2 and password == password2:     
    print('Login sukses')  
    
    while True:         
        JamKerja = float(input("Jam kerja: ")) 
        TarifKerja = float(input("Tarif kerja: Rp. ")) 
        
        
        TotalGaji = JamKerja * TarifKerja
        
        if JamKerja > 160: 
            bonus = TotalGaji * 0.1
            TotalGaji = TotalGaji + bonus 
            
        print("Total gaji: Rp.", TotalGaji) 
        
        pilihan = input("Lagi? (y/n): ") 
        if pilihan.lower() != "y": 
            break 
else:
    print('Login gagal') 
