import os
import qrcode

def create_qr_code(link, folder_name="QR Links"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    file_name = os.path.join(folder_name, f"{link.replace('://', '_').replace('/', '_')}.png")
    qr_img.save(file_name)
    print(f"QR code saved to {file_name}")

if __name__ == "__main__":
    link = input("Enter the link: ").strip()

    if not link:
        print("Please enter a valid link.")
    else:
        create_qr_code(link)
