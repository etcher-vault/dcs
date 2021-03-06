# This file is generated from pydcs_export.lua

from .weapons_data import Weapons
from . import task
from .unittype import FlyingType
from enum import Enum


class HelicopterType(FlyingType):
    helicopter = True


class Ka_50(HelicopterType):
    id = "Ka-50"
    flyable = True
    height = 5.6
    width = 14.4
    length = 15.84
    fuel_max = 1450
    max_speed = 300
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 0
    flare_charge_size = 1
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                7: 40,
                1: 21.5,
                2: 25.7,
                4: 28,
                8: 50,
                9: 55.5,
                5: 30,
                10: 59.9,
                3: 27,
                6: 32
            },
        },
        2: {
            "channels": {
                15: 0.995,
                13: 0.583,
                7: 0.443,
                1: 0.625,
                2: 0.303,
                4: 0.591,
                8: 0.215,
                16: 1.21,
                9: 0.525,
                5: 0.408,
                10: 1.065,
                14: 0.283,
                3: 0.289,
                6: 0.803,
                12: 0.35,
                11: 0.718
            },
        },
    }

    class Liveries:

        class Georgia(Enum):
            georgia_camo = "georgia camo"

        class Australia(Enum):
            Russia_Worn_Black = "Russia Worn Black"

        class Germany(Enum):
            german_8320 = "german 8320"
            german_8332 = "german 8332"

        class Israel(Enum):
            Israel_IAF_camo_1 = "Israel IAF camo 1"
            Israel_IAF_camo_2 = "Israel IAF camo 2"
            Israel_IAF_camo_3 = "Israel IAF camo 3"

        class Norway(Enum):
            norway_camo = "norway camo"

        class Spain(Enum):
            Spain_SAA_Arido = "Spain SAA Arido"
            Spain_SAA_Boscoso = "Spain SAA Boscoso"
            Spain_SAA_Standard = "Spain SAA Standard"

        class Ukraine(Enum):
            Ukraine_Demo = "Ukraine Demo"
            ukraine_camo_1 = "ukraine camo 1"
            ukraine_camo_1_dirt = "ukraine camo 1 dirt"

        class Belgium(Enum):
            belgium_sar = "belgium sar"
            belgium_camo = "belgium camo"
            belgium_olive = "belgium olive"

        class Greece(Enum):
            Greek_Army_Aviation = "Greek Army Aviation"
            Hellenic_Navy_Aviation = "Hellenic Navy Aviation"
            Hellenic_Navy_Aviation_2 = "Hellenic Navy Aviation 2"

        class UK(Enum):
            uk_camo = "uk camo"

        class France(Enum):
            France_Armee_de_Terre_1 = "France Armee de Terre 1"
            France_Armee_de_Terre_2 = "France Armee de Terre 2"
            France_Armee_de_Terre_Desert = "France Armee de Terre Desert"

        class Abkhazia(Enum):
            Abkhazia_1 = "Abkhazia 1"

        class Russia(Enum):
            Russia_Standard_Army = "Russia Standard Army"
            Russia_DOSAAF = "Russia DOSAAF"
            Russia_Demo__024 = "Russia Demo #024"
            Russia_Demo__22__Black_Shark = "Russia Demo #22 `Black Shark`"
            Russia_Demo__Werewolf = "Russia Demo `Werewolf`"
            Russia_Fictional_Swedish = "Russia Fictional Swedish"
            Russia_fictional_desert_scheme = "Russia fictional desert scheme"
            Russia_Fictional_Olive_Grey = "Russia Fictional Olive Grey"
            Russia_Fictional_Snow_Splatter = "Russia Fictional Snow Splatter"
            Russia_Fictional_Tropic_Green = "Russia Fictional Tropic Green"
            Russia_New_Year = "Russia New Year"
            Russia_Standard_Army__Worn = "Russia Standard Army (Worn)"
            Russia_Worn_Black = "Russia Worn Black"

        class Italy(Enum):
            Italy_Aeronautica_Militare = "Italy Aeronautica Militare"
            Italy_Esercito_Italiano = "Italy Esercito Italiano"

        class SouthOssetia(Enum):
            South_Ossetia_1 = "South Ossetia 1"

        class USA(Enum):
            us_army = "us army"
            us_marines_1 = "us marines 1"
            us_marines_2 = "us marines 2"

        class Denmark(Enum):
            denmark_camo = "denmark camo"
            Denmark_navy_trainer = "Denmark navy trainer"

        class Canada(Enum):
            canadian_forces = "canadian forces"

        class TheNetherlands(Enum):
            Netherlands_RNAF = "Netherlands RNAF"
            Netherlands_RNAF_wooded = "Netherlands RNAF wooded"

        class Turkey(Enum):
            Turkey_Fictional_Light_Gray = "Turkey Fictional Light Gray"
            Turkey_Fictional_1 = "Turkey Fictional 1"
            Turkey_Fictional = "Turkey Fictional"
            Turkey_fictional_desert_scheme = "Turkey fictional desert scheme"

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        APU_6___6_9A4172_Vikhr = (1, Weapons.APU_6___6_9A4172_Vikhr)
        Kh_25ML = (1, Weapons.Kh_25ML)
        B_8V20A___20_S_8KOM = (1, Weapons.B_8V20A___20_S_8KOM)
        B_13L___5_S_13_OF = (1, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (1, Weapons.UPK_23_250)
        KMGU_2___96_AO_2_5RT = (1, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (1, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (1, Weapons.FAB_250)
        FAB_500_M62 = (1, Weapons.FAB_500_M62)
        Fuel_tank_Ka_50 = (1, Weapons.Fuel_tank_Ka_50)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (2, Weapons.UPK_23_250)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        Fuel_tank_Ka_50 = (2, Weapons.Fuel_tank_Ka_50)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (3, Weapons.UPK_23_250)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        Fuel_tank_Ka_50 = (3, Weapons.Fuel_tank_Ka_50)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        APU_6___6_9A4172_Vikhr = (4, Weapons.APU_6___6_9A4172_Vikhr)
        Kh_25ML = (4, Weapons.Kh_25ML)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (4, Weapons.UPK_23_250)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (4, Weapons.FAB_250)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        Fuel_tank_Ka_50 = (4, Weapons.Fuel_tank_Ka_50)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Ka_52(HelicopterType):
    id = "Ka-52"
    height = 5.6
    width = 14.4
    length = 15.84
    fuel_max = 1500
    max_speed = 300
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Georgia(Enum):
            standard = "standard"

        class Syria(Enum):
            standard = "standard"

        class Finland(Enum):
            standard = "standard"

        class Australia(Enum):
            standard = "standard"

        class Germany(Enum):
            standard = "standard"

        class SaudiArabia(Enum):
            standard = "standard"

        class Israel(Enum):
            standard = "standard"

        class Croatia(Enum):
            standard = "standard"

        class CzechRepublic(Enum):
            standard = "standard"

        class Norway(Enum):
            standard = "standard"

        class Romania(Enum):
            standard = "standard"

        class Spain(Enum):
            standard = "standard"

        class Ukraine(Enum):
            standard = "standard"

        class Belgium(Enum):
            standard = "standard"

        class Slovakia(Enum):
            standard = "standard"

        class Greece(Enum):
            standard = "standard"

        class UK(Enum):
            standard = "standard"

        class Insurgents(Enum):
            standard = "standard"

        class Hungary(Enum):
            standard = "standard"

        class France(Enum):
            standard = "standard"

        class Abkhazia(Enum):
            standard = "standard"

        class Russia(Enum):
            standard = "standard"

        class Sweden(Enum):
            standard = "standard"

        class Austria(Enum):
            standard = "standard"

        class Switzerland(Enum):
            standard = "standard"

        class Italy(Enum):
            standard = "standard"

        class SouthOssetia(Enum):
            standard = "standard"

        class SouthKorea(Enum):
            standard = "standard"

        class Iran(Enum):
            standard = "standard"

        class China(Enum):
            standard = "standard"

        class Pakistan(Enum):
            standard = "standard"

        class Belarus(Enum):
            standard = "standard"

        class NorthKorea(Enum):
            standard = "standard"

        class Iraq(Enum):
            standard = "standard"

        class Kazakhstan(Enum):
            standard = "standard"

        class Bulgaria(Enum):
            standard = "standard"

        class Serbia(Enum):
            standard = "standard"

        class India(Enum):
            standard = "standard"

        class USAFAggressors(Enum):
            standard = "standard"

        class USA(Enum):
            standard = "standard"

        class Denmark(Enum):
            standard = "standard"

        class Egypt(Enum):
            standard = "standard"

        class Canada(Enum):
            standard = "standard"

        class TheNetherlands(Enum):
            standard = "standard"

        class Turkey(Enum):
            standard = "standard"

        class Japan(Enum):
            standard = "standard"

        class Poland(Enum):
            standard = "standard"

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (1, Weapons.B_8V20A___20_S_8KOM)
        R_73 = (1, Weapons.R_73)
        APU_6___6_9A4172_Vikhr = (1, Weapons.APU_6___6_9A4172_Vikhr)
        B_13L___5_S_13_OF = (1, Weapons.B_13L___5_S_13_OF)
        KMGU_2___96_AO_2_5RT = (1, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (1, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (1, Weapons.FAB_250)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)
        Kh_25ML = (2, Weapons.Kh_25ML)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)
        Kh_25ML = (3, Weapons.Kh_25ML)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)
        APU_6___6_9A4172_Vikhr = (4, Weapons.APU_6___6_9A4172_Vikhr)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        FAB_250 = (4, Weapons.FAB_250)
        R_73 = (4, Weapons.R_73)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.PinpointStrike, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Mi_24V(HelicopterType):
    id = "Mi-24V"
    height = 4.354
    width = 17.3
    length = 20.953
    fuel_max = 1704
    max_speed = 320
    chaff = 0
    flare = 192
    charge_total = 192
    chaff_charge_size = 0
    flare_charge_size = 1

    class Liveries:

        class Georgia(Enum):
            standard = "standard"

        class Ukraine(Enum):
            ukraine = "ukraine"
            Ukraine_UN = "Ukraine UN"

        class Abkhazia(Enum):
            Abkhazia = "Abkhazia"

        class Russia(Enum):
            standard_1 = "standard 1"
            standard_2__faded_and_sun_bleached = "standard 2 (faded and sun-bleached)"
            Russia_FSB = "Russia_FSB"
            Russia_MVD = "Russia_MVD"

        class SouthOssetia(Enum):
            South_Ossetia = "South Ossetia"

    class Pylon1:
        _9M114_Shturm_V___2 = (1, Weapons._9M114_Shturm_V___2)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        UB_32A___32_S_5KO = (2, Weapons.UB_32A___32_S_5KO)
        _9M114_Shturm_V___2 = (2, Weapons._9M114_Shturm_V___2)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (2, Weapons.UPK_23_250)
        Fuel_tank_Ka_50 = (2, Weapons.Fuel_tank_Ka_50)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)
        GUV_VOG = (2, Weapons.GUV_VOG)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        UB_32A___32_S_5KO = (3, Weapons.UB_32A___32_S_5KO)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (3, Weapons.UPK_23_250)
        Fuel_tank_Ka_50 = (3, Weapons.Fuel_tank_Ka_50)
        GUV_YakB_GSHP = (3, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (3, Weapons.GUV_VOG)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        UB_32A___32_S_5KO = (4, Weapons.UB_32A___32_S_5KO)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (4, Weapons.FAB_250)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        B_8M1___20_S_8TsM = (4, Weapons.B_8M1___20_S_8TsM)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (4, Weapons.UPK_23_250)
        Fuel_tank_Ka_50 = (4, Weapons.Fuel_tank_Ka_50)
        GUV_YakB_GSHP = (4, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (4, Weapons.GUV_VOG)

    class Pylon5:
        B_8V20A_CM = (5, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (5, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (5, Weapons.B_8V20A_OM)
        UB_32A___32_S_5KO = (5, Weapons.UB_32A___32_S_5KO)
        _9M114_Shturm_V___2 = (5, Weapons._9M114_Shturm_V___2)
        B_8M1___20_S_8TsM = (5, Weapons.B_8M1___20_S_8TsM)
        B_13L___5_S_13_OF = (5, Weapons.B_13L___5_S_13_OF)
        UPK_23_250 = (5, Weapons.UPK_23_250)
        Fuel_tank_Ka_50 = (5, Weapons.Fuel_tank_Ka_50)
        B_8V20A___20_S_8KOM = (5, Weapons.B_8V20A___20_S_8KOM)
        GUV_VOG = (5, Weapons.GUV_VOG)

    class Pylon6:
        _9M114_Shturm_V___2 = (6, Weapons._9M114_Shturm_V___2)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.Transport, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class Mi_8MTV2(HelicopterType):
    id = "Mi-8MT"
    flyable = True
    large_parking_slot = True
    height = 4.908
    width = 21.33
    length = 25.942
    fuel_max = 1929
    max_speed = 250
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 0
    flare_charge_size = 1

    panel_radio = {
        1: {
            "channels": {
                1: 127.5,
                2: 135,
                4: 127,
                8: 128,
                16: 132,
                17: 138,
                9: 126,
                18: 122,
                5: 125,
                10: 133,
                20: 137,
                11: 130,
                3: 136,
                6: 121,
                12: 129,
                13: 123,
                7: 141,
                14: 131,
                19: 124,
                15: 134
            },
        },
        2: {
            "channels": {
                7: 40,
                1: 21.5,
                2: 25.7,
                4: 28,
                8: 50,
                9: 55.5,
                5: 30,
                10: 59.9,
                3: 27,
                6: 32
            },
        },
    }

    property_defaults = {
        "ExhaustScreen": True,
        "LeftEngineResource": 90,
        "RightEngineResource": 90,
        "AdditionalArmor": True,
        "CargoHalfdoor": True,
    }

    class Properties:

        class ExhaustScreen:
            id = "ExhaustScreen"

        class LeftEngineResource:
            id = "LeftEngineResource"

        class RightEngineResource:
            id = "RightEngineResource"

        class AdditionalArmor:
            id = "AdditionalArmor"

        class CargoHalfdoor:
            id = "CargoHalfdoor"

    class Liveries:

        class Georgia(Enum):
            Georgia = "Georgia"

        class Australia(Enum):
            Australia = "Australia"
            Standard = "Standard"

        class Germany(Enum):
            Germany = "Germany"
            Standard = "Standard"

        class Israel(Enum):
            Israel = "Israel"
            Standard = "Standard"

        class Norway(Enum):
            Norway = "Norway"
            Standard = "Standard"

        class Spain(Enum):
            Spain = "Spain"
            Standard = "Standard"

        class Ukraine(Enum):
            Ukraine = "Ukraine"

        class Belgium(Enum):
            Belgium = "Belgium"

        class Greece(Enum):
            Hellenic_Airforce_SAR = "Hellenic Airforce SAR"
            Hellenic_Army_Aviation = "Hellenic Army Aviation"

        class UK(Enum):
            United_Kingdom = "United Kingdom"
            Standard = "Standard"

        class Insurgents(Enum):
            Insurgents = "Insurgents"
            Standard = "Standard"

        class France(Enum):
            France_ARMY = "France ARMY"
            France_NAVY = "France NAVY"
            Standard = "Standard"

        class Abkhazia(Enum):
            Abkhazia = "Abkhazia"

        class Russia(Enum):
            Russia_VVS_Standard = "Russia_VVS_Standard"
            Russia_Aeroflot = "Russia_Aeroflot"
            Russia_Gazprom = "Russia_Gazprom"
            Russia_KazanVZ = "Russia_KazanVZ"
            Russia_LII_Gromov_RA_25546 = "Russia_LII_Gromov RA-25546"
            Russia_Police = "Russia_Police"
            Russia_UTair = "Russia_UTair"
            Russia_Vertolety_Russia = "Russia_Vertolety_Russia"
            Russia_Naryan_Mar = "Russia_Naryan-Mar"
            Russia_VVS_Grey = "Russia_VVS_Grey"
            Russia_VVS_Grey_2 = "Russia_VVS_Grey_2"
            Russia_VVS_Standard_2 = "Russia_VVS_Standard_2"
            Russia_FSB = "Russia_FSB"
            Russia_MVD_Mozdok = "Russia_MVD_Mozdok"
            Russia_MVD_Standard = "Russia_MVD_Standard"
            Russia_VVS_MA = "Russia_VVS_MA"
            Russia_UN = "Russia_UN"
            Russia_PF_Ambulance = "Russia_PF_Ambulance"
            Russia_Army_Weather = "Russia_Army_Weather"

        class Italy(Enum):
            Italy_ARMY = "Italy ARMY"
            Italy_NAVY = "Italy NAVY"
            Standard = "Standard"

        class SouthOssetia(Enum):
            South_Ossetia = "South Ossetia"

        class China(Enum):
            China_PLAAA_Camo = "China PLAAA Camo"
            China_UN = "China UN"
            China_PLAAA_White = "China PLAAA White"

        class USA(Enum):
            USA_AFG = "USA_AFG"
            Standard = "Standard"

        class Denmark(Enum):
            Denmark = "Denmark"

        class Canada(Enum):
            Canada = "Canada"
            Standard = "Standard"

        class TheNetherlands(Enum):
            Netherlands_ARMY = "Netherlands ARMY"
            Netherlands_NAVY = "Netherlands NAVY"
            Standard = "Standard"

        class Turkey(Enum):
            Turkey = "Turkey"
            Standard = "Standard"

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A___20_S_8KOM = (1, Weapons.B_8V20A___20_S_8KOM)
        FAB_100 = (1, Weapons.FAB_100)
        SAB_100 = (1, Weapons.SAB_100)
        FAB_250 = (1, Weapons.FAB_250)
        GUV_VOG = (1, Weapons.GUV_VOG)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        UPK_23_250 = (2, Weapons.UPK_23_250)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (2, Weapons.FAB_250)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        GUV_YakB_GSHP = (2, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (2, Weapons.GUV_VOG)
        FAB_100 = (2, Weapons.FAB_100)
        SAB_100 = (2, Weapons.SAB_100)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (3, Weapons.FAB_250)
        FAB_100 = (3, Weapons.FAB_100)
        SAB_100 = (3, Weapons.SAB_100)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (4, Weapons.FAB_250)
        FAB_100 = (4, Weapons.FAB_100)
        SAB_100 = (4, Weapons.SAB_100)

    class Pylon5:
        B_8V20A_CM = (5, Weapons.B_8V20A_CM)
        B_8V20A_OM = (5, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (5, Weapons.B_8V20A_OFP2)
        UPK_23_250 = (5, Weapons.UPK_23_250)
        B_8V20A___20_S_8KOM = (5, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (5, Weapons.FAB_250)
        FAB_500_M62 = (5, Weapons.FAB_500_M62)
        GUV_YakB_GSHP = (5, Weapons.GUV_YakB_GSHP)
        GUV_VOG = (5, Weapons.GUV_VOG)
        FAB_100 = (5, Weapons.FAB_100)
        SAB_100 = (5, Weapons.SAB_100)

    class Pylon6:
        B_8V20A_CM = (6, Weapons.B_8V20A_CM)
        B_8V20A_OM = (6, Weapons.B_8V20A_OM)
        B_8V20A_OFP2 = (6, Weapons.B_8V20A_OFP2)
        B_8V20A___20_S_8KOM = (6, Weapons.B_8V20A___20_S_8KOM)
        FAB_100 = (6, Weapons.FAB_100)
        SAB_100 = (6, Weapons.SAB_100)
        FAB_250 = (6, Weapons.FAB_250)
        GUV_VOG = (6, Weapons.GUV_VOG)

    class Pylon7:
        KORD_12_7 = (7, Weapons.KORD_12_7)

    class Pylon8:
        PKT_7_62 = (8, Weapons.PKT_7_62)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8}

    tasks = [task.CAS, task.GroundAttack, task.Transport, task.AFAC, task.AntishipStrike]
    task_default = task.Transport


class Mi_26(HelicopterType):
    id = "Mi-26"
    group_size_max = 1
    large_parking_slot = True
    height = 12.9
    width = 32
    length = 40.854
    fuel_max = 9600
    max_speed = 300
    chaff = 0
    flare = 192
    charge_total = 192
    chaff_charge_size = 0
    flare_charge_size = 1

    class Liveries:

        class Georgia(Enum):
            United_Nations = "United Nations"

        class Syria(Enum):
            United_Nations = "United Nations"

        class Finland(Enum):
            United_Nations = "United Nations"

        class Australia(Enum):
            United_Nations = "United Nations"

        class Germany(Enum):
            United_Nations = "United Nations"

        class SaudiArabia(Enum):
            United_Nations = "United Nations"

        class Israel(Enum):
            United_Nations = "United Nations"

        class Croatia(Enum):
            United_Nations = "United Nations"

        class CzechRepublic(Enum):
            United_Nations = "United Nations"

        class Norway(Enum):
            United_Nations = "United Nations"

        class Romania(Enum):
            United_Nations = "United Nations"

        class Spain(Enum):
            United_Nations = "United Nations"

        class Ukraine(Enum):
            _7th_Separate_Brigade_of_AA__Kalinov = "7th Separate Brigade of AA (Kalinov)"
            United_Nations = "United Nations"

        class Belgium(Enum):
            United_Nations = "United Nations"

        class Slovakia(Enum):
            United_Nations = "United Nations"

        class Greece(Enum):
            United_Nations = "United Nations"

        class UK(Enum):
            United_Nations = "United Nations"

        class Insurgents(Enum):
            United_Nations = "United Nations"

        class Hungary(Enum):
            United_Nations = "United Nations"

        class France(Enum):
            United_Nations = "United Nations"

        class Abkhazia(Enum):
            United_Nations = "United Nations"

        class Russia(Enum):
            RF_Air_Force = "RF Air Force"
            Russia_FSB = "Russia_FSB"
            Russia_MVD = "Russia_MVD"
            United_Nations = "United Nations"

        class Sweden(Enum):
            United_Nations = "United Nations"

        class Austria(Enum):
            United_Nations = "United Nations"

        class Switzerland(Enum):
            United_Nations = "United Nations"

        class Italy(Enum):
            United_Nations = "United Nations"

        class SouthOssetia(Enum):
            United_Nations = "United Nations"

        class SouthKorea(Enum):
            United_Nations = "United Nations"

        class Iran(Enum):
            United_Nations = "United Nations"

        class China(Enum):
            China_Flying_Dragon_Aviation = "China Flying Dragon Aviation"
            United_Nations = "United Nations"

        class Pakistan(Enum):
            United_Nations = "United Nations"

        class Belarus(Enum):
            United_Nations = "United Nations"

        class NorthKorea(Enum):
            United_Nations = "United Nations"

        class Iraq(Enum):
            United_Nations = "United Nations"

        class Kazakhstan(Enum):
            United_Nations = "United Nations"

        class Bulgaria(Enum):
            United_Nations = "United Nations"

        class Serbia(Enum):
            United_Nations = "United Nations"

        class India(Enum):
            United_Nations = "United Nations"

        class USAFAggressors(Enum):
            United_Nations = "United Nations"

        class USA(Enum):
            United_Nations = "United Nations"

        class Denmark(Enum):
            United_Nations = "United Nations"

        class Egypt(Enum):
            United_Nations = "United Nations"

        class Canada(Enum):
            United_Nations = "United Nations"

        class TheNetherlands(Enum):
            United_Nations = "United Nations"

        class Turkey(Enum):
            United_Nations = "United Nations"

        class Japan(Enum):
            United_Nations = "United Nations"

        class Poland(Enum):
            United_Nations = "United Nations"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class Ka_27(HelicopterType):
    id = "Ka-27"
    height = 5.2
    width = 15.9
    length = 15.92
    fuel_max = 2616
    max_speed = 290

    class Liveries:

        class Ukraine(Enum):
            ukraine_camo_1 = "ukraine camo 1"

        class Russia(Enum):
            standard = "standard"

        class China(Enum):
            China_PLANAF = "China PLANAF"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class UH_60A(HelicopterType):
    id = "UH-60A"
    height = 4.893
    width = 16.4
    length = 18.654
    fuel_max = 1100
    max_speed = 300
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Georgia(Enum):
            standard = "standard"

        class Germany(Enum):
            standard = "standard"

        class Israel(Enum):
            ISRAIL_UN = "ISRAIL_UN"
            standard = "standard"

        class Norway(Enum):
            standard = "standard"

        class Spain(Enum):
            standard = "standard"

        class Ukraine(Enum):
            standard = "standard"

        class Belgium(Enum):
            standard = "standard"

        class UK(Enum):
            standard = "standard"

        class France(Enum):
            standard = "standard"

        class Abkhazia(Enum):
            standard = "standard"

        class Russia(Enum):
            standard = "standard"

        class Italy(Enum):
            standard = "standard"

        class SouthOssetia(Enum):
            standard = "standard"

        class USA(Enum):
            standard = "standard"

        class Denmark(Enum):
            standard = "standard"

        class Canada(Enum):
            standard = "standard"

        class TheNetherlands(Enum):
            standard = "standard"

        class Turkey(Enum):
            standard = "standard"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class CH_53E(HelicopterType):
    id = "CH-53E"
    large_parking_slot = True
    height = 7.83
    width = 24.08
    length = 30.18
    fuel_max = 1908
    max_speed = 310
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class USA(Enum):
            standard = "standard"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class CH_47D(HelicopterType):
    id = "CH-47D"
    large_parking_slot = True
    height = 5.998
    width = 18.3
    length = 28.3
    fuel_max = 3600
    max_speed = 300
    chaff = 120
    flare = 120
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Australia(Enum):
            Australia_RAAF = "Australia RAAF"

        class Spain(Enum):
            ch_47_green_spain = "ch-47_green spain"

        class Greece(Enum):
            Greek_Army = "Greek Army"

        class UK(Enum):
            ch_47_green_uk = "ch-47_green uk"

        class USA(Enum):
            standard = "standard"

        class TheNetherlands(Enum):
            ch_47_green_neth = "ch-47_green neth"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class SH_3W(HelicopterType):
    id = "SH-3W"
    large_parking_slot = True
    height = 6.807
    width = 18.91
    length = 30.207
    fuel_max = 2132
    max_speed = 270
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Georgia(Enum):
            standard = "standard"

        class Syria(Enum):
            standard = "standard"

        class Finland(Enum):
            standard = "standard"

        class Australia(Enum):
            standard = "standard"

        class Germany(Enum):
            standard = "standard"

        class SaudiArabia(Enum):
            standard = "standard"

        class Israel(Enum):
            standard = "standard"

        class Croatia(Enum):
            standard = "standard"

        class CzechRepublic(Enum):
            standard = "standard"

        class Norway(Enum):
            standard = "standard"

        class Romania(Enum):
            standard = "standard"

        class Spain(Enum):
            standard = "standard"

        class Ukraine(Enum):
            standard = "standard"

        class Belgium(Enum):
            standard = "standard"

        class Slovakia(Enum):
            standard = "standard"

        class Greece(Enum):
            standard = "standard"

        class UK(Enum):
            standard = "standard"

        class Insurgents(Enum):
            standard = "standard"

        class Hungary(Enum):
            standard = "standard"

        class France(Enum):
            standard = "standard"

        class Abkhazia(Enum):
            standard = "standard"

        class Russia(Enum):
            standard = "standard"

        class Sweden(Enum):
            standard = "standard"

        class Austria(Enum):
            standard = "standard"

        class Switzerland(Enum):
            standard = "standard"

        class Italy(Enum):
            standard = "standard"

        class SouthOssetia(Enum):
            standard = "standard"

        class SouthKorea(Enum):
            standard = "standard"

        class Iran(Enum):
            standard = "standard"

        class China(Enum):
            standard = "standard"

        class Pakistan(Enum):
            standard = "standard"

        class Belarus(Enum):
            standard = "standard"

        class NorthKorea(Enum):
            standard = "standard"

        class Iraq(Enum):
            standard = "standard"

        class Kazakhstan(Enum):
            standard = "standard"

        class Bulgaria(Enum):
            standard = "standard"

        class Serbia(Enum):
            standard = "standard"

        class India(Enum):
            standard = "standard"

        class USAFAggressors(Enum):
            standard = "standard"

        class USA(Enum):
            standard = "standard"

        class Denmark(Enum):
            standard = "standard"

        class Egypt(Enum):
            standard = "standard"

        class Canada(Enum):
            standard = "standard"

        class TheNetherlands(Enum):
            standard = "standard"

        class Turkey(Enum):
            standard = "standard"

        class Japan(Enum):
            standard = "standard"

        class Poland(Enum):
            standard = "standard"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class AH_64A(HelicopterType):
    id = "AH-64A"
    height = 4.15
    width = 14.63
    length = 17.87
    fuel_max = 1157
    max_speed = 300
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Israel(Enum):
            ah_64_a_green_isr = "ah-64_a_green isr"

        class Greece(Enum):
            greek_army = "greek army"

        class UK(Enum):
            ah_64_a_green_uk = "ah-64_a_green uk"

        class USA(Enum):
            standard = "standard"
            standard_dirty = "standard dirty"

        class TheNetherlands(Enum):
            ah_64_a_green_neth = "ah-64_a_green neth"

    class Pylon1:
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        AGM_114K___4 = (1, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon2:
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (2, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        AGM_114K___4 = (2, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon3:
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (3, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        AGM_114K___4 = (3, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon4:
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        AGM_114K___4 = (4, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class AH_64D(HelicopterType):
    id = "AH-64D"
    height = 4.15
    width = 14.63
    length = 17.87
    fuel_max = 1157
    max_speed = 280
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Israel(Enum):
            ah_64_d_isr = "ah-64_d_isr"

        class Greece(Enum):
            greek_army = "greek army"

        class UK(Enum):
            ah_64_d_green_uk = "ah-64_d_green uk"

        class USA(Enum):
            standard = "standard"

        class TheNetherlands(Enum):
            ah_64_d_green_neth = "ah-64_d_green neth"

    class Pylon1:
        AGM_114K___4 = (1, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon2:
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (2, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        AGM_114K___4 = (2, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon3:
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        LAU_61___19_2_75__rockets_MK156_WP = (3, Weapons.LAU_61___19_2_75__rockets_MK156_WP)
        AGM_114K___4 = (3, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    class Pylon4:
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        AGM_114K___4 = (4, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class AH_1W(HelicopterType):
    id = "AH-1W"
    height = 3.9
    width = 14.64
    length = 17.27
    fuel_max = 1250.0
    max_speed = 290
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Israel(Enum):
            standard = "standard"

        class USA(Enum):
            USA_X_Black = "USA X Black"
            USA_Marines = "USA Marines"
            standard = "standard"

        class Turkey(Enum):
            Turkey_1 = "Turkey 1"
            Turkey_2 = "Turkey 2"

    class Pylon1:
        AGM_114K___4 = (1, Weapons.AGM_114K___4)
        BGM_71D_Tow___4 = (1, Weapons.BGM_71D_Tow___4)
        LAU_61___19_2_75__rockets_MK151_HE = (1, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        M260_HYDRA = (1, Weapons.M260_HYDRA)

    class Pylon2:
        LAU_61___19_2_75__rockets_MK151_HE = (2, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        M260_HYDRA = (2, Weapons.M260_HYDRA)
        M260_HYDRA_WP = (2, Weapons.M260_HYDRA_WP)
        LAU_61___19_2_75__rockets_MK156_WP = (2, Weapons.LAU_61___19_2_75__rockets_MK156_WP)

    class Pylon3:
        LAU_61___19_2_75__rockets_MK151_HE = (3, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        M260_HYDRA = (3, Weapons.M260_HYDRA)
        M260_HYDRA_WP = (3, Weapons.M260_HYDRA_WP)
        LAU_61___19_2_75__rockets_MK156_WP = (3, Weapons.LAU_61___19_2_75__rockets_MK156_WP)

    class Pylon4:
        AGM_114K___4 = (4, Weapons.AGM_114K___4)
        LAU_61___19_2_75__rockets_MK151_HE = (4, Weapons.LAU_61___19_2_75__rockets_MK151_HE)
        M260_HYDRA = (4, Weapons.M260_HYDRA)
        BGM_71D_Tow___4 = (4, Weapons.BGM_71D_Tow___4)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class SH_60B(HelicopterType):
    id = "SH-60B"
    height = 4.893
    width = 16.4
    length = 18.654
    fuel_max = 1100
    max_speed = 240
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Liveries:

        class Greece(Enum):
            Hellenic_Navy = "Hellenic Navy"

        class USA(Enum):
            standard = "standard"

    class Pylon1:
        AGM_119B_Penguin = (1, Weapons.AGM_119B_Penguin)

    pylons = {1}

    tasks = [task.AntishipStrike, task.Transport]
    task_default = task.Transport


class UH_1H(HelicopterType):
    id = "UH-1H"
    flyable = True
    height = 4.41
    width = 14.7
    length = 17.62
    fuel_max = 631
    max_speed = 200
    chaff = 0
    flare = 60
    charge_total = 60
    chaff_charge_size = 0
    flare_charge_size = 1
    radio_frequency = 251

    panel_radio = {
        1: {
            "channels": {
                1: 251,
                2: 264,
                4: 256,
                8: 257,
                16: 261,
                17: 267,
                9: 255,
                18: 251,
                5: 254,
                10: 262,
                20: 266,
                11: 259,
                3: 265,
                6: 250,
                12: 268,
                13: 269,
                7: 270,
                14: 260,
                19: 253,
                15: 263
            },
        },
    }

    property_defaults = {
        "ExhaustScreen": True,
        "GunnersAISkill": 90,
        "EngineResource": 90,
    }

    class Properties:

        class ExhaustScreen:
            id = "ExhaustScreen"

        class GunnersAISkill:
            id = "GunnersAISkill"

        class EngineResource:
            id = "EngineResource"

    class Liveries:

        class Georgia(Enum):
            Georgian_AF_Camo = "Georgian AF Camo"
            Georgian_Air_Force = "Georgian Air Force"

        class Australia(Enum):
            Australia_RAAF_171_Sqn = "Australia RAAF 171 Sqn"
            Australia_RAAF_1968 = "Australia RAAF 1968"
            Australia_Royal_Navy = "Australia Royal Navy"

        class Germany(Enum):
            Luftwaffe = "Luftwaffe"

        class Israel(Enum):
            Israel_Army = "Israel Army"

        class Norway(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class Spain(Enum):
            Spanish_Army = "Spanish Army"
            Spanish_UN = "Spanish UN"

        class Ukraine(Enum):
            Ukrainian_Army = "Ukrainian Army"

        class Belgium(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class Greece(Enum):
            Greek_Army_Aviation = "Greek Army Aviation"
            Greek_Army_Aviation_Medic = "Greek Army Aviation Medic"
            Hellenic_Airforce_SAR = "Hellenic Airforce SAR"

        class UK(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class Insurgents(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class France(Enum):
            French_Army = "French Army"

        class Abkhazia(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class Russia(Enum):
            RF_Air_Force_Broken = "RF Air Force Broken"
            RF_Air_Force_Grey = "RF Air Force Grey"

        class Italy(Enum):
            Italy_15B_Stormo_S_A_R__Soccorso = "Italy 15B Stormo S.A.R -Soccorso"
            Italy_E_I__4B_Regg__ALTAIR = "Italy E.I. 4B Regg. ALTAIR"
            Italy_Marina_Militare_s_n__80951_7_20 = "Italy Marina Militare s.n. 80951 7-20"

        class SouthOssetia(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class USA(Enum):
            Army_Standard = "Army Standard"
            _Civilian__Standard = "[Civilian] Standard"
            US_ARMY_1972 = "US ARMY 1972"
            US_DOS = "US DOS"
            US_Ft__Rucker = "US Ft. Rucker"
            US_NAVY = "US NAVY"
            USA_Red_Flag = "USA Red Flag"
            USA_UN = "USA UN"
            XW_PFJ_Air_America = "XW-PFJ Air America"
            _Civilian__Medical = "[Civilian] Medical"
            _Civilian__NASA = "[Civilian] NASA"
            _Civilian__VIP = "[Civilian] VIP"

        class Denmark(Enum):
            _Civilian__Standard = "[Civilian] Standard"

        class Canada(Enum):
            Canadian_Force = "Canadian Force"

        class TheNetherlands(Enum):
            Royal_Netherlands_AF = "Royal Netherlands AF"

        class Turkey(Enum):
            Turkish_Air_Force = "Turkish Air Force"

    class Pylon1:
        M134_L = (1, Weapons.M134_L)

    class Pylon2:
        XM158_MK1 = (2, Weapons.XM158_MK1)
        XM158_MK5 = (2, Weapons.XM158_MK5)
        XM158_M151 = (2, Weapons.XM158_M151)
        XM158_M156 = (2, Weapons.XM158_M156)
        XM158_M274 = (2, Weapons.XM158_M274)
        XM158_M257 = (2, Weapons.XM158_M257)
        M261_MK151 = (2, Weapons.M261_MK151)
        M261_MK156 = (2, Weapons.M261_MK156)

    class Pylon3:
        M134_SIDE_L = (3, Weapons.M134_SIDE_L)
        M60_SIDE_L = (3, Weapons.M60_SIDE_L)

    class Pylon4:
        M134_SIDE_R = (4, Weapons.M134_SIDE_R)
        M60_SIDE_R = (4, Weapons.M60_SIDE_R)

    class Pylon5:
        XM158_MK1 = (5, Weapons.XM158_MK1)
        XM158_MK5 = (5, Weapons.XM158_MK5)
        XM158_M151 = (5, Weapons.XM158_M151)
        XM158_M156 = (5, Weapons.XM158_M156)
        XM158_M274 = (5, Weapons.XM158_M274)
        XM158_M257 = (5, Weapons.XM158_M257)
        M261_MK151 = (5, Weapons.M261_MK151)
        M261_MK156 = (5, Weapons.M261_MK156)

    class Pylon6:
        M134_R = (6, Weapons.M134_R)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.Transport]
    task_default = task.Transport


class Mi_28N(HelicopterType):
    id = "Mi-28N"
    height = 5.087
    width = 17.2
    length = 17.87
    fuel_max = 1500
    max_speed = 305
    chaff = 0
    flare = 128
    charge_total = 128
    chaff_charge_size = 0
    flare_charge_size = 1

    class Liveries:

        class Russia(Enum):
            night = "night"
            standard = "standard"

    class Pylon1:
        B_8V20A_CM = (1, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (1, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (1, Weapons.B_8V20A_OM)
        _9M114_Shturm_V_x_8 = (1, Weapons._9M114_Shturm_V_x_8)
        B_8V20A___20_S_8KOM = (1, Weapons.B_8V20A___20_S_8KOM)
        FAB_250 = (1, Weapons.FAB_250)
        KMGU_2___96_AO_2_5RT = (1, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (1, Weapons.B_13L___5_S_13_OF)
        Fuel_tank_Ka_50 = (1, Weapons.Fuel_tank_Ka_50)
        B_8M1___20_S_8TsM = (1, Weapons.B_8M1___20_S_8TsM)
        FAB_500_M62 = (1, Weapons.FAB_500_M62)
        UPK_23_250 = (1, Weapons.UPK_23_250)
        KMGU_2___96_PTAB_2_5KO = (1, Weapons.KMGU_2___96_PTAB_2_5KO)

    class Pylon2:
        B_8V20A_CM = (2, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (2, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (2, Weapons.B_8V20A_OM)
        FAB_250 = (2, Weapons.FAB_250)
        KMGU_2___96_AO_2_5RT = (2, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (2, Weapons.B_13L___5_S_13_OF)
        Fuel_tank_Ka_50 = (2, Weapons.Fuel_tank_Ka_50)
        B_8M1___20_S_8TsM = (2, Weapons.B_8M1___20_S_8TsM)
        FAB_500_M62 = (2, Weapons.FAB_500_M62)
        UPK_23_250 = (2, Weapons.UPK_23_250)
        KMGU_2___96_PTAB_2_5KO = (2, Weapons.KMGU_2___96_PTAB_2_5KO)
        B_8V20A___20_S_8KOM = (2, Weapons.B_8V20A___20_S_8KOM)

    class Pylon3:
        B_8V20A_CM = (3, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (3, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (3, Weapons.B_8V20A_OM)
        FAB_250 = (3, Weapons.FAB_250)
        KMGU_2___96_AO_2_5RT = (3, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (3, Weapons.B_13L___5_S_13_OF)
        Fuel_tank_Ka_50 = (3, Weapons.Fuel_tank_Ka_50)
        B_8M1___20_S_8TsM = (3, Weapons.B_8M1___20_S_8TsM)
        FAB_500_M62 = (3, Weapons.FAB_500_M62)
        UPK_23_250 = (3, Weapons.UPK_23_250)
        KMGU_2___96_PTAB_2_5KO = (3, Weapons.KMGU_2___96_PTAB_2_5KO)
        B_8V20A___20_S_8KOM = (3, Weapons.B_8V20A___20_S_8KOM)

    class Pylon4:
        B_8V20A_CM = (4, Weapons.B_8V20A_CM)
        B_8V20A_OFP2 = (4, Weapons.B_8V20A_OFP2)
        B_8V20A_OM = (4, Weapons.B_8V20A_OM)
        FAB_250 = (4, Weapons.FAB_250)
        KMGU_2___96_AO_2_5RT = (4, Weapons.KMGU_2___96_AO_2_5RT)
        B_13L___5_S_13_OF = (4, Weapons.B_13L___5_S_13_OF)
        Fuel_tank_Ka_50 = (4, Weapons.Fuel_tank_Ka_50)
        B_8M1___20_S_8TsM = (4, Weapons.B_8M1___20_S_8TsM)
        FAB_500_M62 = (4, Weapons.FAB_500_M62)
        UPK_23_250 = (4, Weapons.UPK_23_250)
        KMGU_2___96_PTAB_2_5KO = (4, Weapons.KMGU_2___96_PTAB_2_5KO)
        _9M114_Shturm_V_x_8 = (4, Weapons._9M114_Shturm_V_x_8)
        B_8V20A___20_S_8KOM = (4, Weapons.B_8V20A___20_S_8KOM)

    pylons = {1, 2, 3, 4}

    tasks = [task.CAS, task.GroundAttack, task.Escort, task.AFAC, task.AntishipStrike]
    task_default = task.CAS


class OH_58D(HelicopterType):
    id = "OH-58D"
    height = 2.29
    width = 10.53
    length = 10.48
    fuel_max = 1100
    max_speed = 220
    chaff = 30
    flare = 30
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 1

    class Pylon1:
        M260_HYDRA = (1, Weapons.M260_HYDRA)
        M260_HYDRA_WP = (1, Weapons.M260_HYDRA_WP)
        AGM114x2_OH_58 = (1, Weapons.AGM114x2_OH_58)
        oh_58_brauning = (1, Weapons.oh_58_brauning)

    class Pylon2:
        M260_HYDRA_WP = (2, Weapons.M260_HYDRA_WP)
        M260_HYDRA = (2, Weapons.M260_HYDRA)
        AGM114x2_OH_58 = (2, Weapons.AGM114x2_OH_58)

    pylons = {1, 2}

    tasks = [task.AFAC, task.Transport, task.GroundAttack, task.Escort, task.AntishipStrike]
    task_default = task.AFAC


class SA342M(HelicopterType):
    id = "SA342M"
    flyable = True
    height = 3.192
    width = 10.5
    length = 11.97
    fuel_max = 416.33
    max_speed = 240
    chaff = 0
    flare = 32
    charge_total = 32
    chaff_charge_size = 0
    flare_charge_size = 1
    eplrs = True
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                6: 40,
                2: 31,
                8: 42,
                3: 32,
                1: 30,
                4: 33,
                5: 34,
                7: 41
            },
        },
    }

    class Liveries:

        class Syria(Enum):
            Syria_Fictional = "Syria Fictional"

        class Germany(Enum):
            Germany_Fictional = "Germany Fictional"

        class Israel(Enum):
            Israel_Fictional = "Israel Fictional"

        class Greece(Enum):
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"

        class UK(Enum):
            UK_Fictional = "UK Fictional"

        class France(Enum):
            Combat = "Combat"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"

        class Russia(Enum):
            Russia_Fictional = "Russia Fictional"

        class Serbia(Enum):
            Serbia_Fictional = "Serbia Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class USA(Enum):
            US_Marines_Fictional = "US Marines Fictional"

    class Pylon1:
        HOT3_ = (1, Weapons.HOT3_)

    class Pylon2:
        HOT3 = (2, Weapons.HOT3)

    class Pylon3:
        HOT3_ = (3, Weapons.HOT3_)

    class Pylon4:
        HOT3 = (4, Weapons.HOT3)

    class Pylon5:
        Sand_Filter = (5, Weapons.Sand_Filter)

    class Pylon6:
        IR_Deflector = (6, Weapons.IR_Deflector)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.AFAC, task.Escort, task.Reconnaissance]
    task_default = task.CAS


class SA342L(HelicopterType):
    id = "SA342L"
    height = 3.192
    width = 10.5
    length = 11.97
    fuel_max = 416.33
    max_speed = 240
    chaff = 0
    flare = 32
    charge_total = 32
    chaff_charge_size = 0
    flare_charge_size = 1
    eplrs = True
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                6: 40,
                2: 31,
                8: 42,
                3: 32,
                1: 30,
                4: 33,
                5: 34,
                7: 41
            },
        },
    }

    class Liveries:

        class Syria(Enum):
            Syria_Fictional = "Syria Fictional"

        class Germany(Enum):
            Germany_Fictional = "Germany Fictional"

        class Israel(Enum):
            Israel_Fictional = "Israel Fictional"

        class Greece(Enum):
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"

        class UK(Enum):
            UK_Fictional = "UK Fictional"

        class France(Enum):
            Combat = "Combat"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"

        class Russia(Enum):
            Russia_Fictional = "Russia Fictional"

        class Serbia(Enum):
            Serbia_Fictional = "Serbia Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class USA(Enum):
            US_Marines_Fictional = "US Marines Fictional"

    class Pylon1:
        pass

    class Pylon2:
        LAU_SNEB68G___8xSNEB68_EAP = (2, Weapons.LAU_SNEB68G___8xSNEB68_EAP)

    class Pylon5:
        Sand_Filter = (5, Weapons.Sand_Filter)

    class Pylon6:
        IR_Deflector = (6, Weapons.IR_Deflector)

    pylons = {1, 2, 5, 6}

    tasks = [task.CAS, task.GroundAttack, task.AFAC, task.Escort, task.Reconnaissance]
    task_default = task.CAS


class SA342Mistral(HelicopterType):
    id = "SA342Mistral"
    height = 3.192
    width = 10.5
    length = 11.97
    fuel_max = 416.33
    max_speed = 240
    chaff = 0
    flare = 32
    charge_total = 32
    chaff_charge_size = 0
    flare_charge_size = 1
    eplrs = True
    radio_frequency = 124

    panel_radio = {
        1: {
            "channels": {
                6: 40,
                2: 31,
                8: 42,
                3: 32,
                1: 30,
                4: 33,
                5: 34,
                7: 41
            },
        },
    }

    class Liveries:

        class Syria(Enum):
            Syria_Fictional = "Syria Fictional"

        class Germany(Enum):
            Germany_Fictional = "Germany Fictional"

        class Israel(Enum):
            Israel_Fictional = "Israel Fictional"

        class Greece(Enum):
            Greece_Cyprus_Fictional_Desert = "Greece Cyprus Fictional Desert"

        class UK(Enum):
            UK_Fictional = "UK Fictional"

        class France(Enum):
            Combat = "Combat"
            Tiger_Meet = "Tiger Meet"
            Tiger_Meet_2 = "Tiger Meet 2"
            Training = "Training"

        class Russia(Enum):
            Russia_Fictional = "Russia Fictional"

        class Serbia(Enum):
            Serbia_Fictional = "Serbia Fictional"
            Yugoslav_Fictional = "Yugoslav Fictional"

        class USA(Enum):
            US_Marines_Fictional = "US Marines Fictional"

    class Pylon1:
        Mistral_ = (1, Weapons.Mistral_)

    class Pylon2:
        Mistral = (2, Weapons.Mistral)

    class Pylon3:
        Mistral_ = (3, Weapons.Mistral_)

    class Pylon4:
        Mistral = (4, Weapons.Mistral)

    class Pylon5:
        Sand_Filter = (5, Weapons.Sand_Filter)

    class Pylon6:
        IR_Deflector = (6, Weapons.IR_Deflector)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [task.AFAC, task.Escort, task.Reconnaissance]
    task_default = task.Escort


helicopter_map = {
    "Ka-50": Ka_50,
    "Ka-52": Ka_52,
    "Mi-24V": Mi_24V,
    "Mi-8MT": Mi_8MTV2,
    "Mi-26": Mi_26,
    "Ka-27": Ka_27,
    "UH-60A": UH_60A,
    "CH-53E": CH_53E,
    "CH-47D": CH_47D,
    "SH-3W": SH_3W,
    "AH-64A": AH_64A,
    "AH-64D": AH_64D,
    "AH-1W": AH_1W,
    "SH-60B": SH_60B,
    "UH-1H": UH_1H,
    "Mi-28N": Mi_28N,
    "OH-58D": OH_58D,
    "SA342M": SA342M,
    "SA342L": SA342L,
    "SA342Mistral": SA342Mistral,
}
