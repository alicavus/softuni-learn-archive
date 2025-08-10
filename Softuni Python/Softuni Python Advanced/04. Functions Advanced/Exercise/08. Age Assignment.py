def age_assignment(*args, **kwargs):
    return "\n".join([f"{name} is {kwargs[name[0]]} years old." for name in sorted(args)])