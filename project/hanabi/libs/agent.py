from typing import List

from game_state import GameState, Card
from .. import GameData


class Agent:
    def __init__(self, name: str, data: GameData.ServerGameStateData, players_names: list):
        self.name = name
        self._game_state = GameState(players_names, name, data)

    def make_move(self) -> None:
        """
        """
        pass

    def track_drawn_card(self, players: list) -> None:
        """
        """
        different_hands = 0
        new_card = None
        player = None
        for p in players:
            # TODO: unresolved reference hands
            if len(p.hand) != len(self.hands[p.name]):
                different_hands += 1
                # NB: newly drawn cards are appended to the right
                new_card = p.hand[-1]
                player = p.name
        assert new_card is not None, "new card not found"
        assert different_hands == 1, "too many different cards"

        assert player != self.name, "Cannot discover my cards"
        self._game_state.append_card_to_player_hand(player, Card(new_card.value, new_card.color))

    def track_played_card(self, player: str, card_idx: int) -> None:
        """
        """
        self._game_state.remove_card_from_hand(player, card_idx)

    def update_trash(self, card) -> None:
        """
        """
        self._game_state.update_trash(Card(rank=card.value, color=card.color))

    def hint_gained(self) -> None:
        """
        """
        self._game_state.gain_hint()

    def hint_consumed(self) -> None:
        """
        """
        self._game_state.use_hint()

    def mistake_made(self) -> None:
        """
        """
        self._game_state.mistake_made()

    def discover_card(self, card: Card, card_idx: int, action_type: str = None) -> None:
        """
        Called whenever the agent plays or discards a card, this function update the deck knowledge if the discovered card is NOT fully determined.

        Args:
            card: the played/discarded card
            card_index: the index of card in agent's hand
            action_type: it's one of ['play', 'mistake', 'discard'] FOR DEBUG ONLY
        """
        # - if passed card is NOT fully determined:
        #   the deck now knows that this card is in game -> update deck knowledge:
        if (not card.is_fully_determined):
            card.reveal_color()
            card.reveal_rank()
            self._game_state.deck.remove_cards([card]) #update deck

        # - if passed card is fully determined:
        #   the deck already "know" that card -> do nothing

    def update_board(self, card) -> None:
        """
        """
        self._game_state.card_correctly_played(card.color)

    def assert_aligned_with_server(self) -> None:
        """
        """
        pass

    def update_knowledge_on_hint(self, hint_type: str, hint_value: int, cards_idx: List[int], destination: str) -> None:
        """
        """
        if destination == self.name:
            pass
        else:
            pass