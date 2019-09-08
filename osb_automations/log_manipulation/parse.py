import sys
import logging
"""Program to re-process payment bridge file"""

def main():
    try:
        logging.info("Payment bridge File {} is re-processed".format(sys.argv[1]))
    except IndexError:
        print("Usage is {} <file-name>".format(sys.argv[0]))
        sys.exit()
if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    logging.info("Running main Function")
    main()
