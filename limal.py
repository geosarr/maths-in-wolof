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

def fukk_fukku(q: int) -> str:
    if q !=1 and q!=3:
        return f"{limal(q)}-{limal(10)}"
    return LIM[q*10]

def been_beenu(r: int) -> str:
    return '-ak-' + limal(r) if r> 0 else ''

def teemeer_teemeeru(n: int) -> str:
    return 


def limal(n: int) -> str:
    assert isinstance(n, int) and n >= 0
    if n in LIM:
        return LIM[n]
    elif n < 10:
        return f"{LIM[5]}-{LIM[n%5]}"
    elif n < 100:
        return f"{fukk_fukku(n//10)}{been_beenu(n%10)}"
    elif n < 1000:
        return 'test'

    
@click.command()
@click.option(
    "--lim", "-l", required=True, type=int
)
def main(lim: int):
    # result = limal(lim)
    for a in range(100):
        print(limal(a))
    # return result

if __name__ == "__main__":
    main()
