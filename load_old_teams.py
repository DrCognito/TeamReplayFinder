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

#ElementsProGaming
PlayerIDs['Virtus Pro'] = collections.OrderedDict()
PlayerIDs['Virtus Pro']['RAMZES666'] = 76561198093117099
PlayerIDs['Virtus Pro']['Noone'] = 76561198066839629
PlayerIDs['Virtus Pro']['9pasha'] = 76561198052689179
PlayerIDs['Virtus Pro']['RodjER'] = 76561198119286646
PlayerIDs['Virtus Pro']['Solo'] = 76561198094822422
ValidityTime['Virtus Pro'] = datetime.datetime(2018, 2, 1, 0, 0, 0, 0)

PlayerIDs['Team Liquid'] = collections.OrderedDict()
PlayerIDs['Team Liquid']['MATUMBAMAN'] = 76561198032578355
PlayerIDs['Team Liquid']['Miracle'] = 76561198065514372
PlayerIDs['Team Liquid']['MinD_ContRoL'] = 76561197994770931
PlayerIDs['Team Liquid']['GH'] = 76561198061622614
PlayerIDs['Team Liquid']['KuroKy'] = 76561198042528392
ValidityTime['Team Liquid'] = datetime.datetime(2017, 1, 2, 0, 0, 0, 0)

PlayerIDs['PSG LGD'] = collections.OrderedDict()
PlayerIDs['PSG LGD']['Ame'] = 76561198085846975
PlayerIDs['PSG LGD']['SomnusM'] = 76561198067128891
PlayerIDs['PSG LGD']['Chalice'] = 76561198055004575
PlayerIDs['PSG LGD']['fy'] = 76561198061960890
PlayerIDs['PSG LGD']['xNova'] = 76561198054561825
ValidityTime['PSG LGD'] = datetime.datetime(2018, 1, 1, 0, 0, 0, 0)

PlayerIDs['Team Secret'] = collections.OrderedDict()
PlayerIDs['Team Secret']['Nisha'] = 76561198082035378
PlayerIDs['Team Secret']['MidOne'] = 76561198076851106
PlayerIDs['Team Secret']['Zai'] = 76561198033828054
PlayerIDs['Team Secret']['YapzOr'] = 76561198049382766
PlayerIDs['Team Secret']['Puppey'] = 76561198047544485
ValidityTime['Team Secret'] = datetime.datetime(2018, 9, 11, 0, 0, 0, 0)

PlayerIDs['Mineski'] = collections.OrderedDict()
PlayerIDs['Mineski']['Mushi'] = 76561198050137285
PlayerIDs['Mineski']['Moon'] = 76561198073723523
PlayerIDs['Mineski']['iceiceice'] = 76561198045038168
PlayerIDs['Mineski']['Jabz'] = 76561198060737259
PlayerIDs['Mineski']['ninjaboogie'] = 76561198051709146
ValidityTime['Mineski'] = datetime.datetime(2017, 8, 16, 0, 0, 0, 0)

PlayerIDs['Vici Gaming'] = collections.OrderedDict()
PlayerIDs['Vici Gaming']['Paparazi'] = 76561198097458967
PlayerIDs['Vici Gaming']['Ori'] = 76561198068069222
PlayerIDs['Vici Gaming']['eLeVeN'] = 76561198094541811
PlayerIDs['Vici Gaming']['LaNm'] = 76561198049689484
PlayerIDs['Vici Gaming']['Fenrir'] = 76561198074066546
ValidityTime['Vici Gaming'] = datetime.datetime(2017, 9, 6, 0, 0, 0, 0)

PlayerIDs['Newbee'] = collections.OrderedDict()
PlayerIDs['Newbee']['Moogy'] = 76561198077547282
PlayerIDs['Newbee']['Sccc'] = 76561198109752622
PlayerIDs['Newbee']['kpii'] = 76561198047278474
PlayerIDs['Newbee']['Kaka'] = 76561198100141760
PlayerIDs['Newbee']['Faith'] = 76561198042593402
ValidityTime['Newbee'] = datetime.datetime(2016, 9, 17, 0, 0, 0, 0)

