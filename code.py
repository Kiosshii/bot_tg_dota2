from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import logging

API_TOKEN = '7902424588:AAEY20T4msY8OQIMb-6ZDzYsZida3e15bLY'   
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # создание клавиатуры
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_heroes = types.KeyboardButton("Герои")  
    keyboard.add(button_heroes)
    await bot.send_message(message.chat.id, "Привет! Я бот по всем героям Dota 2 и их описанию. Если хотите продолжить, нажмите кнопку ниже 'Герои'.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Герои")
async def handle_heroes_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_strength = types.KeyboardButton("Сила")
    button_agility = types.KeyboardButton("Ловкость")
    button_intelligence = types.KeyboardButton("Интеллект")
    button_universal = types.KeyboardButton("Универсальные")

    keyboard.add(button_strength, button_agility)
    keyboard.add(button_intelligence, button_universal)

    await message.reply("Выберите категорию героев:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Сила")
async def handle_strength_heroes(message: types.Message):
    await message.reply('''
/Earthshake
/LegionCommander
/Tidehunter
/Axe
/CentaurWarrunner
/Lifestealer
/Alchemist
/Bristleback
/ChaosKnight
/ElderTitan
/EarthSpirit
/Doom
/Huskar
/Kunkka
/Mars
/NightStalker
/OgreMagi
/Omniknight
/PrimalBeast
/Pudge
/Slardar
/SpiritBreaker
/Sven
/Timbersaw
/Tiny
/TreantProtector
/Underlord
/Tusk
/Undying
/WraithKing
''')

@dp.message_handler(lambda message: message.text == "Ловкость")
async def handle_agility_heroes(message: types.Message):
    await message.reply('''
/Antimage
/DrowRanger
/PhantomAssassin
/Kez
/Spectre
/Meepo
/ArcWarden
/Bloodseeker
/Hoodwink
/Juggernaut
/BountyHunter
/Clinkz
/EmberSpirit
/FacelessVoid
/Gyrocopter
/Luna
/Medusa
/MonkeyKing
/Morphling
/NagaSiren
/PhantomLancer
/Razor
/Riki
/ShadowFiend
/Slark
/Sniper
/TemplarAssassin
/Terrorblade
/TrollWarlord
/Viper
/Ursa
/Weaver
''')

@dp.message_handler(lambda message: message.text == "Интеллект")
async def handle_intelligence_heroes(message: types.Message):
    await message.reply('''
/Lina
/CrystalMaiden
/DeathProphet
/Necrophos
/KeeperoftheLight
/Lion
/Muerta
/AncientApparition
/Disruptor
/Enchantress
/Grimstroke
/Jakiro
/Leshrac
/Lich
/NaturesProphet
/Oracle
/OutworldDestroyer
/Pugna
/Puck
/QueenofPain
/Ringmaster
/ShadowDemon
/ShadowShaman
/Silencer
/SkywrathMage
/StormSpirit
/Tinker
/Warlock
/WitchDoctor
/Zeus
''')

@dp.message_handler(lambda message: message.text == "Универсальные")
async def handle_universal_heroes(message: types.Message):
    await message.reply('''
/Marci
/Enigma
/Techies
/Bane
/Chen
/DarkSeer
/Dazzle
/Invoker
/Broodmother
/Venomancer
/Visage
/VoidSpirit
/Windranger
/WinterWyvern
/VengefulSpirit
/Snapfire
/SandKing
''')

@dp.message_handler(lambda message: not message.text.startswith('/'))  # Обработка некорректных команд
async def handle_invalid_command(message: types.Message):
    await message.reply("Пожалуйста, введите корректную команду или используйте меню.")



@dp.message_handler(commands=['IO', 'io'])# выбор героя io аля чтоб небыло ошибкт с большой и маленькой буквы
async def handle_io_command(message: types.Message):
    await send_io_photo(message)

async def send_io_photo(message: types.Message):
    photo_path = '2007/wisp.jpg'  
    caption = '''
Io — это герой в игре Dota,
который представляет собой совокупность всех сил
притяжения и отторжения в материальном поле.
Может выбрать один из двух аспектов:
Атакующий — Kritzkrieg,
с которым Overcharge увеличивает скорость атаки и урон
от заклинанийобоим связанным героям.
Защитный — Medigun,
предоставляющий броню и
сопротивление магии соответственно.
Ультимативная способность Io — Relocate,
которая даёт возможность ему и связанному с ним союзнику
перенестись в любую точку карты.
Через несколько секунд Io телепортируется обратно,
союзник же вернётся, только если он всё ещё привязан!'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Techies', 'techies'])
async def handle_techies_command(message: types.Message):
    await send_techies_photo(message)

async def send_techies_photo(message: types.Message):
    photo_path = '2007/This.jpg'  
    caption = '''Techies
вспомните длинные поля в 41,
так вот они все были заминированы.
Окунитесь в мир минных полей и самолетов-камикадзе
на одном персонаже.
Хардлайн (3 позиция);
Саппорт (4 позиция);
Саппорт (5 позиция).'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
        
@dp.message_handler(commands=['AntiMage', 'antimage'])
async def handle_antimage_command(message: types.Message):  
    await send_antimage_photo(message)  

async def send_antimage_photo(message: types.Message):  
    photo_path = '2007/antimage.jpg'  
    caption = '''AntiMage
Выжигает ману врагов атаками.
Если AntiMage наберёт полную силу, мало кто сможет его остановить.
Он способен забирать у врагов ману каждым ударом или телепортироваться
на небольшие расстояния, что не позволяет врагам загнать его в угол.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
        
@dp.message_handler(commands=['DrowRanger', 'drowranger'])
async def handle_drowranger_command(message: types.Message):  
    await send_drowranger_photo(message)  

async def send_drowranger_photo(message: types.Message):  
    photo_path = '2007/drow.jpg'  
    caption = '''Drow Ranger
Она не промахнётся!
Замедляет врагов ледяными стрелами
Немногим удаётся спастись от Drow Ranger.
Обезмолвив врагов морозной волной,
она накрывает их градом замедляющих ледяных стрел,
после которого мало кто способен выжить.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Abaddon', 'abaddon'])
async def handle_abaddon_command(message: types.Message):  
    await send_abaddon_photo(message)  

async def send_abaddon_photo(message: types.Message):  
    photo_path = '2007/aba.jpg'  
    caption = '''Abaddon,
способный лечиться за счёт
вражеских атак,
может пережить почти любое нападение.
Он всегда готов вклиниться в битву,
закрывая союзников щитом
и запуская обоюдоострые витки мглы,
которыми он увечит врагов
и исцеляет товарищей.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['Earthshake', 'earthshaker'])
async def handle_earthshaker_command(message: types.Message):  
    await send_earthshaker_photo(message)  

async def send_earthshaker_photo(message: types.Message):  
    photo_path = '2007/hk.jpg'  
    caption = '''Earthshaker
АХАХАХАХХАХА ЭТА ГОДЛИЗЛА БУДЕТ СНИТЬСЯ
В КОШМАРАХ ВСЕХ ГЕРОЕВ КОТОРЫЕ СПАВНЯТ
СЕБЕ КОГО-ТО, ЭТОТ ЧЕРТ КИДАЕТСЯ
ТРУПАМИ ГЕРОЕВ И КРИПОЧКОВ КОТОРЫХ
ОН УБИЛ НО РАЗВЕ НЕ + ВАЙБИК?)
СТОЯ НА ЛАЙНЕ ( а чаще всего это мид)
СТАРАЙТЕСЬ НЕ ВЗБЕСИТЬ
ЭТУ 3-Х ТОННУЮ МАШИНУ ДЛЯ УБИЙСТВ)'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['PhantomAssassin', 'phantomassassin'])
async def handle_phantomassassin_command(message: types.Message):  
    await send_phantomassassin_photo(message)  

async def send_phantomassassin_photo(message: types.Message):  
    photo_path = '2007/fa.jpg'  
    caption = '''Phantom Assassin
идёт в наступление,
едва завидев свою жертву.
Мгновенно сблизившись с ней,
Мортред легко уклоняется от атак
и обрушивает на врага удар за ударом,
любой из которых может
оказаться роковым.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#1       
@dp.message_handler(commands=['Enigma', 'enigma'])
async def handle_Enigma_command(message: types.Message):  
    await send_Enigma_photo(message)  

async def send_Enigma_photo(message: types.Message):  
    photo_path = '2007/en.jpg'  
    caption = '''Enigma
