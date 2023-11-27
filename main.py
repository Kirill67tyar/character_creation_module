from graphic_arts.start_game_banner import run_screensaver
from random import randint

DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3,)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (1, 5,)
    SPECIAL_BUFF: int = 15
    SPECIAL_SKILL: str = 'Удача'

    def __init__(self, name):
        self.name: str = name

    def attack(self):
        attack_value: int = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон, равный {attack_value}'

    def defence(self):
        defence_value: int = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {defence_value} урона'

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple[int, int] = (3, 5,)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (5, 10,)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS: int = (' находчивый воин дальнего боя. '
                                  'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple[int, int] = (5, 10,)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (-2, 2,)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple[int, int] = (-3, -1,)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (2, 5,)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита'


def start_training(char_class: Character) -> str:
    """Эта функция, чтобы мэтивуацию пэдняять"""
    commands: dict = {
        'attack': char_class.attack(),
        'defence': char_class.defence(),
        'special': char_class.special(),
    }

    print('Потренируйся управлять своими навыками.')
    print(
        'Введи одну из команд: attack — чтобы атаковать противника, '
        'defence — чтобы блокировать атаку противника или special '
        '— чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd: str = input('Введи команду: ')
        if cmd in commands:
            # print(commands.get(cmd, 'Выбор действия некорректен.' if cmd != 'skip' else ''))
            print(commands[cmd])
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """Функция для выбора перса."""
    game_classes: dict = {
        'warrior': Warrior,
        'mage': Mage,
        'healer': Healer,
    }
    approve_choice: str = ''
    char_class: Character = Character(char_name)
    while approve_choice != 'y':
        selected_class: str = input(
            'Введи название персонажа, за которого хочешь играть: '
            'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes.get(selected_class, Character)(char_name)
        print(char_class)
        approve_choice: str = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
            'чтобы выбрать другого персонажа ').lower()
    return char_class

if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, '
          'атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: Character = choice_char_class(char_name=char_name)
    print(start_training(char_class=char_class))
