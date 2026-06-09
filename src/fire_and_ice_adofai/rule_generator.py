DEFAULT_PATTERN = [0, 90, 180, 270]


def generate_angles(count, pattern=None):
    pattern = pattern or DEFAULT_PATTERN
    if count <= 0:
        return []
    return [pattern[i % len(pattern)] for i in range(count)]
