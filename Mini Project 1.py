print('Selamat datang di perusahaan') 
print('Masukkan data diri anda')  

username = input('username: ') 
password = input('password: ') 

print('Selamat datang')  
username2 = input('username: ') 
password2 = input('password: ') 

if username == username2 and password == password2:     
    print('Login sukses')  
    
    while True:  # Mulai perulangan di sini       
        JamKerja = float(input("Jam kerja: ")) 
        TarifKerja = float(input("Tarif kerja: Rp. ")) # Input
        
        # Menghitung total gaji
        TotalGaji = JamKerja * TarifKerja
        
        if JamKerja > 160: 
            TotalGaji *= 1.1  # Bonus jika lebih dari 160 jam kerja
            
        print("Total gaji: Rp.", TotalGaji) 
        
        pilihan = input("Lagi? (y/n): ") # Perulangan
        if pilihan.lower() != "y": 
            break  # Menghentikan perulangan jika tidak memilih "y"
else:
    print('Login gagal')  # Eksekusi jika login gagal
