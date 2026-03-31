print("=== 1. LIST - Akses & Manipulasi ===")
my_list = [10, "Halo", 3.14, True, "Python", 42, "AI"]
print(f"List awal: {my_list}")
print(f"Elemen pertama: {my_list[0]}, Elemen terakhir: {my_list[-1]}")
print(f"Slicing [1:6:2]: {my_list[1:6:2]}")

print("\nManipulasi List:")
my_list.append("Baru")
print(f"Setelah append('Baru'): {my_list}")
my_list.insert(2, "Sisip")
print(f"Setelah insert(2, 'Sisip'): {my_list}")
my_list.extend([99, 100])
print(f"Setelah extend([99, 100]): {my_list}")
popped_item = my_list.pop()
print(f"Setelah pop() (mengeluarkan {popped_item}): {my_list}")
my_list.remove("Halo")
print(f"Setelah remove('Halo'): {my_list}")


print("\n=== 2. TUPLE - Immutability & Unpacking ===")
my_tuple = (100, 200, 300, 400, 500)
print(f"Tuple: {my_tuple}")
print(f"Panjang tuple: {len(my_tuple)}")
print(f"Akses indeks ke-2: {my_tuple[2]}")

a, b, *rest = my_tuple
print(f"Unpacking: a={a}, b={b}, rest={rest}")


print("\n=== 3. SET - Keunikan & Operasi Himpunan ===")
set_a = {1, 2, 3, 4, 5, 5, 5} 
set_b = {4, 5, 6, 7, 8}
print(f"Set A (duplikat hilang): {set_a}")
print(f"Set B: {set_b}")

print(f"Union (|): {set_a | set_b}")
print(f"Intersection (&): {set_a & set_b}")
print(f"Difference A - B (-): {set_a - set_b}")
print(f"Symmetric Difference (^): {set_a ^ set_b}")


print("\n=== 4. DICTIONARY - Key/Value Dasar ===")
mahasiswa = {
    "nama": "Rangga",
    "nim": "2308561136",
    "angkatan": 2023,
    "kota": "Denpasar"
}
print(f"Data awal: {mahasiswa}")

mahasiswa["prodi"] = "Informatika"
mahasiswa["kota"] = "Badung"
del mahasiswa["angkatan"]
print(f"Setelah modifikasi: {mahasiswa}")

print(f"Keys: {list(mahasiswa.keys())}")
print(f"Values: {list(mahasiswa.values())}")
print(f"Items: {list(mahasiswa.items())}")

print("Iterasi key: value:")
for key, value in mahasiswa.items():
    print(f"- {key}: {value}")


print("\n=== 5. NESTED STRUCTURES ===")
daftar_buku = [
    {"judul": "Python Dasar", "penulis": "Andi", "tahun": 2018},
    {"judul": "Machine Learning", "penulis": "Budi", "tahun": 2021},
    {"judul": "Data Science", "penulis": "Citra", "tahun": 2019},
    {"judul": "Deep Learning", "penulis": "Dewi", "tahun": 2023}
]

print("Semua judul buku:")
for buku in daftar_buku:
    print(f"- {buku['judul']}")

buku_baru = [buku for buku in daftar_buku if buku['tahun'] >= 2020]
print(f"Buku terbit >= 2020: {buku_baru}")


print("\n=== 6. COMPREHENSION & UTILITAS ===")
list_genap = [x for x in range(1, 21) if x % 2 == 0]
list_kuadrat = [x**2 for x in range(1, 21)]
print(f"List Genap: {list_genap}")
print(f"List Kuadrat: {list_kuadrat}")

dict_angka = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print(f"Dict Ganjil/Genap: {dict_angka}")

kalimat = "Belajar AI"
set_huruf = {huruf.lower() for huruf in kalimat if huruf != " "}
print(f"Set huruf unik dari kalimat '{kalimat}': {set_huruf}")


print("\n=== 7. KEANGGOTAAN & PENCARIAN ===")
target_list = "Python"
if target_list in my_list:
    indeks = my_list.index(target_list)
    print(f"'{target_list}' ditemukan di my_list pada indeks {indeks}")
else:
    print(f"'{target_list}' tidak ditemukan di my_list")

target_set = "a"
if target_set in set_huruf:
    print(f"Huruf '{target_set}' ada di dalam set_huruf") 
     