PlayerIDs['VGJ Thunder'] = collections.OrderedDict()
PlayerIDs['VGJ Thunder']['Sylar'] = 76561198068647788
PlayerIDs['VGJ Thunder']['Freeze'] = 76561198097538713
PlayerIDs['VGJ Thunder']['Yang'] = 76561198100203650
PlayerIDs['VGJ Thunder']['Fade'] = 76561198142597041
PlayerIDs['VGJ Thunder']['ddc'] = 76561198074505099
ValidityTime['VGJ Thunder'] = datetime.datetime(2018, 2, 3, 0, 0, 0, 0)

PlayerIDs['OG'] = collections.OrderedDict()
PlayerIDs['OG']['ana'] = 76561198271626550
PlayerIDs['OG']['Topson'] = 76561198054320440
PlayerIDs['OG']['7ckngMad'] = 76561198048536965
PlayerIDs['OG']['JerAx'] = 76561197987037722
PlayerIDs['OG']['N0tail'] = 76561197979938082
ValidityTime['OG'] = datetime.datetime(2018, 6, 3, 0, 0, 0, 0)

PlayerIDs['Winstrike'] = collections.OrderedDict()
PlayerIDs['Winstrike']['Silent'] = 76561198049535522
PlayerIDs['Winstrike']['Iceberg'] = 76561198210380235
PlayerIDs['Winstrike']['nongrata'] = 76561198091066831
PlayerIDs['Winstrike']['Nofear'] = 76561198053818519
PlayerIDs['Winstrike']['ALWAYSWANNAFLY'] = 76561198051330508
ValidityTime['Winstrike'] = datetime.datetime(2018, 6, 20, 0, 0, 0, 0)

PlayerIDs['Team Serenity'] = collections.OrderedDict()
PlayerIDs['Team Serenity']['zhizhizhi'] = 76561198128294443
PlayerIDs['Team Serenity']['Zyd'] = 76561198085201850
PlayerIDs['Team Serenity']['XinQ'] = 76561198117741251
PlayerIDs['Team Serenity']['Pyw'] = 76561198098808851
PlayerIDs['Team Serenity']['XCJ'] = 76561198077997505
ValidityTime['Team Serenity'] = datetime.datetime(2018, 3, 1, 0, 0, 0, 0)

PlayerIDs['IG'] = collections.OrderedDict()
PlayerIDs['IG']['Agressif'] = 76561198090681764
PlayerIDs['IG']['Xxs'] = 76561198090224486
PlayerIDs['IG']['Srf'] = 76561198116928426
PlayerIDs['IG']['BoBoKa'] = 76561198168095042
PlayerIDs['IG']['Q'] = 76561198100419252
ValidityTime['IG'] = datetime.datetime(2018, 2, 3, 0, 0, 0, 0)

PlayerIDs['Fnatic'] = collections.OrderedDict()
PlayerIDs['Fnatic']['EternaLEnVy'] = 76561198003541947
PlayerIDs['Fnatic']['Abed'] = 76561198114980808
PlayerIDs['Fnatic']['UNiVeRsE'] = 76561198047542075
PlayerIDs['Fnatic']['DJ'] = 76561198062365554
PlayerIDs['Fnatic']['pieliedie'] = 76561197967187728
ValidityTime['Fnatic'] = datetime.datetime(2018, 1, 13, 0, 0, 0, 0)

PlayerIDs['TNC Predator'] = collections.OrderedDict()
PlayerIDs['TNC Predator']['Raven'] = 76561198092575221
PlayerIDs['TNC Predator']['Armel'] = 76561198124797733
PlayerIDs['TNC Predator']['Sam_H'] = 76561198147885039
PlayerIDs['TNC Predator']['Tims'] = 76561198115760109
PlayerIDs['TNC Predator']['Kuku'] = 76561198145216072
ValidityTime['TNC Predator'] = datetime.datetime(2018, 1, 30, 0, 0, 0, 0)

PlayerIDs['VGJ Storm'] = collections.OrderedDict()
PlayerIDs['VGJ Storm']['YawaR'] = 76561198068717835
PlayerIDs['VGJ Storm']['Resolut1on'] = 76561198046990903
PlayerIDs['VGJ Storm']['Sneyking'] = 76561197970632344
PlayerIDs['VGJ Storm']['MSS'] = 76561198046992615
PlayerIDs['VGJ Storm']['SVG'] = 76561198007700414
ValidityTime['VGJ Storm'] = datetime.datetime(2018, 4, 12, 0, 0, 0, 0)

