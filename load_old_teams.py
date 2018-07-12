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

#Mineski steam IDs in order of position
PlayerIDs['Mineski'] = collections.OrderedDict()
PlayerIDs['Mineski']['bimbo']=76561198153180008
PlayerIDs['Mineski']['meracle']=76561198051635104
PlayerIDs['Mineski']['rr']=76561198284058219
PlayerIDs['Mineski']['julz']=76561198216535465
PlayerIDs['Mineski']['ninjaboogie']=76561198051709146
#jessievash


#RaveDota
PlayerIDs['RaveDota'] = collections.OrderedDict()
PlayerIDs['RaveDota']['Ab1ng']=76561198171797209
PlayerIDs['RaveDota']['Kevz']=76561198146685663
PlayerIDs['RaveDota']['WHPH']=76561198218429137
PlayerIDs['RaveDota']['Tims']=76561198115760109
PlayerIDs['RaveDota']['flysolo']=76561198162007218

#PowerRangers
PlayerIDs['PowerRangers'] = collections.OrderedDict()
PlayerIDs['PowerRangers']['Bignum']=76561198050689479
PlayerIDs['PowerRangers']['Afoninje']=76561198023969004
PlayerIDs['PowerRangers']['chshrct']=76561198047136584
PlayerIDs['PowerRangers']['goddam']=76561198023969004
PlayerIDs['PowerRangers']['j4']=76561198036016318

#ElementsProGaming
PlayerIDs['Elements'] = collections.OrderedDict()
PlayerIDs['Elements']['Swiftending']=76561198047017547
PlayerIDs['Elements']['BoraNija']=76561198258948978
PlayerIDs['Elements']['Mitch']=76561198050446094
PlayerIDs['Elements']['dnz']=76561198058433434
PlayerIDs['Elements']['LeBronDota']=76561197995770025
ValidityTime['Elements'] = datetime.datetime(2018, 5, 14, 0, 0, 0, 0)#Whole team

#Kaipi
PlayerIDs['Kaipi'] = collections.OrderedDict()
PlayerIDs['Kaipi']['SingSing']=76561197980022982
PlayerIDs['Kaipi']['bOne7']=76561198048985630
PlayerIDs['Kaipi']['TheCoon']=76561198046964005
PlayerIDs['Kaipi']['SexyBamboe']=76561197980587476
PlayerIDs['Kaipi']['FLUFFNSTUFF']=76561198001736459

#VirtusPro
PlayerIDs['VirtusPro'] = collections.OrderedDict()
PlayerIDs['VirtusPro']['RAMZES666']=76561198093117099
PlayerIDs['VirtusPro']['Noone']=76561198066839629
PlayerIDs['VirtusPro']['9pasha']=76561198052689179
PlayerIDs['VirtusPro']['RodjER']=76561198119286646
PlayerIDs['VirtusPro']['Solo']=76561198094822422
ValidityTime['VirtusPro'] = datetime.datetime(2016, 8, 4, 0, 0, 0, 0)#Whole team

#VegaSquadron
PlayerIDs['VegaSquadron'] = collections.OrderedDict()
PlayerIDs['VegaSquadron']['ALOHADANCE']=76561198083316966
PlayerIDs['VegaSquadron']['G']=76561198047852720
PlayerIDs['VegaSquadron']['AfterLife']=76561198047050811
PlayerIDs['VegaSquadron']['Zayac']=76561198071296043
PlayerIDs['VegaSquadron']['CemaTheSlayeR']=76561198051726500
ValidityTime['VegaSquadron'] = datetime.datetime(2017, 9, 25, 0, 0, 0, 0)#Zayac



#TeamLiquid
PlayerIDs['Liquid'] = collections.OrderedDict()
PlayerIDs['Liquid']['MATUMBAMAN']=76561198032578355
PlayerIDs['Liquid']['Miracle']=76561198065514372
PlayerIDs['Liquid']['MinD_ContRoL']=76561197994770931
PlayerIDs['Liquid']['GH']=76561198061622614
PlayerIDs['Liquid']['KuroKy']=76561198042528392
ValidityTime['Liquid'] = datetime.datetime(2016, 1, 2, 0, 0, 0, 0)#GH

#TeamSecret Oct 16
PlayerIDs['TeamSecret'] = collections.OrderedDict()
PlayerIDs['TeamSecret']['Ace']=76561198057856286
PlayerIDs['TeamSecret']['MidOne']=76561198076851106
PlayerIDs['TeamSecret']['Fata']=76561198047065028
PlayerIDs['TeamSecret']['YapzOr']=76561198049382766
PlayerIDs['TeamSecret']['Puppey']=76561198047544485
#PlayerIDs['TeamSecret']['pieliedie']=[76561197967187728,76561198085071214]
ValidityTime['TeamSecret'] = datetime.datetime(2017, 5, 4, 0, 0, 0, 0)#Yapz0r

