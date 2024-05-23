
from machine import ADC, Pin
import time
import network
import urequests as requests

# Wi-Fi Configuration
SSID = 'your-SSID'
PASSWORD = 'your-PASSWORD'

# Initialize ADC
adc_current = ADC(Pin(26))  # Assuming ADC0 is on GPIO26
adc_voltage = ADC(Pin(27))  # Assuming ADC1 is on GPIO27

# Function to connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    while not wlan.isconnected():
        pass
    
    print('Connected to Wi-Fi')
    print('IP:', wlan.ifconfig()[0])

# Function to read current sensor value
def read_current():
    value = adc_current.read_u16()
    # Convert to current (use sensor's sensitivity)
    current = (value / 65535.0) * 5.0  # 5V ADC range
    current = (current - 2.5) / 0.066  # Sensitivity for ACS712-30A
    return current

# Function to read voltage sensor value
def read_voltage():
    value = adc_voltage.read_u16()
    # Convert to voltage (use sensor's sensitivity)
    voltage = (value / 65535.0) * 5.0  # 5V ADC range
    voltage = voltage * (330.0 / 3.0)  # Voltage divider ratio
    return voltage

# Function to calculate power
def calculate_power(voltage, current, power_factor=0.77):
    power = voltage * current * power_factor
    return power

# Function to send data to Google Drive
def send_data(data):
    url = "YOUR_GOOGLE_SHEET_API_URL"
    response = requests.post(url, json=data)
    return response.status_code

# Main loop
def main():
    connect_wifi()
    
    while True:
        voltage = read_voltage()
        current = read_current()
        power = calculate_power(voltage, current)
        
        data = {
            'voltage': voltage,
            'current': current,
            'power': power
        }
        
        status = send_data(data)
        print(f'Data sent with status code: {status}')
        
        time.sleep(60)  # Send data every 60 seconds

main()

