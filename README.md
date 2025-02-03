# NanoWorks

NanoWorks is a Python utility designed to scan and report on disk health for Windows systems. It provides preemptive alerts to help users address potential disk failures before they occur.

## Features

- Scans all available disk drives on a Windows system.
- Reports the SMART status of each drive.
- Provides alerts if any drives show signs of potential failure.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Clone this repository to your local machine.
2. Ensure Python is installed and added to your system PATH.

## Usage

1. Navigate to the directory containing `nanoworks.py`.
2. Run the script using the command:
   ```bash
   python nanoworks.py
   ```
3. The script will display the health status of each drive and provide alerts for any drives that may be failing.

## Limitations

- This tool is only compatible with Windows operating systems.
- It relies on SMART status, which may not be available on all drives or systems.

## License

This project is licensed under the MIT License.

## Disclaimer

NanoWorks is provided "as-is" without any guarantees. Use at your own risk. Always ensure your data is backed up regularly.