#FlipSid3Tactics
PlayerIDs['FlipSid3Tactics'] = collections.OrderedDict()
PlayerIDs['FlipSid3Tactics']['Sedoy']=76561198013443964
PlayerIDs['FlipSid3Tactics']['tmw']=76561198047106282
PlayerIDs['FlipSid3Tactics']['Shachlo']=76561198084053252
PlayerIDs['FlipSid3Tactics']['VANSKOR']=76561197971815910
PlayerIDs['FlipSid3Tactics']['RodjER']=76561198119286646

#Fantastic Five
PlayerIDs['FantasticFive'] = collections.OrderedDict()
PlayerIDs['FantasticFive']['Illidan']=76561197986582419
PlayerIDs['FantasticFive']['Bzz']=76561198056462556
PlayerIDs['FantasticFive']['L0lik_O']=76561198051967271
PlayerIDs['FantasticFive']['rmN']=76561198047463519
PlayerIDs['FantasticFive']['yol']=76561198036866088

#TheImperial
PlayerIDs['Cloud9'] = collections.OrderedDict()
PlayerIDs['Cloud9']['Ace']=76561198057856286
PlayerIDs['Cloud9']['BabyKnight']=76561198003255542
PlayerIDs['Cloud9']['HeStEJoERoTTeN']=76561198003885423
PlayerIDs['Cloud9']['NoiA']=76561197984149024
PlayerIDs['Cloud9']['Ryze']=76561198359760150
ValidityTime['Cloud9'] = datetime.datetime(2017, 1, 5, 0, 0, 0, 0)#Whole team
#PlayerIDs['Cloud9']['Ryze']=76561197986948192

#Alliance
PlayerIDs['Alliance'] = collections.OrderedDict()
PlayerIDs['Alliance']['qojqva']=76561198047004422
PlayerIDs['Alliance']['miCKe']=76561197972496930
PlayerIDs['Alliance']['Boxi']=76561198000475053
PlayerIDs['Alliance']['iNSaNiA']=76561198077280895
PlayerIDs['Alliance']['Taiga']=76561197978446698
ValidityTime['Alliance'] = datetime.datetime(2018, 6, 3, 0, 0, 0, 0)#qojqva replaced

#Horde
PlayerIDs['Horde'] = collections.OrderedDict()
PlayerIDs['Horde']['Gorgc']=76561198017205597
PlayerIDs['Horde']['Xcalibur']=76561198205638857
PlayerIDs['Horde']['Eskillz']=76561198053233966
PlayerIDs['Horde']['Pablo']=76561198077280895
PlayerIDs['Horde']['Akke']=76561198001554683

#Navi
PlayerIDs['Navi'] = collections.OrderedDict()
PlayerIDs['Navi']['Crystallize']=76561198074884958
PlayerIDs['Navi']['Dendi']=76561198030654385
PlayerIDs['Navi']['GeneRaL']=76561198049816369
PlayerIDs['Navi']['RodjER']=76561198119286646
PlayerIDs['Navi']['SoNNeikO']=76561198077687195

#NiP used to be Escape
PlayerIDs['NiP'] = collections.OrderedDict()
PlayerIDs['NiP']['Era']=76561198060583478
PlayerIDs['NiP']['qojqva']=76561198047004422
PlayerIDs['NiP']['Trixi']=76561197968978034
PlayerIDs['NiP']['iNsania']=76561198014846690
PlayerIDs['NiP']['H4nn1']=76561197981531669
ValidityTime['NiP'] = datetime.datetime(2017, 4, 20, 0, 0, 0, 0)#Whole team

#Sanguine Sharks
PlayerIDs['SanguineSharks'] = collections.OrderedDict()
PlayerIDs['SanguineSharks']['Mambos']=76561198015915632
PlayerIDs['SanguineSharks']['SlashStrike']=76561198026494412
PlayerIDs['SanguineSharks']['Dale']=76561198008241949
PlayerIDs['SanguineSharks']['Seleri']=76561198051995905
PlayerIDs['SanguineSharks']['sehny']=76561198079445782

#Team NP
PlayerIDs['TeamNP'] = collections.OrderedDict()
PlayerIDs['TeamNP']['Aui_2000']=76561198000813202
PlayerIDs['TeamNP']['EternaLEnVy']=76561198003541947
PlayerIDs['TeamNP']['MSS']=76561198046992615
PlayerIDs['TeamNP']['SVG']=76561198007700414
PlayerIDs['TeamNP']['Rose']=76561198047462618


PlayerIDs['FDL'] = collections.OrderedDict()
PlayerIDs['FDL']['Beesa']=76561198130797937
PlayerIDs['FDL']['Num747']=76561198075407158
PlayerIDs['FDL']['MJW']=76561198036439216
PlayerIDs['FDL']['Num04']=76561197972194774
PlayerIDs['FDL']['Stan_King']=76561198047239991

PlayerIDs['Random'] = collections.OrderedDict()
PlayerIDs['Random']['shadow']=76561198089850849
PlayerIDs['Random']['bLink']=76561198061852271
PlayerIDs['Random']['Faith_bian']=76561198078399948
PlayerIDs['Random']['y']=76561198071380415
PlayerIDs['Random']['iceice']=76561198062910293
ValidityTime['Random'] = datetime.datetime(2015, 8, 25, 0, 0, 0, 0) #Whole team


