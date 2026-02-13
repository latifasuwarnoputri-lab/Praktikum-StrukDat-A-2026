 #nomor 1
nilai = [75, 80, 65, 90, 85]
nilai.append(95)
print(nilai)

nilai.pop(2)
print(nilai)

nilai.sort()
print(nilai)

print(nilai[len(nilai)-1])
print(nilai[0])

rata_rata = sum(nilai / len(nilai))
print (rata_rata)

#nomor 2

dosen = ("D001", "Dr. Andi", "Struktur Data", 12)

print(dosen[1:3])

for x in dosen:
    print(x)

ubah = list(dosen)
ubah[3] = 14
#tuples tidak bisa diubah, karena itu kita harus menggantinya dulu menjadi list

#tuple nilainya tidak bisa berubah, dan akan tetap sama dan juga tidak memiliki nilai yang duplikat

#nomor 3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

keahlian_C= keahlian_A.intersection(keahlian_B)
print(keahlian_C)

keahlian_C = keahlian_A.difference(keahlian_B)
print(keahlian_C)

keahlian_B = {"Python", "C++", "Git", "Docker"}
print("java" in thisset)
