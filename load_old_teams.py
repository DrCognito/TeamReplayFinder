import collections
import time
import datetime
from replay_finder.team_info import import_from_old, InitTeamDB
from sqlalchemy.orm import sessionmaker

def getSteam64From32(input32):
    return 76561197960265728 + input32


def getSteam32From64(input64):
    return input64 - 76561197960265728


PlayerIDs = {}
ValidityTime = {}
_TeamIDs = {}

#Queried at 2020-07-16T00:33:41.655134
PlayerIDs['Virtus.pro'] = collections.OrderedDict()
PlayerIDs['Virtus.pro']['iLTW'] = 76561198074261550
PlayerIDs['Virtus.pro']['Noone'] = 76561198066839629
PlayerIDs['Virtus.pro']['Resolut1on'] = 76561198046990903
PlayerIDs['Virtus.pro']['WZayac'] = 76561198071296043
PlayerIDs['Virtus.pro']['Solo'] = 76561198094822422
ValidityTime['Virtus.pro'] = datetime.datetime(2020, 4, 4, 0, 0, 0, 0)
_TeamIDs['Virtus.pro'] = 1883502

PlayerIDs['Natus Vincere'] = collections.OrderedDict()
PlayerIDs['Natus Vincere']['Crystallize'] = 76561198074884958
PlayerIDs['Natus Vincere']['young G'] = getSteam64From32(127530803)
PlayerIDs['Natus Vincere']['9pasha'] = 76561198052689179
PlayerIDs['Natus Vincere']['immersion'] = getSteam64From32(295697470)
PlayerIDs['Natus Vincere']['illias'] = getSteam64From32(187758589)
ValidityTime['Natus Vincere'] = datetime.datetime(2020, 6, 26, 0, 0, 0, 0)
_TeamIDs['Natus Vincere'] = 36

PlayerIDs['Alliance'] = collections.OrderedDict()
PlayerIDs['Alliance']['Nikobaby'] = 76561198373019683
PlayerIDs['Alliance']['LIMMP'] = 76561197972496930
PlayerIDs['Alliance']['s4'] = 76561198001497299
PlayerIDs['Alliance']['Handsken'] = 76561197978446698
PlayerIDs['Alliance']['Fng'] = getSteam64From32(94049589)  # Loan
ValidityTime['Alliance'] = datetime.datetime(2020, 5, 23, 0, 0, 0, 0)
_TeamIDs['Alliance'] = 111474

PlayerIDs['Ninjas in Pyjamas'] = collections.OrderedDict()
PlayerIDs['Ninjas in Pyjamas']['charlie'] = 76561198082315226
PlayerIDs['Ninjas in Pyjamas']['Supream'] = 76561198018778775
PlayerIDs['Ninjas in Pyjamas']['SabeRLighT'] = 76561198086478594
PlayerIDs['Ninjas in Pyjamas']['Era'] = 76561198060583478
PlayerIDs['Ninjas in Pyjamas']['Cr1t'] = getSteam64From32(25907144)
ValidityTime['Ninjas in Pyjamas'] = datetime.datetime(2020, 4, 22, 0, 0, 0, 0)
_TeamIDs['Ninjas in Pyjamas'] = 6214973

PlayerIDs['OG'] = collections.OrderedDict()
PlayerIDs['OG']['midone'] = 76561198076851106
PlayerIDs['OG']['Topson'] = 76561198054320440
PlayerIDs['OG']['Ceb'] = getSteam64From32(88271237)
PlayerIDs['OG']['Saksa'] = 76561198064001473
PlayerIDs['OG']['N0tail'] = 76561197979938082
ValidityTime['OG'] = datetime.datetime(2020, 1, 29, 0, 0, 0, 0)
_TeamIDs['OG'] = 2586976

PlayerIDs['ViKin.gg'] = collections.OrderedDict()
PlayerIDs['ViKin.gg']['Shad'] = getSteam64From32(164962869)
PlayerIDs['ViKin.gg']['BOOM'] = 76561198151092467
PlayerIDs['ViKin.gg']['Tobi'] = 76561198100554096
PlayerIDs['ViKin.gg']['Aramis'] = 76561198052867589
PlayerIDs['ViKin.gg']['Seleri'] = 76561198051995905
ValidityTime['ViKin.gg'] = datetime.datetime(2020, 1, 1, 0, 0, 0, 0)
_TeamIDs['ViKin.gg'] = 6685591

PlayerIDs['Nigma'] = collections.OrderedDict()
PlayerIDs['Nigma']['Miracle'] = 76561198065514372
PlayerIDs['Nigma']['w33'] = 76561198046966189
PlayerIDs['Nigma']['MinDContRoL'] = 76561197994770931
PlayerIDs['Nigma']['Gh'] = 76561198061622614
PlayerIDs['Nigma']['KuroKy'] = 76561198042528392
ValidityTime['Nigma'] = datetime.datetime(2019, 11, 25, 0, 0, 0, 0)
_TeamIDs['Nigma'] = 7554697

