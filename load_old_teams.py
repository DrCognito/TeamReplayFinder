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

#Queried at 2019-08-02T15:47:27.335003
PlayerIDs['Team Secret'] = collections.OrderedDict()
PlayerIDs['Team Secret']['Nisha'] = 76561198082035378
PlayerIDs['Team Secret']['MidOne'] = 76561198076851106
PlayerIDs['Team Secret']['zai'] = 76561198033828054
PlayerIDs['Team Secret']['YapzOr'] = 76561198049382766
PlayerIDs['Team Secret']['Puppey'] = 76561198047544485
ValidityTime['Team Secret'] = datetime.datetime(2018, 9, 11, 0, 0, 0, 0)
_TeamIDs['Team Secret'] = 1838315

PlayerIDs['Virtus Pro'] = collections.OrderedDict()
PlayerIDs['Virtus Pro']['RAMZEs'] = 76561198093117099
PlayerIDs['Virtus Pro']['Noone'] = 76561198066839629
PlayerIDs['Virtus Pro']['9pasha'] = 76561198052689179
PlayerIDs['Virtus Pro']['RodjER'] = 76561198119286646
PlayerIDs['Virtus Pro']['Solo'] = 76561198094822422
ValidityTime['Virtus Pro'] = datetime.datetime(2018, 2, 1, 0, 0, 0, 0)
_TeamIDs['Virtus Pro'] = 1883502

PlayerIDs['Vici Gaming'] = collections.OrderedDict()
PlayerIDs['Vici Gaming']['Paparazi'] = 76561198097458967
PlayerIDs['Vici Gaming']['Ori'] = 76561198068069222
PlayerIDs['Vici Gaming']['Yang'] = 76561198100203650
PlayerIDs['Vici Gaming']['Fade'] = 76561198142597041
PlayerIDs['Vici Gaming']['Dy'] = 76561198103959167
ValidityTime['Vici Gaming'] = datetime.datetime(2018, 9, 9, 0, 0, 0, 0)
_TeamIDs['Vici Gaming'] = 726228

PlayerIDs['Evil Geniuses'] = collections.OrderedDict()
PlayerIDs['Evil Geniuses']['Arteezy'] = 76561198047011640
PlayerIDs['Evil Geniuses']['SumaiL'] = 76561198071885769
PlayerIDs['Evil Geniuses']['s4'] = 76561198001497299
PlayerIDs['Evil Geniuses']['Cr1t'] = 76561197986172872
PlayerIDs['Evil Geniuses']['Fly'] = 76561198054420884
ValidityTime['Evil Geniuses'] = datetime.datetime(2018, 5, 28, 0, 0, 0, 0)
_TeamIDs['Evil Geniuses'] = 39

PlayerIDs['Team Liquid'] = collections.OrderedDict()
PlayerIDs['Team Liquid']['Miracle'] = 76561198065514372
PlayerIDs['Team Liquid']['w33'] = 76561198046966189
PlayerIDs['Team Liquid']['MinDContRoL'] = 76561197994770931
PlayerIDs['Team Liquid']['Gh'] = 76561198061622614
PlayerIDs['Team Liquid']['KuroKy'] = 76561198042528392
ValidityTime['Team Liquid'] = datetime.datetime(2019, 6, 20, 0, 0, 0, 0)
_TeamIDs['Team Liquid'] = 2163

PlayerIDs['PSG.LGD'] = collections.OrderedDict()
PlayerIDs['PSG.LGD']['Ame'] = 76561198085846975
PlayerIDs['PSG.LGD']['Somnus'] = 76561198067128891
PlayerIDs['PSG.LGD']['Chalice'] = 76561198055004575
PlayerIDs['PSG.LGD']['fy'] = 76561198061960890
PlayerIDs['PSG.LGD']['xNova'] = 76561198054561825
ValidityTime['PSG.LGD'] = datetime.datetime(2018, 1, 1, 0, 0, 0, 0)
_TeamIDs['PSG.LGD'] = 15

