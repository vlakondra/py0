import src

def ff(n):
    print(src.a)
    print(n**2)
    with open('data/words.txt','r') as f:
        r=f.read()
    print(r)

print(__name__)
if __name__ =="__main__":
    ff(33)    