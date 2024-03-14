from day_05.transform import map_to_transform, Transformation

TransformList = list[Transformation]
Categories = dict[str, TransformList]


def map_seed(seed: int, transformations: TransformList) -> int:
    for t in transformations:
        if t.contains(seed):
            return t.apply(seed)
    return seed


def get_location(seed: int, categories: Categories) -> int:
    for cat, map_list in categories.items():
        seed = map_seed(seed, map_list)
    return seed


def read_categories(mapping: list[str]) -> Categories:
    categories: Categories = {}
    category: TransformList = []
    for line in mapping:
        if line.strip() == "":
            continue
        if ':' in line:
            category_name = line.split(':')[0].strip()
            category = []
            categories[category_name] = category
        else:
            dst_start, src_start, range_len = [int(s.strip()) for s in line.split(' ')]
            t = map_to_transform(dst_start, src_start, range_len)
            category.append(t)
    return categories


def flatten(categories: Categories) -> TransformList:
    result: TransformList = None
    for cat, tl in categories.values():
        if result is None:
            result = tl
            continue
        
    return result


def get_locations_single(instr: list[str]) -> list[int]:
    seeds = [int(s.strip()) for s in instr[0].split(':')[1].strip().split(' ')]
    categories = read_categories(instr[1:])
    result = []
    for seed in seeds:
        location = get_location(seed, categories)
        result.append(location)
    return result


def get_locations_range(instr: list[str]) -> int:
    seed_ranges: list[tuple[int, int]] = []
    seed_values = instr[0].split(':')[1].strip().split(' ')

    for i in range(0, len(seed_values), 2):
        pair = (int(seed_values[i]), int(seed_values[i + 1]))
        seed_ranges.append(pair)
    categories = read_categories(instr[1:])
    result = None
    for seed_range_start, seed_range_len in seed_ranges:
        for seed in range(seed_range_start, seed_range_start+seed_range_len):
            location = get_location(seed, categories)
            if result is None:
                result = location
            else:
                result = min(location, result)
    return result
