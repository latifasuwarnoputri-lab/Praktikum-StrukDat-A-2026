#kutipan dalam kutipan
print("naruto suka makan 'naruto' di ramennya")# kutipan dalam kutipan dapat digunakan asal kutipannya berbeda dengan  kutipan luarnya

#memasukkan string ke dalam variabel
a = 'warkop DKI'
print(a)

#memasukkan string di banyak baris dengan menggunakan tiga kutipan """
a = """satu ditambah satu sama dengan? 
dua!
that's simple"""
print(a)

#slicing string
b = "Selamat datang"
print(b[2:5]) #pilih karakter mulai dari index ke 2 sampai index ke 5 (tidak termasuk index ke 5)
#output= lam

#slice di awal
b = "Cinta, jawa"
print(b[:5]) #Pindahkan karakter dari posisi awal ke posisi 5 (tidak termasuk):
#output= Cinta

#slice di akhir
b = "sayang, bunda!"
print(b[2:])
#output= yang, bunda!

#slice negatif
b = "Harta dunia"
print(b[-5:-2]) #mulai dari index ke -5 sampai index ke -2 (tidak termasuk index ke -2)
#output= dun

#modifikasi string
#upper case = mengubah semua karakter jadi huruf besar
a = "bahagia selalu"
print(a.upper())

#lower case = mengubah semua karakter jadi huruf kecil
a = "serta muliaaa"
print(a.lower())

#remove whitespace = menghapus spasi dan tab di awal atau akhir string
a = "  panjang umurnya "
print(a.strip())
 #output= "panjang umurnya"

#replace = mengganti karakter dengan karakter lain
a = "baik hatinya"
print(a.replace("h", "J"))

#split = membagi string menjadi substring berdasarkan pemisah tertentu
a = "hidup, ini, sangat, lawak, sekali"
print(a.split(",")) #output = ['hidup', ' ini', ' sangat', ' lawak', ' sekali'] 

#menggabungkan string
#menggabungkan variabel a dan b menjadi variabel c
a = "aku"
b = "jawa"
c = a + b
print(c) #output = akujawa

#menambahkan spasi dengan " "
a = "aku"
b = "jawa"
c = a + " " + b
print(c) #output = aku jawa

#format string

#F-string
#letakkan `f' di depan literal string, dan tambahkan kurung kurawal {}sebagai tempat penampung untuk variabel dan operasi lainnya.
age = 36
txt = f"My name is John, I am {age}"
print(txt) #output = My name is John, I am 36

#placeholder and modifier
#placeholder dapat berisi variabel, operasi, fungsi, dan pengubah untuk memformat nilai
rupiah = 60
txt = f"harganya itu {rupiah} ribu"
print(txt) #output = harganya itu 60 ribu

luas = 60
txt = f"sawitnya {luas:.2f} hektar" #Tampilkan harga dengan 2 angka desimal
print(txt) 

#Lakukan operasi matematika di tempat penampung, dan kembalikan hasilnya:
txt = f"harga mangga {7 + 12} ribu"
print(txt)

#escape character
#Gunakan karakter backslash \sebagai karakter pelolos (escape character).
#Karakter escape memungkinkan untuk menggunakan tanda kutip ganda ketika biasanya Anda tidak diizinkan:

txt = "aku jawa dan \"Vikings\" aku bangga." 
print
#output = aku jawa dan "Vikings" aku bangga.