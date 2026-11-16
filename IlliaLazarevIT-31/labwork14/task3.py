import qrcode

NAME = "Illia Lazarev"
GROUP = "IT-31"

EMAIL = "lazarev.illia.2017@gmail.com"

print(f"{NAME}, {GROUP}")

# Формуємо інформацію для QR-коду
contact_info = f"{NAME}, {GROUP}, {EMAIL}"

# Генеруємо QR-код
image = qrcode.make(contact_info)

# Зберігаємо зображення
image.save("contact.png")

print("saved: contact.png")