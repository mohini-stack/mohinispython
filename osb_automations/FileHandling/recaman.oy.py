import sys
from itertools import count,islice
def sequence():
    """Generate recamans sequence"""
    seen=set()
    a=0
    for n in count(1):
        print("Starting")
        yield a
        seen.add(a)
        print(type(seen))
        c=a-n
        if c<0 or c in seen:
            c=a+n
        a=c
        print("End")

def write_sequence(filename,num):
    """Write recmans sequence to a file"""
    f=open(filename,mode='wt',encoding='utf-8')
    f.writelines("{0}\n".format(r) for r in islice(sequence(),num+1))
    f.close()
if __name__=='__main__':
    write_sequence(sys.argv[1],int(sys.argv[2]))
