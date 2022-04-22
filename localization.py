localizations = {
    'ru': {
        'eat': 'Съесть',
        'decline': 'Отказаться',
        'trash': 'Выбросить',
        'drink': 'Выпить',
        'spill': 'Вылить',

        'self_cook': '{0} приготовил(а) себе "{1}"!',
        'cook': '{0} приготовил(а) "{1}" для вас, {2}!',
        'self_tea': '{0} заварил(а) себе чай "{1}"!',
        'tea': '{0} заварил(а) чай "{1}" для вас, {2}!',

        'wrong_tea_reciever': 'Это не ваш чайок!',
        'wrong_meal_reciever': 'Это не ваше "{0}"!',

        'wrong_tea_spiller': 'Выливать чужой чайок запрещено Женевской конвенцией!',
        'wrong_meal_trasher': '❌Выкидывать чужие вкусняшки НЕЛЬЗЯ.❌',

        'tea_drink': '{0} выпил чай "{1}"!',
        'tea_decline': '{0} отказался пить чай "{1}"!',
        'tea_spill': '{0} вылил нафик чай "{1}"!!',

        'meal_eat': '{0} съел "{1}"!',
        'meal_decline': '{0} отказался от "{1}"!',
        'meal_trash': '{0} выбросил нафик "{1}"!'
    },
    'en': {
        'eat': 'Eat',
        'decline': 'Refuse',
        'trash': 'Throw away',
        'drink': 'Drink',
        'spill': 'Spill out',

        'self_cook': '{0} cooked a "{1}"!',
        'cook': '{0} cooked "{1}" for you, {2}!',
        'self_tea': '{0} made a "{1}" tea!',
        'tea': '{0} made a "{1}" tea for you, {2}!',

        'wrong_tea_reciever': 'It`s not your tea!',
        'wrong_meal_reciever': 'It`s not your "{0}"!',
        
        'wrong_tea_spiller': 'Spilling someone else`s tea is forbidden by the Geneva Convention!',
        'wrong_meal_trasher': '❌You can`t throw away other people`s tasties.❌',
        
        'tea_drink': '{0} drank a "{1}" tea!', 
        'tea_decline': '{0} refused to drink a "{1}" tea!',
        'tea_spill': '{0} spilled out a "{1}" tea!!', 
         
        'meal_eat': '{0} ate a "{1}"!',
        'meal_decline': '{0} refused to eat a "{1}"!',
        'meal_trash': '{0} threw away a "{1}"!'
    }
}

def localize(language, text):
    if not language in localizations:
        language = 'en'
    localization = localizations[language]
    if not text in localization:
        return text
    return localization[text]