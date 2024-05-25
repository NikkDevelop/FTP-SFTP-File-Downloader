# FTP/SFTP File Downloader with Automatic Deletion

## Description

This project is a Python script designed to automatically download files from an FTP/SFTP server, save them to a local directory, and then delete the files from the server. Initially created for transferring files from a phone-hosted FTP/SFTP server, it can be used in any context requiring automated file management from a remote server.

## Features

- Supports both FTP and SFTP protocols for secure file transfers.
- Configurable via a `config.ini` file and environment variables for sensitive information.
- Logs all activities, including successful file transfers and any errors encountered.
- Runs continuously, checking the server at regular intervals for new files to download and delete.

## Usage Instructions

### Prerequisites

- Python 3.x
- Required Python packages: `paramiko`, `python-dotenv`

### Installation

1. **Clone the Repository**:
   ```sh
   https://github.com/NikkDevelop/FTP-SFTP-File-Downloader.git
   cd ftp-sftp-file-downloader
   ```
2. **Install Dependencies**:
Make sure you have Python installed. Then, install the required libraries:
```sh
pip install paramiko python-dotenv
```
3. **Configuration**:
`Environment Variables`:
Create a file named .env in the project directory and add your FTP/SFTP username and password:
```.env
FTP_USER=your_username
FTP_PASS=your_password
```
`Config File`:
Create a file named `config.ini` in the project directory with the following content:
```config.ini
[FTP]
# The hostname or IP address of the FTP/SFTP server
host = 192.168.1.1

# The port number to connect to on the FTP/SFTP server
# Default port for FTP is 21 and for SFTP is 22
port = 22

# The directory on the FTP/SFTP server to monitor for files
directory = /

use_sftp = true  # Set to true to use SFTP, false for FTP

[LOCAL]
# The local directory where files from the FTP/SFTP server will be saved
directory = C:\\photo

[GENERAL]
# The interval in seconds to wait between checks for new files on the FTP/SFTP server
check_interval = 30
```
4. **Run the Script**:
Execute the script to start downloading files:
```sh
python ftp_download_and_delete.py
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

