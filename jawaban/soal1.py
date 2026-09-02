def penilaian(nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = 0.3 * nilai_tugas + 0.3 * nilai_uts + 0.4 * nilai_uas
    return nilai_akhir

def grading(nilai_akhir):
    if nilai_akhir > 84:
        return "A"
    elif nilai_akhir > 69:
        return "B"
    elif nilai_akhir > 59:
        return "C"
    elif nilai_akhir > 49:
        return "D"
    else:
        return "E"