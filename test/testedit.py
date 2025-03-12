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

if __name__ == "__main__":
    unittest.main()
