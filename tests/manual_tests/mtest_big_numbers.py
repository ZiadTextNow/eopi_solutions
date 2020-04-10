if __name__ == '__main__':
    i = 0
    while True:
        try:
            print("num: %d" % (1 << (1 << i)))
        except OverflowError:
            print("max i was: %d" % i)
            break
        i += 1
