# Payment QR Code Generator 💳

A Python application that generates QR codes for UPI (Unified Payments Interface) payment methods, enabling easy payment collection through multiple payment apps.

## Features

- 💰 **Multiple Payment Apps** - Support for PhonePe, Paytm, and Google Pay
- 📱 **QR Code Generation** - Automatic QR code creation from UPI IDs
- 👁️ **Visual Display** - Display QR codes on screen for immediate scanning
- 💾 **File Saving** - Optional saving of QR codes as image files
- 🔐 **UPI Standard** - Uses official UPI URL schema for compatibility
- 🛒 **Merchant Code** - Customizable merchant identification

## Requirements

- Python 3.6 or higher
- qrcode library with PIL support
- pillow (PIL) library for image handling

## Installation

### Step 1: Install Dependencies

```bash
pip install qrcode[pil]
pip install pillow
```

### Step 2: Navigate to Project Folder

```bash
cd "Accept payment with paython"
```

### Step 3: Run the Application

```bash
python main.py
```

## Usage

### Starting the Application

Run the script and enter your UPI ID when prompted:

```
Enter your upi id: yourname@bank
```

### Supported UPI Providers

The application generates QR codes for:

1. **PhonePe** - India's leading UPI app
2. **Paytm** - Multi-purpose payment platform
3. **Google Pay** - Google's payment solution

All three QR codes will be displayed in separate windows.

## UPI ID Format

A valid UPI ID consists of:
- **Username**: Your payment identifier
- **@**: The @ symbol
- **Bank/Provider**: Your bank or payment provider code

### Examples
```
john.doe@hdfcbank
merchant@paytm
business@okhdfcbank
user@ibl
```

### Common UPI Providers
- `@hdfcbank` - HDFC Bank
- `@icici` - ICICI Bank
- `@ibl` - ICICI Bank (alternate)
- `@okhdfcbank` - HDFC Bank (alternate)
- `@paytm` - Paytm Payments Bank
- `@upi` - Generic UPI
- `@sbi` - State Bank of India

## UPI URL Schema

The application uses the standard UPI URL format:

```
upi://pay?pa={UPI_ID}&pn={Recipient_Name}&mc={Merchant_Code}
```

### Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `pa` | Payee Address (UPI ID) | `merchant@bank` |
| `pn` | Payee Name | `John's Business` |
| `mc` | Merchant Category Code | `1234` |

## Example Workflow

```
1. Run python main.py
2. Enter UPI ID: business@hdfcbank
3. Three QR codes are generated and displayed
4. Users can scan with any payment app
5. Optionally save QR codes to disk
```

## Customization

### Modify Recipient Name

Edit the `main.py` file and change the recipient name:

```python
phonepay_url = f'upi://pay?pa={upi_id}&pn=Your Business Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Your Business Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Your Business Name&mc=1234'
```

### Modify Merchant Code

Update the merchant category code (MCC):

```python
# Change 1234 to your actual merchant code
phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20name&mc=YOUR_CODE'
```

### Save QR Codes to Files

Uncomment the save lines in the code:

```python
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
googlepay_qr.save("googlepay_qr.png")
```

This will save the QR codes as PNG image files in your project directory.

## Technical Details

### How QR Codes Work

1. **Input**: UPI ID from user
2. **URL Generation**: Create UPI URL with parameters
3. **Encoding**: Encode URL into QR code format
4. **Display**: Show QR code image on screen
5. **Reading**: Users scan with payment app

### QR Code Format

- **Type**: QR Code (2D barcode)
- **Content**: UPI payment URL
- **Resolution**: Suitable for smartphone scanning
- **Format**: PNG image (when saved)

## Payment Flow

When users scan the QR code:

```
Scan QR Code → Payment App Opens → Amount & Confirmation → Payment Complete
```

## Example Setup for Business

```python
# Customize for your business
upi_id = input("Enter your upi id: ")  # businessname@hdfcbank

# Generate codes with your business info
phonepay_url = f'upi://pay?pa={upi_id}&pn=John\'s%20Store&mc=5411'
paytm_url = f'upi://pay?pa={upi_id}&pn=John\'s%20Store&mc=5411'
googlepay_url = f'upi://pay?pa={upi_id}&pn=John\'s%20Store&mc=5411'
```

## Best Practices

- ✅ Use your business UPI ID for receiving payments
- ✅ Keep merchant code updated and accurate
- ✅ Display QR codes at checkout or payment point
- ✅ Test with actual payment apps before deployment
- ✅ Save QR codes for print materials or digital sharing
- ❌ Don't share UPI IDs publicly without proper security
- ❌ Don't use test UPI IDs in production

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'qrcode'"
- **Solution**: Install with `pip install qrcode[pil]`

### Issue: "No module named 'PIL'"
- **Solution**: Install pillow with `pip install pillow`

### Issue: QR code window doesn't appear
- **Solution**: Ensure pillow is installed correctly
- **Solution**: Check that PIL is working: `python -c "from PIL import Image"`

### Issue: Invalid UPI ID error
- **Solution**: Verify UPI ID format (username@provider)
- **Solution**: Check that you're using a valid UPI provider code

## Use Cases

### Retail & Stores
- Display at checkout counter
- Print for physical signage
- Include in receipts

### Online Businesses
- Website payment integration
- Email payment links
- Invoice attachments

### Services
- Salon/Spa payment collection
- Tuition fees
- Professional services

### Events
- Conference registration payments
- Ticket sales
- Donation collection

### Street Vendors
- Small business payments
- Market stall transactions
- Quick payment collection

## Security Notes

- UPI URLs are safe to share (no sensitive data)
- Users control the payment amount
- QR codes are valid indefinitely
- Merchant code is publicly visible
- Always validate received payments

## Merchant Category Codes (MCC) Examples

| Code | Category |
|------|----------|
| 5411 | Grocery stores |
| 5411 | Supermarkets |
| 5812 | Restaurants |
| 5999 | Miscellaneous retail |
| 7298 | Laundry services |
| 8211 | Education |

## Integration Tips

### For Websites
```html
<img src="phonepe_qr.png" alt="PhonePe Payment">
Scan to pay via PhonePe
```

### For Print Materials
Save QR codes and include in:
- Flyers
- Posters
- Business cards
- Invoices

## Version
1.0

## License
Free to use and modify

## Support
For issues or questions about UPI payments, visit:
- [NPCI - UPI Documentation](https://www.npci.org.in/)
- [PhonePe Merchant](https://merchantonboarding.phonepe.com/)
- [Google Pay UPI](https://pay.google.com/intl/en_in/)
