import enum
from dotenv import load_dotenv
from os import environ as environment
from pathlib import Path
from json import load


class HeroIDType(enum.Enum):
    NPC_NAME = enum.auto()
    NICK_NAME = enum.auto()
    ID_NUMBER = enum.auto()
    ICON_FILENAME = enum.auto()
    SPREADSHEET_NAME = enum.auto()


def convertName(name, input_format, output_format):
    if (input_format, output_format) in convDict:
        return convDict[(input_format, output_format)][name]
    # Try to npc which is a popular option
    if (input_format, HeroIDType.NPC_NAME) in convDict and (HeroIDType.NPC_NAME, output_format) in convDict:
        intermediate = convDict[(input_format, HeroIDType.NPC_NAME)][name]
        return convDict[(HeroIDType.NPC_NAME, output_format)][intermediate]
    elif (input_format == HeroIDType.NPC_NAME and output_format == HeroIDType.ICON_FILENAME):
        intermediate = convDict[(HeroIDType.NPC_NAME, HeroIDType.NICK_NAME)][name]
        return convDict[(HeroIDType.NICK_NAME, HeroIDType.ICON_FILENAME)][intermediate]
    else:
        raise ValueError("No valid conversions for {} and {}".format(input_format, output_format))


heroShortName = {}
heroShortName["npc_dota_hero_antimage"] = "AM"
heroShortName["npc_dota_hero_axe"] = "Axe"
heroShortName["npc_dota_hero_bane"] = "Bane"
heroShortName["npc_dota_hero_bloodseeker"] = "Bloodseeker"
heroShortName["npc_dota_hero_crystal_maiden"] = "CM"
heroShortName["npc_dota_hero_drow_ranger"] = "Drow"
heroShortName["npc_dota_hero_earthshaker"] = "Earthshaker"
heroShortName["npc_dota_hero_juggernaut"] = "Jug"
heroShortName["npc_dota_hero_mirana"] = "Mirana"
heroShortName["npc_dota_hero_morphling"] = "Morphling"
heroShortName["npc_dota_hero_nevermore"] = "Shadowfiend"
heroShortName["npc_dota_hero_phantom_lancer"] = "PL"
heroShortName["npc_dota_hero_puck"] = "Puck"
heroShortName["npc_dota_hero_pudge"] = "Pudge"
heroShortName["npc_dota_hero_razor"] = "Razor"
heroShortName["npc_dota_hero_sand_king"] = "Sandking"
heroShortName["npc_dota_hero_storm_spirit"] = "Storm"
heroShortName["npc_dota_hero_sven"] = "Sven"
heroShortName["npc_dota_hero_tiny"] = "Tiny"
heroShortName["npc_dota_hero_vengefulspirit"] = "Venge"
heroShortName["npc_dota_hero_windrunner"] = "Windrunner"
heroShortName["npc_dota_hero_zuus"] = "Zeus"
heroShortName["npc_dota_hero_kunkka"] = "Kunkka"
heroShortName["npc_dota_hero_lina"] = "Lina"
heroShortName["npc_dota_hero_lion"] = "Lion"
heroShortName["npc_dota_hero_shadow_shaman"] = "S. Shaman"
heroShortName["npc_dota_hero_slardar"] = "Slardar"
heroShortName["npc_dota_hero_tidehunter"] = "Tide"
heroShortName["npc_dota_hero_witch_doctor"] = "W. Doctor"
heroShortName["npc_dota_hero_lich"] = "Lich"
heroShortName["npc_dota_hero_riki"] = "Riki"
heroShortName["npc_dota_hero_enigma"] = "Enigma"
heroShortName["npc_dota_hero_tinker"] = "Tinker"
heroShortName["npc_dota_hero_sniper"] = "Sniper"
heroShortName["npc_dota_hero_necrolyte"] = "Necrophose"
heroShortName["npc_dota_hero_warlock"] = "Warlock"
heroShortName["npc_dota_hero_beastmaster"] = "Beast M"
heroShortName["npc_dota_hero_queenofpain"] = "Qwop"
heroShortName["npc_dota_hero_venomancer"] = "Venomancer"
heroShortName["npc_dota_hero_faceless_void"] = "Void"
heroShortName["npc_dota_hero_skeleton_king"] = "W. King"
heroShortName["npc_dota_hero_death_prophet"] = "D. Prophet"
heroShortName["npc_dota_hero_phantom_assassin"] = "PA"
heroShortName["npc_dota_hero_pugna"] = "Pugna"
heroShortName["npc_dota_hero_templar_assassin"] = "TA"
heroShortName["npc_dota_hero_viper"] = "Viper"
heroShortName["npc_dota_hero_luna"] = "Luna"
heroShortName["npc_dota_hero_dragon_knight"] = "D. Knight"
heroShortName["npc_dota_hero_dazzle"] = "Dazzle"
heroShortName["npc_dota_hero_rattletrap"] = "Clockwork"
heroShortName["npc_dota_hero_leshrac"] = "Leshrac"
heroShortName["npc_dota_hero_furion"] = "Natures Prophet"
heroShortName["npc_dota_hero_life_stealer"] = "Lifestealer"
heroShortName["npc_dota_hero_dark_seer"] = "Dark Seer"
heroShortName["npc_dota_hero_clinkz"] = "Clinkz"
heroShortName["npc_dota_hero_omniknight"] = "Omniknight"
heroShortName["npc_dota_hero_enchantress"] = "Enchantress"
heroShortName["npc_dota_hero_huskar"] = "Huskar"
heroShortName["npc_dota_hero_night_stalker"] = "N. Stalker"
heroShortName["npc_dota_hero_broodmother"] = "Broodmother"
heroShortName["npc_dota_hero_bounty_hunter"] = "Bounty"
heroShortName["npc_dota_hero_weaver"] = "Weaver"
heroShortName["npc_dota_hero_jakiro"] = "Jakiro"
heroShortName["npc_dota_hero_batrider"] = "Batrider"
heroShortName["npc_dota_hero_chen"] = "Chen"
heroShortName["npc_dota_hero_spectre"] = "Spectre"
heroShortName["npc_dota_hero_ancient_apparition"] = "AA"
heroShortName["npc_dota_hero_doom_bringer"] = "Doom"
heroShortName["npc_dota_hero_ursa"] = "Ursa"
heroShortName["npc_dota_hero_spirit_breaker"] = "Spiritbreaker"
heroShortName["npc_dota_hero_gyrocopter"] = "Gyrocopter"
heroShortName["npc_dota_hero_alchemist"] = "Alchemist"
heroShortName["npc_dota_hero_invoker"] = "Invoker"
heroShortName["npc_dota_hero_silencer"] = "Silencer"
heroShortName["npc_dota_hero_obsidian_destroyer"] = "OD"
heroShortName["npc_dota_hero_lycan"] = "Lycan"
heroShortName["npc_dota_hero_brewmaster"] = "Brew."
heroShortName["npc_dota_hero_shadow_demon"] = "S. Demon"
heroShortName["npc_dota_hero_lone_druid"] = "Lone Druid"
heroShortName["npc_dota_hero_chaos_knight"] = "Chaos Knight"
heroShortName["npc_dota_hero_meepo"] = "Meepo"
heroShortName["npc_dota_hero_treant"] = "Treant"
heroShortName["npc_dota_hero_ogre_magi"] = "Ogre"
heroShortName["npc_dota_hero_undying"] = "Undying"
heroShortName["npc_dota_hero_rubick"] = "Rubick"
heroShortName["npc_dota_hero_disruptor"] = "Disruptor"
heroShortName["npc_dota_hero_nyx_assassin"] = "Nyx"
heroShortName["npc_dota_hero_naga_siren"] = "Naga"
heroShortName["npc_dota_hero_keeper_of_the_light"] = "KOTL"
heroShortName["npc_dota_hero_wisp"] = "Wisp"
heroShortName["npc_dota_hero_visage"] = "Visage"
heroShortName["npc_dota_hero_slark"] = "Slark"
heroShortName["npc_dota_hero_medusa"] = "Medusa"
heroShortName["npc_dota_hero_troll_warlord"] = "Warlord"
heroShortName["npc_dota_hero_centaur"] = "Centaur"
heroShortName["npc_dota_hero_magnataur"] = "Magnus"
heroShortName["npc_dota_hero_shredder"] = "Timber"
heroShortName["npc_dota_hero_bristleback"] = "Bristle"
heroShortName["npc_dota_hero_tusk"] = "Tusk"
heroShortName["npc_dota_hero_skywrath_mage"] = "Skywrath"
heroShortName["npc_dota_hero_abaddon"] = "Abaddon"
heroShortName["npc_dota_hero_elder_titan"] = "E Titan"
heroShortName["npc_dota_hero_legion_commander"] = "LC"
heroShortName["npc_dota_hero_techies"] = "Techies"
heroShortName["npc_dota_hero_ember_spirit"] = "Ember"
heroShortName["npc_dota_hero_earth_spirit"] = "Earth Spirit"
heroShortName["npc_dota_hero_abyssal_underlord"] = "Underlord"
heroShortName["npc_dota_hero_terrorblade"] = "Terrorblade"
heroShortName["npc_dota_hero_phoenix"] = "Phoenix"
heroShortName["npc_dota_hero_oracle"] = "Oracle"
heroShortName["npc_dota_hero_winter_wyvern"] = "W Wyvern"
heroShortName["npc_dota_hero_arc_warden"] = "Arc Warden"
heroShortName["npc_dota_hero_monkey_king"] = "Monkey King"
heroShortName["npc_dota_hero_pangolier"] = "Pang"
heroShortName["npc_dota_hero_dark_willow"] = "D Willow"
heroShortName["npc_dota_hero_grimstroke"] = "Grimstroke"
heroShortName["npc_dota_hero_mars"] = "Mars"
heroShortName["npc_dota_hero_snapfire"] = "Snapfire"
heroShortName["npc_dota_hero_void_spirit"] = "Void Spirit"
heroShortName["npc_dota_hero_hoodwink"] = "Hoodwink"
heroShortName["npc_dota_hero_dawnbreaker"] = "Dawn Breaker"
heroShortName["npc_dota_hero_marci"] = "Marci"
heroShortName["npc_dota_hero_primal_beast"] = "Primal Beast"
heroShortName["Other"] = "Other"

