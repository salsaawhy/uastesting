import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver untuk Selenium Grid
    options = Options()
    options.add_argument("--headless")  # Agar berjalan di GitHub Actions (headless)
    driver = webdriver.Remote(
        command_executor='http://selenium-grid-hub:4444/wd/hub',  # URL Hub
        options=options,
        keep_alive=True  # Agar WebDriver tetap hidup
    )
    yield driver
    driver.quit()


# Test 1: Test Login Valid
def test_valid_login(driver):
    driver.get("http://localhost/uas/login.php")
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("nimda666!")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    assert "index.php" in driver.current_url
    print("Login berhasil!")


# Test 2: Test Login Invalid Password
def test_invalid_password(driver):
    driver.get("http://localhost/uas/login.php")
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("wrongpassword")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    try:
        error_message = driver.find_element(By.XPATH, "//label[contains(text(), 'Damn, wrong credentials!!')]").text
    except:
        error_message = ""
    assert "Damn, wrong credentials!!" in error_message
    print("Pesan error muncul: Password salah")


# Test 3: Test Login Empty Fields
def test_empty_fields(driver):
    driver.get("http://localhost/uas/login.php")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)
    assert "login.php" in driver.current_url
    print("Tetap di halaman login karena field kosong.")


# Test 4: Test Delete Button
def test_delete_button(driver):
    driver.get("http://localhost/uas/index.php")
    try:
        delete_button = driver.find_element(By.XPATH, "//a[contains(@href, 'delete.php?id=')]")
        delete_button.click()
        alert = driver.switch_to.alert
        print("Tombol Delete ditekan, muncul konfirmasi: ", alert.text)
        alert.dismiss()  # Batal menghapus
        print("Penghapusan dibatalkan.")
    except Exception as e:
        print("Gagal menekan tombol Delete:", e)


# Test 5: Test Edit Button
def test_edit_button(driver):
    driver.get("http://localhost/uas/index.php")
    try:
        edit_button = driver.find_element(By.XPATH, "//a[contains(@href, 'update.php?id=')]")
        edit_button.click()
        print("Tombol Edit berhasil ditekan.")
        time.sleep(2)  # Tunggu sebelum kembali ke halaman utama
        driver.back()
    except Exception as e:
        print("Gagal menekan tombol Edit:", e)

