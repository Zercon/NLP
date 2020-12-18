from yargy import rule
from yargy import and_
from yargy import or_
from yargy import not_
from yargy.interpretation import fact
from yargy.interpretation import attribute
from yargy.predicates import type as myType
from yargy.predicates import *
from yargy.pipelines import morph_pipeline

Address = fact(
    'Address',
    [attribute('city', None), 
     attribute('street', None),
     attribute('building', None),
     attribute('appartment', None)]
)


City = fact(
    'city', 
    ['type', 'title']
)


CITY_title = morph_pipeline([
    'липецк', 
    'сургут', 
    'нальчик', 
    'москва', 
    'санкт-петербург', 
    'питер', 
    'нижний новгород', 
    'видное'
]).interpretation(
    City.title.normalized()
)


CITY = rule(
    normalized('город').optional().interpretation(City.type),
    CITY_title,
    eq(';').optional()
).interpretation(
    City
)


Street = fact(
    'street',
    ['type', 'title']
)


STREET_type = morph_pipeline([
    'улица',
    'проспект', 
    'шоссе', 
    'бульвар', 
    'тракт', 
    'микрорайон', 
    'проезд', 
    'аллеи'
]).interpretation(
    Street.type
)


STREET_title = morph_pipeline([
    'комсомольский', 
    'катукова', 
    'рабочая', 
    'доватора', 
    'бехтеева', 
    'артема',
    'полиграфическая', 
    'каширское', 
    'октябрьский', 
    'миттова', 
    'алтуфьевское', 
    'югорская', 
    '30 лет победы', 
    'горького', 
    'крылова', 
    'хамовнический вал', 
    'парковая', 
    'пришвина', 
    'Старый Гай',
    'школьная', 
    'юрия гагарина', 
    'гагарина', 
    'юнтоловский', 
    'меркулова', 
    'октябрьская', 
    'тюменский', 
    'олимпийский', 
    'фармана салманова', 
    'мунарева', 
    'новогиреевская', 
    'мусы джалиля', 
    'зеленые',
    'дмитрия ульянова', 
    'маршала захарова', 
    'Кавказский', 
    'зелинского', 
    'московская', 
    'минина', 
    'береговая', 
    'кусковская', 
    'щелковское', 
    'марьинский парк', 
    '3 почтовое отделение', 
    'июльских дней', 
    'семена билецкого', 
    'антонова овсиенко', 
    'генерала армии епишева', 
    'академика байкова', 
    'подзаборного байкова', 
    'монтажника байкова', 
    'джона рида', 
]).interpretation(
    Street.title
)


STREET = rule(
    rule(
        STREET_type,
        myType('RU').optional()
    ).optional(),
    STREET_title,
    STREET_type.optional()
).interpretation(
    Street
)


Building = fact(
    'building',
    ['house', 'corpus', 'structure']
)


HOUSE_number = rule(
    rule(
        myType('INT')
    ),
    rule(
        '/',
        myType('INT')
    ).optional(),
    rule(myType('RU').optional()),
).interpretation(
    Building.house
)


HOUSE = rule(
    normalized('дом').repeatable().optional(),
    normalized('номер').optional(),
    HOUSE_number
)


CORPUS_type = morph_pipeline([
    'корпус', 
    'к'
])


CORPUS = rule(
    CORPUS_type,
    myType('INT').interpretation(Building.corpus)
)


STRUCTURE_type = morph_pipeline([
    'строение', 
    'ст'
])


STRUCTURE = rule(
    STRUCTURE_type,
    myType('INT').interpretation(Building.structure)
)


BUILDING = rule(
    HOUSE,
    CORPUS.optional(),
    STRUCTURE.optional()
).interpretation(
    Building
)


APPARTMENT = rule(
    normalized('квартира'),
    myType('INT').interpretation(Address.appartment)
)



ADDRESS = rule(
    CITY.interpretation(Address.city).optional(), 
    STREET.interpretation(Address.street),
    BUILDING.interpretation(Address.building).optional(),
    APPARTMENT.optional()
).interpretation(
    Address
)