PlayerIDs['FlyToMoon'] = collections.OrderedDict()
PlayerIDs['FlyToMoon']['VTune'] = 76561198112721251
PlayerIDs['FlyToMoon']['Iceberg'] = 76561198210380235
PlayerIDs['FlyToMoon']['GeneRaL'] = 76561198049816369
PlayerIDs['FlyToMoon']['ALOHADANCE'] = 76561198083316966
PlayerIDs['FlyToMoon']['ALWAYSWANNAFLY'] = 76561198051330508
ValidityTime['FlyToMoon'] = datetime.datetime(2020, 2, 21, 0, 0, 0, 0)
_TeamIDs['FlyToMoon'] = 6953913

#Queried at 2020-07-24T01:49:57.379770
PlayerIDs['VP.Prodigy'] = collections.OrderedDict()
PlayerIDs['VP.Prodigy']['epileptick1d'] = getSteam64From32(124801257)
PlayerIDs['VP.Prodigy']['DM'] = 76561198016617237
PlayerIDs['VP.Prodigy']['fn'] = 76561197965416536
PlayerIDs['VP.Prodigy']['Save'] = 76561198278146366
PlayerIDs['VP.Prodigy']['eine'] = 76561198089337610
ValidityTime['VP.Prodigy'] = datetime.datetime(2020, 4, 1, 0, 0, 0, 0)
_TeamIDs['VP.Prodigy'] = 7819701

#Queried at 2020-08-05T00:23:45.903310
PlayerIDs['Evil Geniuses'] = collections.OrderedDict()
PlayerIDs['Evil Geniuses']['Arteezy'] = getSteam64From32(86745912)
PlayerIDs['Evil Geniuses']['Abed'] = 76561198114980808
PlayerIDs['Evil Geniuses']['RAMZES666'] = 76561198093117099
PlayerIDs['Evil Geniuses']['Cr1t'] = 76561197986172872
PlayerIDs['Evil Geniuses']['Fly'] = 76561198054420884
ValidityTime['Evil Geniuses'] = datetime.datetime(2019, 9, 16, 0, 0, 0, 0)
_TeamIDs['Evil Geniuses'] = 39

PlayerIDs['Team Secret'] = collections.OrderedDict()
PlayerIDs['Team Secret']['MATUMBAMAN'] = 76561198032578355
PlayerIDs['Team Secret']['Nisha'] = 76561198082035378
PlayerIDs['Team Secret']['zai'] = 76561198033828054
PlayerIDs['Team Secret']['YapzOr'] = 76561198049382766
PlayerIDs['Team Secret']['Puppey'] = 76561198047544485
ValidityTime['Team Secret'] = datetime.datetime(2019, 11, 4, 0, 0, 0, 0)
_TeamIDs['Team Secret'] = 1838315

PlayerIDs['Team Liquid'] = collections.OrderedDict()
PlayerIDs['Team Liquid']['miCKe'] = 76561198113227791
PlayerIDs['Team Liquid']['qojqva'] = 76561198047004422
PlayerIDs['Team Liquid']['Boxi'] = 76561198037756242
PlayerIDs['Team Liquid']['Taiga'] = 76561198362058302
PlayerIDs['Team Liquid']['iNSaNiA'] = 76561198014846690
ValidityTime['Team Liquid'] = datetime.datetime(2019, 10, 2, 0, 0, 0, 0)
_TeamIDs['Team Liquid'] = 2163

#Queried at 2020-08-10T00:26:49.043267
PlayerIDs['5men'] = collections.OrderedDict()
PlayerIDs['5men']['Ace'] = getSteam64From32(97590558)
PlayerIDs['5men']['Chessie'] = getSteam64From32(172424257)
PlayerIDs['5men']['Xibbe'] = getSteam64From32(50580004)
PlayerIDs['5men']['MISERY'] = getSteam64From32(87382579)
PlayerIDs['5men']['pieliedie'] = getSteam64From32(6922000)
ValidityTime['5men'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['5men'] = 8077174

PlayerIDs['Ninjas in Pyjamas'] = collections.OrderedDict()
PlayerIDs['Ninjas in Pyjamas']['charlie'] = 76561198082315226
PlayerIDs['Ninjas in Pyjamas']['Supream'] = 76561198018778775
PlayerIDs['Ninjas in Pyjamas']['SabeRLighT'] = 76561198086478594
PlayerIDs['Ninjas in Pyjamas']['Era'] = 76561198060583478
PlayerIDs['Ninjas in Pyjamas']['Misha'] = getSteam64From32(90125566)
ValidityTime['Ninjas in Pyjamas'] = datetime.datetime(2020, 4, 22, 0, 0, 0, 0)
_TeamIDs['Ninjas in Pyjamas'] = 6214973

path = None
engine = InitTeamDB(path)
Session = sessionmaker(bind=engine)
session = Session()


def make_db():
    import_from_old(_TeamIDs, PlayerIDs, ValidityTime, session)


make_db()