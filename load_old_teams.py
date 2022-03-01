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
PlayerIDs['Virtus.pro']['Pure'] = 331855530
PlayerIDs['Virtus.pro']['gpk'] = 480412663 # 76561198440678391
PlayerIDs['Virtus.pro']['DM'] = 56351509 # 76561198016617237
PlayerIDs['Virtus.pro']['yamich'] = 9403474
PlayerIDs['Virtus.pro']['Xakoda'] = 217472313
ValidityTime['Virtus.pro'] = datetime.datetime(2022, 1, 5, 0, 0, 0, 0)
_TeamIDs['Virtus.pro'] = 1883502

PlayerIDs['OG'] = collections.OrderedDict()
PlayerIDs['OG']['Yuragi'] = 167976729 # 76561198128242457
PlayerIDs['OG']['bzm'] = 93618577 # 76561198053884305
PlayerIDs['OG']['ATF'] = 183719386 # 76561198143985114
PlayerIDs['OG']['Taiga'] = 401792574 # 76561198362058302
PlayerIDs['OG']['Chu'] = 117483894
# PlayerIDs['OG']['Misha'] = 90125566 # 76561198050391294
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
PlayerIDs['Tundra Esports']['Saksa'] = 103735745 # 76561198047065028
PlayerIDs['Tundra Esports']['Sneyking'] = 10366616 # 76561197970632344
ValidityTime['Tundra Esports'] = datetime.datetime(2021, 4, 6, 0, 0, 0, 0)
_TeamIDs['Tundra Esports'] = 8291895

PlayerIDs['Gladiators'] = collections.OrderedDict()
PlayerIDs['Gladiators']['dyrachyo'] = 116934015 # 76561198077199743
PlayerIDs['Gladiators']['BOOM'] = 190826739 # 76561198151092467
PlayerIDs['Gladiators']['Ace'] = 97590558 # 76561198057856286
PlayerIDs['Gladiators']['tOfu'] = 16497807 # 76561197976763535
PlayerIDs['Gladiators']['Seleri'] = 91730177 # 76561198051995905
ValidityTime['Gladiators'] = datetime.datetime(2021, 9, 14, 0, 0, 0, 0)
_TeamIDs['Gladiators'] = 8599101

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
# PlayerIDs['Team Spirit']['Mira'] = 256156323 # 76561198216422051
PlayerIDs['Team Spirit']['RodjER'] = 159020918
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

#Queried at 2022-02-16T17:26:10.161275
PlayerIDs['Entity'] = collections.OrderedDict()
PlayerIDs['Entity']['Crystallis'] = 127617979 # 76561198087883707
PlayerIDs['Entity']['Stormstormer'] = 96803083 # 76561198057068811
PlayerIDs['Entity']['Tobi'] = 140288368 # 76561198100554096
PlayerIDs['Entity']['Kataomi'] = 196878136 # 76561198157143864
PlayerIDs['Entity']['Fishman'] = 127565532 # 76561198087831260
ValidityTime['Entity'] = datetime.datetime(2021, 11, 23, 0, 0, 0, 0)
_TeamIDs['Entity'] = 8605863

PlayerIDs['Brame'] = collections.OrderedDict()
PlayerIDs['Brame']['Focus'] = 196490133 # 76561198156755861
PlayerIDs['Brame']['ThuG'] = 107855479 # 76561198068121207
PlayerIDs['Brame']['Eleven'] = 27178898 # 76561197987444626
PlayerIDs['Brame']['dEsire'] = 115464954 # 76561198075730682
PlayerIDs['Brame']['SsaSpartan'] = 92949094 # 76561198053214822
ValidityTime['Brame'] = datetime.datetime(2022, 1, 1, 0, 0, 0, 0)
_TeamIDs['Brame'] = 8112124

#Queried at 2022-02-23T22:52:32.610467
PlayerIDs['Fnatic'] = collections.OrderedDict()
PlayerIDs['Fnatic']['Raven'] = 132309493 # 76561198092575221
PlayerIDs['Fnatic']['Armel'] = 164532005 # 76561198124797733
PlayerIDs['Fnatic']['Jabz'] = 100471531 # 76561198060737259
PlayerIDs['Fnatic']['DJ'] = 102099826 # 76561198062365554
PlayerIDs['Fnatic']['Jaunuel'] = 148526973 # 76561198108792701
ValidityTime['Fnatic'] = datetime.datetime(2021, 11, 20, 0, 0, 0, 0)
_TeamIDs['Fnatic'] = 350190

PlayerIDs['Nigma Galaxy SEA'] = collections.OrderedDict()
PlayerIDs['Nigma Galaxy SEA']['inYourdreaM'] = 181716137 # 76561198141981865
PlayerIDs['Nigma Galaxy SEA']['w33'] = 86700461
PlayerIDs['Nigma Galaxy SEA']['mizu'] = 91369376 # 76561198051635104
PlayerIDs['Nigma Galaxy SEA']['Jhocam'] = 152859296 # 76561198113125024
PlayerIDs['Nigma Galaxy SEA']['poloson'] = 76904792 # 76561198037170520
ValidityTime['Nigma Galaxy SEA'] = datetime.datetime(2021, 9, 14, 0, 0, 0, 0)
_TeamIDs['Nigma Galaxy SEA'] = 8572181

PlayerIDs['TSM FTX'] = collections.OrderedDict()
PlayerIDs['TSM FTX']['Timado'] = 97658618 # 76561198057924346
PlayerIDs['TSM FTX']['Bryle'] = 238239590 # 76561198198505318
PlayerIDs['TSM FTX']['SabeRLighT'] = 126212866 # 76561198086478594
PlayerIDs['TSM FTX']['MoonMeander'] = 38628747 # 76561197998894475
PlayerIDs['TSM FTX']['DuBu'] = 145550466 # 76561198105816194
ValidityTime['TSM FTX'] = datetime.datetime(2021, 9, 14, 0, 0, 0, 0)
_TeamIDs['TSM FTX'] = 8260983

PlayerIDs['BOOM Esports'] = collections.OrderedDict()
PlayerIDs['BOOM Esports']['JaCkky'] = 392565237 # 76561198352830965
PlayerIDs['BOOM Esports']['Yopaj'] = 324277900 # 76561198284543628
PlayerIDs['BOOM Esports']['Fbz'] = 156328257 # 76561198116593985
PlayerIDs['BOOM Esports']['TIMS'] = 155494381 # 76561198115760109
PlayerIDs['BOOM Esports']['skem'] = 100594231 # 76561198060859959
ValidityTime['BOOM Esports'] = datetime.datetime(2021, 9, 14, 0, 0, 0, 0)
_TeamIDs['BOOM Esports'] = 7732977

path = None
engine = InitTeamDB(path)
Session = sessionmaker(bind=engine)
session = Session()


def make_db():
    import_from_old(_TeamIDs, PlayerIDs, ValidityTime, session)


make_db()