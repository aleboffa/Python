# Write your solution here
def longest(strings: list):
    long=""
    for string in strings:
        if len(long) < len(string):
            long=string

    return long




if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))