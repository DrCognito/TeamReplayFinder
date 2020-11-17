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

# PlayerIDs['Natus Vincere'] = collections.OrderedDict()
# PlayerIDs['Natus Vincere']['Crystallize'] = 76561198074884958
# PlayerIDs['Natus Vincere']['young G'] = getSteam64From32(127530803)
# PlayerIDs['Natus Vincere']['9pasha'] = 76561198052689179
# PlayerIDs['Natus Vincere']['immersion'] = getSteam64From32(295697470)
# PlayerIDs['Natus Vincere']['illias'] = getSteam64From32(187758589)
# ValidityTime['Natus Vincere'] = datetime.datetime(2020, 6, 26, 0, 0, 0, 0)
# _TeamIDs['Natus Vincere'] = 36

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

PlayerIDs['Evil Geniuses'] = collections.OrderedDict()
PlayerIDs['Evil Geniuses']['Arteezy'] = getSteam64From32(86745912)
PlayerIDs['Evil Geniuses']['Abed'] = getSteam64From32(480412663)
PlayerIDs['Evil Geniuses']['RAMZES666'] = 76561198093117099
PlayerIDs['Evil Geniuses']['Cr1t'] = 76561197986172872
PlayerIDs['Evil Geniuses']['Fly'] = 76561198054420884
ValidityTime['Evil Geniuses'] = datetime.datetime(2019, 9, 16, 0, 0, 0, 0)
_TeamIDs['Evil Geniuses'] = 39

PlayerIDs['Nigma'] = collections.OrderedDict()
PlayerIDs['Nigma']['Miracle'] = 76561198065514372
PlayerIDs['Nigma']['w33'] = 76561198046966189
PlayerIDs['Nigma']['MinDContRoL'] = 76561197994770931
PlayerIDs['Nigma']['Gh'] = 76561198061622614
PlayerIDs['Nigma']['rMN'] = getSteam64From32(87197791)
ValidityTime['Nigma'] = datetime.datetime(2019, 11, 25, 0, 0, 0, 0)
_TeamIDs['Nigma'] = 7554697

