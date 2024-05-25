import os
import paramiko
import logging
from datetime import datetime
import time
from dotenv import load_dotenv
import configparser

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(filename='ftp_downloader.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    encoding='utf-8')

# Load configuration from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# FTP/SFTP server and local storage settings
ftp_host = config['FTP']['host']
ftp_port = int(config['FTP']['port'])
ftp_user = os.getenv('FTP_USER')
ftp_pass = os.getenv('FTP_PASS')
ftp_directory = config['FTP']['directory']
local_directory = config['LOCAL']['directory']
check_interval = int(config['GENERAL']['check_interval'])
use_sftp = config.getboolean('FTP', 'use_sftp', fallback=False)

# Function to download and delete files using SFTP
def download_and_delete_files_sftp():
    try:
        logging.info(f'Connecting to SFTP server: {ftp_host} on port {ftp_port}')
        transport = paramiko.Transport((ftp_host, ftp_port))
        transport.connect(username=ftp_user, password=ftp_pass)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.chdir(ftp_directory)

        files = sftp.listdir()

        for file_name in files:
            local_file_path = os.path.join(local_directory, file_name)

            sftp.get(file_name, local_file_path)
            sftp.remove(file_name)
            logging.info(f'Downloaded and deleted {file_name}')

        sftp.close()
        transport.close()
    except Exception as e:
        logging.error(f'SFTP error: {e}')

# Function to download and delete files using FTP
def download_and_delete_files_ftp():
    import ftplib
    try:
        logging.info(f'Connecting to FTP server: {ftp_host} on port {ftp_port}')
        ftp = ftplib.FTP()
        ftp.connect(ftp_host, ftp_port)
        ftp.login(ftp_user, ftp_pass)
        ftp.cwd(ftp_directory)

        files = ftp.nlst()

        for file_name in files:
            local_file_path = os.path.join(local_directory, file_name)

            with open(local_file_path, 'wb') as local_file:
                ftp.retrbinary('RETR ' + file_name, local_file.write)

            ftp.delete(file_name)
            logging.info(f'Downloaded and deleted {file_name}')

        ftp.quit()
    except ftplib.all_errors as e:
        logging.error(f'FTP error: {e}')

if __name__ == '__main__':
    while True:
        if use_sftp:
            download_and_delete_files_sftp()
        else:
            download_and_delete_files_ftp()
        logging.info(f'Waiting for {check_interval} seconds before next check...')
        time.sleep(check_interval)