heroByID = {}
heroByID[1] = "npc_dota_hero_antimage"
heroByID[2] = "npc_dota_hero_axe"
heroByID[3] = "npc_dota_hero_bane"
heroByID[4] = "npc_dota_hero_bloodseeker"
heroByID[5] = "npc_dota_hero_crystal_maiden"
heroByID[6] = "npc_dota_hero_drow_ranger"
heroByID[7] = "npc_dota_hero_earthshaker"
heroByID[8] = "npc_dota_hero_juggernaut"
heroByID[9] = "npc_dota_hero_mirana"
heroByID[10] = "npc_dota_hero_morphling"
heroByID[11] = "npc_dota_hero_nevermore"
heroByID[12] = "npc_dota_hero_phantom_lancer"
heroByID[13] = "npc_dota_hero_puck"
heroByID[14] = "npc_dota_hero_pudge"
heroByID[15] = "npc_dota_hero_razor"
heroByID[16] = "npc_dota_hero_sand_king"
heroByID[17] = "npc_dota_hero_storm_spirit"
heroByID[18] = "npc_dota_hero_sven"
heroByID[19] = "npc_dota_hero_tiny"
heroByID[20] = "npc_dota_hero_vengefulspirit"
heroByID[21] = "npc_dota_hero_windrunner"
heroByID[22] = "npc_dota_hero_zuus"
heroByID[23] = "npc_dota_hero_kunkka"
heroByID[25] = "npc_dota_hero_lina"
heroByID[26] = "npc_dota_hero_lion"
heroByID[27] = "npc_dota_hero_shadow_shaman"
heroByID[28] = "npc_dota_hero_slardar"
heroByID[29] = "npc_dota_hero_tidehunter"
heroByID[30] = "npc_dota_hero_witch_doctor"
heroByID[31] = "npc_dota_hero_lich"
heroByID[32] = "npc_dota_hero_riki"
heroByID[33] = "npc_dota_hero_enigma"
heroByID[34] = "npc_dota_hero_tinker"
heroByID[35] = "npc_dota_hero_sniper"
heroByID[36] = "npc_dota_hero_necrolyte"
heroByID[37] = "npc_dota_hero_warlock"
heroByID[38] = "npc_dota_hero_beastmaster"
heroByID[39] = "npc_dota_hero_queenofpain"
heroByID[40] = "npc_dota_hero_venomancer"
heroByID[41] = "npc_dota_hero_faceless_void"
heroByID[42] = "npc_dota_hero_skeleton_king"
heroByID[43] = "npc_dota_hero_death_prophet"
heroByID[44] = "npc_dota_hero_phantom_assassin"
heroByID[45] = "npc_dota_hero_pugna"
heroByID[46] = "npc_dota_hero_templar_assassin"
heroByID[47] = "npc_dota_hero_viper"
heroByID[48] = "npc_dota_hero_luna"
heroByID[49] = "npc_dota_hero_dragon_knight"
heroByID[50] = "npc_dota_hero_dazzle"
heroByID[51] = "npc_dota_hero_rattletrap"
heroByID[52] = "npc_dota_hero_leshrac"
heroByID[53] = "npc_dota_hero_furion"
heroByID[54] = "npc_dota_hero_life_stealer"
heroByID[55] = "npc_dota_hero_dark_seer"
heroByID[56] = "npc_dota_hero_clinkz"
heroByID[57] = "npc_dota_hero_omniknight"
heroByID[58] = "npc_dota_hero_enchantress"
heroByID[59] = "npc_dota_hero_huskar"
heroByID[60] = "npc_dota_hero_night_stalker"
heroByID[61] = "npc_dota_hero_broodmother"
heroByID[62] = "npc_dota_hero_bounty_hunter"
heroByID[63] = "npc_dota_hero_weaver"
heroByID[64] = "npc_dota_hero_jakiro"
heroByID[65] = "npc_dota_hero_batrider"
heroByID[66] = "npc_dota_hero_chen"
heroByID[67] = "npc_dota_hero_spectre"
heroByID[68] = "npc_dota_hero_ancient_apparition"
heroByID[69] = "npc_dota_hero_doom_bringer"
heroByID[70] = "npc_dota_hero_ursa"
heroByID[71] = "npc_dota_hero_spirit_breaker"
heroByID[72] = "npc_dota_hero_gyrocopter"
heroByID[73] = "npc_dota_hero_alchemist"
heroByID[74] = "npc_dota_hero_invoker"
heroByID[75] = "npc_dota_hero_silencer"
heroByID[76] = "npc_dota_hero_obsidian_destroyer"
heroByID[77] = "npc_dota_hero_lycan"
heroByID[78] = "npc_dota_hero_brewmaster"
heroByID[79] = "npc_dota_hero_shadow_demon"
heroByID[80] = "npc_dota_hero_lone_druid"
heroByID[81] = "npc_dota_hero_chaos_knight"
heroByID[82] = "npc_dota_hero_meepo"
heroByID[83] = "npc_dota_hero_treant"
heroByID[84] = "npc_dota_hero_ogre_magi"
heroByID[85] = "npc_dota_hero_undying"
heroByID[86] = "npc_dota_hero_rubick"
heroByID[87] = "npc_dota_hero_disruptor"
heroByID[88] = "npc_dota_hero_nyx_assassin"
heroByID[89] = "npc_dota_hero_naga_siren"
heroByID[90] = "npc_dota_hero_keeper_of_the_light"
heroByID[91] = "npc_dota_hero_wisp"
heroByID[92] = "npc_dota_hero_visage"
heroByID[93] = "npc_dota_hero_slark"
heroByID[94] = "npc_dota_hero_medusa"
heroByID[95] = "npc_dota_hero_troll_warlord"
heroByID[96] = "npc_dota_hero_centaur"
heroByID[97] = "npc_dota_hero_magnataur"
heroByID[98] = "npc_dota_hero_shredder"
heroByID[99] = "npc_dota_hero_bristleback"
heroByID[100] = "npc_dota_hero_tusk"
heroByID[101] = "npc_dota_hero_skywrath_mage"
heroByID[102] = "npc_dota_hero_abaddon"
heroByID[103] = "npc_dota_hero_elder_titan"
heroByID[104] = "npc_dota_hero_legion_commander"
heroByID[105] = "npc_dota_hero_techies"
heroByID[106] = "npc_dota_hero_ember_spirit"
heroByID[107] = "npc_dota_hero_earth_spirit"
heroByID[108] = "npc_dota_hero_abyssal_underlord"
heroByID[109] = "npc_dota_hero_terrorblade"
heroByID[110] = "npc_dota_hero_phoenix"
heroByID[111] = "npc_dota_hero_oracle"
heroByID[112] = "npc_dota_hero_winter_wyvern"
heroByID[113] = "npc_dota_hero_arc_warden"
heroByID[114] = "npc_dota_hero_monkey_king"
heroByID[120] = "npc_dota_hero_pangolier"
heroByID[119] = "npc_dota_hero_dark_willow"
heroByID[121] = "npc_dota_hero_grimstroke"
heroByID[129] = "npc_dota_hero_mars"
heroByID[126] = "npc_dota_hero_void_spirit"
heroByID[128] = "npc_dota_hero_snapfire"
heroByID[123] = "npc_dota_hero_hoodwink"
heroByID[135] = "npc_dota_hero_dawnbreaker"
heroByID[136] = "npc_dota_hero_marci"
heroByID[137] = "npc_dota_hero_primal_beast"

