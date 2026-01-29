#Cetak pesan berdasarkan apakah kondisinya True atau false:

a = 45
b = 76

if b < a:
  print("b lebih kecil dari a")
else:
  print("a lebih kecil dari b")

#mengevaluasi nilai boolean
#Fungsi ini bool()memungkinkan Anda untuk mengevaluasi nilai apa pun, dan memberikan hasil berupa nilai True atau False

#evaluasi nilai dan angka
print(bool("annyeong")) #output= True
print(bool(35)) #output= True

#mengevaluasi dua variabel
x = "Nyawit"
y = 45

print(bool(x)) #output= True
print(bool(y)) #output= True

#sebagian nilai true
 #Semua string , angka, dan list adalah True, kecuali nilainya kosong atau bernilai 0.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#sebagian nilai false
 #Beberapa nilai yang dianggap False adalah: None, False, 0, dan string kosong.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

 #False terjadi jika ada objek yang dibuat dari kelas dengan __len__fungsi yang mengembalikan 0 atau False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#fungsi mengembalikan nilai boolean
 #Cetak jawaban dari sebuah fungsi:
def myFunction() :
  return True

print(myFunction())

#Cetak "YA!" jika fungsi mengembalikan nilai True, jika tidak, cetak "TIDAK!"
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") #output= YES!


#Periksa apakah suatu objek merupakan bilangan bulat atau bukan:
x = 345
print(isinstance(x, int)) #output= True
