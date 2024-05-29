import qrcode
def generate_qrcode(url):
    qr = qrcode.Qrcode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    qr.add_data(url)
    qr.make(Fit = True)


    my_code= qr.make_image(Fill_colors="black", back_color="white")
    my_code.save("my_qrcode.png")
    my_code.show()


if __name__ == "__main__":
    website_url = "https://www.instagram.com/santosh_paudel01/"

    generate_qrcode(website_url)
    print(f"QR code for '{website_url}'")    