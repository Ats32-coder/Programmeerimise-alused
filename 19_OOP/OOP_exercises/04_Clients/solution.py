"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Clients earnings per day since the start.

        You can either calculate the value or save it into a new attribute and return the value.
        """
        earnings = (self.current_amount - self.starting_amount) / self.account_age
        return earnings


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    clients_list = []
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip()

                parts = line.split(",")

                if len(parts) == 5:
                    name = parts[0]
                    bank = parts[1]
                    age = int(parts[2])
                    starting_sum = int(parts[3])
                    current_sum = int(parts[4])

                    client_object = Client(name, bank, age, starting_sum, current_sum)
                    clients_list.append(client_object)

    except FileNotFoundError:
        print(f"Faili nimega {filename} ei leitud")

    return clients_list


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    all_clients = read_from_file_into_list(filename)

    filtered_clients = []
    for client in all_clients:
        if client.bank == bank:
            filtered_clients.append(client)
    return filtered_clients


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    all_clients = read_from_file_into_list(filename)

    best_client = None
    max_earnings = 0

    for client in all_clients:
        current_earnings = client.earnings_per_day()

        if current_earnings > 0:

            if best_client is None or current_earnings > max_earnings:
                max_earnings = current_earnings
                best_client = client

            elif current_earnings == max_earnings:
                if client.account_age < best_client.account_age:
                    best_client = client

    return best_client


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    all_clients = read_from_file_into_list(filename)

    worst_client = None
    max_loss = 0

    for client in all_clients:
        current_earnings = client.earnings_per_day()

        if current_earnings < 0:

            if worst_client is None or current_earnings < max_loss:
                max_loss = current_earnings
                worst_client = client

            elif current_earnings == max_loss:
                if client.account_age < worst_client.account_age:
                    worst_client = client

    return worst_client


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]
    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]
    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz