import collections
import time
import datetime
from replay_finder.team_info import import_from_old, InitTeamDB
from sqlalchemy.orm import sessionmaker
from util import convert_to_32_bit, convert_to_64_bit

def getSteam64From32(input32):
    return 76561197960265728 + input32


def getSteam32From64(input64):
    return input64 - 76561197960265728


PlayerIDs = {}
ValidityTime = {}
_TeamIDs = {}

PlayerIDs['OG'] = collections.OrderedDict()
PlayerIDs['OG']['midone'] = 76561198076851106
PlayerIDs['OG']['Topson'] = 76561198054320440
PlayerIDs['OG']['Ceb'] = convert_to_64_bit(88271237)
PlayerIDs['OG']['Saksa'] = 76561198064001473
PlayerIDs['OG']['N0tail'] = 76561197979938082
ValidityTime['OG'] = datetime.datetime(2020, 1, 29, 0, 0, 0, 0)
_TeamIDs['OG'] = 2586976

#Queried at 2021-11-16T17:14:18.556747
PlayerIDs['Evil Geniuses'] = collections.OrderedDict()
PlayerIDs['Evil Geniuses']['Arteezy'] = convert_to_64_bit(86745912)
PlayerIDs['Evil Geniuses']['Abed'] = convert_to_64_bit(154715080)
PlayerIDs['Evil Geniuses']['iceiceice'] = convert_to_64_bit(84772440)
PlayerIDs['Evil Geniuses']['Cr1t'] = convert_to_64_bit(25907144)
PlayerIDs['Evil Geniuses']['Fly'] = convert_to_64_bit(94155156)
ValidityTime['Evil Geniuses'] = datetime.datetime(2020, 11, 14, 0, 0, 0, 0)
_TeamIDs['Evil Geniuses'] = 39

#Queried at 2021-11-16T17:56:59.051731
PlayerIDs['PSG.LGD'] = collections.OrderedDict()
PlayerIDs['PSG.LGD']['Ame'] = 898754153 #76561198859019881
PlayerIDs['PSG.LGD']['NothingToSay'] = 173978074 #76561198134243802
PlayerIDs['PSG.LGD']['Faithbian'] = 118134220 #76561198078399948
PlayerIDs['PSG.LGD']['XinQ'] = 157475523 #76561198117741251
PlayerIDs['PSG.LGD']['y'] = 111114687 #76561198071380415
ValidityTime['PSG.LGD'] = datetime.datetime(2020, 9, 16, 0, 0, 0, 0)
_TeamIDs['PSG.LGD'] = 15

#Queried at 2021-11-17T00:24:11.780161
PlayerIDs['Virtus.pro'] = collections.OrderedDict()
PlayerIDs['Virtus.pro']['Nightfall'] = 124801257 # 76561198085066985
PlayerIDs['Virtus.pro']['gpk'] = 480412663 # 76561198440678391
PlayerIDs['Virtus.pro']['DM'] = 56351509 # 76561198016617237
PlayerIDs['Virtus.pro']['Save'] = 317880638
PlayerIDs['Virtus.pro']['Kingslayer'] = 187758589 # 76561198148024317
ValidityTime['Virtus.pro'] = datetime.datetime(2020, 11, 5, 0, 0, 0, 0)
_TeamIDs['Virtus.pro'] = 1883502

PlayerIDs['OG'] = collections.OrderedDict()
PlayerIDs['OG']['Yuragi'] = 167976729 # 76561198128242457
PlayerIDs['OG']['bzm'] = 93618577 # 76561198053884305
PlayerIDs['OG']['ATF'] = 183719386 # 76561198143985114
PlayerIDs['OG']['Taiga'] = 401792574 # 76561198362058302
PlayerIDs['OG']['Misha'] = 90125566 # 76561198050391294
ValidityTime['OG'] = datetime.datetime(2021, 11, 21, 0, 0, 0, 0)
_TeamIDs['OG'] = 2586976

path = None
engine = InitTeamDB(path)
Session = sessionmaker(bind=engine)
session = Session()


def make_db():
    import_from_old(_TeamIDs, PlayerIDs, ValidityTime, session)


make_db()