Затягивает врагов в чёрную дыру, нанося им урон
О происхождении этой сущности
неизвестно ровным счётом ничего.
Многие опасаются Enigma из-за
его способности создать чёрную дыру,
которая удерживает врагов
и делает их лёгкой мишенью.
Вместе с вездесущими союзными
эйдолонами он атакует врагов издалека.'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#2
@dp.message_handler(commands=['Huskar', 'huskar'])
async def handle_Huskar_command(message: types.Message):  
    await send_Huskar_photo(message)  

async def send_Huskar_photo(message: types.Message):  
    photo_path = '2007/hus.jpg'  
    caption = '''Huskar
Жертвует своим здоровьем,
чтобы наносить больше урона
Чем меньше у Huskar здоровья,
тем опаснее он становится.
Своим ультом он мгновенно лишает себя
и противника части здоровья,
а на грани смерти может обрушить
на своих врагов шквал горящих копий.'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#3
@dp.message_handler(commands=['LegionCommander', 'legioncommander'])
async def handle_LegionCommander_command(message: types.Message):  
    await send_LegionCommander_photo(message)  

async def send_LegionCommander_photo(message: types.Message):  
    photo_path = '2007/lg.jpg'  
    caption = '''Legion Commander
Вот эта милфачка,
играется как керии и как инициатор битв.
Так и на легкой так и на сложной стоит.
Из минусов нету контроля.
Из плюсов если она раскачается
и своей ультой затянет вас на дулэль
ДА ЕЩЕ И ВЫИГРАЕТ, это гг.
Она будет бегать по всей карте
и искать самого слабого дабы
баф от ульты рос и рос,
чтобы урона было МИЛЛИАРД.
Желательно убивать самой первой,
чтобы не  добивала ультой лоу хпешных =)'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#4
@dp.message_handler(commands=['Lina', 'lina'])
async def handle_Lina_command(message: types.Message):  
    await send_Lina_photo(message)  

async def send_Lina_photo(message: types.Message):  
    photo_path = '2007/lina.jpg'  
    caption = '''Lina 
Опасная и хрупкая Lina
легко свалит любого одинокого врага.
Она поражает противников огнём и молнией,
а каждое произнесённое
ей заклинание увеличивает скорость её атаки,
не давая выжить никому.'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#5
@dp.message_handler(commands=['Meepo', 'meepo'])
async def handle_Meepo_command(message: types.Message):  
    await send_Meepo_photo(message)  

async def send_Meepo_photo(message: types.Message):  
    photo_path = '2007/meep.jpg'  
    caption = '''Meepo
Пятеро сильнее одного
Призвав до пяти своих полноценных копий,
Meepo способен сражаться на всех фронтах
одновременно. Он распределяет своих клонов
по полю боя и, заметив врага,
приковывает его к земле,
со взрывом телепортирует к себе
остальные копии и добивает истощённую жертву.'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#6
@dp.message_handler(commands=['ArcWarden', 'arcwarden'])
async def handle_ArcWarden_command(message: types.Message):  
    await send_ArcWarden_photo(message)  

async def send_ArcWarden_photo(message: types.Message):  
    photo_path = '2007/arc.jpg'  
    caption = '''Arc Warden
Копирует себя, чтобы вести войну на два фронта
Arc Warden — разбитый осколок
той древней мощи,
что породила самих Древних,
и он намерен прекратить схватку Света и Тьмы.
Сковывайте одиноких врагов
потоками энергии или искажайте пространство,
создавая защитное поле для союзников.
Призывайте призрачные искры,
нападающие на приблизившихся противников,
или же полную копию самого себя
со всеми предметами и способностями,
способную сокрушить неприятеля.'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#7
@dp.message_handler(commands=['Kez', 'kez'])
async def handle_Kez_command(message: types.Message):  
    await send_Kez_photo(message)  

async def send_Kez_photo(message: types.Message):  
    photo_path = '2007/kez.jpg'  
    caption = '''Kez
Пернатое возмездие!
Обычно в бою Кеза окрыляет фантазия:
он на лету меняет катану на саи и обратно,
чтобы при надобности нападать, рубить,
парировать и отступать.
Но когда Кез берётся за дело всерьёз,
он может заранее приготовиться
к любому развитию событий
и верно распорядиться своим арсеналом,
чтобы атаковать, избежать
или попросту перехитрить противников.'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#8
@dp.message_handler(commands=['Marci', 'marci'])
async def handle_Marci_command(message: types.Message):  
    await send_Marci_photo(message)  

async def send_Marci_photo(message: types.Message):  
    photo_path = '2007/mar.jpg'  
    caption = '''Marci
Скачет по полю боя и
отбрасывает врагов стремительными атаками
Доказывая, что неиссякаемая верность
даёт несравненную силу,
Марси всегда готова вступить в битву
и не жалеет кулаков,
чтобы защитить своих компаньонов.
Легко перебрасывая друзей
и врагов по полю боя,
она с радостью врывается
в любой поединок, предоставляет союзникам
столь нужное преимущество
и применяет скрытую силу, при виде которой
даже боги предпочитают
не вступать в конфликт с героиней.'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['Tidehunter', 'tidehunter'])
async def handle_Tidehunter_command(message: types.Message):  
    await send_Tidehunter_photo(message)  

async def send_Tidehunter_photo(message: types.Message):  
    photo_path = '2007/arbuz.jpg'  
    caption = '''Tidehunter,или же арбуз
Этот повелитель морей,
огромное существо у которого много хп
+ брони из-за чего убить его
бывает иногда проблемой.
Есть крутые скиллы
на станн и на атаку по облости.
Играется как танк'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Spectre', 'spectre'])
async def handle_Spectre_command(message: types.Message):  
    await send_Spectre_photo(message)  

async def send_Spectre_photo(message: types.Message):  
    photo_path = '2007/spc.jpg'  
    caption = '''Spectre
У вас было когда нибудь ощущение,
того что за вами следят?
Так вот, если вы видите
в вражеском пулле  этого героя.
Бойтесь, ибо спрятаться от неё не получится.
Можете бежать плакать, реветь вы умрёте!
Если вы видите её в вашем пулле,
можете радоваться ибо это,
надеждная рука помощи в сложную драку.
Самое главное дать ей раскачаться
и купить нужные шмотки
ибо на линии стоит очень плохо =)'''
    
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Axe', 'axe'])
async def handle_axe_command(message: types.Message):  
    await send_axe_photo(message)  

async def send_axe_photo(message: types.Message):  
    photo_path = '2007/axe.jpg'  
    caption = '''Axe
рубит одного врага за другим,
неизменно ступая впереди своей команды.
Он вынуждает противников вступить в бой,
а затем отвечает на их удары
смертоносными взмахами топора.
Нещадно круша ослабленных врагов,
он всегда несётся вперёд.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['centaurwarrunner', 'CentaurWarrunner'])
async def handle_CentaurWarrunner_command(message: types.Message):  
    await send_CentaurWarrunner_photo(message)  

async def send_CentaurWarrunner_photo(message: types.Message):  
    photo_path = '2007/DR.jpg'  
    caption = '''Centaur Warrunner
умело наносит и принимает урон.
Он ведёт команду в наступление,
оглушает своим топотом врагов
и мгновенно отвечает на каждый удар,
ускоряя как союзников,
так и смерть неприятелей.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['AncientApparition', 'ancientapparition'])
async def handle_AncientApparition_command(message: types.Message):  
    await send_AncientApparition_photo(message)  

async def send_AncientApparition_photo(message: types.Message):  
    photo_path = '2007/fi.jpg'  
    caption = '''Ancient Apparition
способный запустить мощный
заряд льда через всё поле битвы,
может заморозить раненых врагов до смерти,
где бы те ни находились.
Он держит врагов в напряжении,
замедляя их и помогая своим союзникам.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['', ''])
async def handle__command(message: types.Message):  
    await send__photo(message)  

async def send__photo(message: types.Message):  
    photo_path = 'jpg'  
    caption = ''''''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['Bloodseeker', 'bloodseeker'])
async def handle_Bloodseeker_command(message: types.Message):  
    await send_Bloodseeker_photo(message)  

async def send_Bloodseeker_photo(message: types.Message):  
    photo_path = '2007/bl.jpg'  
    caption = '''Bloodseeker
Bпостоянно ставит противников
перед непростым выбором.
Окропив кровью обширную территорию,
он вынуждает врагов отступать,
а под его чудовищным ультом
жертва либо стоит на месте, либо погибает.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Bane', 'bane'])
async def handle_Bane_command(message: types.Message):  
    await send_Bane_photo(message)  

