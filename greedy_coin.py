import sys

def get_change(m):
    a=0
    a=int(m/5)
    m=m%10
    a=a+int(m/2)
    m=m%5
    m=a+m
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
#coin assumed to be 1, 2, 5
