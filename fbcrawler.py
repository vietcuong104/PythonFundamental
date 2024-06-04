from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import os

# Khai báo đường dẫn đến thư mục lưu trữ ảnh
download_directory = "/Users/phamvietcuong/Downloads/enli"

# Khai báo đường dẫn đến trang album ảnh của Facebook
album_url = "https://www.facebook.com/profile.php?id=100010171150095&sk=photos_by"

# Khai báo thông tin đăng nhập của bạn
username = "0375235456"
password = "vlxx.xyz"

# Khởi tạo trình duyệt (ở đây là Chrome)
driver = webdriver.Chrome()

# Mở trang album ảnh
driver.get(album_url)

# Tìm các trường nhập liệu cho tên người dùng và mật khẩu và điền thông tin đăng nhập
username_input = driver.find_element(By.ID, "email")
username_input.send_keys(username)

password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(password)

# Submit thông tin đăng nhập
password_input.send_keys(Keys.ENTER)

# Đợi một khoảng thời gian để trang được tải hoàn toàn (có thể cần điều chỉnh thời gian chờ)
driver.implicitly_wait(1)



# Chờ một khoảng thời gian để trang được tải đúng cách
time.sleep(5)

# Lấy tất cả các thẻ ảnh trong album
images = driver.find_elements("xpath",'//div[contains( text( ), photo_str)]')
# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Lặp qua từng ảnh và tải xuống
for idx, image in enumerate(images):
    image_url = image.get_attribute('src')
    image_name = f"image_{idx}.jpg"
    image_path = os.path.join(download_directory, image_name)

    # Tải ảnh về máy
    response = requests.get(image_url)
    with open(image_path, 'wb') as f:
        f.write(response.content)

# Đóng trình duyệt
driver.quit()

print("Tải ảnh thành công!")
