import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Mengatur WebDriver untuk terhubung dengan Selenium Grid
        options = Options()
        options.add_argument("--headless")  # Agar berjalan di GitHub Actions (headless)
        cls.driver = webdriver.Remote(
            command_executor='http://selenium-grid-hub:4444/wd/hub',  # URL Hub
            options=options,
            keep_alive=True  # Agar WebDriver tetap hidup
        )

    def test_valid_login(self):
        """Test login dengan kredensial yang benar."""
        driver = self.driver
        driver.get("http://localhost/uas/login.php")
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("nimda666!")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        self.assertIn("index.php", driver.current_url)
        print("Login berhasil!")

    def test_invalid_password(self):
        """Test login dengan password salah."""
        driver = self.driver
        driver.get("http://localhost/uas/login.php")
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

    def test_empty_fields(self):
        """Test login tanpa mengisi username dan password."""
        driver = self.driver
        driver.get("http://localhost/uas/login.php")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        self.assertIn("login.php", driver.current_url)
        print("Tetap di halaman login karena field kosong.")


if __name__ == "__main__":
    unittest.main()
