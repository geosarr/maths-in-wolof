import click

# Lim yu jitu ci been been yi, fukk fukk yi,
# téeméer téemer yi, juuni juuni yi, ...
LIM = {
    0: "tus",
    1: "been",
    2: "ñaar",
    3: "ñatt",
    4: "ñeent",
    5: "juròom",
    10: "fukk",
    30: "fanweer",
    100: "téeméer",
    1000: "junni",
    int(1e6): "milliong",
    int(1e9): "milliard",
}


def fukk_fukku(n: int) -> str:
    return _limal(n, 10, [1, 3])


def teemeer_teemeeru(n) -> str:
    return _limal(n, 100)


def junni_junniu(n: int) -> str:
    return _limal(n, 1000)


def milliong_milliongu(n: int) -> str:
    return _limal(n, int(1e6))


def milliar_milliaru(n: int) -> str:
    return _limal(n, int(1e9))


def _limal(n: int, d: int, wute: list[int] = [1]) -> str:
    q, r = n // d, n % d
    lim = f"{limal(q)}-{limal(d)}" if q not in wute else limal(q * d)
    return f"{lim}-ak-{limal(r)}" if r > 0 else lim


def limal(n: int) -> str:
    if not isinstance(n, int):
        raise NotImplementedError("n lim bu mët la wara done.")
    if n < 0:
        raise NotImplementedError("n dafa wara >= 0.")
    if n in LIM:
        return LIM[n]
    elif n < 10:
        return f"{LIM[5]}-{LIM[n%5]}"
    elif n < 100:
        return fukk_fukku(n)
    elif n < 1000:
        return teemeer_teemeeru(n)
    elif n < 1e6:
        return junni_junniu(n)
    elif n < 1e9:
        return milliong_milliongu(n)
    elif n < 1e12:
        return milliar_milliaru(n)
    raise NotImplementedError


@click.command()
@click.option("--lim", "-l", required=True, type=int)
def main(lim: int):
    # result = limal(lim)
    for a in range(1, 1000000):
        print(a, ";", limal(a))
    # return result


if __name__ == "__main__":
    main()