async def send_Bane_photo(message: types.Message):  
    photo_path = '2007/ben.jpg'  
    caption = '''Bane
наводит ужас на врагов
своим арсеналом обездвиживающих способностей.
Погружая противников в заразительные кошмары
или удерживая их на месте,
он даёт союзникам достаточно времени,
чтобы прикончить неприятеля.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Chen', 'chen'])
async def handle_Chen_command(message: types.Message):  
    await send_Chen_photo(message)  

async def send_Chen_photo(message: types.Message):  
    photo_path = '2007/chen.jpg'  
    caption = '''Chen
Обратив лесных существ в свою веру,
Chen ведёт свою импровизированную
армию на помощь команде.
Он насылает свою паству на противников,
отправляет союзников в безопасное место,
а в крайнем случае излечивает их,
где бы они ни были.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['DarkSeer', 'darkseer'])
async def handle_DarkSeer_command(message: types.Message):  
    await send_DarkSeer_photo(message)  

async def send_DarkSeer_photo(message: types.Message):  
    photo_path = '2007/drk.jpg'  
    caption = '''Dark Seer
Изворотливый стратег Dark Seer
мастерски манипулирует
местоположением своих врагов.
Он способен затянуть их под удары
союзников и обратить мощь неприятелей
против них самих своей отражающей стеной.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Dazzle', 'dazzle'])
async def handle_Dazzle_command(message: types.Message):  
    await send_Dazzle_photo(message)  

async def send_Dazzle_photo(message: types.Message):  
    photo_path = '2007/dazl.jpg'  
    caption = '''Dazzle
Рождённый поддерживать своих сторонников,
Dazzle не даёт соратникам умереть,
пока те уничтожают врагов.
Его необычные заклинания
вплетаются в броню,
ослабляя противников
и усиливая союзников.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Hoodwink', 'hoodwink'])
async def handle_Hoodwink_command(message: types.Message):  
    await send_Hoodwink_photo(message)  

async def send_Hoodwink_photo(message: types.Message):  
    photo_path = '2007/hood.jpg'  
    caption = '''Hoodwink
всегда спешит туда,
где ждёт беда, и готова противостоять
любой угрозе из призрачного леса,
ставшего ей домом. Даже с тяжёлым
арбалетом она мимолётно прошмыгивает
меж веток и листьев, и выследить
её в бою почти невозможно.
На мгновение потеряете её из виду,
и она уже у вас за спиной
— а ваша остолбенелая туша висит в её сетях.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['CrystalMaiden', 'crystalmaiden'])
async def handle_CrystalMaiden_command(message: types.Message):  
    await send_CrystalMaiden_photo(message)  

async def send_CrystalMaiden_photo(message: types.Message):  
    photo_path = '2007/krs.jpg'  
    caption = '''Crystal Maiden
пригодится любой команде,
ведь она даёт союзникам ману
и не позволяет врагам сбежать.
А когда представляется случай,
она может уничтожить врагов
своим сокрушительным ультом.'''
        
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Juggernaut', 'juggernaut'])
async def handle_Juggernaut_command(message: types.Message):  
    await send_Juggernaut_photo(message)  

async def send_Juggernaut_photo(message: types.Message):  
    photo_path = '2007/jag.jpg'  
    caption = '''Juggernaut
разрубает своих врагов шквалом
рассекающих ударов. Мало кто сможет
остановить или пережить его
отчаянное наступление,ведь,
набрав обороты, он становится
практически неуязвимым.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['DeathProphet', 'deathprophet'])
async def handle_DeathProphet_command(message: types.Message):  
    await send_DeathProphet_photo(message)  

async def send_DeathProphet_photo(message: types.Message):  
    photo_path = '2007/123.jpg'  
    caption = '''Death Prophet
Своей армией призраков
уничтожает как противников,
так и их постройки.
Возглавив наступление и выпуская
одну смертоносную волну за другой,
она может повергнуть врагов в отчаяние.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Necrophos', 'necrophos'])
async def handle_Necrophos_command(message: types.Message):  
    await send_Necrophos_photo(message)  

async def send_Necrophos_photo(message: types.Message):  
    photo_path = '2007/nec.jpg'  
    caption = '''Necrophos
всюду несёт благополучие
друзьям и смерть — врагам.
Излечивая союзников и нанося
противникам урон каждым пульсом смерти,
он изничтожает врагов одним лишь
своим присутствием. Также Necrophos может
воззвать к помощи самого жнеца,
который надолго задержит
жертву в мире ином.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['KeeperoftheLight', 'KeeperoftheLight'])
async def handle_KeeperoftheLight_command(message: types.Message):  
    await send_KeeperoftheLight_photo(message)  

async def send_KeeperoftheLight_photo(message: types.Message):  
    photo_path = '2007/kpz.jpg'  
    caption = '''Keeper of the Light
полезен любой команде.
Он манипулирует маной
врагов и союзников, повергает с
лабых противников волнами света и,
преисполнившись сиянием,
ведёт соратников в наступление.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Lion', 'lion'])
async def handle_Lion_command(message: types.Message):  
    await send_Lion_photo(message)  

async def send_Lion_photo(message: types.Message):  
    photo_path = '2007/lion.jpg'  
    caption = '''Lion
не даёт врагам выбраться
из своей цепкой хватки.
Он оглушает жертву
каменными шипами и на время
превращает её в безобидную зверушку.
Если одних его заклинаний
не хватит, чтобы расправиться с врагом,
он обязательно даст команде достаточно времени.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
@dp.message_handler(commands=['Lifestealer', 'lifestealer'])
async def handle_Lifestealer_command(message: types.Message):  
    await send_Lifestealer_photo(message)  

async def send_Lifestealer_photo(message: types.Message):  
    photo_path = '2007/zom.jpg'  
    caption = '''Lifestealer
смог подобраться близко
к своей жертве, то её
уже ничего не спасёт.
Он может забраться внутрь
крипа или союзника,
чтобы, оказавшись возле врага,
неожиданно вырваться из
носителя и разорвать
жертву своими когтями.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Invoker', 'invoker'])
async def handle_Invoker_command(message: types.Message):  
    await send_Invoker_photo(message)  

async def send_Invoker_photo(message: types.Message):  
    photo_path = '2007/inoker.jpg'  
    caption = '''Invoker
Благодаря обширному арсеналу заклинаний
Invoker может приспособиться
к ходу любой битвы,комбинируя
три магичесих компонента,
он может сотворить
одно из десяти заклинаний,
позволяющих уничтожить
врага или спастись от него.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Muerta', 'muerta'])
async def handle_Muerta_command(message: types.Message):  
    await send_Muerta_photo(message)  

async def send_Muerta_photo(message: types.Message):  
    photo_path = '2007/muerta.png'  
    caption = '''Muerta
Повелительница смерти Муэрта
ступает по миру живых,
устрашая своих жертв
виртуозными выстрелами и насылая
духов на врагов.
Муэрта всегда готова
присмирить беспечных противников
огнём из запасного пистолета
и обрушить на них бесплотную
ярость проклятых, зайдя за вуаль духов.
'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Broodmother', 'broodmother'])
async def handle_Broodmother_command(message: types.Message):  
    await send_Broodmother_photo(message)  

async def send_Broodmother_photo(message: types.Message):  
    photo_path = '2007/mama.jpg'  
    caption = '''Broodmother
Скользя по своей паутине,
Broodmother взращивает армию пауков,
которые вместе с её командой
наступают на базу врага.
Если на пути встречается жертва,
паучиха присоединяется к своим
отпрыскам и нападает,замедляя врагов
ядовитыми укусами и утоляя
свой животный голод.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Puck', 'puck'])
async def handle_Puck_command(message: types.Message):  
    await send_Puck_photo(message)  

async def send_Puck_photo(message: types.Message):  
    photo_path = '2007/puck.jpg'  
    caption = '''Puck
Игривый и увёртливый Puck
мастерски запутывает противников.
Он может переместиться на небольшое
расстояние с помощью своей
смертоносной сферы и обезмолвить
врагов магической пылью,
а когда противник опомнится,
будет слишком поздно:
Puck уже исчезнет за горизонтом.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#1
@dp.message_handler(commands=['Alchemist', 'alchemist'])
async def handle_Alchemist_command(message: types.Message):  
    await send_Alchemist_photo(message)  

async def send_Alchemist_photo(message: types.Message):  
    photo_path = '2007/alko.jpg'  
    caption = '''Alchemist или же Алхимик
