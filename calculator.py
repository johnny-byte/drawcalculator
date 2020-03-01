from decimal import Decimal


class S(object):

    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __gt__(self, other):
        if other.start < self.start:
            return True

        if other.start == self.start and other.end != self.end:
            raise Exception("Substring error")  # it must not be

    def __str__(self):
        return "start = {}, end = {}".format(self.start, self.end)


def foo():
    s = "((54 * 3)) + 34 + 75 + ( 76 + 58 + (78 / 2))"

    # lbc: int = None  # left bracket counter
    # rbc: int = None  # right bracket counter

    lbp = []  # left bracket position
    rbp = []  # right bracket position

    ret = []

    for i in range(len(s)):
        if s[i] == '(':
            # lbc = lbc + 1 if lbc is not None else 1
            lbp.append(i)
        elif s[i] == ')':
            # rbc = rbc + 1 if rbc is not None else 1
            # lbc=lbc-1

            # rbp.append(i)

            ret.append(S(lbp.pop(), i))

    # print(lbc)
    # print(lbp)
    # print(rbc)
    # print(rbp)
    print(ret)


if __name__ == "__main__":
    print("MAIN")
    foo()