PlayerIDs['EG'] = collections.OrderedDict()
PlayerIDs['EG']['Arteezy']=76561198047011640
PlayerIDs['EG']['Suma1L']=76561198071885769
PlayerIDs['EG']['UNiVeRsE']=76561198047542075
PlayerIDs['EG']['zai']=76561198033828054
PlayerIDs['EG']['Cr1t']=76561197986172872
PlayerIDs['EG']['BenchID']=PlayerIDs['EG']['Cr1t']
ValidityTime['EG'] = datetime.datetime(2016, 9, 15, 0, 0, 0, 0)#Everyone bar universe




PlayerIDs['Newbee'] = collections.OrderedDict()
PlayerIDs['Newbee']['Moogy']=76561198077547282#was uuu9
PlayerIDs['Newbee']['Sccc']=76561198109752622
PlayerIDs['Newbee']['kpii']=76561198047278474
PlayerIDs['Newbee']['kaka']=76561198100141760
PlayerIDs['Newbee']['Faith']=76561198042593402
ValidityTime['Newbee'] = datetime.datetime(2016, 9, 17, 0, 0, 0, 0)#uu9, scc, faith

PlayerIDs['EHOME'] = collections.OrderedDict()
PlayerIDs['EHOME']['Sylar']=76561198068647788
PlayerIDs['EHOME']['old chicken']=76561198096143960
PlayerIDs['EHOME']['old eLeVeN']=76561198094541811
PlayerIDs['EHOME']['old LaNm']=76561198049689484
PlayerIDs['EHOME']['Garder']=76561198103015917


PlayerIDs['Execration'] = collections.OrderedDict()
PlayerIDs['Execration']['Gabbi'] = 76561198112811187
PlayerIDs['Execration']['Nando'] = 76561198140278041
PlayerIDs['Execration']['DJ'] = 76561198062365554
PlayerIDs['Execration']['Owa'] = 76561198077048642
PlayerIDs['Execration']['Kim0'] = 76561198051920312

PlayerIDs['OG'] = collections.OrderedDict()
PlayerIDs['OG']['ana']=76561198271626550
PlayerIDs['OG']['Topson']=76561198054320440
PlayerIDs['OG']['7Mad']=76561198048536965
PlayerIDs['OG']['JerAx']=76561197987037722
PlayerIDs['OG']['N0tail']=76561197979938082
ValidityTime['OG'] = datetime.datetime(2018, 6, 3, 0, 0, 0, 0)#Resolut1on

PlayerIDs['MVP'] = collections.OrderedDict()
PlayerIDs['MVP']['FoREv']=76561198049199322
PlayerIDs['MVP']['QO']=76561198053385497
PlayerIDs['MVP']['Velo']=76561198070805039
PlayerIDs['MVP']['Febby']=76561198072643187
PlayerIDs['MVP']['Dubu']=76561198105816194
#Forev is too new!
PlayerIDs['MVP']['BenchID']=PlayerIDs['MVP']['QO']

PlayerIDs['Complexity'] = collections.OrderedDict()
PlayerIDs['Complexity']['Moo']=76561198044695409
PlayerIDs['Complexity']['canceL']=76561198101955961
PlayerIDs['Complexity']['monkeys-forever']=76561198047076771
PlayerIDs['Complexity']['Zfreek']=76561198011094390
PlayerIDs['Complexity']['melonzz']=76561198009583456

PlayerIDs['LGDFY'] = collections.OrderedDict()
PlayerIDs['LGDFY']['Monet']=76561198108481367
PlayerIDs['LGDFY']['Super']=76561198051147887
PlayerIDs['LGDFY']['Inflame']=76561198071455445
PlayerIDs['LGDFY']['Ahfu']=76561198079842570
PlayerIDs['LGDFY']['ddc']=76561198074505099
#PlayerIDs['LGDFY']['LPC']=
#Due to subs for monet and lpc change benchid
ValidityTime['LGDFY'] = datetime.datetime(2016, 9, 17, 0, 0, 0, 0)#Monet, super

PlayerIDs['LGD'] = collections.OrderedDict()
PlayerIDs['LGD']['Ame']=76561198137682430
PlayerIDs['LGD']['Maybe']=76561198067128891
PlayerIDs['LGD']['Eleven']=76561198094541811
PlayerIDs['LGD']['Yao']=76561198059143738
PlayerIDs['LGD']['Victoria']=76561198067347106

PlayerIDs['iGV'] = collections.OrderedDict()
PlayerIDs['iGV']['Paparazi']=76561198097458967
PlayerIDs['iGV']['Sakata']=76561198134146057
PlayerIDs['iGV']['InJuly']=76561198071557321
PlayerIDs['iGV']['super']=76561198063305227
PlayerIDs['iGV']['Dogf1ghts']=76561198064206703
ValidityTime['iGV'] = datetime.datetime(2016, 3, 19, 0, 0, 0, 0)#Whole team

PlayerIDs['mousesports'] = collections.OrderedDict()
PlayerIDs['mousesports']['Madara']=76561198055695796
PlayerIDs['mousesports']['ThuG']=76561198068121207
PlayerIDs['mousesports']['Skylark']=76561197987444626
PlayerIDs['mousesports']['Maybe']=76561198047219142
PlayerIDs['mousesports']['SsaSpartan']=76561198053214822

