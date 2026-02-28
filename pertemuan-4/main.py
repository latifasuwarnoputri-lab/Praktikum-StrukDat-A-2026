import konverter
from kurs import kurs
from tabulate import tabulate

def menampilkan_tabel():

    data_tabel = [[k, f'{v:,.0f}'.replace(',', '.')] for k, v in kurs.items()]

    print("===KONVERTER MATA UANG===")
    print (tabulate(data_tabel, headers= ['kode', 'Kurs'], tablefmt="grid"))

def main():
    menampilkan_tabel()

    dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
    ke = input ("Ke (IDR/USD/EUR/SGD/JPY): ").upper()

    jumlah = float(input("jumlah : "))

    if dari == "IDR":
        hasil = konverter.idr_ke_uang_lain (jumlah, ke)
        hasil_pas = int(hasil * 100) /100

        jumlah_idr = f'RP{jumlah:,.0f}'.replace(',', '.')
        print(f"{jumlah_idr}, = {hasil_pas} {ke}")

    else:
        hasil = konverter.uang_lain_ke_idr (jumlah, dari)
        hasil_idr = f'{hasil:,.0f}'.replace(',', '.')
        print(f"{jumlah} {dari} = RP{hasil_idr}")

if __name__ == "__main__":
    main()