#Queried at 2019-08-02T15:58:40.596347
PlayerIDs['Fnatic'] = collections.OrderedDict()
PlayerIDs['Fnatic']['JAbz'] = 76561198060737259
PlayerIDs['Fnatic']['Abed'] = 76561198114980808
PlayerIDs['Fnatic']['iceiceice'] = 76561198045038168
PlayerIDs['Fnatic']['DJ'] = 76561198062365554
PlayerIDs['Fnatic']['DuBu'] = 145550466

ValidityTime['Fnatic'] = datetime.datetime(2019, 6, 28, 0, 0, 0, 0)
_TeamIDs['Fnatic'] = 350190

PlayerIDs['Ninjas in Pyjamas'] = collections.OrderedDict()
PlayerIDs['Ninjas in Pyjamas']['Ace'] = 76561198057856286
PlayerIDs['Ninjas in Pyjamas']['Fata'] = 76561198047065028
PlayerIDs['Ninjas in Pyjamas']['33'] = 76561198046964005
PlayerIDs['Ninjas in Pyjamas']['Saksa'] = 76561198064001473
PlayerIDs['Ninjas in Pyjamas']['PPD'] = 76561198046993283
ValidityTime['Ninjas in Pyjamas'] = datetime.datetime(2018, 9, 1, 0, 0, 0, 0)
_TeamIDs['Ninjas in Pyjamas'] = 6214973

PlayerIDs['TNC Predator'] = collections.OrderedDict()
PlayerIDs['TNC Predator']['Gabbi'] = 76561198112811187
PlayerIDs['TNC Predator']['ARMEL'] = 76561198124797733
PlayerIDs['TNC Predator']['Kuku'] = 76561198145216072
PlayerIDs['TNC Predator']['Tims'] = 76561198115760109
PlayerIDs['TNC Predator']['eyyou'] = 76561198133741952
ValidityTime['TNC Predator'] = datetime.datetime(2019, 2, 5, 0, 0, 0, 0)
_TeamIDs['TNC Predator'] = 2108395

PlayerIDs['OG'] = collections.OrderedDict()
PlayerIDs['OG']['ana'] = 76561198271626550
PlayerIDs['OG']['Topson'] = 76561198054320440
PlayerIDs['OG']['Ceb'] = 76561198048536965
PlayerIDs['OG']['JerAx'] = 76561197987037722
PlayerIDs['OG']['N0tail'] = 76561197979938082
ValidityTime['OG'] = datetime.datetime(2019, 3, 13, 0, 0, 0, 0)
_TeamIDs['OG'] = 2586976

PlayerIDs['Alliance'] = collections.OrderedDict()
PlayerIDs['Alliance']['miCKe'] = 76561198113227791
PlayerIDs['Alliance']['qojqva'] = 76561198047004422
PlayerIDs['Alliance']['Boxi'] = 76561198037756242
PlayerIDs['Alliance']['Taiga'] = 76561198362058302
PlayerIDs['Alliance']['iNSaNia'] = 76561198014846690
ValidityTime['Alliance'] = datetime.datetime(2018, 6, 3, 0, 0, 0, 0)
_TeamIDs['Alliance'] = 111474