#WarriorsGaming Unity
PlayerIDs['Team Bazaar'] = collections.OrderedDict()
PlayerIDs['Team Bazaar']['Ahjit']=76561198086683001
PlayerIDs['Team Bazaar']['NaNa']=76561198073723523
PlayerIDs['Team Bazaar']['Ben']=76561198069205052
PlayerIDs['Team Bazaar']['Ahfu']=76561198079842570
PlayerIDs['Team Bazaar']['xNova']=76561198054561825
ValidityTime['Team Bazaar'] = datetime.datetime(2017, 1, 12, 0, 0, 0, 0) #Ben 2017-01-12

PlayerIDs['Faceless'] = collections.OrderedDict()
PlayerIDs['Faceless']['Black']=76561197981555031
PlayerIDs['Faceless']['Jabz']=76561198060737259
PlayerIDs['Faceless']['iceiceice']=76561198045038168
PlayerIDs['Faceless']['xy']=76561198045682762
PlayerIDs['Faceless']['NutZ']=76561198049869377
ValidityTime['Faceless'] = datetime.datetime(2016, 9, 3, 0, 0, 0, 0)#Whole team


PlayerIDs['Thunderbirds'] = collections.OrderedDict()
PlayerIDs['Thunderbirds']['Resolut1on']=76561198046990903
PlayerIDs['Thunderbirds']['w33']=76561198046966189
PlayerIDs['Thunderbirds']['MoonMeander']=76561197998894475
PlayerIDs['Thunderbirds']['MiSeRy']=76561198047648307
PlayerIDs['Thunderbirds']['Saksa']=76561198064001473
PlayerIDs['Thunderbirds']['BenchID']=PlayerIDs['Thunderbirds']['Saksa']
ValidityTime['Thunderbirds'] = datetime.datetime(2016, 8, 25, 0, 0, 0, 0)#Moonmeander to DC


PlayerIDs['Infamous'] = collections.OrderedDict()
PlayerIDs['Infamous']['Benjaz'] = 76561198154787641
PlayerIDs['Infamous']['Kotaro'] = 76561198056091436
PlayerIDs['Infamous']['Valquiria'] = 76561198086111525
PlayerIDs['Infamous']['StingeR'] = 76561198079896884
PlayerIDs['Infamous']['Accel'] = 76561198060061874

PlayerIDs['DigitalChaos'] = collections.OrderedDict()
PlayerIDs['DigitalChaos']['mason'] = 76561198275923688
PlayerIDs['DigitalChaos']['Abed'] = 76561198252727004
PlayerIDs['DigitalChaos']['BuLba'] = 76561197990502939
PlayerIDs['DigitalChaos']['DuBu'] = 76561198105816194
PlayerIDs['DigitalChaos']['DeMoN'] = 76561198046071242
ValidityTime['DigitalChaos'] = datetime.datetime(2017, 1, 6, 0, 0, 0, 0)#Abed (team onyx)

PlayerIDs['Clutch Gamers'] = collections.OrderedDict()
PlayerIDs['Clutch Gamers']['Armel'] = 76561198124797733
PlayerIDs['Clutch Gamers']['Ab1ng'] = 76561198171797209
PlayerIDs['Clutch Gamers']['Rappy'] = 76561198082098941
PlayerIDs['Clutch Gamers']['Boombacs'] = 76561198087342769
PlayerIDs['Clutch Gamers']['Flysolo'] = 76561198162007218

PlayerIDs['Rex Regum'] = collections.OrderedDict()
PlayerIDs['Rex Regum']['KelThuzard'] = 76561198210999588
PlayerIDs['Rex Regum']['yabyoo'] = 76561198080204734 
PlayerIDs['Rex Regum']['KoaLa'] = 76561198050812965
PlayerIDs['Rex Regum']['Xepher'] = 76561198081669956
PlayerIDs['Rex Regum']['Eden'] = 76561198009048628
ValidityTime['Rex Regum'] = datetime.datetime(2017, 2, 3, 0, 0, 0, 0) #Xepher swapped from mid.

PlayerIDs['Geek Fam'] = collections.OrderedDict()
PlayerIDs['Geek Fam']['Syeonix'] = 76561198074090895
PlayerIDs['Geek Fam']['Teehee'] = 76561198071024795
PlayerIDs['Geek Fam']['Velo'] = 76561198070805039
PlayerIDs['Geek Fam']['Roddgeee'] = 76561198068983210
PlayerIDs['Geek Fam']['Crimson'] = 76561198070886088
ValidityTime['Geek Fam'] = datetime.datetime(2017, 1, 8, 0, 0, 0, 0)#Velo 2017-01-08

PlayerIDs['TNC'] = collections.OrderedDict()
PlayerIDs['TNC']['Raven'] = 76561198092575221
PlayerIDs['TNC']['Kuku'] = 76561198145216072
PlayerIDs['TNC']['Sam_H'] = 76561198147885039
PlayerIDs['TNC']['Tims'] = 76561198115760109
PlayerIDs['TNC']['1437']=76561198047462618
ValidityTime['TNC'] = datetime.datetime(2017, 5, 16, 0, 0, 0, 0)#Tims

