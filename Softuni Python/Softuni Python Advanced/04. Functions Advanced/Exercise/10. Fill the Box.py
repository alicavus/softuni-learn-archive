def fill_the_box(height, length, width, *args):
    end_idx = args.index("Finish")
    capacity = height * length * width
    cubes = sum(args[:end_idx]) if end_idx else 0
    left_space = capacity - cubes

    return f"There is free space in the box. You could put {left_space} more cubes." if left_space >= 0 \
        else f"No more free space! You have {-left_space} more cubes."