# nama_variabel = ()
# nama_variabel = dict()  

# kamus = {1:'satu', 2:'dua', 3:'tiga'}
# print (kamus[1])

# #untuk menambahkan item ke dictionary

# kamus [4]= 'empat'
# print(kamus[4])

# #mengubah

# kamus [1] = 'unoo'
# print(kamus[1])

# print(len(kamus))


# kal = 'terima kasih'
# d = {}
# for i in kal:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)    


# var = {'1':'satu', '2':'dua', '3':'tiga'}
# print (var.get('1',0))  #satu
# print (var.get('4',0))  #0


# kalimat = 'halo nama saya gwen'
# d = {}
# for i in kalimat:
#     d[i] = d.get(i,0) + 1
# print (d)

# nama_file = "teks_contoh.txt"

# with open(nama_file, 'r') as file:
#     kemunculan_kata = {}
#     for baris in file:
#         kata_kata = baris.split()
#         for kata in kata_kata:
#             kata = kata.strip(".,!?;:\"")
#             kemunculan_kata[kata] = kemunculan_kata.get(kata, 0) + 1
# print("Kemunculan kata-kata dalam file:")
# for kata, jumlah in kemunculan_kata.items():
#     print(f"{kata}: {jumlah}")


# data = {"a": 1, "b": 2, "c": 3}

# for key in data:
#     print(key)


# data = {"a": 1, "b": 2, "c": 3}

# for key, value in data.items():
#     print(f"Key: {key}, Value: {value}")


# data = {"c": 3, "a": 1, "b": 2}

# sorted_keys = sorted(data)
# print("Kunci-kunci dictionary yang terurut:")
# for key in sorted_keys:
#     print(key, ":", data[key])



import string

nama_file = "teks_dengan_tanda_baca.txt"

kemunculan_kata = {}
with open(nama_file, 'r') as file:
    teks = file.read()
    teks_tanpa_tanda_baca = teks.translate(str.maketrans('', '', string.punctuation))
    teks_tanpa_tanda_baca = teks_tanpa_tanda_baca.lower()
    kata_kata = teks_tanpa_tanda_baca.split()
    for kata in kata_kata:
        kemunculan_kata[kata] = kemunculan_kata.get(kata, 0) + 1

print("Kemunculan kata-kata dalam file:")
for kata, jumlah in kemunculan_kata.items():
    print(f"{kata}: {jumlah}")
