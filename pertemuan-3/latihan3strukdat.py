class Person:
  def __init__(self, nama, jenisKelamin, umur):
    self.nama = nama
    self.jenisKelamin = jenisKelamin
    self.umur = umur

class Karyawan(Person):
  pass

class Karyawan(Person):
    def __init__(self, nama, jenisKelamin, umur, gaji):
        super().__init__(nama, jenisKelamin, umur)
        self._gaji = gaji

    
    def get_gaji(self):
        return self._gaji
    
    def set_gaji(self):
        return self._gaji

class Rekening:
  def __init__(self, noRekening, pin):
    self.noRekening = noRekening
    self.__pin = pin

  def get_pin(self):
    return self.__pin

  def set_pin(self, pin):
    if pin > 6 :
      self.__pin = pin
    else:
      print("pin harus lebih dari 6")

p1 = Karyawan("sinta", "perempuan", 20, 1000089)
r1 = Rekening("12333", "23563")

print(r1.get_pin())
print(p1.nama)
print(p1.get_gaji())