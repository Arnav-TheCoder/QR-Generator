import qrcode

def generate_qr():
    link = input("Enter the link you want to convert into a QR code: ").strip()
    if not link:
        print("Please enter a valid link.")
        return

    file_name = input("Enter a file name for the QR code (without extension): ").strip()
    if not file_name:
        file_name = "qr_code"

    img = qrcode.make(link)
    img.save(f"{file_name}.png")

    print(f"QR code saved as {file_name}.png")

if __name__ == "__main__":
    generate_qr()
