# FILENAME = "example-input copy.txt"
FILENAME = "puzzle-input.txt"


class Lock:
    dial = 50
    n_zeroes = 0

    def tick(self, direction):
        self.dial += direction
        if self.dial == -1:
            self.dial = 99
        if self.dial == 100:
            self.dial = 0
        if self.dial == 0:
            self.n_zeroes += 1

    def turn(self, steps, direction):
        print(f" | {self.dial:3}", end="")
        for _ in range(steps):
            self.tick(direction)
        print(f" -> {self.dial:3} | ", end="")
        print(self.n_zeroes)


with open(FILENAME, "r") as input_file:
    lock = Lock()
    for line in input_file.read().split('\n')[:-1]:
        direction = 1 if line[0] == "R" else -1
        magnitude = int(line[1:])
        print(f"{line:4}", end="")
        lock.turn(magnitude, direction)

    print(lock.n_zeroes)
