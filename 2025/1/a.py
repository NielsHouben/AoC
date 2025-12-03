# FILENAME = "example-input.txt"
FILENAME = "puzzle-input.txt"


class Lock:
    dial = 50
    n_zeroes = 0

    def tick(self, step):
        self.dial += step
        self.dial = self.dial % 99 - self.dial // 99
        self.dial = self.dial % 99 - self.dial // 99  # again because initial adjustment might place it outside of range
        self.n_zeroes += self.dial == 0


with open(FILENAME, "r") as input_file:
    lock = Lock()
    for line in input_file.read().split('\n')[:-1]:
        direction = 1 if line[0] == "R" else -1
        magnitude = int(line[1:])
        lock.tick(direction * magnitude)

    print(lock.n_zeroes)
