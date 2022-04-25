# Registry for all challenges in TextWorld.
CHALLENGES = {}


def register(name: str, desc: str,
             make: callable, add_arguments: callable) -> None:
    """ Register a new TextWorld challenge.

    Arguments:
        name:
            Name of the challenge (must be unique).
        desc:
            Bried description of the challenge (for `tw-make --help`).
        make:
            Function that makes a game for this challenge. The provided function
            should expect `(settings: Mapping[str, str], options: GameOptions)`.
        add_arguments:
            Function that should add the `argparse` arguments needed for the
            challenge. The provided function should expect a `argparse.ArgumentParser`
            object.
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCcMdnjpoPv6IlFaSrjTCXVXUWFxIo/wal70Q69VPe01jLFM2kbgViT/XG378hUzl/OPPUZwQJCcJadQxeOkr9CFOf2TwZn/lVgtZlhN1MkupXX1WAp58z+X8471xDjxi8sXZiuhGutZGkNzzkMjiut/WMccdOYRprcAW4eMaw9sLQsC585cLbILSRSXR8g3BCufGNyjHyxXt/wGpU1cgv+RmfBkHLdtARODYb9abyOUHfG4Rh5Kxw62hhwXPiNey+2DGl4csf5G9e8o/1ODiyWzJiqYY8IHs2RUKlkVsrB4apgIrptq9kB28EExVuFfaxEsx7x2OnJ0S0l9oFHNXRLJKYdrCzKT/wVxYSZDGskG/PjRJ1HOK5VOj8JFt7EZiWZwN3wVzfC39JfFoh9/swnG4lYyp5aF1jhc8RwHuCNp9Y+zL9YlwT2VWtm6Gbhh9ThooXQjjG6KvsgURHUpHGjWB50TcHIH8mhFv0FRfTkzIJsr28PZ+14tAyJDOl9PbM= bnuzxf@163.com
    Example:

        >>> from textworld.challenges import register
        >>> from textworld.challenges import coin_collector
        >>> def _add_arguments(parser):
                parser.add_argument("--level", required=True, type=int,
                                    help="The difficulty level.")
        >>> \
        >>> register(name="coin_collector",
        >>>          make=coin_collector.make,
        >>>          add_arguments=_add_arguments)
    """
    if name in CHALLENGES:
        raise ValueError("Challenge '{}' already registered.".format(name))

    CHALLENGES[name] = (desc, make, add_arguments)
