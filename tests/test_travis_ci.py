import scripts.travis_ci as travis_ci


def test_square_num():
    assert (travis_ci.square_num(2) == 4)
    assert (travis_ci.square_num(1) == 1)


def test_square_num_neg():
    assert (travis_ci.square_num(-3) == 9)


