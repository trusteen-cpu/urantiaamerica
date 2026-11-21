import sys
n=int(sys.argv[1]); L=open("QUEUE.txt",encoding="utf-8").read().splitlines()
print("\n".join(L[:n])); open("QUEUE.txt","w",encoding="utf-8").write("\n".join(L[n:])+"\n")
