import argparse


def square_num(innum):
    """

    :param innum:
    :return:
    """
    return innum * innum


def arguments_parsing():
    """

    :return:
    """

    parser = argparse.ArgumentParser(description='testing.')
    parser.add_argument("--mojbroj", type=int,
                        help="display a given number")

    args = parser.parse_args()
    return args


def travis_ci():
    args = arguments_parsing()
    print(args.mojbroj)
    print(square_num(args.mojbroj))


if __name__ == '__main__':
    travis_ci()
