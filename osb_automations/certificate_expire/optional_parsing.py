import argparse
import pathlib
import glob
import os


CONGIF_FILE="/opt/SP/home/test/Final/mohini/file/certs/ssl_config.txt"
NOT_NEEDED_JKS="/opt/SP/home/test/Final/mohini/file/certs/not_needed_cert.txt"
LIST_OF_FILES=[]
certs=['*.crt','*.jks']
parser = argparse.ArgumentParser()
parser.add_argument("--search_path", action='store',
                    dest='SEARCH_PATH',
                    help='Stores default search path')
parser.add_argument("--dafault_jks_pass", action='store',
                    dest='DEFAULT_JKS_PASS',
                    help='Stores default JKS password')
parser.add_argument("--cert_types", action='store',
                    dest='CERT_TYPES',
                    help='Stores default CERT types')


results = parser.parse_args()
SEARCH_PATH=results.SEARCH_PATH
DEFAULT_JKS_PASS=results.DEFAULT_JKS_PASS
CERT_TYPES=results.CERT_TYPES
certs=(results.CERT_TYPES).split(",")



def files_list():
    FILES=[]

    for files in list(certs):
        print("[INFO]Current path is"+os.getcwd())

        files="*."+files
        print("File types :" + files)
        for txt_file in pathlib.Path().glob(files):
            print("Text File  :  "+str(txt_file))
            FILES.append(str(txt_file))

files_list()



