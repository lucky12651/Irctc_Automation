# Train Booking System with Selenium

This repository contains a Python script that automates the process of searching and booking trains on the IRCTC website using Selenium and Google Cloud Vision API. The script helps users find available trains, choose a train, provide passenger details, and complete the booking process.

## Prerequisites

To use this script, you need to have the following installed on your system:

- Python (>=3.6)
- Google Cloud SDK
- Chrome WebDriver for Selenium

Also, make sure to replace the API key file path (`/Users/vaibhav/Desktop/python/advance-wavelet-385212-6e0fa109b948.json`) in the script with your own Google Cloud Vision API key.

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/train-booking-system.git
cd train-booking-system
```

2. Install the required Python libraries:

```bash
pip install selenium google-cloud-vision
```

3. Update the script with your IRCTC username and password:

```python
# Replace the empty strings with your IRCTC username and password
username = "your_username_here"
password = "your_password_here"
```

## How to Run

To run the train booking script, execute the following command:

```bash
python train_booking.py
```

The script will open a Chrome browser, log in to the IRCTC website, search for available trains, select a train, and proceed with the booking process. The user will need to provide the passenger name, age, and gender during the booking process.

Please note that the script uses Google Cloud Vision API to automatically detect and enter the CAPTCHA text during the booking process. Make sure you have the correct API key and access to the Vision API service.

## Important Note

This script is intended for educational purposes only and should be used responsibly. Automated access to websites might violate the website's terms of service or legal restrictions. Use this script at your own risk.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
