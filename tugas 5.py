def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    hasil = sum(angka) / len(angka)
    return round(hasil, 2)

class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self):
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"

if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(f"Tambah(5, 7): {tambah(5, 7)}")
    print(f"Tambah(10): {tambah(10)}")
    print(f"Rata-rata([80, 90, 100]): {rata_rata([80, 90, 100])}")
    print(f"Rata-rata([]): {rata_rata([])}")

    print("\n=== CLASS STUDENT ===")
    mhs1 = Student("Budi", "A123")
    mhs1.tambah_nilai(80.0)
    mhs1.tambah_nilai(85.0)
    print(mhs1)
    print(f"Rata-rata: {mhs1.rata_nilai()}, Status: {mhs1.status()}")

    print()

    mhs2 = Student("Rangga", "2308561136")
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(65.0)
    print(mhs2)
    print(f"Rata-rata: {mhs2.rata_nilai()}, Status: {mhs2.status()}")