# PlayerIDs[''] = collections.OrderedDict()
# PlayerIDs[''][''] = 

PlayerIDs['Bazaar Youth'] = collections.OrderedDict()
PlayerIDs['Bazaar Youth']['xiaNG'] = 76561198104601317
PlayerIDs['Bazaar Youth']['ChYuan'] = 76561198073700931
PlayerIDs['Bazaar Youth']['wenn'] = 76561198082183137
PlayerIDs['Bazaar Youth']['wL'] = 76561198054110340
PlayerIDs['Bazaar Youth']['yaNG'] = 76561198047046401

PlayerIDs['Team Freedom'] = collections.OrderedDict()
PlayerIDs['Team Freedom']['YawaR'] = 76561198068717835
PlayerIDs['Team Freedom']['CCnC'] = 76561198181931958
PlayerIDs['Team Freedom']['Sneyking'] = 76561197970632344
PlayerIDs['Team Freedom']['FrancisLee'] = 76561198197124361
PlayerIDs['Team Freedom']['StanKing'] = 76561198047239991

PlayerIDs['Team Spirit'] = collections.OrderedDict()
PlayerIDs['Team Spirit']['Bzz'] = 76561198056462556
PlayerIDs['Team Spirit']['Iceberg'] = 76561198210380235
PlayerIDs['Team Spirit']['DkPhobos'] = 76561198054604695
PlayerIDs['Team Spirit']['fng'] = 76561198054315317
PlayerIDs['Team Spirit']['VANSKOR'] = 76561197971815910


PlayerIDs['Friends'] = collections.OrderedDict()
PlayerIDs['Friends']['Bignum'] = 76561198050689479
PlayerIDs['Friends']['yoky'] = 76561198072516509
PlayerIDs['Friends']['AfterLife'] = 76561198047050811
PlayerIDs['Friends']['ALOHADANCE'] = 76561198083316966
PlayerIDs['Friends']['NoFear'] = 76561198053818519

PlayerIDs['Elements Pro'] = collections.OrderedDict()
PlayerIDs['Elements Pro']['Swiftending'] = 76561198047017547
PlayerIDs['Elements Pro']['kole'] = 76561198052236803
PlayerIDs['Elements Pro']['Mitch'] = 76561198050446094
PlayerIDs['Elements Pro']['LeBronDota'] = 76561197995770025
PlayerIDs['Elements Pro']['g0g1'] = 76561198003667181
ValidityTime['Elements Pro'] = datetime.datetime(2016, 12, 21, 0, 0, 0, 0)#Kole 2016-12-21

PlayerIDs['Penta'] = collections.OrderedDict()
PlayerIDs['Penta']['oliver'] = 76561198060324070
PlayerIDs['Penta']['w33'] = 76561198046966189
PlayerIDs['Penta']['Buugi'] = 76561197984275146
PlayerIDs['Penta']['dnz'] = 76561198058433434
PlayerIDs['Penta']['rmN'] = 76561198047463519
ValidityTime['Penta'] = datetime.datetime(2018, 2, 5, 0, 0, 0, 0)#w33 2018-02-05

PlayerIDs['ProDota'] = collections.OrderedDict()
PlayerIDs['ProDota']['Garter'] = 76561198047059467
PlayerIDs['ProDota']['Keyser'] = 76561198047027410
PlayerIDs['ProDota']['33'] = 76561198046964005
PlayerIDs['ProDota']['MiLAN'] = 76561198058438585
PlayerIDs['ProDota']['j4'] = 76561198036016318
ValidityTime['ProDota'] = datetime.datetime(2017, 4, 5, 0, 0, 0, 0)#Reform except Garter

PlayerIDs['iG'] = collections.OrderedDict()
PlayerIDs['iG']['BurNIng'] = 76561198051158462
PlayerIDs['iG']['Op'] = 76561198166078878
PlayerIDs['iG']['Xxs'] = 76561198090224486
PlayerIDs['iG']['BoBoKa'] = 76561198168095042
PlayerIDs['iG']['Q'] = 76561198100419252
ValidityTime['iG'] = datetime.datetime(2016, 9, 17, 0, 0, 0, 0)#Burning, Op, Q

PlayerIDs['SGesports'] = collections.OrderedDict()
PlayerIDs['SGesports']['hFn'] = 76561198054270445
PlayerIDs['SGesports']['4dr'] = 76561198046203108
PlayerIDs['SGesports']['Tavo'] = 76561198078222576
PlayerIDs['SGesports']['KINGRD'] = 76561198045119556
PlayerIDs['SGesports']['c4t'] = 76561197997923885
ValidityTime['SGesports'] = datetime.datetime(2016, 11, 13, 0, 0, 0, 0)#Whole team