PlayerIDs['Evil Geniuses'] = collections.OrderedDict()
PlayerIDs['Evil Geniuses']['Arteezy'] = 76561198047011640
PlayerIDs['Evil Geniuses']['Suma1L'] = 76561198071885769
PlayerIDs['Evil Geniuses']['s4'] = 76561198001497299
PlayerIDs['Evil Geniuses']['Cr1t'] = 76561197986172872
PlayerIDs['Evil Geniuses']['Fly'] = 76561198054420884
ValidityTime['Evil Geniuses'] = datetime.datetime(2018, 5, 28, 0, 0, 0, 0)

PlayerIDs['Optic Gaming'] = collections.OrderedDict()
PlayerIDs['Optic Gaming']['Pajkatt'] = 76561198047551057
PlayerIDs['Optic Gaming']['CCnC '] = 76561198181931958
PlayerIDs['Optic Gaming']['33'] = 76561198046964005
PlayerIDs['Optic Gaming']['zai'] = 76561198033828054
PlayerIDs['Optic Gaming']['ppd'] = 76561198046993283
ValidityTime['Optic Gaming'] = datetime.datetime(2017, 12, 21, 0, 0, 0, 0)

PlayerIDs['Pain Gaming'] = collections.OrderedDict()
PlayerIDs['Pain Gaming']['hFn'] = 76561198054270445
PlayerIDs['Pain Gaming']['w33'] = 76561198046966189
PlayerIDs['Pain Gaming']['tavo'] = 76561198078222576
PlayerIDs['Pain Gaming']['Kingrd'] = 76561198045119556
PlayerIDs['Pain Gaming']['Duster'] = 76561198076790780
ValidityTime['Pain Gaming'] = datetime.datetime(2018, 4, 14, 0, 0, 0, 0)

#KL major additions
PlayerIDs['Alliance'] = collections.OrderedDict()
PlayerIDs['Alliance']['qojqva'] = 76561198047004422
PlayerIDs['Alliance']['miCKe'] = 76561198113227791
PlayerIDs['Alliance']['Boxi'] = 76561198037756242
PlayerIDs['Alliance']['iNSaNiA'] = 76561198014846690
PlayerIDs['Alliance']['Taiga'] = 76561198362058302
ValidityTime['Alliance'] = datetime.datetime(2018, 6, 3, 0, 0, 0, 0)

PlayerIDs['Ninjas in Pyjamas'] = collections.OrderedDict()
PlayerIDs['Ninjas in Pyjamas']['Ace'] = 76561198057856286
PlayerIDs['Ninjas in Pyjamas']['Fata'] = 76561198047065028
PlayerIDs['Ninjas in Pyjamas']['33'] = 76561198046964005
PlayerIDs['Ninjas in Pyjamas']['Saksa'] = 76561198064001473
PlayerIDs['Ninjas in Pyjamas']['ppd'] = 76561198046993283
ValidityTime['Ninjas in Pyjamas'] = datetime.datetime(2018, 9, 15, 0, 0, 0, 0)

PlayerIDs['Vega Squadron'] = collections.OrderedDict()
PlayerIDs['Vega Squadron']['Madara'] = 76561198055695796
PlayerIDs['Vega Squadron']['DM'] = 76561198016617237
PlayerIDs['Vega Squadron']['KheZu'] = 76561198129291346
PlayerIDs['Vega Squadron']['Maybe Next Time '] = 76561198047219142
PlayerIDs['Vega Squadron']['Peksu'] = 76561198111335318
ValidityTime['Vega Squadron'] = datetime.datetime(2018, 10, 28, 0, 0, 0, 0)

PlayerIDs['madjor atendari'] = collections.OrderedDict()
PlayerIDs['madjor atendari']['Power'] = 76561198047111480
PlayerIDs['madjor atendari']['lil pleb'] = 76561198064176721
PlayerIDs['madjor atendari']['Vihren'] = 76561198047153381
PlayerIDs['madjor atendari']['eN'] = 76561198070460321
PlayerIDs['madjor atendari']['CTOMAHEH1'] = 76561198274849896
ValidityTime['madjor atendari'] = datetime.datetime(2018, 9, 12, 0, 0, 0, 0)

