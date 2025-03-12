# test_cases.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class TestDelete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/uas/index.php")

    def test_delete_button(self):
        """Test tombol Delete."""
        driver = self.driver
        try:
            delete_button = driver.find_element(By.XPATH, "//a[contains(@href, 'delete.php?id=')]")
            delete_button.click()
            alert = driver.switch_to.alert
            print("Tombol Delete ditekan, muncul konfirmasi: ", alert.text)
            alert.dismiss()  # Batal menghapus
            print("Penghapusan dibatalkan.")
        except Exception as e:
            print("Gagal menekan tombol Delete:", e)

    def tearDown(self):
        self.driver.quit()


class TestEdit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/uas/index.php")

    def test_edit_button(self):
        """Test tombol Edit."""
        driver = self.driver
        try:
            edit_button = driver.find_element(By.XPATH, "//a[contains(@href, 'update.php?id=')]")
            edit_button.click()
            print("Tombol Edit berhasil ditekan.")
            time.sleep(2)  # Tunggu sebelum kembali ke halaman utama
            driver.back()
        except Exception as e:
            print("Gagal menekan tombol Edit:", e)

    def tearDown(self):
        self.driver.quit()


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/uas/login.php")

    def test_valid_login(self):
        """Test login dengan kredensial yang benar."""
        driver = self.driver
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("nimda666!")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(2)
        self.assertIn("index.php", driver.current_url)
        print("Login berhasil!")

    def tearDown(self):
        self.driver.quit()


class TestInvalidLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/uas/login.php")

    def test_invalid_password(self):
        """Test login dengan password salah."""
        driver = self.driver
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("wrongpassword")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(2)
        try:
            error_message = driver.find_element(By.XPATH, "//label[contains(text(), 'Damn, wrong credentials!!')]").text
        except:
            error_message = ""

        self.assertIn("Damn, wrong credentials!!", error_message)
        print("Pesan error muncul: Password salah")

    def tearDown(self):
        self.driver.quit()


class TestEmptyLoginFields(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/uas/login.php")

    def test_empty_fields(self):
        """Test login tanpa mengisi username dan password."""
        driver = self.driver
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(2)

        # Cek apakah masih di halaman login (karena browser menangani required)
        self.assertIn("login.php", driver.current_url)
        print("Tetap di halaman login karena field kosong.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
