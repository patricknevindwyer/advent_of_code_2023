from functools import reduce


def part_01(filename: str) -> None:
    """
    Determine which games are possible, sum the game IDs.

    :param filename:
    :return:
    """
    limit = {"red": 12, "green": 13, "blue": 14}
    print(
        sum(
            [
                game["id"]
                for game in parse_games(filename)
                if is_game_possible(game, limit=limit)
            ]
        )
    )


def part_02(filename: str) -> None:
    """
    Calculate a "game power" for each game, based on the minimum number
    of cubes required to play all the sets in the game. Sum the power
    for all games.

    :param filename:
    :return:
    """
    print(sum([game_power(game) for game in parse_games(filename)]))


def game_power(game: dict[str, any]) -> int:
    """
    Determine the power of a given game. This is the minimum
    number of cubes required for the game, multiplied together.

    :param game:
    :return:
    """
    colors = {"red": 0, "blue": 0, "green": 0}
    for subset in game["sets"]:
        for color, count in subset.items():
            if count > colors[color]:
                colors[color] = count
    return reduce(lambda a, b: a * b, colors.values(), 1)


def is_game_possible(game: dict[str, any], limit: dict[str, int]) -> bool:
    """
    Is the given game, with one or more subsets, possible?

    :param game: Parsed game
    :param limit: Known maximum of each cube type
    :return: True if the game is possible
    """

    for subset in game["sets"]:
        for cube, count in subset.items():
            if count > limit[cube]:
                return False
    return True


def parse_games(filename: str) -> list[dict[str, any]]:
    """
    Return a list of the games, with each game a separate
    item in the list, such that a game looks like:

        {
            "id": 11,
            "sets": [
                {"red":6, "blue": 4, "green": 0},
                ...
            ]
        }
    :param filename: Dat file
    :return: Dataset
    """
    with open(filename, "r") as raw:
        data = raw.read()

    res = []
    for game in data.strip().split("\n"):
        # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        [game_id, raw_subsets] = game.split(": ")

        # generate the subsets
        subsets = []
        for raw_subset in raw_subsets.split("; "):
            cubes = raw_subset.split(", ")
            subset = {"blue": 0, "red": 0, "green": 0}
            for cube in cubes:
                [num, col] = cube.split(" ")
                subset[col] = int(num)
            subsets.append(subset)

        # structure the game data for this game
        game_data = {"id": int(game_id.split(" ")[-1]), "sets": subsets}
        res.append(game_data)
    return res