Ходит со своим дружком
( умным) на спине и кидают зелья,
в нынешнее время один из хороших
кери с большим потенциалом и вин рейтом'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#2
@dp.message_handler(commands=['Bristleback', 'bristleback'])
async def handle_Bristleback_command(message: types.Message):  
    await send_Bristleback_photo(message)  

async def send_Bristleback_photo(message: types.Message):  
    photo_path = '2007/tvar.jpg'  
    caption = '''Bristleback или же Ёжик
Такая противная тварь это жесть.
Ходит плюется в вас слизью чтобы
вы двигались меньше, так еще
и если бить сзади то будет вас
бить своими иголками на спине,
противный двух кнопочный перс.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#3
@dp.message_handler(commands=['ChaosKnight', 'chaosknight'])
async def handle_ChaosKnight_command(message: types.Message):  
    await send_ChaosKnight_photo(message)  

async def send_ChaosKnight_photo(message: types.Message):  
    photo_path = '2007/xxx.jpg'  
    caption = '''Chaos Knight 
 сам по себе армия.
 Он способен призывать кавалерию
 своих двойников и разрушать
 постройки врага, а когда покажутся защитники,
 он расколет реальность и перенесёт
 себя и свои копии на расстояние,
 достаточное для рокового взмаха булавы.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#4
@dp.message_handler(commands=['Dawnbreaker', 'dawnbreaker'])
async def handle_Dawnbreaker_command(message: types.Message):  
    await send_Dawnbreaker_photo(message)  

async def send_Dawnbreaker_photo(message: types.Message):  
    photo_path = '2007/khk.jpg'  
    caption = '''Dawnbreaker
Честно не знаю почему ее все так любят,
обычный персонаж ну ладно
yкей она красивая где-то.
Скиллы противные но не прям
чтобы умирать от нее по кд,
в целом обычный персонаж который
кидается своим молотом и делает джагу джагу'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#5
@dp.message_handler(commands=['Doom', 'doom'])
async def handle_Doom_command(message: types.Message):  
    await send_Doom_photo(message)  

async def send_Doom_photo(message: types.Message):  
    photo_path = '2007/doom.jpg'  
    caption = '''Doom
Doom забирает жизни своих врагов разными способами.
Он пожирает существ, чтобы перенять их способности,
а также способен наслать на врага адское пламя,
не дающее тому использовать способности и предметы.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#6
@dp.message_handler(commands=['EarthSpirit', 'earthspirit'])
async def handle_EarthSpirit_command(message: types.Message):  
    await send_EarthSpirit_photo(message)  

async def send_EarthSpirit_photo(message: types.Message):  
    photo_path = '2007/3131.jpg'  
    caption = '''Earth Spirit или же Земеля
держит противников в смятении
и поддерживает друзей в бою.
Приспосабливаясь к ходу любой
битвы, он наносит врагам урон
своими каменными копиями и спасает
товарищей, вырывая их из объятий смерти.
Один из  сложных персов
ибо не все могут понять
допустим его 4 скилл втф)'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#7
@dp.message_handler(commands=['ElderTitan', 'eldertitan'])
async def handle_ElderTitan_command(message: types.Message):  
    await send_ElderTitan_photo(message)  

async def send_ElderTitan_photo(message: types.Message):  
    photo_path = '2007/edrtit.jpg'  
    caption = '''Elder Titan
Разведав территорию своим астральным духом,
Elder Titan готов атаковать с любого направления.
Он останавливает противников ударом копыта,
разъедает их защиту одним лишь своим присутствием
и повергает неприятелей, расколов почву под ними'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#8
@dp.message_handler(commands=['Kunkka', 'Kunkka'])
async def handle_Kunkka_command(message: types.Message):  
    await send_Kunkka_photo(message)  

async def send_Kunkka_photo(message: types.Message):  
    photo_path = '2007/kun.jpg'  
    caption = '''Kunkka или Кунка
АРРР СВИСТАТЬ ВСЕХ
НАВВЕРХ ЯКОРЬ МНЕ В ЗАД
ЭТОТ КАПИТАН КОРОБЛЕЙМОЖЕТ
ВЫПУТСТИТЬ НА ВАС
КОРАБЛЬ И НАРИСОВАТЬ
ПОД ВАМИ ПРОХОД ЧТОБЫ ВЫ
ЕЩЕ И ПОСЛЕ ВЕРНУЛИСЬ НАЗАД МЕРЗКИЙ
НО ПРИКОЛЬНЫЙ ТИП,
ТАК СКАЗАТЬ ВИСКАРЬ МНЕ В ЗАД'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#9
@dp.message_handler(commands=['Mars', 'mars'])
async def handle_Mars_command(message: types.Message):  
    await send_Mars_photo(message)  

async def send_Mars_photo(message: types.Message):  
    photo_path = '2007/mars.jpg'  
    caption = '''Mars или Марс или Маяс)
 рождён для сражений: он пронзает врагов
 своим легендарным копьём, а от нападений
 его защищает смертоносный щит. Окружив
 противника солдатами своего верного легиона,
 покровитель воинов не позволяет ему сбежать,
 и даже самая безнадёжная схватка окажется во
 власти бога войны — ведь численное
 преимущество всегда на его стороне.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#10
@dp.message_handler(commands=['', ''])
async def handle__command(message: types.Message):  
    await send__photo(message)  

async def send__photo(message: types.Message):  
    photo_path = ''  
    caption = ''''''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#11
@dp.message_handler(commands=['NightStalker', 'nightstalker'])
async def handle_NightStalker_command(message: types.Message):  
    await send_NightStalker_photo(message)  

async def send_NightStalker_photo(message: types.Message):  
    photo_path = '2007/stalker.jpg'  
    caption = '''Night Stalker
Когда солнце скрывается за горизонтом,
на охоту выходит Night Stalker.
Проносясь сквозь тёмные чащи,
он замедляет жертву и раздирает её в клочья.
А если восход угрожает его планам,
он может затмить светило и продолжить нападение.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['OgreMagi', 'ogremagi'])
async def handle_OgreMagi_command(message: types.Message):  
    await send_OgreMagi_photo(message)  

async def send_OgreMagi_photo(message: types.Message):  
    photo_path = '2007/222.jpg'  
    caption = '''Ogre Magi
ЫХЫЫХ ОГР ДВЕ ХАЛАВЫ
Благодаря возможности многократно
приумножить эффект
каждого своего заклинания
и толике удачи Ogre Magi
способен обратить врагов
в пепел или усилить союзников.
Но, разумеется, полагаться лишь на удачу — дело неблагодарное..'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#1
@dp.message_handler(commands=['Omniknight', 'omniknight'])
async def handle_Omniknight_command(message: types.Message):  
    await send_Omniknight_photo(message)  

async def send_Omniknight_photo(message: types.Message):  
    photo_path = '2007/is.jpg'  
    caption = '''Omniknight
Ну тварюга если честн полная
всегда готов помочь своей команде
на передовой. Он излечивает союзников
заклинанием, наносящим урон всем врагам
вокруг, а в случае чего берётся
за свой могучий молот и оберегает
соратников от вреда'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#2
@dp.message_handler(commands=['PrimalBeast', 'primalbeast'])
async def handle_PrimalBeast_command(message: types.Message):  
    await send_PrimalBeast_photo(message)  

async def send_PrimalBeast_photo(message: types.Message):  
    photo_path = '2007/terex.jpg'  
    caption = '''Primal Beast или Динозаврик 
Primal Beast свирепо
расталкивает врагов и союзников,
чтобы вклиниться в битву
и устроить переполох.
Этот зверь являет
неминуемую угрозу
для любого противника,
наказывая своих обидчиков
и упиваясь возможностью схватить
добычу и вбить её в землю,
пока от неё не останется лишь кровавое месиво'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#3
@dp.message_handler(commands=['Pudge', 'pudge'])
async def handle_Pudge_command(message: types.Message):  
    await send_Pudge_photo(message)  

async def send_Pudge_photo(message: types.Message):  
    photo_path = '2007/pudg.jpg'  
    caption = '''Pudge
ОДА СБОРКА ИЗ 9 МОМЧЕГОВ НА ПУДЖА ПРИСУТСТВУЕТ?)
Каждый точный бросок знаменитого
крюка вселяет страх во врагов Pudge,
ведь, притянув жертву, он расчленяет её
своим тесаком. С каждым убийством его
здоровье и урон увеличиваются,
и вскоре погибель от его рук становится неизбежной'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


#4
@dp.message_handler(commands=['', ''])
async def handle__command(message: types.Message):  
    await send__photo(message)  

async def send__photo(message: types.Message):  
    photo_path = ''  
    caption = ''''''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#5
@dp.message_handler(commands=['Slardar', 'slardar'])
async def handle_Slardar_command(message: types.Message):  
    await send_Slardar_photo(message)  

async def send_Slardar_photo(message: types.Message):  
    photo_path = '2007/riba.jpg'  
    caption = '''Slardar
