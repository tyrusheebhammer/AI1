from queue import Queue

def main():
    myq = Queue()
    myq.put(5)
    print(myq.get())
    pass


if __name__ == '__main__':
    main()