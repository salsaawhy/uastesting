from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Mengatur WebDriver untuk terhubung dengan Selenium Grid
options = Options()
options.add_argument("--headless")  # Agar berjalan di GitHub Actions (headless)

# Pengaturan untuk Selenium Grid
driver = webdriver.Remote(
    command_executor='http://selenium-grid-hub:4444/wd/hub',  # URL Hub
    options=options,
    keep_alive=True  # Agar WebDriver tetap hidup
)

class TestLogin(unittest.TestCase):
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
