from typing import Any, Dict
from copy import deepcopy


def op_one(values: Dict[int, int], index: int) -> None:
    values[values[index + 3]] = values[values[index + 1]] + values[values[index + 2]]


def op_two(values: Dict[int, int], index: int) -> None:
    values[values[index + 3]] = values[values[index + 1]] * values[values[index + 2]]


def write_output(input_file: str, result: Any) -> None:
    with open(f"{input_file}.out", "w") as output:
        print(result)
        output.write(f"{result}\n")


def extract_values(input_file: str) -> Dict[int, int]:
    with open(input_file, "r") as contents:
        lines = contents.readlines()
        values = dict()
        index = 0
        for line in lines:
            integers = line.strip().split(",")
            for integer in integers:
                if integer:
                    values[index] = int(integer.strip())
                    index += 1
        return values


def one(input_file: str) -> None:
    values = extract_values(input_file)
    index = len(values)
    values[1] = 12
    values[2] = 2
    length = index
    process_index = 0
    while process_index < length:
        if values[process_index] == 1:
            op_one(values, process_index)
        elif values[process_index] == 2:
            op_two(values, process_index)
        elif values[process_index] == 99:
            break
        else:
            raise NotImplementedError(f"{process_index}: {values[process_index]}")
        process_index += 4
    write_output(input_file, values[0])


def two(input_file: str) -> None:
    values = extract_values(input_file)
    length = len(values)
    noun = 1
    verb = 0
    while True:
        local_values = deepcopy(values)
        local_values[1] = noun
        local_values[2] = verb
        process_index = 0
        while process_index < length:
            try:
                if local_values[process_index] == 1:
                    op_one(local_values, process_index)
                elif local_values[process_index] == 2:
                    op_two(local_values, process_index)
                elif local_values[process_index] == 99:
                    break
                else:
                    break
                process_index += 4
            except KeyError:
                break
        if local_values[0] == 19690720:
            return write_output(input_file, 100 * noun + verb)
        else:
            if noun <= 10000:
                noun += 1
            elif verb <= 10000:
                verb += 1
                noun = 0
            else:
                raise IndexError()


if __name__ == "__main__":
    one("./2.1")
    two("./2.2")
