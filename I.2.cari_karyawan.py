# MENCARI KARYAWAN DENGAN GOLONGAN DARAH TERTENTU
nama = {
    'ANDI': 'A', 'BUDI' : 'B', 'CACA' : 'AB', 'DEDI' : 'O',
    'ARYO': 'A', 'BARA' : 'B', 'CHIKA': 'AB', 'DERRY': 'O',
}

cari = (input('Ketik karyawan atau gol. darah: ')).upper()
info = []
for i,j in nama.items():
    if cari==j:
        info.append(i)
    elif cari==i:
        info.append(j)
print(f'Informasi tentang {cari} adalah {info}')