PlayerIDs['VGJ'] = collections.OrderedDict()
PlayerIDs['VGJ']['Agressif'] = 76561198090681764
PlayerIDs['VGJ']['Freeze'] = 76561198097538713
PlayerIDs['VGJ']['rOtK'] = 76561198051963819
PlayerIDs['VGJ']['fy'] = 76561198061960890
PlayerIDs['VGJ']['Fenrir'] = 76561198074066546
ValidityTime['VGJ'] = datetime.datetime(2016, 12, 26, 0, 0, 0, 0)#Freeze, fy

PlayerIDs['Effect'] = collections.OrderedDict()
PlayerIDs['Effect']['Sedoy'] = 76561198013443964
PlayerIDs['Effect']['Afoninje'] = 76561198042118224
PlayerIDs['Effect']['Shachlo'] = 76561198084053252
PlayerIDs['Effect']['ArsZeeqq'] = 76561198060294063
PlayerIDs['Effect']['RodjER'] = 76561198119286646
ValidityTime['Effect'] = datetime.datetime(2017, 1, 29, 0, 0, 0, 0)#Whole team


PlayerIDs['Empire'] = collections.OrderedDict()
PlayerIDs['Empire']['Resolut1on'] = 76561198046990903
PlayerIDs['Empire']['fn'] = 76561197965416536
PlayerIDs['Empire']['Ghostik'] = 76561198053113162
PlayerIDs['Empire']['RodjER'] = 76561198119286646
PlayerIDs['Empire']['Miposhka'] = 76561198073597242
ValidityTime['Empire'] = datetime.datetime(2017, 1, 8, 0, 0, 0, 0)#2017-01-08

PlayerIDs['VG'] = collections.OrderedDict()
PlayerIDs['VG']['Hao'] = 76561198048774243
PlayerIDs['VG']['Ori'] = 76561198068069222
PlayerIDs['VG']['Yang'] = 76561198100203650
PlayerIDs['VG']['Hym'] = 76561198095649787
PlayerIDs['VG']['ChuaN'] = 76561198048818941
#ValidityTime['VG'] = datetime.datetime(2017, 5, 12, 0, 0, 0, 0)#Hao
ValidityTime['VG'] = datetime.datetime(2017, 1, 6, 0, 0, 0, 0)#Hao

PlayerIDs['HappyFeet'] = collections.OrderedDict()
PlayerIDs['HappyFeet']['Jeyo'] = 76561198047626134
PlayerIDs['HappyFeet']['Benhur'] = 76561198137350948
PlayerIDs['HappyFeet']['Yaj'] = 76561198172149841
PlayerIDs['HappyFeet']['Julz'] = 76561198216535465
PlayerIDs['HappyFeet']['JessieVash'] = 76561198047038662

PlayerIDs['Crescendo'] = collections.OrderedDict()
PlayerIDs['Crescendo']['13abyKnight'] = 76561198003255542
PlayerIDs['Crescendo']['Excalibur'] = 76561198205638857
PlayerIDs['Crescendo']['syndereN'] = 76561197964547457
PlayerIDs['Crescendo']['EGM'] = 76561197964182156
PlayerIDs['Crescendo']['Akke'] = 76561198001554683
#2017-05-23
ValidityTime['Crescendo'] = datetime.datetime(2017, 5, 23, 0, 0, 0, 0)#Formed

PlayerIDs['Danish Bears'] = collections.OrderedDict()
PlayerIDs['Danish Bears']['Ace'] = 76561198057856286
PlayerIDs['Danish Bears']['747'] = 76561198075407158
PlayerIDs['Danish Bears']['HeStEJoE-RoTTeN'] = 76561198003885423
PlayerIDs['Danish Bears']['NoiA'] = 76561197984149024
PlayerIDs['Danish Bears']['Ryze'] = 76561197986948192
ValidityTime['Danish Bears'] = datetime.datetime(2017, 5, 19, 0, 0, 0, 0)#Reformed

PlayerIDs['4Protect5'] = collections.OrderedDict()
PlayerIDs['4Protect5']['Five'] = 76561198154938395
PlayerIDs['4Protect5']['SlashStrike'] = 76561198026494412
PlayerIDs['4Protect5']['etakaka'] = 76561198049304158
PlayerIDs['4Protect5']['DancingDragon'] = 76561198009690232
PlayerIDs['4Protect5']['eskillz'] = 76561198053233966
ValidityTime['4Protect5'] = datetime.datetime(2017, 3, 19, 0, 0, 0, 0)#Reformed


PlayerIDs['TeamSingularity'] = collections.OrderedDict()
PlayerIDs['TeamSingularity']['Adamsson'] = 76561198802022697
PlayerIDs['TeamSingularity']['Mastermind'] = 76561198052743718
PlayerIDs['TeamSingularity']['Mikey'] = 76561198137254121
PlayerIDs['TeamSingularity']['Solen'] = 76561197966369130
PlayerIDs['TeamSingularity']['Bashruk'] = 76561198046306000
ValidityTime['TeamSingularity'] = datetime.datetime(2018, 1, 31, 0, 0, 0, 0)#Adamsson

PlayerIDs['Cool Beans'] = collections.OrderedDict()
PlayerIDs['Cool Beans']['Loda'] = 76561198061761348
PlayerIDs['Cool Beans']['miCKe'] = 76561198113227791
PlayerIDs['Cool Beans']['Niqua'] = 76561197985441310
PlayerIDs['Cool Beans']['ComeWithMe'] = 76561198045640935
PlayerIDs['Cool Beans']['iNsania'] = 76561198014846690

