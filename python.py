# Contoh 1 
print("contoh 1")
print("positif = 10")
print("positif = -10")
print("\n")

# Variable
positif = 10
negatif = -10

if positif == 10:
    print("benar")
if positif > negatif:
    print("benar")
if positif > 9:
    print("benar")
if positif >= negatif:
    print("benar")
if positif != negatif:
    print("benar")
# tidak akan dijalankan karena kondisi logisnya false
if positif <= negatif:
    print("salah")
print("\n")

#Latihan 1
print("Latihan 1")
print("apel = 25")
print("anggur = 30")
print("\n")

# Variable
apel = 25
anggur = 30

print("Apakah anggur lebih besar dari apel?")
if anggur > apel:
    print("benar")
else:
    print(salah)

print("Apakah apel tidak sama dengan anggur?")
if apel != anggur:
    print("benar")
else:
    print("salah")
print("Apakah Apel lebih kecil atau tidak sama dengan anggur?")
if apel <= anggur:
    print("benar")
else:
    print(salah)

print("\n") # pemisah

# Latihan 2
print("Latihan 2")
print("mouse = 45")
print("keyboard = 45")

# Variable
mouse = 45
keyboard = 45
print("\n")
print("mouse lebih kecil dari keyboard")
if mouse < keyboard:
    print("benar")
else:
    print("salah")
print("mouse sama dengan keyboard")
if mouse == keyboard:
    print("benar")
else:
    print("salah")
print("\n")

# contoh 2 
print("contoh 2")
# predikat nilai
predikat_nilai = [
    "1. Predikat A untuk nilai >=90",
    "2. Predikat B untuk nilai >=80 < 90",
    "3. Predikat C untuk nilai >=60 < 80",
    "4. Predikat D untuk nilai >=40 < 60",
    "5. Selain itu , maka predikat E"
]
for predikat_nilai in predikat_nilai:
    print(predikat_nilai)
print("\n")

nilai = int(input("Masukkan Nilai Untuk predikat Nilai: "))
if nilai >= 90:
    print("predikat A")
elif nilai >= 80:
    print("predikat B")
elif nilai >= 60:
    print("predikat C")
elif nilai >= 40:
    print("predikat D")
else:
    print("predikat E")

print('\n')

# Latihan 3
print("Latihan 3")
print("Nilai besar dari 75 Lulus")
print("Nilai kecil dari 75 Tidak Lulus")
nilai2 = int(input("Masukkan Nilai: "))
if nilai2 >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")