Всегда готовый найти и сокрушить врагов
Slardar шустро вползает в битву. Раскрыв
расположение противника и разрушив его броню,
он сокращает расстояние до жертвы и держит
её на месте сокрушительными водными всплесками
и оглушающими ударами своего внушительного трезубца'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#1
@dp.message_handler(commands=['SpiritBreaker', 'spiritbreaker'])
async def handle_SpiritBreaker_command(message: types.Message):  
    await send_SpiritBreaker_photo(message)  

async def send_SpiritBreaker_photo(message: types.Message):  
    photo_path = '2007/pivo.jpg'  
    caption = '''Spirit Breaker или Подпивасик)
Если появится подкова над вашей
головой ну вы уже явно не убежите)
Мобильный и агрессивный Spirit Breaker
носится по полю боя, навязывая
противнику схватку. Каждый оглушающий
удар его палицы выводит врага из строя.
Жертва попытается убежать,
но достаточно пары вардов,
и прятаться будет негде'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#2
@dp.message_handler(commands=['Sven', 'sven'])
async def handle_Sven_command(message: types.Message):  
    await send_Sven_photo(message)  

async def send_Sven_photo(message: types.Message):  
    photo_path = '2007/sven.jpg'  
    caption = '''Sven 
всегда рад сражению.
Он оглушает столпившихся врагов,
а после использования ульта,
увеличивающего урон героя,
противники погибают от пары ударов огромного меча.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#3
@dp.message_handler(commands=['Timbersaw', 'timbersaw'])
async def handle_Timbersaw_command(message: types.Message):  
    await send_Timbersaw_photo(message)  

async def send_Timbersaw_photo(message: types.Message):  
    photo_path = '2007/drova.jpg'  
    caption = '''Timbersaw
АХАХАХХА ЧЕЛОВЕК БЕНЗОПИЛА НЕНАВИДЕТЬ ДЕРЕВЬЯ ВСЕ ДЕРЕВЬЯ ДОЛЖНЫ БЫТЬ РАЗРУШЕНЫ 
ВЫХЫХВАЫВХЗПЫХЫПЗХЫПЗЫ ХУК МИНУС ДЕРЕВЬЯ ПИЛА ЛЕТАЕТ ПИЛА СТРЕЛЯЕТ АЗАЗАХАХАХАХАХ
ну короче угарный тип ломает деревья наносит урон кайф че)'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#4
@dp.message_handler(commands=['Tiny', 'tiny'])  
async def handle_Tiny_command(message: types.Message):  
    await send_Tiny_photo(message)  

async def send_Tiny_photo(message: types.Message):  
    photo_path = '2007/tiny.jpg'  
    caption = '''Tiny
становящийся больше и сильнее по ходу битвы,
устрашает противника. Он швыряет героев
и крипов в своих врагов или оглушает их
камнепадом. Набрав мощь, он с лёгкостью
разрушит вражескую базу'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#5
@dp.message_handler(commands=['TreantProtector', 'TreantProtector'])  
async def handle_TreantProtector_command(message: types.Message):  
    await send_TreantProtector_photo(message)  

async def send_TreantProtector_photo(message: types.Message):  
    photo_path = '2007/derevo.jpg'  
    caption = '''Treant Protector
Великодушный  защищает своих соратников
и союзные постройки восстанавливающей бронёй.
Незаметно перемещаясь меж деревьев,
он связывает врагов корнями
и передаёт их жизненные силы товарищам.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#6
@dp.message_handler(commands=['Tusk', 'tusk'])  
async def handle_Tusk_command(message: types.Message):  
    await send_Tusk_photo(message)  

async def send_Tusk_photo(message: types.Message):  
    photo_path = '2007/tusk.jpg'  
    caption = '''Tusk
 никогда не против затеять драку.
 Он отрезает врагам путь
 к отступлению стеной ледяных осколков,
 собирает союзников в гигантский снежный
 ком и влетает в нём в противников,
 завершая комбинацию фирменным
 сногсшибательным ударом.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


#8
@dp.message_handler(commands=['Underlord', 'underlord'])  
async def handle_Underlord_command(message: types.Message):  
    await send_Underlord_photo(message)  

async def send_Underlord_photo(message: types.Message):  
    photo_path = '2007/Undying.jpg'  
    caption = '''Underlord
обрушивает волны рокового пламени на врагов,
обездвиженных своей злобной хваткой.
Он ослабляет атаки противников одним
своим видом, упивается праздником смерти,
получая прилив сил с каждым недругом,
павшим в его присутствии,
и разрывает полотно реальности,
перемещаясь с союзниками по полю брани.
Жестокая кара ждёт каждого,
кто восстанет против Врогроша, Владыки бездны'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#9
@dp.message_handler(commands=['WraithKing', 'wraithking'])  
async def handle_WraithKing_command(message: types.Message):  
    await send_WraithKing_photo(message)  

async def send_WraithKing_photo(message: types.Message):  
    photo_path = '2007/WraithKing.jpg'  
    caption = '''Wraith King
бесстрашно рвётся в бой,
оглушая и разрубая врагов,
пока те не покорятся его воле.
Если противники справятся
с ним один раз, возрождающий
ульт даст Остариону ещё один
шанс сразить своих неприятелей'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#8
@dp.message_handler(commands=['BountyHunter', 'bountyhunter'])  
async def handle_BountyHunter_command(message: types.Message):  
    await send_BountyHunter_photo(message)  

async def send_BountyHunter_photo(message: types.Message):  
    photo_path = '2007/hunt.jpg'  
    caption = '''Bounty Hunter
незримо крадётся по следам своих
врагов и не даёт им скрыться из виду.
Когда его жертва падает замертво,
он и его союзники получают хорошую прибыль
Ну тупа инвиз + доп урон + кража денег имбулька'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['Clinkz', 'Clinkz'])  
async def handle_Clinkz_command(message: types.Message):  
    await send_Clinkz_photo(message)  

async def send_Clinkz_photo(message: types.Message):  
    photo_path = '2007/demon.jpg'  
    caption = '''Clinkz
незримо рыщет по полю битвы,
и от внезапного нападения не спастись никому.
Этот изворотливый лучник накрывает
врагов дождём огненных стрел,
а затем призывает в бой
армию пылающих собратьев'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)



@dp.message_handler(commands=['FacelessVoid', 'facelessvoid'])  
async def handle_FacelessVoid_command(message: types.Message):  
    await send_FacelessVoid_photo(message)  

async def send_FacelessVoid_photo(message: types.Message):  
    photo_path = '2007/vaid.jpg'  
    caption = '''Faceless Void
Для Faceless Void важна каждая секунда.
Он стремительно перемещается, ускорив
ход времени, а затем,
манипулируя им, уклоняется от ударов,
останавливает его на большой территории
и уничтожает замерших врагов.
Имея в своём распоряжении достаточно времени,
он становится невероятно могучим'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption) 


@dp.message_handler(commands=['EmberSpirit', 'emberspirit'])  
async def handle_EmberSpirit_command(message: types.Message):  
    await send_EmberSpirit_photo(message)  

async def send_EmberSpirit_photo(message: types.Message):  
    photo_path = '2007/ogon.jpg'  
    caption = '''Ember Spirit
Ловкий и неуловимый стремительно
атакует всех врагов вокруг
и связывает их горящими цепями.
Он быстро перемещается по полю
битвы с помощью своих взрывающихся копий,
и немногие смогут избежать пламени или обуздать его'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Gyrocopter', 'gyrocopter'])  
async def handle_Gyrocopter_command(message: types.Message):  
    await send_Gyrocopter_photo(message)  

async def send_Gyrocopter_photo(message: types.Message):  
    photo_path = '2007/sass.jpg'  
    caption = '''Gyrocopter
летает по полю боя, держа свой арсенал наготове.
Расстреливая всех ближайших врагов
из пушки и сокрушая их залпами ракет,
он с лёгкостью расправляется
с противниками, если наберёт достаточную мощь'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Luna', 'luna'])  
async def handle_Luna_command(message: types.Message):  
    await send_Luna_photo(message)  

async def send_Luna_photo(message: types.Message):  
    photo_path = '2007/luna.jpg'  
    caption = '''Luna
