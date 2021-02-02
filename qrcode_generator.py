import pyqrcode
def qrcode_generator():
    x=input()
    qrcode_encrpy=pyqrcode.create(x)
    qrcode_encrpy.png("test.png",scale=6)
    print("Qrcode is generated successfully")
if __name__=="__main__":
    qrcode_generator()
    