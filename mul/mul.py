import sys

def mul(x,y):
    print("mul: %d" % x*y)
    return x*y

def main():    
    if len(sys.argv) == 3:
        mul(int(sys.argv[1]),int(sys.argv[2]))
    else:
        print("ERROR:",str(len(sys.argv)-1)," arguments given instead of 2")

if __name__ == "__main__":
    main()
