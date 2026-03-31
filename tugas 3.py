nama = "Rangga"
umur = 21
berat_badan = 65.5
is_mahasiswa = True
koleksi_pokemon = ["Pikachu", "Bulbasaur", "Squirtle", "Charizard", "Mewtwo"]

teks = "Halo, nama saya " + nama
print(teks)
print(len(teks))
print(teks.upper())
print(teks.lower())

x = 20
y = 6
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)

print(koleksi_pokemon[3])
koleksi_pokemon.append("Snorlax")
koleksi_pokemon.remove("Bulbasaur")
koleksi_pokemon.pop()

input_nama = input("Masukkan nama: ")
input_umur = input("Masukkan umur: ")
print("Halo, nama saya " + input_nama + " dan umur saya " + input_umur + " tahun.")