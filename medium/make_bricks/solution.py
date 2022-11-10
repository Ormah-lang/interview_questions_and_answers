

# check if the sum of the small bricks given and the big bricks given is greater than or equal to goal
# check if goal modulo the size of big brick is less than or equal to the number of small blocks
# if yes - return True
# else - return False
def make_bricks(small, big, goal):
    small_size = 1
    big_size = 5
    if small_size * small + big_size * big >= goal:
        if goal % big_size <= small:
            return True
    return False


if __name__ == "__main__":
    # test cases
    print(make_bricks(3, 1, 8))

    print(make_bricks(3, 1, 9))

    print(make_bricks(3, 2, 10))

    print(make_bricks(6, 0, 11))