x = 5
print(type(x)) #mencetak tipe data dari variabel x, output: <class 'int>

x = "sampai jumpa"	#str = string digunakan untuk menyimpan teks
x = 56	#int = tipe data bilangan bulat
x = 35,4	#float = tipe data bilangan desimal
x = 5j	#complex = tipe data bawaan (built-in) yang merepresentasikan bilangan kompleks, terdiri dari bagian riil dan bagian imajiner,
x = ["stoberi", "mangga", "apel"]	#list	
x = ("jawa", "batak", "cina")	#tuple= tipe data sama yang terurut yang tidak dapat  diubah
x = range(5)	#range = tipe data yang mempresentasikan urutan bilangan bulat yang terurt
x = {"nama" : "agus", "banyak sawit" : 36}	#dict = tipe data koleksi yang terstruktur, tidak berurutan (unordered), dan mutable (dapat diubah) yang menyimpan data dalam pasangan kunci-nilai (key-value pair).
x = {"buaya", "manusia", "kucing"}	#set = Kumpulan item unik tanpa urutan (unordered). Set tidak mengizinkan adanya duplikasi data
x = frozenset({"apple", "banana", "cherry"})	#frozenset = mirip dengan set tetapi tipe datanya tidak dapat diubah
x = True	#bool = tipe data yang hanya memiliki dua nilai, true atau false
x = b"izin"	#bytes = tipe data menyimpan urutan byte (data biner)
x = bytearray(4)	#bytearray = mirip dengan byte, tapi dapat diubah
x = memoryview(bytes(3))	#memoryview	= memungkinkan mengakses internal data dari sebuah objek (seperti bytes atau bytearray) tanpa harus menyalinnya.
x = None	#NoneType = ketiadaan nilai atau variabel yang belum diisi

#membuat tipe data yang spesifik
x = str("bersyukur")	#str	
x = int(35)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="kartini", age = 67)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))