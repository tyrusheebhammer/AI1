from testpackage import Sumclass as sc


def main():
    sumcl = sc.Sumclass()
    print(sumcl.i)
    for _ in range(10):
        sumcl.add1()
    pass


if __name__ == '__main__':
    main()