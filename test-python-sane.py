import sane
import os
import subprocess

def scan_image():
    # Initialize SANE
    sane.init()
    
    # List available scanners
    devices = sane.get_devices()
    if not devices:
        print("No scanners found.")
        return

    # Select the first available scanner
    scanner_name = devices[0][0]
    print(f"Using scanner: {scanner_name}")

    # Open the scanner
    scanner = sane.open(scanner_name)

    # Set scan parameters
    scanner.mode = 'color'  # or 'gray' for grayscale
    scanner.resolution = 300  # Set resolution in DPI

    # Start the scan
    print("Scanning...")
    image = scanner.scan()

    # Save the scanned image
    output_file = "scanned_image.png"
    image.save(output_file)
    print(f"Image saved as {output_file}")

    # Open the scanned image in Eye of GNOME
    subprocess.run(['eog', output_file])

if __name__ == "__main__":
    scan_image()

