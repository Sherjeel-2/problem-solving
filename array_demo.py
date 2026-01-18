#!/usr/bin/env python3

def demo_list_basic():
    a = [10, 20, 30]
    print("original:", a)
    print("index 1:", a[1])
    a[1] = 25
    print("after update:", a)
    a.append(40)
    a.insert(0, 5)
    print("after append/insert:", a)
    a.pop()       # remove last
    a.pop(0)      # remove first
    print("after pops:", a)
    print("length:", len(a))
    print("slice [1:3]:", a[1:3])
    for i, v in enumerate(a):
        print("  idx", i, "value", v)

def demo_search_sort():
    b = [3, 1, 4, 1, 5, 9, 2]
    print("\nunsorted:", b)
    print("contains 5:", 5 in b)
    print("index of 4:", b.index(4))
    print("sorted (new):", sorted(b))
    b.sort(reverse=True)
    print("in-place sort desc:", b)
    print("min,max:", min(b), max(b))

def demo_multidim():
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print("\nmatrix:", m)
    print("row 1:", m[1])
    print("element (2,2):", m[2][2])
    print("traverse:")
    for r in m:
        for c in r:
            print(c, end=" ")
        print()

def demo_typed_array():
    import array
    t = array.array('i', [1, 2, 3])
    print("\ntyped array (int):", t.tolist())
    t.append(4)
    print("after append:", t.tolist())

def demo_dynamic_resize():
    a = []
    print("\ndynamic resize (append):")
    for i in range(8):
        a.append(i)
        print("  appended", i, "len=", len(a))

def main():
    demo_list_basic()
    demo_search_sort()
    demo_multidim()
    demo_typed_array()
    demo_dynamic_resize()

if __name__ == "__main__":
    main()
