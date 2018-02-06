import os


def add_numbers(nbr_1, nbr_2):
    return nbr_1 + nbr_2


if __name__ == '__main__':
    nbr_1 = float(str(os.environ['nbr_1']))
    nbr_2 = float(str(os.environ['nbr_2']))

    print(add_numbers(nbr_1, nbr_2))
