class SudokuCell:
    def __init__(self, value: int) -> None:
        self.candidates = set([value]) if value else set(range(1, 10))
        self.solved = False
        self.value = None

    def solve(self):
        self.solved = True
        self.value = list(self.candidates)[0]

    def is_ready(self):
        return not self.solved and len(self.candidates) == 1

    def discard(self, value: int) -> None:
        self.candidates.discard(value)
        if not len(self.candidates):
            raise RuntimeError

    def discard_all_but(self, remaining_value: int) -> None:
        for value in self.candidates:
            if value == remaining_value:
                continue
            self.discard(value)
