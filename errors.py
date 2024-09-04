class outOfBoundsError(Exception):
    def __init__(self, value, min, max) -> None:
        super().__init__(f"int: value is not in bounds {min}, {max}")