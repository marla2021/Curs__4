from unit import Hero
from typing import Optional


class Game:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.game_processing = False
        self.game_results = ""

    def run(self, player: Hero, enemy: Hero):
        self.player = player
        self.enemy = enemy
        self.game_processing = True

    # Метод «Проверка здоровья игроков» —
    # если здоровье одного из игроков закончилось,
    # выполняем метод «Конец игры».
    def _check_hp(self) -> Optional[str]:
        if self.player.hp <= 0 and self.enemy.hp <= 0:
            return self._end_game(result="В этой игре никто не победил")
        if self.player.hp <= 0:
            return self._end_game(result="Игрок проиграл")
        if self.enemy.hp <= 0:
            return self._end_game(result="Игрок победил")
        return None

    # возвращает строку с результатом боя.
    def _end_game(self, result: str):
        self.game_processing = False
        self.game_results = result
        return result

    # проходит проверка, осталось ли еще здоровье у игроков.
    # Если да, тогда происходит восстановление выносливости игроков,
    # противник наносит удар, и снова наступает ход игрока.
    # Если нет, тогда метод «Проверка здоровья игроков»
    # возвращает строку с результатом боя.
    def next_move(self) -> str:
        results = self._check_hp()
        if results:
            return results
        if not self.game_processing:
            return self.game_results
        results = self.enemy_hit()
        self._stamina_regenerate()
        return results

    # регенерируем выносливость
    def _stamina_regenerate(self):
        self.player.regenerate_stamina()
        self.enemy.regenerate_stamina()

    # враг наносит удар игроку, если есть урон, игрок принимает удар
    def enemy_hit(self) -> str:
        delta_damage: Optional[float] = self.enemy.hit(self.player)
        if delta_damage is not None:
            self.player.take_hit(delta_damage)
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
