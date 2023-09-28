kpl_sebelumnya = int(input('KPL Sebelumnya = '))
jarak_sebelumnya = int(input('Jarak Sebelumnya = '))

hasil_sebelumnya = jarak_sebelumnya/kpl_sebelumnya
print(hasil_sebelumnya)

kpl_sesudahnya = int(input('KPL Sesudahnya = '))
jarak_sesudahnya = int(input('Jarak Sesudahnya = '))

hasil_sesudahnya = jarak_sesudahnya/kpl_sesudahnya
print(hasil_sesudahnya)

hasil_selisih_jarak = jarak_sesudahnya - jarak_sebelumnya
if hasil_selisih_jarak<0 :
    hasil_selisih_jarak = hasil_selisih_jarak * -1

print(hasil_selisih_jarak)

hasil_selisih_pembagian = hasil_sesudahnya - hasil_sebelumnya
if hasil_selisih_pembagian<0 :
    hasil_selisih_pembagian = hasil_selisih_pembagian * -1

print(hasil_selisih_pembagian)

hasil = hasil_selisih_jarak / hasil_selisih_pembagian

print(hasil)
