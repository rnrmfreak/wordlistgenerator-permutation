charmap = {
    'a' : ['a','A','@','4'],
    'b' : ['b','B','8'],
    'c' : ['c','C'],
    'd' : ['d','D'],
    'e' : ['e','E','3'],
    'f' : ['f','F'],
    'g' : ['g','G','9'],
    'h' : ['h','H'],
    'i' : ['i','1','!','I'],
    'j' : ['j','J'],
    'k' : ['k','K'],
    'l' : ['l','L'],
    'm' : ['m','M'],
    'n' : ['n','N'],
    'o' : ['o','O','0'],
    'p' : ['p','P'],
    'q' : ['q','Q'],
    'r' : ['r','R'],
    's' : ['s','S','5','$'],
    't' : ['t','T'],
    'v' : ['v','V'],
    'w' : ['w','W'],
    'x' : ['x','X'],
    'y' : ['y','Y'],
    'z' : ['z','Z'], 
}

def permutation(word, p):
    result = []

    # Tidak ada lagi yang bisa dilakukan jika melebihi karakter
    # terakhir
    if p >= len(word):
        return result

    # Periksa apakah karakter sekarang ada di map
    # Jika ada lakukan perubahan untuk setiap karakter tersebut
    if word[p] in charmap:
        # Buat kata baru dengan karakter tersebut
        for c in charmap[word[p]]:
            w = word[:p] + c + word[p+1:]
            result.append(w)
            result += permutation(w, p+1)
    # Jika tidak, lanjut iterasi ke karakter selanjutnya
    else:
        result.append(word)
        result += permutation(word, p+1)

    return result


def save(word,file):
    # Cari permutasi dan kembalikan nilai unik
    L = list(sorted(set(permutation(word, 0))))
    with open(file+".txt", "a") as f:
        for w in L:
            f.write("{}\n".format(w))

choice = "y"
file = raw_input("Nama File : ")
while choice=="y":
    word = raw_input("masukkan kata : ")
    save(word,file)
    choice = raw_input("tambah kata lagi?? [y/n] : ")


