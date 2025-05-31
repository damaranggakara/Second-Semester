#TUGAS PPT STRUKTUR DATA LATIHAN 1 SAMPE 10





# LATIHAN 8
#input
input_list = input("Masukkan kata-kata(pisahkan dengan koma): ")
user_list = [kata.strip() for kata in input_list.split(',')]

#fungsi
def ganjil(daftar):
    hasil = []
    for elemen in daftar:
        if len(elemen) % 2 != 0:
            hasil.append(elemen)
    return ' '.join(hasil)

#hasil
hasil_output = ganjil(user_list)
print("Output =", hasil_output)


# LATIHAN 9
#input
dna = input("Input kode DNA: ")

#fungsi
def konversi(dna):
    result = ""
    for char in dna:
        if char.upper() == 'A':
            result += 'U'
        elif char.upper() == 'T':
            result += 'A'
        elif char.upper() == 'G':
            result += 'C'
        elif char.upper() == 'C':
            result += 'G'
        else:
            result += char
    return result

#hasil
RNA = konversi(dna)
print("Konversi DNA ke mRNA:", RNA)
