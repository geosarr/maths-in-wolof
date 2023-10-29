import click

# Lim yu jitu ci been been yi, fukk fukk yi,
# téeméer téemer yi, juuni juuni yi
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
}


def been_beenu(b: int) -> str:
    assert 0 <= b < 10
    return f"-ak-{limal(b)}" if b > 0 else ""


def fukk_fukku(f: int) -> str:
    assert 0 < f < 10
    if f != 1 and f != 3:
        return f"{limal(f)}-{limal(10)}"
    return limal(f * 10)


def teemeer_teemeeru(t: int) -> str:
    assert 0 < t < 10
    if t != 1:
        return f"{limal(t)}-{limal(100)}"
    return limal(100)


def junni_junniu(t: int) -> str:
    assert 0 < t < 1000
    if t != 1:
        return f"{limal(t)}-{limal(1000)}"
    return limal(1000)


def limal(n: int) -> str:
    assert isinstance(n, int) and n >= 0
    if n in LIM:
        return LIM[n]
    elif n < 10:
        return f"{LIM[5]}-{LIM[n%5]}"
    elif n < 100:
        return f"{fukk_fukku(n//10)}{been_beenu(n%10)}"
    elif n < 1000:
        return f"{teemeer_teemeeru(n//100)}-ak-{limal(n%100)}"
    elif n < 1e6:
        return f"{junni_junniu(n//1000)}-ak-{limal(n%1000)}"


@click.command()
@click.option("--lim", "-l", required=True, type=int)
def main(lim: int):
    # result = limal(lim)
    for a in range(1, 1000000):
        print(a, ";", limal(a))
    # return result


if __name__ == "__main__":
    main()
