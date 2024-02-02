import copy
with open("3.txt") as f:
    b = f.read()

b = b.lower()

# task a)
def task_3_1(lst):
    b = copy.copy(lst)
    while True:
        prev = False
        next = True
        idx = b.find("one")
        if idx == -1:
            print("False")
            break
        if idx == 0:
            prev = True
            if not (b[idx+3].isalpha()):
                print("True")
                break
        
        if (not (b[idx+3].isalpha())) and (not b[idx-1].isalpha()):
            print("True")
            break
        
        b = b[:idx] + " " + b[idx+3:]
# task_a(b)

def task_3_2(inp):
    b = copy.copy(inp)
    abc = 0
    signs = 0
    c = 0
    for i in b:
        if i.isalpha():
            c +=1
        else:
            if c > 1:
                abc+=1
                c = 0

    for i in b:
        if i in "-*+":
            c +=1
        else:
            if c > 1:
                signs += 1
                c = 0
    

    print(abc, signs)

# task_3_2(b)

    
def alpha_counter(inp):
    b = copy.copy(inp)
    abc = 0
    c = 0
    for i in b:
        if i.isalpha():
            c +=1
        else:
            if c > 1:
                abc+=1
                c = 0
    return abc

def task_3_3(inp):
    b = copy.copy(inp)
    if alpha_counter(b)<2:
        return
    c = 0
    frst_ltr = True
    idx_1 = None
    len1 = 0
    idx_2 = None
    for n, i in enumerate(b):
        if i.isalpha():
            if frst_ltr:
                frst_ltr = False
                idx_1 = n
            c +=1
        else:
            if c > 1:
                # abc+=1
                len1 = c
                c = 0
                break
        if n == len(b) - 1:
            if c > 1:
                # abc+=1
                len1 = c
                c = 0
    b2 = b[idx_1+len1:]
    frst_ltr = True
    for n, i in enumerate(b2):
        if i.isalpha():
            if frst_ltr:
                frst_ltr = False
                idx_2 = n
            c +=1
        else:
            if c > 1:
                # abc+=1
                len2 = c
                c = 0
                break
        if n == len(b2) - 1:
            if c > 1:
                # abc+=1
                len2 = c
                c = 0
    
    repl = b[idx_1+len1:len(b[:idx_1+len1]) + idx_2].replace("+", "1").replace("-", "2").replace("*", "3")

    b = b[:idx_1+len1] + repl + b[len(b[:idx_1+len1]) + idx_2:]
    # закоментировано т.к. меняет файл и тестить неудобно
    # with open("3.txt", "w") as f:
    #     f.write(b)
# task_3_3(b)

def task3_4(inp):
    b = copy.copy(inp)
    if alpha_counter(b)<3:
        return
    c = 0
    frst_ltr = True
    idx_1 = None
    len1 = 0
    idx_2 = None
    len2 = 0
    idx_3 = None
    len3 = 0
    for n, i in enumerate(b):
        if i.isalpha():
            if frst_ltr:
                frst_ltr = False
                idx_1 = n
            c +=1
        else:
            if c > 1:
                # abc+=1
                len1 = c
                c = 0
                break
        if n == len(b) - 1:
            if c > 1:
                # abc+=1
                len1 = c
                c = 0
    b2 = b[idx_1+len1:]
    frst_ltr = True
    for n, i in enumerate(b2):
        if i.isalpha():
            if frst_ltr:
                frst_ltr = False
                idx_2 = n
            c +=1
        else:
            if c > 1:
                # abc+=1
                len2 = c
                c = 0
                break
        if n == len(b2) - 1:
            if c > 1:
                # abc+=1
                len2 = c
                c = 0
    prev1 = len(b[:idx_1+len1])
    b3 = b[prev1 + idx_2 + len2:]
    frst_ltr = True
    for n, i in enumerate(b3):
        if i.isalpha():
            if frst_ltr:
                frst_ltr = False
                idx_3 = n
            c +=1
        else:
            if c > 1:
                # abc+=1
                len3 = c
                c = 0
                break
        if n == len(b3) - 1:
            if c > 1:
                # abc+=1
                len3 = c
                c = 0
    prev2 = len(b[:prev1 + idx_2 + len2])
    all = (
    b[idx_1: idx_1 + len1] + 
    b[prev1 + idx_2: prev1 + idx_2 + len2] +
    b[prev2 + idx_3: prev2 + idx_3 + len3]
    )
    return all.count("f")

print(task3_4(b))