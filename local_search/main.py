from local_search.bruteforce import BruteForce
from local_search.stochastic import Stochastic


def main():
    brutef = BruteForce()
    print(brutef.max(), '\n')
    stochf = Stochastic()
    print(stochf.max(), '\n')


if __name__ == '__main__':
    main()