PlayerIDs['MangoBay'] = collections.OrderedDict()
PlayerIDs['MangoBay']['Fey'] = 76561198138298284
PlayerIDs['MangoBay']['garter'] = 76561198047059467
PlayerIDs['MangoBay']['bOne7'] = 76561198048985630
PlayerIDs['MangoBay']['Qupe'] = 76561198078343881
PlayerIDs['MangoBay']['Flash'] = 76561198052294119
ValidityTime['MangoBay'] = datetime.datetime(2018, 9, 5, 0, 0, 0, 0)

PlayerIDs['The Final Tribe'] = collections.OrderedDict()
PlayerIDs['The Final Tribe']['Frost'] = 76561198129624977
PlayerIDs['The Final Tribe']['Chessie'] = 76561198132689985
PlayerIDs['The Final Tribe']['jonassomfan'] = 76561198000475053
PlayerIDs['The Final Tribe']['Handsken'] = 76561197978446698
PlayerIDs['The Final Tribe']['Era'] = 76561198060583478
ValidityTime['The Final Tribe'] = datetime.datetime(2018, 4, 14, 0, 0, 0, 0)

# PlayerIDs[''] = collections.OrderedDict()
# PlayerIDs[''][''] = 
# PlayerIDs[''][''] = 
# PlayerIDs[''][''] = 
# PlayerIDs[''][''] = 
# PlayerIDs[''][''] = 
# ValidityTime[''] = datetime.datetime(2018, 4, 14, 0, 0, 0, 0)

PlayerIDs['Hippomaniacs'] = collections.OrderedDict()
PlayerIDs['Hippomaniacs']['Curry'] = 76561198012671730
PlayerIDs['Hippomaniacs']['Supream'] = 76561198018778775
PlayerIDs['Hippomaniacs']['SabeRLighT'] = 76561198086478594
PlayerIDs['Hippomaniacs']['Muf'] = 76561198028273089
PlayerIDs['Hippomaniacs']['sehny'] = 76561198079445782
ValidityTime['Hippomaniacs'] = datetime.datetime(2018, 9, 4, 0, 0, 0, 0)

PlayerIDs['ferzee'] = collections.OrderedDict()
PlayerIDs['ferzee']['Daxak'] = 76561198073006451
PlayerIDs['ferzee']['Afoninje'] = 76561198042118224
PlayerIDs['ferzee']['AfterLife'] = 76561198047050811
PlayerIDs['ferzee']['KingR'] = 76561198143259310
PlayerIDs['ferzee']['VANSKOR'] = 76561197971815910
ValidityTime['ferzee'] = datetime.datetime(2018, 9, 14, 0, 0, 0, 0)

_TeamIDs = {}

_TeamIDs['Virtus Pro'] = 1883502
_TeamIDs['Team Liquid'] = 2163
_TeamIDs['PSG LGD'] = 15
_TeamIDs['Team Secret'] = 1838315
_TeamIDs['Mineski'] = 543897
_TeamIDs['Vici Gaming'] = 726228
_TeamIDs['Newbee'] = 1375614
_TeamIDs['VGJ Thunder'] = 5027210
_TeamIDs['OG'] = 2586976
_TeamIDs['Winstrike'] = 5229127
_TeamIDs['Team Serenity'] = 5066616
_TeamIDs['IG'] = 5
_TeamIDs['Fnatic'] = 350190
_TeamIDs['TNC Predator'] = 2108395
_TeamIDs['VGJ Storm'] = 5228654
_TeamIDs['Evil Geniuses'] = 39
_TeamIDs['Optic Gaming'] = 5026801
_TeamIDs['Pain Gaming'] = 67

_TeamIDs['Alliance'] = 111474
_TeamIDs['Ninjas in Pyjamas'] = 6214973
_TeamIDs['Vega Squadron'] = 2006913
_TeamIDs['madjor atendari'] = 6211505
_TeamIDs['MangoBay'] = 6187923
_TeamIDs['The Final Tribe'] = 5059375

_TeamIDs['ferzee'] = 6209143
_TeamIDs['Hippomaniacs'] = 3214090

#Queried at 2018-10-15T23:28:25.749090
PlayerIDs['compLexity Gaming'] = collections.OrderedDict()
PlayerIDs['compLexity Gaming']['Skem'] = 76561198060859959
PlayerIDs['compLexity Gaming']['Limmp'] = 76561197972496930
PlayerIDs['compLexity Gaming']['Sneyking'] = 76561197970632344
PlayerIDs['compLexity Gaming']['Zfreek'] = 76561198011094390
PlayerIDs['compLexity Gaming']['EternaLEnVy'] = 76561198003541947
ValidityTime['compLexity Gaming'] = datetime.datetime(2018, 9, 11, 0, 0, 0, 0)
_TeamIDs['compLexity Gaming'] = 3

