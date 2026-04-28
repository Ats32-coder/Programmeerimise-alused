"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialize a card with value and suit."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Return string representation of the card."""
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
              "J", "Q", "K", "A"]

    def __init__(self):
        """Initialize an empty hand."""
        self.cards = []

    def can_add_card(self, card: Card) -> bool:
        """Check if a card can be added to the hand."""
        if len(self.cards) >= 5:
            return False

        if card.value not in self.values or card.suit not in self.suits:
            return False

        for c in self.cards:
            if c.value == card.value and c.suit == card.suit:
                return False

        return True

    def add_card(self, card: Card):
        """Add a card to the hand if possible."""
        if self.can_add_card(card):
            self.cards.append(card)

    def can_remove_card(self, card: Card):
        """Check if a card can be removed from the hand."""
        return card in self.cards

    def remove_card(self, card: Card):
        """Remove a card from the hand if possible."""
        if self.can_remove_card(card):
            self.cards.remove(card)

    def get_cards(self):
        """Return all cards in the hand."""
        return self.cards

    def _value_indices(self):
        """Return sorted indices of card values."""
        return sorted([self.values.index(card.value) for card in self.cards])

    def _value_counts(self):
        """Return counts of each card value."""
        counts = {}
        for card in self.cards:
            counts[card.value] = counts.get(card.value, 0) + 1
        return counts

    def is_straight(self):
        """Check if the hand is a straight."""
        if len(self.cards) != 5:
            return False

        indices = self._value_indices()

        for i in range(4):
            if indices[i] + 1 != indices[i + 1]:
                return False
        return True

    def is_flush(self):
        """Check if all cards have the same suit."""
        if len(self.cards) != 5:
            return False

        suits = [card.suit for card in self.cards]
        return len(set(suits)) == 1

    def is_straight_flush(self):
        """Check if the hand is both straight and flush."""
        return self.is_straight() and self.is_flush()

    def is_full_house(self):
        """Check if the hand is a full house."""
        if len(self.cards) != 5:
            return False

        counts = self._value_counts().values()
        return sorted(counts) == [2, 3]

    def is_four_of_a_kind(self):
        """Check if the hand has four cards of the same value."""
        if len(self.cards) != 5:
            return False

        return 4 in self._value_counts().values()

    def is_three_of_a_kind(self):
        """Check if the hand has three cards of the same value."""
        if len(self.cards) != 5:
            return False

        counts = self._value_counts().values()
        return 3 in counts and not self.is_full_house()

    def is_pair(self):
        """Check if the hand has exactly one pair."""
        if len(self.cards) != 5:
            return False

        counts = list(self._value_counts().values())
        return counts.count(2) == 1

    def get_hand_type(self):
        """Return the type of the poker hand."""
        if len(self.cards) < 5:
            return None

        if self.is_straight_flush():
            return "straight flush"
        if self.is_four_of_a_kind():
            return "four of a kind"
        if self.is_full_house():
            return "full house"
        if self.is_flush():
            return "flush"
        if self.is_straight():
            return "straight"
        if self.is_three_of_a_kind():
            return "three of a kind"
        if self.is_pair():
            return "pair"
        return "high card"

    def __repr__(self):
        """Return string representation of the hand."""
        card_list = ", ".join(str(card) for card in self.cards)
        hand_type = self.get_hand_type()

        if hand_type:
            return f"I got a {hand_type} with cards: {card_list}"
        return f"I'm holding {card_list}"