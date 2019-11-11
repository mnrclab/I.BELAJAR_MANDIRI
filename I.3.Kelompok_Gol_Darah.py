# MEMBUAT KELOMPOK BELAJAR BERDASARKAN GOLONGAN DARA
#     ATURAN: Golongan darah A dengan B, GOlongan darah AB dengan O
kelompok1 = []
kelompok2 = []
for i,j in nama.items():
    if j=='A' or j=='B':
        kelompok1.append(i)
    else:
        kelompok2.append(i)
print(f'Anggota kelompok 1 adalah {kelompok1}')
print(f'Anggota kelompok2 adalah {kelompok2}')