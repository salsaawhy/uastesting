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

if __name__ == "__main__":
    unittest.main()
