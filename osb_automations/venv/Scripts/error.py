import sys
import os
import logging

class LegacyError():
    def __init__():
        logging.info("Inside Init")
        print("Inside Init")
    def log_file_identification():
        logging.info("Lets do Log Identification")
        log_file="server.log"
        return log_file
    def extract_logs(log_file):
        logging.info("Lets extract logs")
        print(log_file)

if __name__=="__main__":
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Inside Init")
    lr=LegacyError()
    log_file =LR.log_file_identification()
    extract_logs(log_file)
