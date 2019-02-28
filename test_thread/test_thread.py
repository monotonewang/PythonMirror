import _thread


def print_time(thread_name, delay):
    print("%s,%s" % (thread_name, delay))


_thread.start_new_thread(print_time, ("Thread-2", 4,))

# _thread.start_new_thread(print_time)

# _thread.start_new_thread(print_time("x", 1),("a","b"))