PlayerIDs['HellRaisers'] = collections.OrderedDict()
PlayerIDs['HellRaisers']['33'] = 76561198046964005
PlayerIDs['HellRaisers']['Keyser'] = 76561198047027410
PlayerIDs['HellRaisers']['SexyBamboe'] = 76561197980587476
PlayerIDs['HellRaisers']['MiLAN'] = 76561198058438585
PlayerIDs['HellRaisers']['j4'] = 76561198036016318

PlayerIDs['RocketScientists'] = collections.OrderedDict()
PlayerIDs['RocketScientists']['NoX'] = 76561198129624977
PlayerIDs['RocketScientists']['Mastermind'] = 76561198052743718
PlayerIDs['RocketScientists']['Mikey'] = 76561198137254121
PlayerIDs['RocketScientists']['solen'] = 76561197966369130
PlayerIDs['RocketScientists']['Bashruk'] = 76561198046306000

PlayerIDs['No Diggity'] = collections.OrderedDict()
PlayerIDs['No Diggity']['Era'] = 76561198060583478
PlayerIDs['No Diggity']['MagE'] = 76561198138632092
PlayerIDs['No Diggity']['jonassomfan'] = 76561198000475053
PlayerIDs['No Diggity']['Handsken'] = 76561197978446698
PlayerIDs['No Diggity']['syndereN'] = 76561197964547457

PlayerIDs['Mid or Feed'] = collections.OrderedDict()
PlayerIDs['Mid or Feed']['Timado'] = 76561198057924346
PlayerIDs['Mid or Feed']['canceL'] = 76561198101955961
PlayerIDs['Mid or Feed']['KheZu'] = 76561198129291346
PlayerIDs['Mid or Feed']['w33'] = 76561198046966189
PlayerIDs['Mid or Feed']['syndereN'] = 76561197964547457

PlayerIDs['Final Tribe'] = collections.OrderedDict()
PlayerIDs['Final Tribe']['Era'] = 76561198060583478
PlayerIDs['Final Tribe']['Frost'] = 76561198129624977
PlayerIDs['Final Tribe']['jonassomfan'] = 76561198000475053
PlayerIDs['Final Tribe']['Pablo'] = 76561198077280895
PlayerIDs['Final Tribe']['Handsken'] = 76561197978446698
ValidityTime['Final Tribe'] = datetime.datetime(2018, 1, 28, 0, 0, 0, 0)#Final Tribe

PlayerIDs['Mad Lads'] = collections.OrderedDict()
PlayerIDs['Mad Lads']['Qojkva'] = 76561198047004422
PlayerIDs['Mad Lads']['Madara'] = 76561198055695796
PlayerIDs['Mad Lads']['Khezu'] = 76561198129291346
PlayerIDs['Mad Lads']['MaybeNextTime'] = 76561198047219142
PlayerIDs['Mad Lads']['Synderen'] = 76561197964547457


PlayerIDs['BlinkPool'] = collections.OrderedDict()
PlayerIDs['BlinkPool']['Madara'] = 76561198055695796
PlayerIDs['BlinkPool']['Keyser'] = 76561198047027410
PlayerIDs['BlinkPool']['Khezu'] = 76561198129291346
PlayerIDs['BlinkPool']['MISERY'] = 76561198047648307
PlayerIDs['BlinkPool']['Saksa'] = 76561198064001473

PlayerIDs['Kinguin'] = collections.OrderedDict()
PlayerIDs['Kinguin']['Exotic_Deer'] = 76561198022799638
PlayerIDs['Kinguin']['Nisha'] = 76561198082035378
PlayerIDs['Kinguin']['Patos'] = 76561198052632791
PlayerIDs['Kinguin']['eL_lisasH'] = 76561198017782041
PlayerIDs['Kinguin']['kacor'] = 76561197986622583
ValidityTime['Kinguin'] = datetime.datetime(2017, 9, 15, 0, 0, 0, 0)#Picked up from "lets do it"


PlayerIDs['Double Dimension'] = collections.OrderedDict()
PlayerIDs['Double Dimension']['Ditya Ra'] = 76561198129447626
PlayerIDs['Double Dimension']['Xcalibur'] = 76561198205638857
PlayerIDs['Double Dimension']['Mag'] = 76561198047068572
PlayerIDs['Double Dimension']['MiLAN'] = 76561198058438585
PlayerIDs['Double Dimension']['j4'] = 76561198036016318
ValidityTime['Double Dimension'] = datetime.datetime(2018, 2, 6, 0, 0, 0, 0)#Picked up from Planet Dog

PlayerIDs['SwissQualityGaming'] = collections.OrderedDict()
PlayerIDs['SwissQualityGaming']['RvP'] = 76561198076179908
PlayerIDs['SwissQualityGaming']['Tr1cky'] = 76561198060085308
PlayerIDs['SwissQualityGaming']['Madkingz'] = 76561198029868701
PlayerIDs['SwissQualityGaming']['W1sh'] = 76561198080879620
PlayerIDs['SwissQualityGaming']['davy'] = 76561197966464875