быстро врывается в битву,
кромсая противника своими отскакивающими
атаками. Если враги идут в наступление,
она призывает на помощь силу Луны
и сокрушает их жгучим лучом или лунным градом'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Medusa', 'Medusa'])  
async def handle_Medusa_command(message: types.Message):  
    await send_Medusa_photo(message)  

async def send_Medusa_photo(message: types.Message):  
    photo_path = '2007/medusa.jpg'  
    caption = '''Medusa
всегда возглавляет наступление.
Она сдерживает любое нападение
противника магическим щитом
и расправляется с группами врагов,
выпуская сразу несколько стрел.
Набрав полную силу,
она заставит окаменеть кого угодно'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['MonkeyKing', 'monkeyking'])  
async def handle_MonkeyKing_command(message: types.Message):  
    await send_MonkeyKing_photo(message)  

async def send_MonkeyKing_photo(message: types.Message):  
    photo_path = '2007/monkey.jpg'  
    caption = '''Monkey King
В поисках славной битвы скачет
по кронам деревьев и застаёт врагов врасплох,
стремительно нападая с высоты.
Готовый переломить ход сражения
верной армией солдат-обезьян,
этот неуловимый трюкач торжествует
в хаосе битвы и останавливает
своим легендарным посохом любого беглеца'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Morphling', 'morphling'])  
async def handle_Morphling_command(message: types.Message):  
    await send_Morphling_photo(message)  

async def send_Morphling_photo(message: types.Message):  
    photo_path = '2007/morf.jpg'  
    caption = '''Morphling
Благодаря способности
вливаться в любую ситуацию Morphling увёртлив
и смертоносен. Если его пытаются загнать в угол,
он уходит от врага на своей волне или увеличивает
здоровье и перемещается к созданному
им ложному двойнику героя'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['NagaSiren', 'NagaSiren'])  
async def handle_NagaSiren_command(message: types.Message):  
    await send_NagaSiren_photo(message)  

async def send_NagaSiren_photo(message: types.Message):  
    photo_path = '2007/seldka.jpg'  
    caption = '''Naga Siren
 отправляет в наступление свои копии,
 а затем связывает и убивает врагов.
 Своей песней она выводит противников
 из строя, позволяя подготовиться к
 нападению или немедленно отступить'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['PhantomLancer', 'PhantomLancer'])  
async def handle_PhantomLancer_command(message: types.Message):  
    await send_PhantomLancer_photo(message)  

async def send_PhantomLancer_photo(message: types.Message):  
    photo_path = '2007/makaka.jpg'  
    caption = '''Phantom Lancer
уничтожает противников бесконечным запасом
своих клонов. Его армия иллюзий сметает
вражеские силы и укрепления шквалом
молниеносных ударов, а заодно запутывает
противника, позволяя избежать опасности'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Razor', 'razor'])  
async def handle_Razor_command(message: types.Message):  
    await send_Razor_photo(message)  

async def send_Razor_photo(message: types.Message):  
    photo_path = '2007/razor.jpg'  
    caption = '''Razor
властитель смертоносной бури,
всегда готов к сражению.
Он поджаривает врагов расширяющимся
кольцом энергетической плазмы,
а также лишает их мощи, наращивая свою собственную'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Riki', 'riki'])  
async def handle_Riki_command(message: types.Message):  
    await send_Riki_photo(message)  

async def send_Riki_photo(message: types.Message):  
    photo_path = '2007/riki.jpg'  
    caption = '''Riki
крадётся по полю боя, скрываясь от глаз
противника. Он тщательно выжидает момент
и бросается в бой сквозь свою дымовую завесу,
нанося удар в спину ещё до того, как враги что-то поймут'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['ShadowFiend', 'ShadowFiend'])  
async def handle_ShadowFiend_command(message: types.Message):  
    await send_ShadowFiend_photo(message)  

async def send_ShadowFiend_photo(message: types.Message):  
    photo_path = '2007/sf.jpg'  
    caption = '''Shadow Fiend
КОЙЛ КОЙЛ КОЙЛ ДЕВКА ПРЯМО ПОДО МНОЙ
НУ ТУПА КОРОЧЕ ZXC ЧЕЛИК ДЛЯ 1 НА 1
ZXC СФЕЧИКАХ ВСЕ ГУЛИ ДЕД ИНСАЙДЫ ОНЛИ СФЧИК 
КРУТОЙ ТИПЧИК СКИЛЫ НАЙС ЗАБИРАЕТ ДУШИ ТВОИХ БЫВШИХ===)))'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Slark', 'slark'])  
async def handle_Slark_command(message: types.Message):  
    await send_Slark_photo(message)  

async def send_Slark_photo(message: types.Message):  
    photo_path = '2007/slark.jpg'  
    caption = '''Slark
способен впрыгнуть в гущу
сражения и выйти из него живым.
Он всегда рад приковать заблудшего
врага к месту, украсть его сущность
ударами своего кинжала, а в случае
чего мгновенно испариться'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['Sniper', 'sniper'])  
async def handle_Sniper_command(message: types.Message):  
    await send_Sniper_photo(message)  

async def send_Sniper_photo(message: types.Message):  
    photo_path = '2007/sna.jpg'  
    caption = '''Sniper
Сеять смерть на расстоянии — вот что
умеет лучше всего. Он сдерживает
своих врагов нескончаемым градом пуль,
а в подходящий момент добивает их смертельным выстрелом'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['TemplarAssassin', 'templarassassin'])  
async def handle_TemplarAssassin_command(message: types.Message):  
    await send_TemplarAssassin_photo(message)  

async def send_TemplarAssassin_photo(message: types.Message):  
    photo_path = '2007/templ.jpg'  
    caption = '''Templar Assassin
заполняет поле боя замедляющими ловушками
и прячется в невидимости,готовясь в любой
момент наброситься на жертву. Напав,
она пробивает врагов насквозь
своими псионическими клинками
и отражает ответные удары преломляющим щитом'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Terrorblade', 'terrorblade'])  
async def handle_Terrorblade_command(message: types.Message):  
    await send_Terrorblade_photo(message)  

async def send_Terrorblade_photo(message: types.Message):  
    photo_path = '2007/teror.jpg'  
    caption = '''Terrorblade
Своими могучими иллюзиями он обманывает
врагов и разрушает их постройки,
а если нужно предотвратить смерть
или ослабить соперника,
он меняется здоровьем с союзником или противником'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['TrollWarlord', 'TrollWarlord'])  
async def handle_TrollWarlord_command(message: types.Message):  
    await send_TrollWarlord_photo(message)  

async def send_TrollWarlord_photo(message: types.Message):  
    photo_path = '2007/TrollWarlord.jpg'  
    caption = '''Troll Warlord
Грозный боец Troll Warlord способен
сражаться как в ближнем,
так и в дальнем бою.
Он машет своими топорами
и крутит ими вокруг себя,
нанося удары всё быстрее,
и увеличивает скорость атаки
всех союзников, где бы они ни были'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Ursa', 'ursa'])  
async def handle_Ursa_command(message: types.Message):  
    await send_Ursa_photo(message)  

async def send_Ursa_photo(message: types.Message):  
    photo_path = '2007/ursa.jpg'  
    caption = '''Ursa
раздирает плоть своей жертвы,
с каждым ударом нанося ей всё
больше урона. Он ненадолго увеличивает
скорость своих ударов, замедляет
противников неподалёку и быстро
разрывает их на кусочки'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Viper', 'viper'])  
async def handle_Viper_command(message: types.Message):  
    await send_Viper_photo(message)  

async def send_Viper_photo(message: types.Message):  
    photo_path = '2007/vip.jpg'  
    caption = '''Viper
Ядовитый Viper несёт погибель
любой своей жертве. Токсины,
которыми он плюётся, ослабляют
и замедляют врага, а Viper
просто делает то, что умеет
лучше всего: продолжает источать яд.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Weaver', 'weaver'])  
async def handle_Weaver_command(message: types.Message):  
    await send_Weaver_photo(message)  

async def send_Weaver_photo(message: types.Message):  
    photo_path = '2007/Weaver.jpg'  
    caption = '''Weaver
сбегает от врагов лишь для того,
чтобы напасть вновь. Он способен
на время стать невидимым или вовсе
ускользнуть от смерти, вернув своё
местоположение и состояние здоровья
на несколько секунд назад.
Его изворотливость позволяет
доставлять врагам массу неприятностей'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['AncientApparition', 'ancientapparition'])  
async def handle_AncientApparition_command(message: types.Message):  
    await send_AncientApparition_photo(message)  

