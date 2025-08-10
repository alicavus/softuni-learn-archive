def math_operations(*numbers, **kwargs):
    for idx in range(len(numbers)):
        match idx % 4:
            case 0:
                kwargs["a"] += numbers[idx]
            case 1:
                kwargs["s"] -= numbers[idx]
            case 2:
                kwargs["d"] /= numbers[idx] if numbers[idx] else 1
            case 3:
                kwargs["m"] *= numbers[idx]
    return "\n".join([f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda el: (-el[1], el[0]))])
 