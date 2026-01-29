x = 5
print(type(x)) #mencetak tipe data dari variabel x, output: <class 'int>

x = "Hello World"	#str = string digunakan untuk menyimpan teks
x = 20	#int = tipe data bilangan bulat
x = 20.5	#float = tipe data bilangan desimal
x = 1j	#complex = tipe data bawaan (built-in) yang merepresentasikan bilangan kompleks, terdiri dari bagian riil dan bagian imajiner,
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple= tipe data sama yang terurut yang tidak dapat  diubah
x = range(6)	#range = tipe data yang mempresentasikan urutan bilangan bulat yang terurt
x = {"name" : "John", "age" : 36}	#dict = tipe data koleksi yang terstruktur, tidak berurutan (unordered), dan mutable (dapat diubah) yang menyimpan data dalam pasangan kunci-nilai (key-value pair).
x = {"apple", "banana", "cherry"}	#set = Kumpulan item unik tanpa urutan (unordered). Set tidak mengizinkan adanya duplikasi data
x = frozenset({"apple", "banana", "cherry"})	#frozenset = mirip dengan set tetapi tipe datanya tidak dapat diubah
x = True	#bool = tipe data yang hanya memiliki dua nilai, true atau false
x = b"Hello"	#bytes = tipe data menyimpan urutan byte (data biner)
x = bytearray(5)	#bytearray = mirip dengan byte, tapi dapat diubah
x = memoryview(bytes(5))	#memoryview	= memungkinkan mengakses internal data dari sebuah objek (seperti bytes atau bytearray) tanpa harus menyalinnya.
x = None	#NoneType = ketiadaan nilai atau variabel yang belum diisi

#membuat tipe data yang spesifik
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))