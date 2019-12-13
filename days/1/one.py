

def one(input_file: str) -> None:
    with open(input_file, "r") as contents:
        result = sum(map(lambda x: int(x) // 3 - 2, contents.readlines()))

    with open(f"{input_file}.out", "w") as output:
        print(result)
        output.write(f"{result}\n")


def two(input_file: str) -> None:
    def remaining(x: int):
        return x // 3 - 2

    with open(input_file, "r") as contents:
        result = 0
        for line in contents.readlines():
            value = int(line)
            partial = remaining(value)
            while partial > 0:
                result += partial
                partial = remaining(partial)

    with open(f"{input_file}.out", "w") as output:
        print(result)
        output.write(f"{result}\n")


if __name__ == "__main__":
    one("./1.1")
    two("./1.2")