#Queried at 2020-08-24T16:29:08.763672
PlayerIDs['Cyber Legacy'] = collections.OrderedDict()
PlayerIDs['Cyber Legacy']['Cooman'] = 76561198135729387
PlayerIDs['Cyber Legacy']['MagicaL'] = 76561198132246824
PlayerIDs['Cyber Legacy']['Blizzy'] = 76561198194965622
PlayerIDs['Cyber Legacy']['Bignum'] = 76561198050689479
PlayerIDs['Cyber Legacy']['CemaTheSlayer'] = 76561198051726500
ValidityTime['Cyber Legacy'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Cyber Legacy'] = 7669103

PlayerIDs['Omegalil'] = collections.OrderedDict()
PlayerIDs['Omegalil']['Kelen'] = 76561198056454854
PlayerIDs['Omegalil']['Sunlight'] = 76561198001903020
PlayerIDs['Omegalil']['Malik'] = getSteam64From32(203351055)
PlayerIDs['Omegalil']['grim reaper'] = getSteam64From32(91405276)
PlayerIDs['Omegalil']['HappyDyurara'] = 76561198305126946
ValidityTime['Omegalil'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Omegalil'] = 8077147

PlayerIDs['EXTREMUM'] = collections.OrderedDict()
PlayerIDs['EXTREMUM']['nefrit'] = 76561198076514883
PlayerIDs['EXTREMUM']['mellojul'] = 76561198001070814
PlayerIDs['EXTREMUM']['Malik'] = getSteam64From32(7542148)
PlayerIDs['EXTREMUM']['velheor'] = 76561198042571493
PlayerIDs['EXTREMUM']['G'] = 76561198047852720
ValidityTime['EXTREMUM'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['EXTREMUM'] = 7542148

PlayerIDs['Cyberium Seed'] = collections.OrderedDict()
PlayerIDs['Cyberium Seed']['lilpleb'] = 76561198064176721
PlayerIDs['Cyberium Seed']['Mastermind'] = 76561198052743718
PlayerIDs['Cyberium Seed']['Samsam'] = 76561198847923582
PlayerIDs['Cyberium Seed']['b1kA'] = getSteam64From32(348703642)
PlayerIDs['Cyberium Seed']['Puber'] = 76561198259479562
ValidityTime['Cyberium Seed'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Cyberium Seed'] = 8021531

PlayerIDs['Team Unique'] = collections.OrderedDict()
PlayerIDs['Team Unique']['Palantimos'] = 76561198077147248
PlayerIDs['Team Unique']['19teen'] = 76561198360974756
PlayerIDs['Team Unique']['633'] = 76561198056462556
PlayerIDs['Team Unique']['illusion'] = getSteam64From32(126702445)
PlayerIDs['Team Unique']['VANSKOR'] = 76561197971815910
ValidityTime['Team Unique'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Team Unique'] = 7820540

PlayerIDs['HellRaisers'] = collections.OrderedDict()
PlayerIDs['HellRaisers']['Nix'] = 76561197972131055
PlayerIDs['HellRaisers']['ksani'] = 76561198059421563
PlayerIDs['HellRaisers']['funn1k'] = 76561198046988871
PlayerIDs['HellRaisers']['Lil'] = getSteam64From32(106809101)
PlayerIDs['HellRaisers']['KingR'] = getSteam64From32(182993582)
ValidityTime['HellRaisers'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['HellRaisers'] = 7422789

#Queried at 2020-08-31T15:26:47.031569
PlayerIDs['KHAN'] = collections.OrderedDict()
PlayerIDs['KHAN']['young G'] = getSteam64From32(127530803)
PlayerIDs['KHAN']['naive'] = 76561198056449704
PlayerIDs['KHAN']['chshrct'] = 76561198047136584
PlayerIDs['KHAN']['Gilgir'] = 76561198146261995
PlayerIDs['KHAN']['j4'] = getSteam64From32(75750590)
ValidityTime['KHAN'] = datetime.datetime(2020, 6, 21, 0, 0, 0, 0)
_TeamIDs['KHAN'] = 7453744

#Queried at 2020-09-08T16:13:17.420831
PlayerIDs['B8'] = collections.OrderedDict()
PlayerIDs['B8']['Crystallis'] = 76561198087883707
PlayerIDs['B8']['Dendi'] = 76561198030654385
PlayerIDs['B8']['Lasthero'] = 76561198050590468
PlayerIDs['B8']['5up'] = getSteam64From32(313198707)
PlayerIDs['B8']['Fishman'] = 76561198087831260
ValidityTime['B8'] = datetime.datetime(2020, 6, 7, 0, 0, 0, 0)
_TeamIDs['B8'] = 7684041

PlayerIDs['Team Unique'] = collections.OrderedDict()
PlayerIDs['Team Unique']['Palantimos'] = 76561198077147248
PlayerIDs['Team Unique']['19teen'] = 76561198360974756
PlayerIDs['Team Unique']['633'] = 76561198056462556
PlayerIDs['Team Unique']['illusion'] = getSteam64From32(126702445)
PlayerIDs['Team Unique']['VANSKOR'] = 76561197971815910
ValidityTime['Team Unique'] = datetime.datetime(2020, 6, 14, 0, 0, 0, 0)
_TeamIDs['Team Unique'] = 7820540

PlayerIDs['Team Empire'] = collections.OrderedDict()
PlayerIDs['Team Empire']['SmilingKnight'] = 76561198115428035
PlayerIDs['Team Empire']['gwynbleidd'] = getSteam64From32(200362560)
PlayerIDs['Team Empire']['Petushara'] = getSteam64From32(363871826)
PlayerIDs['Team Empire']['sayuw'] = getSteam64From32(145065875)
PlayerIDs['Team Empire']['EcNart'] = 76561198026886689
ValidityTime['Team Empire'] = datetime.datetime(2020, 6, 14, 0, 0, 0, 0)
_TeamIDs['Team Empire'] = 46


#Queried at 2020-09-08T16:13:17.420831
PlayerIDs['Mudgolems'] = collections.OrderedDict()
PlayerIDs['Mudgolems']['skiter'] = getSteam64From32(100058342)
PlayerIDs['Mudgolems']['BoraNija'] = getSteam64From32(298683250)
PlayerIDs['Mudgolems']['33'] = getSteam64From32(86698277)
PlayerIDs['Mudgolems']['MiLAN'] = getSteam64From32(98172857)
PlayerIDs['Mudgolems']['Fata'] = getSteam64From32(86799300)
ValidityTime['Mudgolems'] = datetime.datetime(2020, 12, 8, 0, 0, 0, 0)
_TeamIDs['Mudgolems'] = 8121295

#Queried at 2020-09-30T23:57:55.050943
PlayerIDs['Natus Vincere'] = collections.OrderedDict()
PlayerIDs['Natus Vincere']['VTune'] = 76561198112721251
PlayerIDs['Natus Vincere']['Iceberg'] = 76561198210380235
PlayerIDs['Natus Vincere']['GeneRaL'] = 76561198049816369
PlayerIDs['Natus Vincere']['RodjER'] = 76561198119286646
PlayerIDs['Natus Vincere']['ALWAYSWANNAFLY'] = 76561198051330508
ValidityTime['Natus Vincere'] = datetime.datetime(2020, 9, 22, 0, 0, 0, 0)
_TeamIDs['Natus Vincere'] = 36

# PlayerIDs['FlyToMoon'] = collections.OrderedDict()
# PlayerIDs['FlyToMoon']['VTune'] = 76561198112721251
# PlayerIDs['FlyToMoon']['Iceberg'] = 76561198210380235
# PlayerIDs['FlyToMoon']['GeneRaL'] = 76561198049816369
# PlayerIDs['FlyToMoon']['RodjER'] = getSteam64From32(159020918)
# PlayerIDs['FlyToMoon']['ALWAYSWANNAFLY'] = 76561198051330508
# ValidityTime['FlyToMoon'] = datetime.datetime(2020, 2, 21, 0, 0, 0, 0)
# _TeamIDs['FlyToMoon'] = 6953913

PlayerIDs['Winstrike Team'] = collections.OrderedDict()
PlayerIDs['Winstrike Team']['agressivechild'] = 76561198125937156
PlayerIDs['Winstrike Team']['re1bl'] = getSteam64From32(439345730)
PlayerIDs['Winstrike Team']['DkFogas'] = 76561198175119462
PlayerIDs['Winstrike Team']['Dukalis'] = 76561198033666810
PlayerIDs['Winstrike Team']['yamich'] = 76561197969669202
ValidityTime['Winstrike Team'] = datetime.datetime(2020, 7, 20, 0, 0, 0, 0)
_TeamIDs['Winstrike Team'] = 7118032

PlayerIDs['Yellow Submarine'] = collections.OrderedDict()
PlayerIDs['Yellow Submarine']['Yatoro'] = getSteam64From32(321580662)
PlayerIDs['Yellow Submarine']['mio'] = getSteam64From32(114933489)
PlayerIDs['Yellow Submarine']['Collapse'] = getSteam64From32(302214028)
PlayerIDs['Yellow Submarine']['so bad'] = getSteam64From32(107023378)
PlayerIDs['Yellow Submarine']['Miposhka'] = getSteam64From32(113331514)
ValidityTime['Yellow Submarine'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Yellow Submarine'] = 2576071


PlayerIDs['Tempo'] = collections.OrderedDict()
PlayerIDs['Tempo']['krylat'] = 76561198111014074
PlayerIDs['Tempo']['Noob'] = 76561198100563280
PlayerIDs['Tempo']['Mitch'] = 76561198050446094
PlayerIDs['Tempo']['dnz'] = 76561198058433434
PlayerIDs['Tempo']['LeBron'] = 76561197995770025
ValidityTime['Tempo'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Tempo'] = 7556672

#Queried at 2020-11-02T13:38:12.792222
PlayerIDs['Brame'] = collections.OrderedDict()
PlayerIDs['Brame']['Focus'] = getSteam64From32(196490133)
PlayerIDs['Brame']['W1sh'] = 76561198080879620
PlayerIDs['Brame']['Skylark'] = 76561197987444626
PlayerIDs['Brame']['Stomanen1'] = getSteam64From32(314584168)
PlayerIDs['Brame']['SsaSpartan'] = 76561198053214822
ValidityTime['Brame'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Brame'] = 8112124

#Queried at 2020-11-02T13:38:12.792222
PlayerIDs['Live To Win'] = collections.OrderedDict()
PlayerIDs['Live To Win']['iLTW'] = getSteam64From32(113995822)
PlayerIDs['Live To Win']['fn'] = getSteam64From32(5150808)
PlayerIDs['Live To Win']['Afterlife'] = getSteam64From32(86785083)
PlayerIDs['Live To Win']['Immersion'] = getSteam64From32(295697470)
PlayerIDs['Live To Win']['SoNNeikO'] = getSteam64From32(117421467)
ValidityTime['Live To Win'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Live To Win'] = 8161113

#Queried at 2020-11-07T03:47:50.431763
PlayerIDs['Gambit Esports'] = collections.OrderedDict()
PlayerIDs['Gambit Esports']['yy'] = getSteam64From32(116934015)
PlayerIDs['Gambit Esports']['Lorenof'] = getSteam64From32(210053851)
PlayerIDs['Gambit Esports']['meLes'] = getSteam64From32(148180390)
PlayerIDs['Gambit Esports']['XSvamp1Re'] = getSteam64From32(326327879)
PlayerIDs['Gambit Esports']['eine'] = 76561198089337610
ValidityTime['Gambit Esports'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Gambit Esports'] = 6209143

#Queried at 2020-11-12T17:37:55.790242
PlayerIDs['Cyberium'] = collections.OrderedDict()
PlayerIDs['Cyberium']['lil pleb'] = getSteam64From32(103910993)
PlayerIDs['Cyberium']['Mastermind'] = getSteam64From32(92477990)
PlayerIDs['Cyberium']['Airu'] = getSteam64From32(41843638)
PlayerIDs['Cyberium']['goddam'] = getSteam64From32(63703276)
PlayerIDs['Cyberium']['Gatciy'] = getSteam64From32(104185879)
ValidityTime['Cyberium'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Cyberium'] = 7486089

PlayerIDs['Nemiga Gaming'] = collections.OrderedDict()
PlayerIDs['Nemiga Gaming']['tatakae'] = 76561198278080177
PlayerIDs['Nemiga Gaming']['Ainkrad'] = getSteam64From32(196482746)
PlayerIDs['Nemiga Gaming']['TheChosenOne'] = 76561198256492424
PlayerIDs['Nemiga Gaming']['Petru44o'] = getSteam64From32(86317757)
PlayerIDs['Nemiga Gaming']['Lodine'] = 76561198073885576
ValidityTime['Nemiga Gaming'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Nemiga Gaming'] = 5014799

path = None
engine = InitTeamDB(path)
Session = sessionmaker(bind=engine)
session = Session()


def make_db():
    import_from_old(_TeamIDs, PlayerIDs, ValidityTime, session)


make_db()