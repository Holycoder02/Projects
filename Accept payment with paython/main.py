import qrcode

#Taking upi id as input from user
upi_id = input("Enter your upi id: ")

#upi://pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESsAGE

#defining the payment url based on the upi ID and the payment app
#you can modify these url based on the payment app you want to use

phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR Codes for each payment app

phonepe_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

#Save the QR code as image file(optional)
# phonepe_qr.save("phonepe_qr.png")
# paytm_qr.save("paytm_qr.png")
# googlepay_qr.save("googlepay_qr.png")

#Dispaly the qr coddes (you may need to install pillow/PIL libary) 
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()


