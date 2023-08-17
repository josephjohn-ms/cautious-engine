import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter year of publication: ")
    book_info = f"Title: {title}\nAuthor: {author}\nYear: {year}"
    
    file_name = "generated_qr_code.png"
    generate_qr_code(book_info, file_name)
    print(f"QR code saved as {file_name}")