HeroLongName = {}
HeroLongName["AM"] = "npc_dota_hero_antimage"
HeroLongName["Axe"] = "npc_dota_hero_axe"
HeroLongName["Bane"] = "npc_dota_hero_bane"
HeroLongName["Bloodseeker"] = "npc_dota_hero_bloodseeker"
HeroLongName["CM"] = "npc_dota_hero_crystal_maiden"
HeroLongName["Drow"] = "npc_dota_hero_drow_ranger"
HeroLongName["Earthshaker"] = "npc_dota_hero_earthshaker"
HeroLongName["Jug"] = "npc_dota_hero_juggernaut"
HeroLongName["Mirana"] = "npc_dota_hero_mirana"
HeroLongName["Morphling"] = "npc_dota_hero_morphling"
HeroLongName["Shadowfiend"] = "npc_dota_hero_nevermore"
HeroLongName["PL"] = "npc_dota_hero_phantom_lancer"
HeroLongName["Puck"] = "npc_dota_hero_puck"
HeroLongName["Pudge"] = "npc_dota_hero_pudge"
HeroLongName["Razor"] = "npc_dota_hero_razor"
HeroLongName["Sandking"] = "npc_dota_hero_sand_king"
HeroLongName["Storm"] = "npc_dota_hero_storm_spirit"
HeroLongName["Sven"] = "npc_dota_hero_sven"
HeroLongName["Tiny"] = "npc_dota_hero_tiny"
HeroLongName["Venge"] = "npc_dota_hero_vengefulspirit"
HeroLongName["Windrunner"] = "npc_dota_hero_windrunner"
HeroLongName["Zeus"] = "npc_dota_hero_zuus"
HeroLongName["Kunkka"] = "npc_dota_hero_kunkka"
HeroLongName["Lina"] = "npc_dota_hero_lina"
HeroLongName["Lion"] = "npc_dota_hero_lion"
HeroLongName["S. Shaman"] = "npc_dota_hero_shadow_shaman"
HeroLongName["Slardar"] = "npc_dota_hero_slardar"
HeroLongName["Tide"] = "npc_dota_hero_tidehunter"
HeroLongName["W. Doctor"] = "npc_dota_hero_witch_doctor"
HeroLongName["Lich"] = "npc_dota_hero_lich"
HeroLongName["Riki"] = "npc_dota_hero_riki"
HeroLongName["Enigma"] = "npc_dota_hero_enigma"
HeroLongName["Tinker"] = "npc_dota_hero_tinker"
HeroLongName["Sniper"] = "npc_dota_hero_sniper"
HeroLongName["Necrophose"] = "npc_dota_hero_necrolyte"
HeroLongName["Warlock"] = "npc_dota_hero_warlock"
HeroLongName["Beast M"] = "npc_dota_hero_beastmaster"
HeroLongName["Qwop"] = "npc_dota_hero_queenofpain"
HeroLongName["Venomancer"] = "npc_dota_hero_venomancer"
HeroLongName["Void"] = "npc_dota_hero_faceless_void"
HeroLongName["W. King"] = "npc_dota_hero_skeleton_king"
HeroLongName["D. Prophet"] = "npc_dota_hero_death_prophet"
HeroLongName["PA"] = "npc_dota_hero_phantom_assassin"
HeroLongName["Pugna"] = "npc_dota_hero_pugna"
HeroLongName["TA"] = "npc_dota_hero_templar_assassin"
HeroLongName["Viper"] = "npc_dota_hero_viper"
HeroLongName["Luna"] = "npc_dota_hero_luna"
HeroLongName["D. Knight"] = "npc_dota_hero_dragon_knight"
HeroLongName["Dazzle"] = "npc_dota_hero_dazzle"
HeroLongName["Clockwork"] = "npc_dota_hero_rattletrap"
HeroLongName["Leshrac"] = "npc_dota_hero_leshrac"
HeroLongName["Natures Prophet"] = "npc_dota_hero_furion"
HeroLongName["Lifestealer"] = "npc_dota_hero_life_stealer"
HeroLongName["Dark Seer"] = "npc_dota_hero_dark_seer"
HeroLongName["Clinkz"] = "npc_dota_hero_clinkz"
HeroLongName["Omniknight"] = "npc_dota_hero_omniknight"
HeroLongName["Enchantress"] = "npc_dota_hero_enchantress"
HeroLongName["Huskar"] = "npc_dota_hero_huskar"
HeroLongName["N. Stalker"] = "npc_dota_hero_night_stalker"
HeroLongName["Broodmother"] = "npc_dota_hero_broodmother"
HeroLongName["Bounty"] = "npc_dota_hero_bounty_hunter"
HeroLongName["Weaver"] = "npc_dota_hero_weaver"
HeroLongName["Jakiro"] = "npc_dota_hero_jakiro"
HeroLongName["Batrider"] = "npc_dota_hero_batrider"
HeroLongName["Chen"] = "npc_dota_hero_chen"
HeroLongName["Spectre"] = "npc_dota_hero_spectre"
HeroLongName["AA"] = "npc_dota_hero_ancient_apparition"
HeroLongName["Doom"] = "npc_dota_hero_doom_bringer"
HeroLongName["Ursa"] = "npc_dota_hero_ursa"
HeroLongName["Spiritbreaker"] = "npc_dota_hero_spirit_breaker"
HeroLongName["Gyrocopter"] = "npc_dota_hero_gyrocopter"
HeroLongName["Alchemist"] = "npc_dota_hero_alchemist"
HeroLongName["Invoker"] = "npc_dota_hero_invoker"
HeroLongName["Silencer"] = "npc_dota_hero_silencer"
HeroLongName["OD"] = "npc_dota_hero_obsidian_destroyer"
HeroLongName["Lycan"] = "npc_dota_hero_lycan"
HeroLongName["Brew."] = "npc_dota_hero_brewmaster"
HeroLongName["S. Demon"] = "npc_dota_hero_shadow_demon"
HeroLongName["Lone Druid"] = "npc_dota_hero_lone_druid"
HeroLongName["Chaos Knight"] = "npc_dota_hero_chaos_knight"
HeroLongName["Meepo"] = "npc_dota_hero_meepo"
HeroLongName["Treant"] = "npc_dota_hero_treant"
HeroLongName["Ogre"] = "npc_dota_hero_ogre_magi"
HeroLongName["Undying"] = "npc_dota_hero_undying"
HeroLongName["Rubick"] = "npc_dota_hero_rubick"
HeroLongName["Disruptor"] = "npc_dota_hero_disruptor"
HeroLongName["Nyx"] = "npc_dota_hero_nyx_assassin"
HeroLongName["Naga"] = "npc_dota_hero_naga_siren"
HeroLongName["KOTL"] = "npc_dota_hero_keeper_of_the_light"
HeroLongName["Wisp"] = "npc_dota_hero_wisp"
HeroLongName["Visage"] = "npc_dota_hero_visage"
HeroLongName["Slark"] = "npc_dota_hero_slark"
HeroLongName["Medusa"] = "npc_dota_hero_medusa"
HeroLongName["Warlord"] = "npc_dota_hero_troll_warlord"
HeroLongName["Centaur"] = "npc_dota_hero_centaur"
HeroLongName["Magnus"] = "npc_dota_hero_magnataur"
HeroLongName["Timber"] = "npc_dota_hero_shredder"
HeroLongName["Bristle"] = "npc_dota_hero_bristleback"
HeroLongName["Tusk"] = "npc_dota_hero_tusk"
HeroLongName["Skywrath"] = "npc_dota_hero_skywrath_mage"
HeroLongName["Abaddon"] = "npc_dota_hero_abaddon"
HeroLongName["E Titan"] = "npc_dota_hero_elder_titan"
HeroLongName["LC"] = "npc_dota_hero_legion_commander"
HeroLongName["Techies"] = "npc_dota_hero_techies"
HeroLongName["Ember"] = "npc_dota_hero_ember_spirit"
HeroLongName["Earth Spirit"] = "npc_dota_hero_earth_spirit"
HeroLongName["Underlord"] = "npc_dota_hero_abyssal_underlord"
HeroLongName["Terrorblade"] = "npc_dota_hero_terrorblade"
HeroLongName["Phoenix"] = "npc_dota_hero_phoenix"
HeroLongName["Oracle"] = "npc_dota_hero_oracle"
HeroLongName["W Wyvern"] = "npc_dota_hero_winter_wyvern"
HeroLongName["Arc Warden"] = "npc_dota_hero_arc_warden"
HeroLongName["Monkey King"] = "npc_dota_hero_monkey_king"
HeroLongName["Pang"] = "npc_dota_hero_pangolier"
HeroLongName["D Willow"] = "npc_dota_hero_dark_willow"
HeroLongName["Grimstroke"] = "npc_dota_hero_grimstroke"
HeroLongName["Mars"] = "npc_dota_hero_mars"
HeroLongName["Void Spirit"] = "npc_dota_hero_void_spirit"
HeroLongName["Snapfire"] = "npc_dota_hero_snapfire"
HeroLongName["Hoodwink"] = "npc_dota_hero_hoodwink"
HeroLongName["Dawn Breaker"] = "npc_dota_hero_dawnbreaker"
HeroLongName["Marci"] = "npc_dota_hero_marci"
HeroLongName["Primal Beast"] = "npc_dota_hero_primal_beast"
HeroLongName["Other"] = "Other"

