'''
=========================================================
Graded Challenge 1

Nama : Jeni Kasturi
Batch : BSD-002

Program ini dibuat untuk menambah barang, menghapus barang, 
menampilkan barang di keranjang, serta menjumlahkan seluruh harga barang belanjaan 
yang terdapat pada keranjang belanja
========================================================
'''

class CartItem:
    '''class ini digunakan untuk inisiasi cart item dengan atribut nama barang dan harga'''
    def __init__(self, nama, harga):
        """function ini digunakan untuk inisasi nama barang dan harga barang"""
        self.nama_barang = nama
        self.harga_barang = harga  


class ShoppingCart:
    """class ini digunaakan untuk inisiasi shopping cart dengan list barang"""

    def __init__(self):
        """function ini digunakan untuk inisiasi list barang"""
        self.barang = []

    def menambah_barang(self, item):
        """function ini digunakan untuk menyimpan barang dan harga yang telah diinput"""
        self.barang.append(item)
        print(f'Barang "{item.nama_barang}" berhasil dimasukkan ke keranjang.')

    def menghapus_barang(self, hapus_barang):
        """function ini digunakan untuk menghapus barang dengan menginput nama barang"""
        barang_baru =[]
        for i in self.barang:
            if i.nama_barang != hapus_barang:
                barang_baru.append(i)
            else:
                continue
        self.barang = barang_baru

    def menampilkan_barang(self):
        """function ini digunakan untuk menampilkan list barang"""
        if self.barang is not None:
            for i in range(len(self.barang)):
                print(f'{i+1}. {self.barang[i].nama_barang} - Rp {self.barang[i].harga_barang}')
        else:
            print('Tidak ada barang di keranjang!')

    def menghitungTotalBarang(self):
        """function ini digunakan untuk menghitung total harga barang"""
        pass
        total = 0
        for item in self.barang:
            total = item.harga_barang + total
        print(f'Total belanja: Rp {total}.00')


    def user_interface(self):
        """function ini digunakan untuk menyimpan interface menu"""
        while True:
            print(' ')
            print('Selamat Datang di Keranjang Belanja Toko Makmur!')
            print(' ')
            print('Menu:') 
            print('1. Menambah Barang')
            print('2. Hapus Barang')
            print('3. Tampilkan Barang di Keranjang')
            print('4. Lihat Total Belanja')
            print('5. Exit')
            print(' ')

            pilihan = int(input('Pilihan: '))
            if pilihan == 1:
                nama = str(input('Masukan nama barang: '))
                harga = int(input('Masukan harga: '))
                item = CartItem(nama, harga)
                self.menambah_barang(item)
            elif pilihan == 2:
                nama = input('Masukan nama barang yang ingin dihapus: ')
                self.menghapus_barang(nama)
                print(f'Barang "{nama}" berhasil dihapus di keranjang belanja.')
            elif pilihan == 3:
                print('Barang di keranjang: ')
                self.menampilkan_barang()
            elif pilihan == 4:
                self.menghitungTotalBarang()
            elif pilihan == 5:
                print('Sampai Jumpa! Terimakasih sudah belanja di Toko Makmur.')
                break
            else:
                print('Pilihannya salah. Coba lagi ya.')

if __name__ == "__main__":
     cart = ShoppingCart()
     cart.user_interface()
 