class Transformation:

    def __init__(self, start: int, end: int, add: int):
        self.start = start
        self.end = end
        self.add = add

    def contains(self, value: int) -> bool:
        return self.start <= value <= self.end

    def apply(self, value: int) -> int:
        if self.contains(value):
            return value + self.add
        else:
            return value

    def is_overlapping(self, other) -> bool:
        return self.start <= other.end and other.start <= other.end

    def is_inside(self, other) -> bool:
        return other.start < self.start and self.end < other.end

    def merge(self, other) -> list:
        if not self.is_overlapping(other):
            return [self, other]
        # case 2
        if self.is_inside(other):
            return other.merge(self)
        # case 3
        if other.is_inside(self):
            left = Transformation(self.start, other.start-1, self.add)
            merged = Transformation(other.start, other.end, self.add + other.add)
            right = Transformation(other.end + 1, self.end, self.add)
            return [left, merged, right]

        if self.start == other.start:
            if self.end == other.end:
                # case 1
                return [Transformation(self.start, self.end, self.add + other.add)]
            if other.end < self.end:
                # case 4
                left = Transformation(self.start, other.end, self.add + other.add)
                right = Transformation(other.end+1, self.end, self.add)
                return [left, right]
            if self.end < other.end:
                # case 8
                left = Transformation(self.start, self.end, self.add + other.end)
                right = Transformation(self.end+1, other.end, other.add)
                return [left, right]
        if self.end == other.end:
            # case 5
            left = Transformation(self.start, other.start-1, self.add)
            right = Transformation(other.start, self.end, self.add + other.add)
            return [left, right]
        if other.start < self.start:
            left = Transformation(other.start, self.start - 1, other.add)
            if self.end == other.end:
                # case 9
                right = Transformation(self.start, self.end, self.add + other.add)
                return [left, right]
            # case 6
            mid = Transformation(self.start, other.end, self.add + other.add)
            right = Transformation(other.end + 1, self.end, self.add)
            return [left, mid, right]
        if self.start < other.start:
            # case 7
            left = Transformation(self.start, other.start-1, self.add)
            mid = Transformation(other.start, self.end, self.add + other.add)
            right = Transformation(self.end + 1, other.end, other.add)
            return [left, mid, right]
        assert False


def map_to_transform(dst_start, src_start, range) -> Transformation:
    return Transformation(src_start, src_start + range - 1, dst_start - src_start)