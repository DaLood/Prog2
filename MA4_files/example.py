from time import perf_counter as pc
from time import sleep as pause




def runner():
    print("Performing a costly function")
    pause(1)
    print("Function complete")


# if __name__ == "__main__":
#     start = pc()
#     runner()
#     end = pc()
#     print(f"Process took {round(end-start, 2)} seconds")
#
# if __name__ == "__main__":
#     start = pc()
#     for _ in range(10):
#         runner()
#     end = pc()
#     print(f"Process took {round(end - start, 2)} seconds")




# import multiprocessing as mp

# p1 = mp.Process(target=runner)
# p2 = mp.Process(target=runner)
#
# p1.start()
# p2.start()



# if __name__ == "__main__":
#     start = pc()
#     p1 = mp.Process(target=runner)
#     p2 = mp.Process(target=runner)
#     p1.start()
#     p2.start()
#     end = pc()
#     print(f"Process took {round(end-start, 2)} seconds")


# if __name__ == "__main__":
#     start = pc()
#     p1 = mp.Process(target=runner)
#     p2 = mp.Process(target=runner)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     end = pc()
#     print(f"Process took {round(end-start, 2)} seconds")



import concurrent.futures as future


# with future.ProcessPoolExecutor() as ex:
#     p1 = ex.submit(some_method, some_arg, some_other_arg, ...) # Starts first
#     p2 = ex.submit(some_method, some_arg, some_other_arg, ...) # Starts second
#     r1 = p1.result() # Program waits until p1 is complete before assigning r2
#     r2 = p2.result()
# print("all done") # Will be printed once all processes are completed




def runner(n):
    print(f"Performing costly function {n}")
    pause(n)
    return f"Function {n} has completed"


if __name__ == "__main__":
    start = pc()

    with future.ProcessPoolExecutor() as ex:
        p = [5, 4, 3, 2, 1]
        results = ex.map(runner, p)

        for r in results:
            print(r)

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")