PlayerIDs['Keen Gaming'] = collections.OrderedDict()
PlayerIDs['Keen Gaming']['oldchicken'] = 76561198096143960
PlayerIDs['Keen Gaming']['一'] = 76561198215485600
PlayerIDs['Keen Gaming']['eLeVeN'] = 76561198094541811
PlayerIDs['Keen Gaming']['kaka'] = 76561198100141760
PlayerIDs['Keen Gaming']['Dark'] = 76561198357728633
ValidityTime['Keen Gaming'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Keen Gaming'] = 2626685

#Queried at 2019-08-02T16:08:55.559342
# Newbee acquired forward gaming (below)
# PlayerIDs['Newbee'] = collections.OrderedDict()
# PlayerIDs['Newbee']['Sccc'] = 76561198109752622
# PlayerIDs['Newbee']['Moogy'] = 76561198077547282
# PlayerIDs['Newbee']['Sansheng'] = 76561198061149436
# PlayerIDs['Newbee']['Waixi'] = 76561198096841331
# PlayerIDs['Newbee']['awen'] = 76561198113181681
# PlayerIDs['Newbee']['Fenrir'] = 76561198074066546
# PlayerIDs['Newbee']['jiajia'] = 76561198063541626
# ValidityTime['Newbee'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
# _TeamIDs['Newbee'] = 1375614

#Queried at 2019-08-02T16:16:54.202865
PlayerIDs['Newbee'] = collections.OrderedDict()
PlayerIDs['Newbee']['YawaR'] = 76561198068717835
PlayerIDs['Newbee']['CCnC'] = 76561198181931958
PlayerIDs['Newbee']['Sneyking'] = 76561197970632344
PlayerIDs['Newbee']['MSS'] = 76561198046992615
PlayerIDs['Newbee']['pieliedie'] = 76561197967187728
ValidityTime['Newbee'] = datetime.datetime(2019, 3, 24, 0, 0, 0, 0)
_TeamIDs['Newbee'] = 6214538

PlayerIDs['Infamous'] = collections.OrderedDict()
PlayerIDs['Infamous']['K1'] = 164685175
PlayerIDs['Infamous']['Chris Luck'] = 153836240
PlayerIDs['Infamous']['Wisper'] = 292921272
PlayerIDs['Infamous']['Scofield'] = 157989498
PlayerIDs['Infamous']['Stinger'] = 119631156
ValidityTime['Infamous'] = datetime.datetime(2019, 7, 1, 0, 0, 0, 0)
_TeamIDs['Infamous'] = 2672298


#Queried at 2019-08-02T16:32:52.494411
PlayerIDs['Chaos Esports'] = collections.OrderedDict()
PlayerIDs['Chaos Esports']['vtFαded'] = 76561198102405046
PlayerIDs['Chaos Esports']['MATUMBAMAN'] = 76561198032578355
PlayerIDs['Chaos Esports']['KheZu'] = 76561198129291346
PlayerIDs['Chaos Esports']['MiLAN'] = 76561198058438585
PlayerIDs['Chaos Esports']['Misery'] = 76561198047648307
ValidityTime['Chaos Esports'] = datetime.datetime(2019, 6, 24, 0, 0, 0, 0)
_TeamIDs['Chaos Esports'] = 7203342
#_TeamIDs['Chaos Esports'] = 6666989

PlayerIDs['Natus Vincere'] = collections.OrderedDict()
PlayerIDs['Natus Vincere']['Crystallize'] = 76561198074884958
PlayerIDs['Natus Vincere']['MagicaL'] = 76561198132246824
PlayerIDs['Natus Vincere']['Blizzy'] = 76561198194965622
PlayerIDs['Natus Vincere']['Zayac'] = 76561198071296043
PlayerIDs['Natus Vincere']['SoNNeikO'] = 76561198077687195
ValidityTime['Natus Vincere'] = datetime.datetime(2019, 4, 24, 0, 0, 0, 0)
_TeamIDs['Natus Vincere'] = 36

PlayerIDs['Royal Never Give Up'] = collections.OrderedDict()
PlayerIDs['Royal Never Give Up']['Monet'] = 76561198108481367
PlayerIDs['Royal Never Give Up']['Setsu'] = 76561198100088082
PlayerIDs['Royal Never Give Up']['LaNm'] = 76561198049689484
PlayerIDs['Royal Never Give Up']['ahfu'] = 76561198079842570
PlayerIDs['Royal Never Give Up']['Flyby'] = 186627166
ValidityTime['Royal Never Give Up'] = datetime.datetime(2019, 4, 14, 0, 0, 0, 0)
_TeamIDs['Royal Never Give Up'] = 6209804

PlayerIDs['Mineski'] = collections.OrderedDict()
PlayerIDs['Mineski']['Nikobaby'] = 76561198373019683
PlayerIDs['Mineski']['Moonn'] = 76561198073723523
PlayerIDs['Mineski']['kpii'] = 76561198047278474
PlayerIDs['Mineski']['ragingpotato'] = 76561198153180008
PlayerIDs['Mineski']['ninjaboogie'] = 76561198051709146
ValidityTime['Mineski'] = datetime.datetime(2019, 9, 14, 0, 0, 0, 0)
_TeamIDs['Mineski'] = 543897

path = None
engine = InitTeamDB(path)
Session = sessionmaker(bind=engine)
session = Session()


def make_db():
    import_from_old(_TeamIDs, PlayerIDs, ValidityTime, session)


make_db()