HeroIconPrefix = Path(environment['ICON_PATH'])
HeroIcon = {}
HeroIcon["AM"] = "antimage.png"
HeroIcon["Axe"] = "axe.png"
HeroIcon["Bane"] = "bane.png"
HeroIcon["Bloodseeker"] = "bloodseeker.png"
HeroIcon["CM"] = "crystal_maiden.png"
HeroIcon["Drow"] = "drow.png"
HeroIcon["Earthshaker"] = "earthshaker.png"
HeroIcon["Jug"] = "juggernaut.png"
HeroIcon["Mirana"] = "mirana.png"
HeroIcon["Morphling"] = "morphling.png"
HeroIcon["Shadowfiend"] = "nevermore.png"
HeroIcon["PL"] = "phantom_lancer.png"
HeroIcon["Puck"] = "puck.png"
HeroIcon["Pudge"] = "pudge.png"
HeroIcon["Razor"] = "razor.png"
HeroIcon["Sandking"] = "sandking.png"
HeroIcon["Storm"] = "storm_spirit.png"
HeroIcon["Sven"] = "sven.png"
HeroIcon["Tiny"] = "tiny.png"
HeroIcon["Venge"] = "vengefulspirit.png"
HeroIcon["Windrunner"] = "windrunner.png"
HeroIcon["Zeus"] = "zuus.png"
HeroIcon["Kunkka"] = "kunkka.png"
HeroIcon["Lina"] = "lina.png"
HeroIcon["Lion"] = "lion.png"
HeroIcon["S. Shaman"] = "shadow_shaman.png"
HeroIcon["Slardar"] = "slardar.png"
HeroIcon["Tide"] = "tidehunter.png"
HeroIcon["W. Doctor"] = "witch_doctor.png"
HeroIcon["Lich"] = "lich.png"
HeroIcon["Riki"] = "riki.png"
HeroIcon["Enigma"] = "enigma.png"
HeroIcon["Tinker"] = "tinker.png"
HeroIcon["Sniper"] = "sniper.png"
HeroIcon["Necrophose"] = "necrolyte.png"
HeroIcon["Warlock"] = "warlock.png"
HeroIcon["Beast M"] = "beastmaster.png"
HeroIcon["Qwop"] = "queenofpain.png"
HeroIcon["Venomancer"] = "venomancer.png"
HeroIcon["Void"] = "faceless_void.png"
HeroIcon["W. King"] = "skeleton_king.png"
HeroIcon["D. Prophet"] = "death_prophet.png"
HeroIcon["PA"] = "phantom_assassin.png"
HeroIcon["Pugna"] = "pugna.png"
HeroIcon["TA"] = "templar_assassin.png"
HeroIcon["Viper"] = "viper.png"
HeroIcon["Luna"] = "luna.png"
HeroIcon["D. Knight"] = "dragon_knight.png"
HeroIcon["Dazzle"] = "dazzle.png"
HeroIcon["Clockwork"] = "rattletrap.png"
HeroIcon["Leshrac"] = "leshrac.png"
HeroIcon["Natures Prophet"] = "furion.png"
HeroIcon["Lifestealer"] = "life_stealer.png"
HeroIcon["Dark Seer"] = "dark_seer.png"
HeroIcon["Clinkz"] = "clinkz.png"
HeroIcon["Omniknight"] = "omniknight.png"
HeroIcon["Enchantress"] = "enchantress.png"
HeroIcon["Huskar"] = "huskar.png"
HeroIcon["N. Stalker"] = "night_stalker.png"
HeroIcon["Broodmother"] = "broodmother.png"
HeroIcon["Bounty"] = "bounty_hunter.png"
HeroIcon["Weaver"] = "weaver.png"
HeroIcon["Jakiro"] = "jakiro.png"
HeroIcon["Batrider"] = "batrider.png"
HeroIcon["Chen"] = "chen.png"
HeroIcon["Spectre"] = "spectre.png"
HeroIcon["AA"] = "ancient_apparition.png"
HeroIcon["Doom"] = "doom.png"
HeroIcon["Ursa"] = "ursa.png"
HeroIcon["Spiritbreaker"] = "spirit_breaker.png"
HeroIcon["Gyrocopter"] = "gyrocopter.png"
HeroIcon["Alchemist"] = "alchemist.png"
HeroIcon["Invoker"] = "invoker.png"
HeroIcon["Silencer"] = "silencer.png"
HeroIcon["OD"] = "obsidian_destroyer.png"
HeroIcon["Lycan"] = "lycan.png"
HeroIcon["Brew."] = "brewmaster.png"
HeroIcon["S. Demon"] = "shadow_demon.png"
HeroIcon["Lone Druid"] = "lone_druid.png"
HeroIcon["Chaos Knight"] = "chaos_knight.png"
HeroIcon["Meepo"] = "meepo.png"
HeroIcon["Treant"] = "treant.png"
HeroIcon["Ogre"] = "ogre_magi.png"
HeroIcon["Undying"] = "undying.png"
HeroIcon["Rubick"] = "rubick.png"
HeroIcon["Disruptor"] = "disruptor.png"
HeroIcon["Nyx"] = "nyx_assassin.png"
HeroIcon["Naga"] = "naga_siren.png"
HeroIcon["KOTL"] = "keeper_of_the_light.png"
HeroIcon["Wisp"] = "wisp.png"
HeroIcon["Visage"] = "visage.png"
HeroIcon["Slark"] = "slark.png"
HeroIcon["Medusa"] = "medusa.png"
HeroIcon["Warlord"] = "troll_warlord.png"
HeroIcon["Centaur"] = "centaur.png"
HeroIcon["Magnus"] = "magnataur.png"
HeroIcon["Timber"] = "shredder.png"
HeroIcon["Bristle"] = "bristleback.png"
HeroIcon["Tusk"] = "tusk.png"
HeroIcon["Skywrath"] = "skywrath_mage.png"
HeroIcon["Abaddon"] = "abaddon.png"
HeroIcon["E Titan"] = "elder_titan.png"
HeroIcon["LC"] = "legion_commander.png"
HeroIcon["Techies"] = "techies.png"
HeroIcon["Ember"] = "ember_spirit.png"
HeroIcon["Earth Spirit"] = "earth_spirit.png"
HeroIcon["Underlord"] = "abyssal_underlord.png"
HeroIcon["Terrorblade"] = "terrorblade.png"
HeroIcon["Phoenix"] = "phoenix.png"
HeroIcon["Oracle"] = "oracle.png"
HeroIcon["W Wyvern"] = "winter_wyvern.png"
HeroIcon["Arc Warden"] = "arcwarden.png"
HeroIcon["Other"] = "other2.png"
HeroIcon["Monkey King"] = "monkey_king.png"
HeroIcon["Pang"] = "pangolier.png"
HeroIcon["D Willow"] = "dark_willow.png"
HeroIcon["Grimstroke"] = "grimstroke.png"
HeroIcon["Mars"] = "mars.png"
HeroIcon["Snapfire"] = "snapfire.png"
HeroIcon["Void Spirit"] = "void_spirit.png"
HeroIcon["Hoodwink"] = "hoodwink.png"
HeroIcon["Dawn Breaker"] = "dawnbreaker.png"
HeroIcon["Marci"] = "marci.png"
HeroIcon["Primal Beast"] = "primal_beast.png"

