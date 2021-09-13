#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_arguments = len(argv[1:])
    args = argv[1:]
    count = len(args)

    print("{} {}{}".format(count, "argument" if count == 1 else "arguments",
                           ":" if count > 0 else "."))
    for num_list, arg_list in enumerate(args):
        print("{}: {}".format(num_list + 1, arg_list))
