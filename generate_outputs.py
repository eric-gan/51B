NUM_PPL = 10 # set to number of people
NUM_BUS = 4 # set to number of buses

def partition(people):
    """
    Finds all partitions of a group of people

    param people: An iterable containing the names of the people to partition
    type people: __iter__
    """

    if len(people) == 1:
        yield [ people ]
        return

    first = people[0]
    for smaller in partition(people[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller

groups = list(range(1, NUM_PPL + 1))

for n, p in enumerate(partition(groups), 1):
    # p corresponds to an individual partition
    if len(p) == NUM_BUS:
        print(p)