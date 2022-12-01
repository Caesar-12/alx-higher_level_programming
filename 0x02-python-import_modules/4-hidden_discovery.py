#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    func_list = dir(hidden_4)

    for func in func_list:
        if func[0] != '_' and func[1] != '_':
            print("{:s}".format(func))
