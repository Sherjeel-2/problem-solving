import array

def demo_list():
    print("Python list (dynamic array) demo")
    a = [10, 20, 30]                 # creation
    print("initial:", a)

    a.append(40)                     # append
    print("after append(40):", a)

    a.insert(1, 15)                  # insert at index
    print("after insert(1,15):", a)

    a.remove(20)                     # remove by value
    print("after remove(20):", a)

    popped = a.pop()                 # pop last
    print("popped:", popped, "->", a)

    print("index of 15:", a.index(15))# search (raises if not found)
    print("slice a[1:3]:", a[1:3])    # slicing (O(k))

    a.extend([50, 60])               # extend multiple values
    print("after extend([50,60]):", a)

    a.sort()                         # in-place sort
    print("after sort():", a)

    print("traverse:")
    for i, v in enumerate(a):
        print(f"  idx={i}, val={v}")

def demo_typed_array():
    print("\narray.array (typed contiguous array) demo")
    ai = array.array('i', [1, 2, 3])  # 'i' = signed int
    print("initial:", ai.tolist())

    ai.append(4)
    print("after append(4):", ai.tolist())

    ai.insert(2, 99)
    print("after insert(2,99):", ai.tolist())

    val = ai.pop(1)
    print("popped index 1:", val, "->", ai.tolist())

    try:
        ai.remove(999)               # remove raises ValueError if not found
    except ValueError:
        print("remove(999) -> not found")

    print("final (as list):", ai.tolist())

if __name__ == "__main__":
    demo_list()
    demo_typed_array()