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

#Queried at 2021-12-09T18:42:47.871476
PlayerIDs['Nigma Galaxy'] = collections.OrderedDict()
PlayerIDs['Nigma Galaxy']['iLTW'] = 113995822 # 76561198074261550
PlayerIDs['Nigma Galaxy']['Miracle'] = 105248644 # 76561198065514372
PlayerIDs['Nigma Galaxy']['MinDContRoL'] = 34505203 # 76561197994770931
PlayerIDs['Nigma Galaxy']['Gh'] = 101356886 # 76561198061622614
PlayerIDs['Nigma Galaxy']['KuroKy'] = 82262664 # 76561198042528392
ValidityTime['Nigma Galaxy'] = datetime.datetime(2021, 4, 10, 0, 0, 0, 0)
_TeamIDs['Nigma Galaxy'] = 7554697

PlayerIDs['Alliance'] = collections.OrderedDict()
PlayerIDs['Alliance']['Nikobaby'] = 412753955 # 76561198373019683
PlayerIDs['Alliance']['Supream'] = 58513047 # 76561198018778775
PlayerIDs['Alliance']['LESLÃO'] = 87063175 # 76561198047328903
PlayerIDs['Alliance']['Aramis'] = 92601861 # 76561198052867589
PlayerIDs['Alliance']['Handsken'] = 18180970 # 76561197978446698
ValidityTime['Alliance'] = datetime.datetime(2021, 11, 18, 0, 0, 0, 0)
_TeamIDs['Alliance'] = 111474

PlayerIDs['Team Liquid'] = collections.OrderedDict()
PlayerIDs['Team Liquid']['MATUMBAMAN'] = 72312627 # 76561198032578355
PlayerIDs['Team Liquid']['m1CKe'] = 152962063 # 76561198113227791
PlayerIDs['Team Liquid']['zai'] = 73562326 # 76561198033828054
PlayerIDs['Team Liquid']['Boxi'] = 77490514 # 76561198037756242
PlayerIDs['Team Liquid']['iNsania'] = 54580962 # 76561198014846690
ValidityTime['Team Liquid'] = datetime.datetime(2021, 11, 17, 0, 0, 0, 0)
_TeamIDs['Team Liquid'] = 2163

PlayerIDs['Team Secret'] = collections.OrderedDict()
PlayerIDs['Team Secret']['Nisha'] = 121769650 # 76561198082035378
PlayerIDs['Team Secret']['SumaiL'] = 111620041 # 76561198071885769
PlayerIDs['Team Secret']['iceiceice'] = 84772440 # 76561198045038168
PlayerIDs['Team Secret']['YapzOr'] = 89117038 # 76561198049382766
PlayerIDs['Team Secret']['Puppey'] = 87278757 # 76561198047544485
ValidityTime['Team Secret'] = datetime.datetime(2021, 11, 18, 0, 0, 0, 0)
_TeamIDs['Team Secret'] = 1838315

PlayerIDs['Tundra Esports'] = collections.OrderedDict()
PlayerIDs['Tundra Esports']['skiter'] = 100058342 # 76561198060324070
PlayerIDs['Tundra Esports']['Nine'] = 94786276 # 76561198055052004
PlayerIDs['Tundra Esports']['33'] = 86698277 # 76561198046964005
PlayerIDs['Tundra Esports']['Sneyking'] = 10366616 # 76561197970632344
PlayerIDs['Tundra Esports']['Fata'] = 86799300 # 76561198047065028
ValidityTime['Tundra Esports'] = datetime.datetime(2021, 4, 6, 0, 0, 0, 0)
_TeamIDs['Tundra Esports'] = 8291895

PlayerIDs['Team Tickles'] = collections.OrderedDict()
PlayerIDs['Team Tickles']['dyrachyo'] = 116934015 # 76561198077199743
PlayerIDs['Team Tickles']['BOOM'] = 190826739 # 76561198151092467
PlayerIDs['Team Tickles']['Ace'] = 97590558 # 76561198057856286
PlayerIDs['Team Tickles']['tOfu'] = 16497807 # 76561197976763535
PlayerIDs['Team Tickles']['Seleri'] = 91730177 # 76561198051995905
ValidityTime['Team Tickles'] = datetime.datetime(2021, 9, 14, 0, 0, 0, 0)
_TeamIDs['Team Tickles'] = 8599101

PlayerIDs['Coolguys'] = collections.OrderedDict()
PlayerIDs['Coolguys']['ThuG'] = 107855479 # 76561198068121207
PlayerIDs['Coolguys']['Noob'] = 140297552 # 76561198100563280
PlayerIDs['Coolguys']['Funn1k'] = 86723143 # 76561198046988871
PlayerIDs['Coolguys']['OmaR'] = 152168157 # 76561198112433885
PlayerIDs['Coolguys']['dnz'] = 98167706 # 76561198058433434
ValidityTime['Coolguys'] = datetime.datetime(2021, 9, 14, 0, 0, 0, 0)
_TeamIDs['Coolguys'] = 8598999

#Queried at 2021-12-14T17:33:08.393564
PlayerIDs['Team Spirit'] = collections.OrderedDict()
PlayerIDs['Team Spirit']['Yatoro'] = 321580662 # 76561198281846390
PlayerIDs['Team Spirit']['TORONTOTOKYO'] = 431770905 # 76561198392036633
PlayerIDs['Team Spirit']['CoLLapse'] = 302214028 # 76561198262479756
PlayerIDs['Team Spirit']['Mira'] = 256156323 # 76561198216422051
PlayerIDs['Team Spirit']['Miposhka'] = 113331514 # 76561198073597242
ValidityTime['Team Spirit'] = datetime.datetime(2021, 3, 1, 0, 0, 0, 0)
_TeamIDs['Team Spirit'] = 7119388

PlayerIDs['Natus Vincere'] = collections.OrderedDict()
PlayerIDs['Natus Vincere']['VTune'] = 152455523 # 76561198112721251
PlayerIDs['Natus Vincere']['Noone'] = 106573901 # 76561198066839629
PlayerIDs['Natus Vincere']['GeneRaL'] = 89550641 # 76561198049816369
PlayerIDs['Natus Vincere']['ALOHADANCE'] = 123051238 # 76561198083316966
PlayerIDs['Natus Vincere']['Solo'] = 134556694 # 76561198094822422
ValidityTime['Natus Vincere'] = datetime.datetime(2021, 9, 22, 0, 0, 0, 0)
_TeamIDs['Natus Vincere'] = 36


path = None
engine = InitTeamDB(path)
Session = sessionmaker(bind=engine)
session = Session()


def make_db():
    import_from_old(_TeamIDs, PlayerIDs, ValidityTime, session)


make_db()