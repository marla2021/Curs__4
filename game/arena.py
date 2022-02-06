from unit import Hero
from typing import Optional


# class SingletonMeta(type):
#     _instances = {}
#
#     def __call__(self, *args, **kwargs):
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]


class Game():
    def __init__(self):
        self.player = None
        self.enemy = None
        self.game_processing = False
        self.game_results = ""

    def run(self, player: Hero, enemy: Hero):
        self.player = player
        self.enemy = enemy
        self.game_processing = True

    def _check_hp(self) -> Optional[str]:
        if self.player.hp <= 0 and self.enemy.hp <= 0:
            return self._end_game(result="В этой игре никто не победил")
        if self.player.hp <= 0:
            return self._end_game(result="Игрок проиграл")
        if self.enemy.hp <= 0:
            return self._end_game(result="Игрок победил")
        return None

    def _end_game(self, result: str):
        self.game_processing = False
        self.game_results = result
        return results

    def next_move(self) -> str:
        if results := self._check_hp():
            return results
        if not self.game_processing:
            return self.game_results
        results = self.enemy_hit()
        self._stamina_regenerate()
        return results

    def _stamina_regenerate(self):
        self.player.regenerate_stamina()
        self.enemy.regenerate_stamina()

    def enemy_hit(self) -> str:
        delta_damage: Optional[float] = self.enemy.hit(self.player)
        if delta_damage is not None:
            self.enemy.take_hit(delta_damage)
            results = f"Враг наносит вам урон {delta_damage}"
        else:
            results = f"Врагу не хватает выносливости, чтобы нанести удар"
        return results

    def player_hit(self):
        delta_damage: Optional[float] = self.player.hit(self.enemy)
        if delta_damage is not None:
            self.enemy.take_hit(delta_damage)
            return f"<p>Вы наносите врагу урон {delta_damage}</p><p>{self.next_move()}</p>"
        return f"<p>Вам не хватает выносливости для удара</p><p>{self.next_move()}</p>"

    def player_use_skill(self) -> str:
        delta_damage: Optional[float] = self.player.use_skill()
        if delta_damage is not None:
            self.enemy.take_hit(delta_damage)
            return f"<p>Вы наносите врагу урон {delta_damage}</p><p>{self.next_move()}</p>"
        return f"<p>Вам не хватает выносливости для использования навыка</p><p>{self.next_move()}</p>"
