# funkcje

def skroc(x:int) -> int:
    if x < 10:
        return 0
    else:
        liczba = str(x)[:-1]
        # print(liczba)
        return int(liczba)

def dopisz(x:int) -> int:
    if x == 0:
        return 0
    else:
        return int(str(x)+"0")

def ostatnia(x: int) -> int:
    return int(str(x)[-1:])

# print(skroc(249))
#
# print(dopisz(29))
#
# print(ostatnia(307))
def f(a,b) -> int:
    if b == 0:
        w = 0
        return w
    k = ostatnia(b)
    w = f(a,skroc(b))
    w = dopisz(w)
    # print(w)
    while k > 0:
        w = w + a
        print("wykonano")
        k -= 1
    return w

#1.1 i 1.2.
# print(f(4,125))
# 42, 2 => 82
# 4, 125 => 500
# 103, 104 => 10712 -> wywola sie tyle ile b+1
# 987654321, 123456789 => 10 razy wywola sie

#1.3.
print(f(2024, 1000)) # raz sie wykona
f(2024, 1234) # wykona sie  10 razy