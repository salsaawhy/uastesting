from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Konfigurasi WebDriver untuk Selenium Grid (menggunakan Docker)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Pastikan menggunakan URL yang mengarah ke Selenium Grid yang berjalan di localhost:4444
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',  # URL Selenium Grid di Docker
    options=options
)

# Buka halaman index.php
driver.get("http://localhost/uas/index.php")

time.sleep(2)  # Tunggu sebentar agar halaman dimuat sepenuhnya

# Login jika diperlukan
try:
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    username_input.send_keys("admin")  # Ganti dengan username yang benar
    password_input.send_keys("nimda666!")  # Ganti dengan password yang benar
    login_button.click()
    time.sleep(2)  # Tunggu setelah login
except:
    print("Sudah login atau tidak memerlukan login.")

# Uji tombol Edit (Update)
try:
    edit_button = driver.find_element(By.XPATH, "//a[contains(@href, 'update.php?id=')]" )
    edit_button.click()
    print("Tombol Edit berhasil ditekan.")
    time.sleep(2)  # Tunggu sebelum kembali ke halaman utama
    driver.back()
except Exception as e:
    print("Gagal menekan tombol Edit:", e)

# Uji tombol Delete
try:
    delete_button = driver.find_element(By.XPATH, "//a[contains(@href, 'delete.php?id=')]" )
    delete_button.click()
    alert = driver.switch_to.alert
    print("Tombol Delete ditekan, muncul konfirmasi: ", alert.text)
    alert.dismiss()  # Batal menghapus
    print("Penghapusan dibatalkan.")
except Exception as e:
    print("Gagal menekan tombol Delete:", e)

# Tutup browser setelah beberapa detik
time.sleep(3)
driver.quit()
