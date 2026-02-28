from kurs import kurs

def idr_ke_uang_lain (jumlah, kode_mata_uang):

    nilai_tukar = kurs [kode_mata_uang]
    return jumlah / nilai_tukar

def uang_lain_ke_idr (jumlah, kode_mata_uang):

    nilai_tukar = kurs[kode_mata_uang]
    return jumlah  * nilai_tukar