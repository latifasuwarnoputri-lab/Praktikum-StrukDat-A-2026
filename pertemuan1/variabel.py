#membuat variabel
a = 'baby'
b = 'bus' 
print(a)
print(b)

x = 13     # x adalah tipe data int
x = "Ucup" # x adalah tipe data str
print(x)

#casting berguna untuk menentukan tipe data
x = str(5)    # x akan jadi '5'
y = int(5)    # y akan jadi 5
z = float(5)  # z akan jadi 5.0

#mengetahui tipe data dengan type()
c = 3
d = "izin"
print(type(c))
print(type(d))

#string bisa menggunakan satu atau dua tanda kutip
e = "lalapan"
#sama dengan
e = 'lalapan'

#nama variabel sangat mempengaruhi
s = "sate"
S = "taichan"
print(s)
#maka outputnya akan menghasilkan nilai dari variabel s bukan S

#penulisan nama variabel

#camel case
iniNamanyaVariabel = "asli"
#setiap huruf awal setelah kata pertama menggunakan huruf besar

#pascal case
IniNamanyaVariabel = "asli"
#setiap huruf awal pada setiap kata menggunakan huruf besar

#snake case
ini_namanya_variabel = "asli"
#setiap kata dipisahkan dengan garis bawah (_)

#memasukkan variabel lebih dari satu
x, y, z = "pisang", "coklat", "keju"
print(x)
print(y)
print(z)

#satu value dengan banyak variabel di satu baris
x = y = z = "coklat lumer"
print(x)
print(y)
print(z)

#jika memiliki nilai yang banyak dalam sebuah array list,tuple,maka nilainya dapat diekstrak ke variabel
rasaRoti = ["kacang", "coklat", "keju"]
x, y, z = rasaRoti
print(x)
print(y)
print(z)

#output variabel
x = "python seru banget"
print(x)

#output dengan variabel lebih dari satu dapat menggunakan koma
x = "Python"
y = "seru"
z = "banget"
print(x, y, z)

x = "Python"
y = "seru"
z = "banget"
print(x, y, z) #output juga bisa menggunakan +

x = 8
y = 14
print(x + y) #karakter + bisa digunakan sebagai operator matematika

x = 6
y = "Hari"
print(x, y) #menggabungkan angka dengan huruf bisa menggunakan ,

#variabel global

#Buat variabel di luar fungsi, dan gunakan variabel tersebut di dalam fungsi.
x = "ez banget"

def iniFungsi():
  print("Python itu " + x)

iniFungsi()

#Buat variabel di dalam fungsi, dengan nama yang sama dengan variabel global
x = "asik"

def myfunc():
  x = "seru"
  print("Python itu " + x)

myfunc()

print("Python itu " + x)

#jika menggunakan kata kunci global, variabelnya akan menjadi global
def myfunc():
  global x
  x = "lebih mudah dari bahasa c"

myfunc()

print("Python itu " + x)

