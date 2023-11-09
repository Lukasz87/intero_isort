from natsort import natsorted, ns


def intero(*args, **kwargs) -> list:
    return natsorted(*args, alg=ns.IGNORECASE | ns.PATH)