async def send_AncientApparition_photo(message: types.Message):  
    photo_path = '2007/101.jpg'  
    caption = '''Ancient Apparition
способный запустить мощный заряд льда
через всё поле битвы, может заморозить
раненых врагов до смерти,
где бы те ни находились.
Он держит врагов в напряжении,
замедляя их и помогая своим союзникам'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#1
@dp.message_handler(commands=['Disruptor', 'disruptor'])  
async def handle_Disruptor_command(message: types.Message):  
    await send_Disruptor_photo(message)  

async def send_Disruptor_photo(message: types.Message):  
    photo_path = '2007/102.jpg'  
    caption = '''Disruptor
мастерски разрушает планы врагов.
Он способен создать непроходимый
барьер и спустить на попавшихся в
ловушку врагов бурю безмолвия,
а если противник предпримет что-то
неожиданное, то Disruptor вернёт его туда,
где тот находился раньше'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#2
@dp.message_handler(commands=['Enchantress', 'enchantress'])  
async def handle_Enchantress_command(message: types.Message):  
    await send_Enchantress_photo(message)  

async def send_Enchantress_photo(message: types.Message):  
    photo_path = '2007/103.jpg'  
    caption = '''Enchantress
Опасная вблизи и смертоносная на расстоянии,
Enchantress пронзает врагов атаками,
которые становятся тем сильнее,
чем больше расстояние до цели.
Благодаря способности замедлять
своих врагов и зачаровать лесных
существ она всегда найдёт способ
одержать победу в схватке'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#3
@dp.message_handler(commands=['Grimstroke', 'grimstroke'])  
async def handle_Grimstroke_command(message: types.Message):  
    await send_Grimstroke_photo(message)  

async def send_Grimstroke_photo(message: types.Message):  
    photo_path = '2007/105.jpg'  
    caption = '''Grimstroke
Мастерски манипулируя битвой со стороны,
Grimstroke изучает каждого неприятеля до
самых мелочей, чтобы появиться из
чернильной тьмы и мановением кисти
оглушить врагов и связать их вместе.
Он с наслаждением досаждает противникам,
\натравливая на них своих фантомных рабов,
и аккуратно выбирает момент,
когда сможет отправить нескольких
врагов на тот свет судьбоносным взмахом кисти'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#4
@dp.message_handler(commands=['Jakiro', 'jakiro'])  
async def handle_Jakiro_command(message: types.Message):  
    await send_Jakiro_photo(message)  

async def send_Jakiro_photo(message: types.Message):  
    photo_path = '2007/106.jpg'  
    caption = '''Jakiro
Не довольствуясь одним только огнём,
близнецы примораживают к земле
пытающихся спастись противников,
а пока те горят, Jakiro разрушает
вражеские постройки своим жидким пламенем'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#5
@dp.message_handler(commands=['Leshrac', 'leshrac'])  
async def handle_Leshrac_command(message: types.Message):  
    await send_Leshrac_photo(message)  

async def send_Leshrac_photo(message: types.Message):  
    photo_path = '2007/108.jpg'  
    caption = '''Leshrac
Своими мощными заклинаниями Leshrac
одинаково хорошо справляется и с врагами,
и с их постройками. Расчищая путь своими разрушительными
способностями, он продвигается вглубь вражеской территории,
раскалывает землю под ногами противников,
оглушает их и оставляет на растерзание союзникам'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#6
@dp.message_handler(commands=['Lich', 'lich'])  
async def handle_Lich_command(message: types.Message):  
    await send_Lich_photo(message)  

async def send_Lich_photo(message: types.Message):  
    photo_path = '2007/110.jpg'  
    caption = '''Lich
Паря над полем битвы,
Lich подпитывает свои силы
союзными крипами и помогает
союзникам своим замедляющим холодом.
Если противники по глупости сбились
в кучу, то он расправится сразу со
всеми своим отскакивающим ультом'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#8
@dp.message_handler(commands=['Oracle', 'oracle'])  
async def handle_Oracle_command(message: types.Message):  
    await send_Oracle_photo(message)  

async def send_Oracle_photo(message: types.Message):  
    photo_path = '2007/112.jpg'  
    caption = '''Oracle
Аккуратно сочетая свои
замысловатые умения,
Oracle предрекает удел
своих друзей и врагов.
Окутав союзника неясным
будущим, он даёт ему
пожить ещё немного,
чтобы уничтожить противник
или даже избежать страшной участ'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#9
@dp.message_handler(commands=['OutworldDestroyer', 'outworlddestroyer'])  
async def handle_OutworldDestroyer_command(message: types.Message):  
    await send_OutworldDestroyer_photo(message)  

async def send_OutworldDestroyer_photo(message: types.Message):  
    photo_path = '2007/115.jpg'  
    caption = '''Outworld Destroyer
Похищая разум своих жертв, Outworld Destroyer
превращает чистый интеллект
в инструмент разрушения.
Ослабив врагов залпом магической энергии,
он проверяет их разум на прочность
и сжигает ману тем, кто выжил'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#10
@dp.message_handler(commands=['Pugna', 'pugna'])  
async def handle_Pugna_command(message: types.Message):  
    await send_Pugna_photo(message)  

async def send_Pugna_photo(message: types.Message):  
    photo_path = '2007/120.jpg'  
    caption = '''Pugna
Умелый колдун Pugna обращает силы противника
против него же, подрывая его
оборону и укрепления.
Пока его тотем бьёт ближайших врагов,
осмелившихся использовать магию,
сам Pugna вытягивает из них жизнь,
чтобы быть готовым к следующему наступлению'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#11
@dp.message_handler(commands=['QueenofPain', 'QueenofPain'])  
async def handle_QueenofPain_command(message: types.Message):  
    await send_QueenofPain_photo(message)  

async def send_QueenofPain_photo(message: types.Message):  
    photo_path = '2007/125.jpg'  
    caption = '''Queen of Pain
нападает без предупреждения,
уничтожая собравшихся вместе
противников своим оглушающим криком.
Если враг смог сдержать её натиск,
она не позволяет ему отступить,
замедляя броском кинжала'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

#13
@dp.message_handler(commands=['Ringmaster', 'Ringmaster'])  
async def handle_Ringmaster_command(message: types.Message):  
    await send_Ringmaster_photo(message)  

async def send_Ringmaster_photo(message: types.Message):  
    photo_path = '2007/130.jpg'  
    caption = '''Ringmaster
Поле боя — театр, а Колиостро на нём тот ещё режиссёр-затейник.
Управляя боями с присущим артисту шиком, он укрощает врагов
грозным кнутом и бесконечным запасом ножей
укрывает союзников от опасности в своём хитроумном
ящике и всегда собирает толпу невольных зрителей,
устремивших взор на его завораживающее колесо'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#14

@dp.message_handler(commands=['Rubick', 'Rubick'])  
async def handle_Rubick_command(message: types.Message):  
    await send_Rubick_photo(message)  

async def send_Rubick_photo(message: types.Message):  
    photo_path = '2007/159.jpg'  
    caption = '''Rubick
неустанно ищет полезные вражеские
способности, которые можно использовать
против их бывших владельцев. Поднимая
противников в воздух и указывая,
где им упасть, Rubick сеет хаос в их рядах'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#15
@dp.message_handler(commands=['ShadowDemon', 'ShadowDemon'])  
async def handle_ShadowDemon_command(message: types.Message):  
    await send_ShadowDemon_photo(message)  

async def send_ShadowDemon_photo(message: types.Message):  
    photo_path = '2007/160.jpg'  
    caption = '''Shadow Demon
опасен своей способностью наносить
урон и разведывать поле боя облаками
демонического яда. Он ненадолго изгоняет
врага в иной мир,
позволяя товарищам оказать жертве
тёплый приём, накладывает на противников
проклятья и призывает иллюзии,
обращая силу соперников против них самих'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#16
@dp.message_handler(commands=['ShadowShaman', 'ShadowShaman'])  
async def handle_ShadowShaman_command(message: types.Message):  
    await send_ShadowShaman_photo(message)  

async def send_ShadowShaman_photo(message: types.Message):  
    photo_path = '2007/170.jpg'  
    caption = '''Shadow Shaman
быстро расчищает своей команде
путь до вражеского Древнего. Он способен
поразить противников ударом
энергии, превратить нападающего
в беспомощное животное и призвать
могучие змеиные тотемы, которые
с лёгкостью разрушат вражеские постройки'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#17
@dp.message_handler(commands=['Silencer', 'Silencer'])  
async def handle_Silencer_command(message: types.Message):  
    await send_Silencer_photo(message)  

async def send_Silencer_photo(message: types.Message):  
    photo_path = '2007/200.jpg'  
    caption = '''Silencer