SheetHeroMap = {
               "npc_dota_hero_abaddon": "abaddon",
               "npc_dota_hero_alchemist": "alchemist",
               "npc_dota_hero_ancient_apparition": "ancient_apparition",
               "npc_dota_hero_antimage": "antimage",
               "npc_dota_hero_arc_warden": "arc_warden",
               "npc_dota_hero_axe": "axe",
               "npc_dota_hero_bane": "bane",
               "npc_dota_hero_batrider": "batrider",
               "npc_dota_hero_beastmaster": "beastmaster",
               "npc_dota_hero_bloodseeker": "bloodseeker",
               "npc_dota_hero_bounty_hunter": "bounty_hunter",
               "npc_dota_hero_brewmaster": "brewmaster",
               "npc_dota_hero_bristleback": "bristleback",
               "npc_dota_hero_broodmother": "broodmother",
               "npc_dota_hero_centaur": "centaur",
               "npc_dota_hero_chaos_knight": "chaos_knight",
               "npc_dota_hero_chen": "chen",
               "npc_dota_hero_clinkz": "clinkz",
               "npc_dota_hero_rattletrap": "clockwerk",
               "npc_dota_hero_crystal_maiden": "crystal_maiden",
               "npc_dota_hero_dark_willow": "dark_willow",
               "npc_dota_hero_dark_seer": "dark_seer",
               "npc_dota_hero_dazzle": "dazzle",
               "npc_dota_hero_death_prophet": "death_prophet",
               "npc_dota_hero_disruptor": "disruptor",
               "npc_dota_hero_doom_bringer": "doom",
               "npc_dota_hero_dragon_knight": "dragon_knight",
               "npc_dota_hero_drow_ranger": "drow_ranger",
               "npc_dota_hero_earth_spirit": "earth_spirit",
               "npc_dota_hero_earthshaker": "earthshaker",
               "npc_dota_hero_elder_titan": "elder_titan",
               "npc_dota_hero_ember_spirit": "ember_spirit",
               "npc_dota_hero_enchantress": "enchantress",
               "npc_dota_hero_enigma": "enigma",
               "npc_dota_hero_faceless_void": "faceless_void",
               "npc_dota_hero_gyrocopter": "gyrocopter",
               "npc_dota_hero_huskar": "huskar",
               "npc_dota_hero_invoker": "invoker",
               "npc_dota_hero_wisp": "wisp",
               "npc_dota_hero_jakiro": "jakiro",
               "npc_dota_hero_juggernaut": "juggernaut",
               "npc_dota_hero_keeper_of_the_light": "keeper_of_the_light",
               "npc_dota_hero_kunkka": "kunkka",
               "npc_dota_hero_legion_commander": "legion_commander",
               "npc_dota_hero_leshrac": "leshrac",
               "npc_dota_hero_lich": "lich",
               "npc_dota_hero_life_stealer": "lifestealer",
               "npc_dota_hero_lina": "lina",
               "npc_dota_hero_lion": "lion",
               "npc_dota_hero_lone_druid": "lone_druid",
               "npc_dota_hero_luna": "luna",
               "npc_dota_hero_lycan": "lycan",
               "npc_dota_hero_magnataur": "magnus",
               "npc_dota_hero_medusa": "medusa",
               "npc_dota_hero_meepo": "meepo",
               "npc_dota_hero_mirana": "mirana",
               "npc_dota_hero_monkey_king": "monkey_king",
               "npc_dota_hero_morphling": "morphling",
               "npc_dota_hero_naga_siren": "naga_siren",
               "npc_dota_hero_furion": "natures_prophet",
               "npc_dota_hero_necrolyte": "necrophos",
               "npc_dota_hero_night_stalker": "night_stalker",
               "npc_dota_hero_nyx_assassin": "nyx_assassin",
               "npc_dota_hero_ogre_magi": "ogre_magi",
               "npc_dota_hero_omniknight": "omniknight",
               "npc_dota_hero_oracle": "oracle",
               "npc_dota_hero_obsidian_destroyer": "outworld_devourer",
               "npc_dota_hero_pangolier": "pangolier",
               "npc_dota_hero_phantom_assassin": "phantom_assassin",
               "npc_dota_hero_phantom_lancer": "phantom_lancer",
               "npc_dota_hero_phoenix": "phoenix",
               "npc_dota_hero_puck": "puck",
               "npc_dota_hero_pudge": "pudge",
               "npc_dota_hero_pugna": "pugna",
               "npc_dota_hero_queenofpain": "queenofpain",
               "npc_dota_hero_razor": "razor",
               "npc_dota_hero_riki": "riki",
               "npc_dota_hero_rubick": "rubick",
               "npc_dota_hero_sand_king": "sand_king",
               "npc_dota_hero_shadow_demon": "shadow_demon",
               "npc_dota_hero_nevermore": "shadow_fiend",
               "npc_dota_hero_shadow_shaman": "shadow_shaman",
               "npc_dota_hero_silencer": "silencer",
               "npc_dota_hero_skywrath_mage": "skywrath_mage",
               "npc_dota_hero_slardar": "slardar",
               "npc_dota_hero_slark": "slark",
               "npc_dota_hero_sniper": "sniper",
               "npc_dota_hero_spectre": "spectre",
               "npc_dota_hero_spirit_breaker": "spirit_breaker",
               "npc_dota_hero_storm_spirit": "storm_spirit",
               "npc_dota_hero_sven": "sven",
               "npc_dota_hero_techies": "techies",
               "npc_dota_hero_templar_assassin": "templar_assassin",
               "npc_dota_hero_terrorblade": "terrorblade",
               "npc_dota_hero_tidehunter": "tidehunter",
               "npc_dota_hero_shredder": "timbersaw",
               "npc_dota_hero_tinker": "tinker",
               "npc_dota_hero_tiny": "tiny",
               "npc_dota_hero_treant": "treant",
               "npc_dota_hero_troll_warlord": "troll_warlord",
               "npc_dota_hero_tusk": "tusk",
               "npc_dota_hero_abyssal_underlord": "underlord",
               "npc_dota_hero_undying": "undying",
               "npc_dota_hero_ursa": "ursa",
               "npc_dota_hero_vengefulspirit": "vengefulspirit",
               "npc_dota_hero_venomancer": "venomancer",
               "npc_dota_hero_viper": "viper",
               "npc_dota_hero_visage": "visage",
               "npc_dota_hero_warlock": "warlock",
               "npc_dota_hero_weaver": "weaver",
               "npc_dota_hero_windrunner": "windrunner",
               "npc_dota_hero_winter_wyvern": "winter_wyvern",
               "npc_dota_hero_witch_doctor": "witch_doctor",
               "npc_dota_hero_skeleton_king": "wraith_king",
               "npc_dota_hero_zuus": "zeus",
               "npc_dota_hero_grimstroke": "grimstroke",
               "npc_dota_hero_mars": "mars",
               "npc_dota_hero_hoodwink": "hoodwink",
               "npc_dota_hero_dawnbreaker": "dawnbreaker",
               "npc_dota_hero_marci": "marci",
}

hero_portrait_prefix = Path(environment['PORTRAIT_PATH'])
with open(Path('./data/hero_portraits.json'), 'r') as f:
    hero_portrait = load(f)

convDict = {
    (HeroIDType.NPC_NAME, HeroIDType.NICK_NAME): heroShortName,
    (HeroIDType.ID_NUMBER, HeroIDType.NPC_NAME): heroByID,
    (HeroIDType.NICK_NAME, HeroIDType.NPC_NAME): HeroLongName,
    (HeroIDType.NICK_NAME, HeroIDType.ICON_FILENAME): HeroIcon,
    (HeroIDType.NPC_NAME, HeroIDType.SPREADSHEET_NAME): SheetHeroMap
}