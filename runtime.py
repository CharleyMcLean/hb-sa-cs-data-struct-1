# Discussion Questions

# 1. When calculating the Big O notation for a particular algorithm, it’s
# necessary to consider the length of time it takes for the algorithm to run as
# the algorithm’s workload approaches infinity. You can think of the workload as
# the number of tasks required to complete a job. What determines the workload
# of figuring out whether your box of animal crackers contains an elephant?

# If the workload is the number of tasks required to complete a job, it would
# be determined by the number of animal crackers in my box.


# 2. Order the following runtimes in descending order of efficiency (that is,
# fastest runtimes first, slowest last) as n approaches infinity:

# O(1), O(log n), O(n), O(n log n), O(n2), O(2n) (i.e. 2 to the n-th power)


############################################################################

def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [       O(n)        ]


    """

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [               ]

    """

    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [       O(n2)        ]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    for x in s:
        if -x in s:
            result.append([-x, x])

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [      O(n2)      ]

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y:
                result.append((x, y))
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [       O(n2)       ]

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y and (y, x) not in result:
                result.append((x, y))
    return result
