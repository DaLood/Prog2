"""
Solutions to exam tasks for module 4.
"""

# A9
def matrix(x,n):
    """Method that returns a list of lists (with contents of each row of M),
    using a list comprehension"""
    return [[a**c for c in range(n)] for a in x]

# A10
def dice(n):
	"""Method thats simulates a broken dice. Do not modify."""
	from random import choice
	return [choice([1,2,3,4,5,5]) for _ in range(n)]


def dice_average():
    import concurrent.futures as future
    times = 20
    n_per = 100
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(dice, [n_per for i in range(times)])

    x = list(results)
    return sum(x[0])/len(x[0])



# B4
def thumbnail():
    """Method that creates thumbnails of all .png and .jpg images in 
    current directory, and saves them in a directory called 'thumb' 
    (created if it does not exist). Excution should be done in parallel."""
    pass # remove and write your code here

#-------------------------------
def main():
    print('Test of A9 ')
    x=[5, 1.5, 3]
    print(matrix(x,3))
    print(matrix(x,4))

    print('Test of A10 ')
    print(dice_average())
    # print('Test of B4 ')
    # thumbnail()



if __name__ == "__main__":
    main()