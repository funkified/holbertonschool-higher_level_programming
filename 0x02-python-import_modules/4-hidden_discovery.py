#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name_list = dir(hidden_4)
    for i in name_list:
        if i[:2] != "__":
            print("{}".format(i))
