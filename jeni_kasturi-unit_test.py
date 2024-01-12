import unittest 
from jeni_kasturi_app import CartItem, ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        '''function ini digunakan untuk set up cart''' 
        self.cart = ShoppingCart()

    def test_menambah_barang(self):
        '''function ini digunakan untuk testing menambah barang '''
        item = CartItem("Apel", 3200)
        self.cart.menambah_barang(item)
        self.assertEqual(len(self.cart.barang), 1)

    def test_menghapus_barang(self):
        '''function ini digunakan untuk mengetes function menghapus barang'''
        item = CartItem("Apel", 3200)
        self.cart.menghapus_barang(item)
        self.assertEqual(len(self.cart.barang), 0)

    def test_menghitungTotalBarang(self):
        '''function ini digunakan untuk mengetes function menghitung total barang'''
        self.assertEqual(self.cart.menghitungTotalBarang(), None)

if __name__ == "__main__":
    unittest.main()
    
