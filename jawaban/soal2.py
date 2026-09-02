from soal1 import penilaian, grading

nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = penilaian(nilai_tugas, nilai_uts, nilai_uas)

print(f"| {'Nama':11} :", nama, type(nama))
print(f"| {'Nilai Akhir':12}: {nilai_akhir:.2f}", type(nilai_akhir))

nilai_akhir = penilaian(nilai_tugas, nilai_uts, nilai_uas)
grade = grading(nilai_akhir)

print(f"Nilai {nilai_akhir} -> Grade {grade}")