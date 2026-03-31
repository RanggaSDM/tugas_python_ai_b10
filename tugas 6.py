import numpy as np
import pandas as pd
import os

np.random.seed(42)

def hitung_statistik_numpy():
    nilai_ujian = np.random.randint(50, 100, size=10)
    
    statistik = {
        "rata_rata": np.mean(nilai_ujian),
        "median": np.median(nilai_ujian),
        "std_deviasi": np.std(nilai_ujian),
        "nilai_min": np.min(nilai_ujian),
        "nilai_max": np.max(nilai_ujian)
    }
    return nilai_ujian, statistik

def buat_dataframe_pandas(nilai_numpy):
    data = {
        "nama": ["Andi", "Budi", "Citra", "Dewi", "Eka"],
        "nim": ["001", "002", "003", "004", "005"],
        "nilai": nilai_numpy[:5]
    }
    df = pd.DataFrame(data)
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")
    return df

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = len(self.df[self.df["nilai"] >= threshold])
        total = len(self.df)
        return (lulus / total) * 100

    def save_summary(self, path: str):
        with open(path, "a") as f:
            f.write("\n=== RINGKASAN OOP GRADEBOOK ===\n")
            f.write(f"Rata-rata Kelas: {self.average()}\n")
            f.write(f"Persentase Kelulusan: {self.pass_rate()}%\n")
            f.write(f"Detail Data:\n{self.df.to_string()}\n")

    def __str__(self):
        return f"GradeBook(Jumlah Data={len(self.df)}, Rata-rata={self.average()})"

if __name__ == "__main__":
    # 1. NumPy Section
    print("=== NUMPY ===")
    nilai_array, stats = hitung_statistik_numpy()
    print(f"Array Nilai: {nilai_array}")
    for k, v in stats.items():
        print(f"{k.replace('_', ' ').title()}: {v:.2f}")

    # 2. Pandas Section
    print("\n=== PANDAS ===")
    df_mhs = buat_dataframe_pandas(nilai_array)
    print(df_mhs.head())

    # 3. File I/O (Tulis Ringkasan Awal)
    file_path = "ringkasan_tugas6.txt"
    with open(file_path, "w") as f:
        f.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        for k, v in stats.items():
            f.write(f"{k}: {v:.2f}\n")
        f.write("\n=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah Baris: {len(df_mhs)}\n")
        f.write(f"Lulus: {len(df_mhs[df_mhs['status'] == 'LULUS'])}\n")
        f.write(f"Tidak Lulus: {len(df_mhs[df_mhs['status'] == 'TIDAK LULUS'])}\n")

    # 4. OOP Section
    print("\n=== OOP: GRADEBOOK ===")
    my_gb = GradeBook(df_mhs)
    print(my_gb)
    print(f"Rata-rata: {my_gb.average()}")
    print(f"Pass Rate: {my_gb.pass_rate()}%")
    my_gb.save_summary(file_path)
    print(f"\nLaporan telah disimpan di {file_path}") 