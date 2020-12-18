from yargy import rule
from yargy import and_
from yargy import or_
from yargy import not_
from yargy.interpretation import fact
from yargy.interpretation import attribute
from yargy.predicates import type as myType
from yargy.predicates import *
from yargy.pipelines import morph_pipeline

FullName = fact(
    'Name',
    ['name','surn','patr']
)

NAME = morph_pipeline([
    'Петр',
    'дмитрий',
    'елена',
    'юлия',
    'людмила',
    'елена',
    'анюта',
    'артем',
    'олег'
]).interpretation(
    FullName.name
)

PATR = morph_pipeline([
    'Васильевич',
    'вячеславович',
    'владимировна',
    'михайловна',
    'владимировна',
    'витальевич',
    'викторович'
]).interpretation(
    FullName.patr
)

SURN = morph_pipeline([
    'Иванов',
    'шипицын',
    'басалаева',
    'глушенков',
    'терентьева',
    'веретельников'
]).interpretation(
    FullName.surn
)

FULLNAME = or_(
    rule(
    NAME.interpretation(FullName.name),
    SURN.interpretation(FullName.surn).optional(),
    PATR.interpretation(FullName.patr).optional()
),rule(
    NAME.interpretation(FullName.name),
    PATR.interpretation(FullName.patr).optional(),
    SURN.interpretation(FullName.surn).optional()
),rule(
    SURN.interpretation(FullName.surn),
    PATR.interpretation(FullName.patr).optional(),
    NAME.interpretation(FullName.name).optional()
),rule(
    SURN.interpretation(FullName.surn),
    NAME.interpretation(FullName.name).optional(),
    PATR.interpretation(FullName.patr).optional()
),rule(
    NAME.interpretation(FullName.name).optional(),
    PATR.interpretation(FullName.patr),
    SURN.interpretation(FullName.surn).optional()
),rule(    
    SURN.interpretation(FullName.surn).optional(),
    PATR.interpretation(FullName.patr),
    NAME.interpretation(FullName.name).optional()
)
).interpretation(
    FullName
)