PlayerIDs['Immortals'] = collections.OrderedDict()
PlayerIDs['Immortals']['MP'] = 76561198061715811
PlayerIDs['Immortals']['Ryoya'] = 76561198075407158
PlayerIDs['Immortals']['Velo'] = 76561198070805039
PlayerIDs['Immortals']['Febby'] = 76561198072643187
PlayerIDs['Immortals']['DuBu'] = 76561198105816194

PlayerIDs['Kingdra'] = collections.OrderedDict()
PlayerIDs['Kingdra']['CharlieDota'] = 76561198082315226
PlayerIDs['Kingdra']['canceL'] = 76561198101955961
PlayerIDs['Kingdra']['SexyBamboe'] = 76561197980587476
PlayerIDs['Kingdra']['Biryu'] = 76561198047689051
PlayerIDs['Kingdra']['Jabbz'] = 76561198021208742

PlayerIDs['WindAndRain'] = collections.OrderedDict()
PlayerIDs['WindAndRain']['ritsu'] = 76561198137914641
PlayerIDs['WindAndRain']['Bryle'] = 76561198198505318
PlayerIDs['WindAndRain']['FoREv'] = 76561198049199322
PlayerIDs['WindAndRain']['MiLAN'] = 76561198058438585
PlayerIDs['WindAndRain']['Kitrak'] = 76561198148090048


_TeamIDs = {}

_TeamIDs['Random'] = 4253054

_TeamIDs['PlanetOdd'] = 4251435

_TeamIDs['mousesports'] = 26

_TeamIDs['EG']=39

_TeamIDs['Newbee']=1375614

_TeamIDs['EHOME']=4

_TeamIDs['Execration']=2581813

_TeamIDs['OG']=2586976

_TeamIDs['MVP']=1148284

_TeamIDs['TeamNP']=3214108

_TeamIDs['Complexity']=3

_TeamIDs['LGDFY']=3331948

_TeamIDs['LGD']=15

_TeamIDs['iGV']=2640025

_TeamIDs['VirtusPro']=1883502

_TeamIDs['Faceless']=3326875

_TeamIDs['Team Bazaar']=2659468

_TeamIDs['Alliance'] = 111474

_TeamIDs['Horde'] = 3326680

_TeamIDs['TeamSecret'] = 1838315

_TeamIDs['Cloud9'] = 2533075

_TeamIDs['Liquid'] = 2163

_TeamIDs['Navi'] = 36

_TeamIDs['VegaSquadron'] = 2006913

_TeamIDs['Infamous'] = 2672298

_TeamIDs['DigitalChaos'] = 5196328

_TeamIDs['Clutch Gamers'] = 3659536

_TeamIDs['Rex Regum'] = 1105664

_TeamIDs['Geek Fam'] = 3586078

_TeamIDs['TNC'] = 2108395

_TeamIDs['Mineski'] = 543897

_TeamIDs['Bazaar Youth'] = 3931120

_TeamIDs['Team Freedom'] = 4372042

_TeamIDs['Team Spirit'] = 2621843

_TeamIDs['Friends'] = 3332295

_TeamIDs['Elements Pro'] = 2537636

_TeamIDs['Elements'] = 5767350

_TeamIDs['Penta'] = 3704482

_TeamIDs['ProDota'] = 2552670

_TeamIDs['SGesports'] = 3580606

_TeamIDs['iG'] = 5

_TeamIDs['VGJ'] = 3547682

_TeamIDs['Effect'] = 2790766

_TeamIDs['NiP'] = 3729377

_TeamIDs['Empire'] = 46

_TeamIDs['VG'] = 726228

_TeamIDs['HappyFeet'] = 3725701

_TeamIDs['Crescendo'] = 4328182

_TeamIDs['Danish Bears'] = 464103

_TeamIDs['4Protect5'] = 3152713

_TeamIDs['TeamSingularity'] = 4186376

_TeamIDs['Cool Beans'] = 4703773

_TeamIDs['Planet Dog'] = 4593831

_TeamIDs['No Diggity'] = 5032952

_TeamIDs['Mid or Feed'] = 5059633

_TeamIDs['HellRaisers'] = 1846548

_TeamIDs['RocketScientists'] = 4541043

_TeamIDs['Final Tribe'] = 5059375

_TeamIDs['Mad Lads'] = 5229049

_TeamIDs['Kinguin'] = 5039050

_TeamIDs['Double Dimension'] = 5167588

_TeamIDs['SwissQualityGaming'] = 5097652

_TeamIDs['Immortals'] = 5040783

_TeamIDs['Five Dogs'] = -3

_TeamIDs['BlinkPool'] = 5870144

_TeamIDs['Kingdra'] = 2786652

_TeamIDs['WindAndRain'] = 5725202


#path = 'sqlite://'
path = None
engine = InitTeamDB(path)
Session = sessionmaker(bind=engine)
session = Session()

def make_db():
    import_from_old(_TeamIDs, PlayerIDs, ValidityTime, session)

make_db()