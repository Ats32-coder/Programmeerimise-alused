"""Dictionary exercises."""


def get_hobbies(hobbies_dict: dict, name: str) -> list:
    """
    Return the hobbies of a given person.

    hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }

    get_hobbies(hobbies, "Tom")  => ["running", "reading"]
    get_hobbies(hobbies, "Timmy")  => "name not in dictionary"

    :param hobbies_dict: dictionary with peoples' hobbies.
    :param name: name of person whose hobbies are to be returned.

    :return: List of hobbies of the person with given name or "name not in dictionary".
    """
    if name in hobbies_dict:
        return hobbies_dict[name]
    else:
        return "name not in dictionary"


def find_tallest(height_dict: dict) -> str:
    """
    Return the name of the tallest peron in given dictionary.

    find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190}) => "Jhon"

    :param height_dict: dictionary with peoples' names and heights
    :return name of tallest person in given dict.
    """
    tallest = max(height_dict, key=height_dict.get)
    return tallest


def remove_sixes(six_dict: dict) -> dict:
    """
    Return a dictionary where all keys which's values are dividable by six are removed.

    remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}) => {"a": 4, "b": 8}

    :param six_dict: dictionary to be modified.
    :return: dict without values that are dividable by six.
    """
    result = {}
    for key, value in six_dict.items():
        if value % 6 != 0:
            result[key] = value
    return result


def exchange_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been exchanged.

    exchange_keys_and_values({"a": "b", "c": "d"}) => {"b": "a", "d": "c"}

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been exchanged.
    """
    return {value: key for key, value in exchange_dict.items()}


def main():
    """Test the exchange_keys_and_values function."""
    my_dict = {"a": "b", "c": "d"}
    print(exchange_keys_and_values(my_dict))


def count_symbol_appearances(stringy: str) -> dict:
    """
    Return dict where key is the symbol and the value is the count this symbol is present in the string.

    count_symbol_appearances("hello hi") => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}

    :param stringy: string to be processed.
    :return: dictionary with symbol counts.
    """
    counts = {}
    for char in stringy:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where key the is a symbol and the value is a list of words starting with this symbol.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting symbol and corresponding words in order of appearance.
    """
    result = {}
    for word in strings:
        first_char = word[0]
        if first_char in result:
            result[first_char].append(word)
        else:
            result[first_char] = [word]
    return result


if __name__ == '__main__':
    hobbies = {
        "Tom": ["running", "reading"],
        "John": ["movies", "music", "swimming"]
    }
    print(get_hobbies(hobbies, "Tom"))
    print(get_hobbies(hobbies, "Timmy"))

    height_dict = {"Tom": 186, "Mari": 175, "Jhon": 190}
    print(find_tallest(height_dict))

    print(remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}))
    main()

    result = count_symbol_appearances("hello hi")
    print(result)

    print(organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]))