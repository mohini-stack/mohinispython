import sys;
config_file=sys.argv[1]
def file_list(config_file):
    f=open(config_file)
    files=print(f.readlines())
    f.close()
    print(files)