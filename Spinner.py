def counterClockwise(x):                    # membuat funciton bernama counterClockwise dengan 1 argument yaitu 'x'
    hasil = []                              # membuat list kosong dengan variabel hasil
    temp = []                               # membuat list kosong dengan variabel temp
    for i in range(len(x),0,-1):            # looping dengan i sebanyak panjang data (len(x)), dengan start pada len(x), pada kasus ini yaitu 3, stop pada 0 dengan step -1 sehingga hasilnya 3,2,1
        for j in range(len(x)):             # looping dengan j sebanyak panjang data, start pada 0, dan stop di len(x), sehingga hasilnya 0,1,2
            temp.append(x[j][i-1])          # menambahkan element x[j][i-1] kedalam list 'temp'. i dikurangi 1 karena index maksimal pada data adalah 2, sedangan i maksimal adalah 3
        hasil.append(temp)                  # setelah keluar dari loop "for j in range(len(x)):", list temp akan dimasukkan kedalam hasil
        temp = []                           # list temp dikosongkan kembali untuk menampung element pada loop berikutnya
    return hasil                            # output dari fungsi berupa list hasil

data = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
counterClockwise(data)