PlayerIDs['ROOONS'] = collections.OrderedDict()
PlayerIDs['ROOONS']['BananaSlamJamma'] = 76561198065444496
PlayerIDs['ROOONS']['iAnnihilate'] = 76561198052972365
PlayerIDs['ROOONS']['monkeys-forever'] = 76561198047076771
PlayerIDs['ROOONS']['Boris'] = 76561198054630653
PlayerIDs['ROOONS']['Jubei'] = 76561198064541693
ValidityTime['ROOONS'] = datetime.datetime(2018, 9, 27, 0, 0, 0, 0)
_TeamIDs['ROOONS'] = 6266671

PlayerIDs['Infamous Gaming'] = collections.OrderedDict()
PlayerIDs['Infamous Gaming']['Timado'] = 76561198057924346
PlayerIDs['Infamous Gaming']['Papita'] = 76561197988336300
PlayerIDs['Infamous Gaming']['Wisper'] = 76561198253187000
PlayerIDs['Infamous Gaming']['Scofield'] = 157989498
PlayerIDs['Infamous Gaming']['MoOz'] = 76561198309576604
ValidityTime['Infamous Gaming'] = datetime.datetime(2018, 9, 7, 0, 0, 0, 0)
_TeamIDs['Infamous Gaming'] = 2672298

PlayerIDs['The Final Tribe'] = collections.OrderedDict()
PlayerIDs['The Final Tribe']['Frost'] = 76561198129624977
PlayerIDs['The Final Tribe']['Chessie'] = 76561198132689985
PlayerIDs['The Final Tribe']['Jonassomfan'] = 76561198000475053
PlayerIDs['The Final Tribe']['Handsken'] = 76561197978446698
PlayerIDs['The Final Tribe']['Era'] = 76561198060583478
ValidityTime['The Final Tribe'] = datetime.datetime(2018, 9, 6, 0, 0, 0, 0)
_TeamIDs['The Final Tribe'] = 5059375

PlayerIDs['Natus Vincere'] = collections.OrderedDict()
PlayerIDs['Natus Vincere']['Crystallize'] = 76561198074884958
PlayerIDs['Natus Vincere']['MagicaL'] = 76561198132246824
PlayerIDs['Natus Vincere']['Blizzy'] = 76561198194965622
PlayerIDs['Natus Vincere']['Chu'] = 76561198077749622
PlayerIDs['Natus Vincere']['SoNNeikO'] = 76561198077687195
ValidityTime['Natus Vincere'] = datetime.datetime(2018, 9, 7, 0, 0, 0, 0)
_TeamIDs['Natus Vincere'] = 36

PlayerIDs['Royal Never Give Up'] = collections.OrderedDict()
PlayerIDs['Royal Never Give Up']['Monet'] = 76561198108481367
PlayerIDs['Royal Never Give Up']['xy'] = 76561198161860152
PlayerIDs['Royal Never Give Up']['Srf'] = 76561198116928426
PlayerIDs['Royal Never Give Up']['ahfu'] = 76561198079842570
PlayerIDs['Royal Never Give Up']['343'] = 76561198071300317
ValidityTime['Royal Never Give Up'] = datetime.datetime(2018, 9, 15, 0, 0, 0, 0)
_TeamIDs['Royal Never Give Up'] = 6209804

PlayerIDs['Tigers'] = collections.OrderedDict()
PlayerIDs['Tigers']['AhJit'] = 76561198086683001
PlayerIDs['Tigers']['inYourdreaM'] = 76561198141981865
PlayerIDs['Tigers']['MoonMeander'] = 76561197998894475
PlayerIDs['Tigers']['Xepher'] = 76561198081669956
PlayerIDs['Tigers']['1437'] = 76561198047462618
ValidityTime['Tigers'] = datetime.datetime(2018, 9, 8, 0, 0, 0, 0)
_TeamIDs['Tigers'] = 6187627



#path = 'sqlite://'
path = None
engine = InitTeamDB(path)
Session = sessionmaker(bind=engine)
session = Session()

def make_db():
    import_from_old(_TeamIDs, PlayerIDs, ValidityTime, session)

make_db()