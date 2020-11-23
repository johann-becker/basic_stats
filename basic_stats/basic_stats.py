# This Function runs basic stats on a list input. It will return the mean, stdev, and a histogram of the input list.
def basic2(x):
    import matplotlib.pyplot as plt
    n = len(x)
    # Determine the mean of the input list
    meani = []  # create empty variable
    for i in x:
        meani.append(i / n)  # Add answer to meani
    mean = sum(meani)
    print("The mean is:", mean)

    # Determine the standard deviation of input list
    sqdif = []  # empty variable
    for i in x:
        sqdif.append((i - mean) ** 2)  # Add result for x in xlist to sqdif
    stdev = (sum(sqdif) / (n - 1)) ** (1 / 2)

    print("The Standard Deviation is:", stdev)

    # Plot histogram of input data
    plt.hist(x)

    return mean, stdev