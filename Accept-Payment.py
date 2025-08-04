import qrcode
from PIL import Image

# Taking UPI ID and amount as input
upi_id = input("Enter your UPI ID: ")
amount = input("Enter the amount (NPR): ")

# Define the payment URLs with NPR currency
esewa_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amount}&cu=NPR'
google_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amount}&cu=NPR'
fone_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amount}&cu=NPR'

# Create QR code for each payment app
esewa_qr = qrcode.make(esewa_url)
google_qr = qrcode.make(google_url)
fone_qr = qrcode.make(fone_url)

# Save the QR code to image file
esewa_qr.save('esewa_qr.png')
google_qr.save('google_qr.png')
fone_qr.save('fone_qr.png')

# Display the QR code (optional)
esewa_qr.show()
google_qr.show()
fone_qr.show()