изменяет ход каждого сражения,
запрещая врагам использовать заклинания.
Он кромсает противников глефами и крадёт
у них интеллект, не давая соперникам
получить преимущество.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#18
@dp.message_handler(commands=['SkywrathMage', 'SkywrathMage'])  
async def handle_SkywrathMage_command(message: types.Message):  
    await send_SkywrathMage_photo(message)  

async def send_SkywrathMage_photo(message: types.Message):  
    photo_path = '2007/210.jpg'  
    caption = '''Skywrath Mage
Смертоносный, но хрупкий Skywrath Mage быстро
уничтожает врагов залпами мощной магии.
Он сотрёт в порошок кого угодно благодаря
своей способности обезмолвить противника,
сделав его уязвимым к заклинаниям'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#19
@dp.message_handler(commands=['StormSpirit', 'StormSpirit'])  
async def handle_StormSpirit_command(message: types.Message):  
    await send_StormSpirit_photo(message)  

async def send_StormSpirit_photo(message: types.Message):  
    photo_path = '2007/300.jpg'  
    caption = '''Storm Spirit
не пропускает ни одного сражения.
Он молнией проносится по карте,
со всех сторон бьёт врагов своими
взрывными копиями и заряженными
атаками и исчезает с поля битвы,
прежде чем шокированные противники
успеют среагировать'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)
#20

@dp.message_handler(commands=['NaturesProphet', 'NaturesProphet'])  
async def handle_NaturesProphet_command(message: types.Message):  
    await send_NaturesProphet_photo(message)  

async def send_NaturesProphet_photo(message: types.Message):  
    photo_path = '2007/111.jpg'  
    caption = '''Nature's Prophet
будто вездусущ: вот он в гуще боя,
а вот уже подготавливает ресурсы
для следующей атаки.
Благодаря способности телепортироваться
в любое место и мгновенно создать
армию воинов-энтов, он нападает
на противников, когда те этого
не ожидают. ( он по фарму чемпион'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Tinker', 'Tinker'])  
async def handle_Tinker_command(message: types.Message):  
    await send_Tinker_photo(message)  

async def send_Tinker_photo(message: types.Message):  
    photo_path = '2007/350.jpg'  
    caption = '''Tinker
сокрушает врагов своей армией механизмов
и другими смертоносными устройствами.
Набрав мощь, он способен нападать
по нескольким фронтам благодаря ульту,
который перезаряжает все его способности.'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Warlock', 'Warlock'])  
async def handle_Warlock_command(message: types.Message):  
    await send_Warlock_photo(message)  

async def send_Warlock_photo(message: types.Message):  
    photo_path = '2007/Warlock.jpg'  
    caption = '''Warlock
Призвав на помощь демона-голема,
Warlock уничтожает врагов и их постройки.
Но чернокнижник способен сеять хаоc
и без посторонней помощи: одним лишь
словом он излечивает союзников и калечит
противников — или связывает врагов в общей агонии'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['WitchDoctor', 'WitchDoctor'])  
async def handle_WitchDoctor_command(message: types.Message):  
    await send_WitchDoctor_photo(message)  

async def send_WitchDoctor_photo(message: types.Message):  
    photo_path = '2007/WitchDoctor.jpg'  
    caption = '''Witch Doctor
идеально дополняет любую команду.
Мало кто сравнится
с ним по универсальности:
он может постепенно излечивать
товарищей, оглушать и насмерть
проклинать врагов, а также уничтожать
их своим мощным ультом'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Zeus', 'Zeus'])  
async def handle_Zeus_command(message: types.Message):  
    await send_Zeus_photo(message)  

async def send_Zeus_photo(message: types.Message):  
    photo_path = '2007/500.jpg'  
    caption = '''Zeus
Никому не спастись от ярости Zeus.
Он использует молнию, чтобы
разведывать ближайшие территории,
пускает заряд электричества,
скачущий по нескольким врагам,
или призывает вселяющий ужас шквал
молний на всех противников сразу.
Zeus найдет врагов, где бы те ни были'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Venomancer', 'venomancer'])  
async def handle_Venomancer_command(message: types.Message):  
    await send_Venomancer_photo(message)  

async def send_Venomancer_photo(message: types.Message):  
    photo_path = '2007/Venomancer.jpg'  
    caption = '''Venomancer
несёт своим врагам медленную смерть.
Он взращивает бесконечную армию прыскающих
ядом защитников, а стоит неприятелям показаться рядом,
он выпускает огромное облако яда,
надолго ослабляющего недругов'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Visage', 'visage'])  
async def handle_Visage_command(message: types.Message):  
    await send_Visage_photo(message)  

async def send_Visage_photo(message: types.Message):  
    photo_path = '2007/Visage.jpg'  
    caption = '''Visage
Разведывая смертоносными гаргульями поле боя,
Visage покрывает себя бронёй и ищет битвы.
Оказавшись рядом со схваткой,
он обращает страдания тех, кто получает урон,
в мощные заряды энергии и сокрушает ими врагов'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['voidspirit', 'voidspirit'])  
async def handle_VoidSpirit_command(message: types.Message):  
    await send_VoidSpirit_photo(message)  

async def send_VoidSpirit_photo(message: types.Message):  
    photo_path = '2007/VoidSpirit.jpg'  
    caption = '''Void Spirit
Дух пустоты хранит секреты,
которые могут расколоть сознание смертного.
Он покидает Сокрытый храм,
несёт дозор над всем полем битвы
и по своей воле может покинуть мир
смертных и вернуться в него. В мгновения
нужды взывая к защите скрытой реальности,
он легко обходит врагов, чтобы ударить,
откуда он сам пожелает'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)


@dp.message_handler(commands=['Windranger', 'windranger'])  
async def handle_Windranger_command(message: types.Message):  
    await send_Windranger_photo(message)  

async def send_Windranger_photo(message: types.Message):  
    photo_path = '2007/Windranger.jpg'  
    caption = '''Windranger
Проворная и ловкая Windranger
всегда поджидает подходящего
момента для нападения. Она постояннo
в движении — даже когда расчищает путь
смертоносным выстрелом или связывает врагов,
чтобы нашпиговать их стрелами'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['WinterWyvern', 'WinterWyvern'])  
async def handle_WinterWyvern_command(message: types.Message):  
    await send_WinterWyvern_photo(message)  

async def send_WinterWyvern_photo(message: types.Message):  
    photo_path = '2007/WinterWyvern.jpg'  
    caption = '''Winter Wyvern
бороздит небо над полем боя,
замедляя врагов жгучим льдом.
Если враги по глупости столпятся,
она обернёт их
против одного из товарищей
и обдаст всех ледяными осколками'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['VengefulSpirit', 'VengefulSpirit'])  
async def handle_VengefulSpirit_command(message: types.Message):  
    await send_VengefulSpirit_photo(message)  

async def send_VengefulSpirit_photo(message: types.Message):  
    photo_path = '2007/VengefulSpirit.jpg'  
    caption = '''Vengeful Spirit
напоминает о себе даже после смерти.
Она постоянно сеет хаос в рядах врагов,
обмениваясь местами с другими героями неподалёку,
оглушая врагов и ослабляя того, кто её одолеет'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['Snapfire', 'Snapfire'])  
async def handle_Snapfire_command(message: types.Message):  
    await send_Snapfire_photo(message)  

async def send_Snapfire_photo(message: types.Message):  
    photo_path = '2007/Snapfire.jpg'  
    caption = '''Snapfire
 будет рада как отстрелить кому-нибудь
 ноги из своего верного дробовика,
 так и накормить всех до отвала своим вкусным
 , но немного взрывным печеньем.
 Беатрикс с удовольствием рассекает по
 полю битвы на своей драконьей жабе Мортимере,
 готовая выкосить врагов своей самодельной
 крупнокалиберной пушкой и добить их
 залпом лавовых шаров Мортимера'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)

@dp.message_handler(commands=['SandKing', 'SandKing'])  
async def handle_SandKing_command(message: types.Message):  
    await send_SandKing_photo(message)  

async def send_SandKing_photo(message: types.Message):  
    photo_path = '2007/SandKing.jpg'  
    caption = '''Sand King
Немногие способны пережить нападение Sand King.
Он разрушает смертоносными волнами ульта всё вокруг себя,
скрывается от ответных ударов в
песчаной буре и оглушает врагов, поддевая их снизу'''
    
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo, caption=caption)








if __name__ == '__main__':  
    executor.start_polling(dp, skip_updates=True)


                



                

                
