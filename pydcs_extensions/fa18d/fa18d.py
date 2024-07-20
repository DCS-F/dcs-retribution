from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons


from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons


class WeaponsFA18D:
    VSN_Fuel_Tank_330_gallons = {
        "clsid": "{VSN_F18D_PTB}",
        "name": "VSN Fuel Tank 330 gallons",
        "weight": 1150,
    }


inject_weapons(WeaponsFA18D)


@planemod
class VSN_FA18D(PlaneType):
    id = "VSN_FA18D"
    flyable = True
    height = 4.66
    width = 11.43
    length = 17.07
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        CATM_9M = (1, Weapons.CATM_9M)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (1, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (
            2,
            Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (
            2,
            Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (
            2,
            Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (
            2,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (
            2,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_2_LAU_127_AIM_120B = (2, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (2, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (
            2,
            Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_,
        )
        LAU_117_AGM_65F = (2, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            2,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     2,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     2,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     2,
        #     Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     2,
        #     Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     2,
        #     Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     2,
        #     Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            2,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (2, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            2,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            2,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            2,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            2,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (
            2,
            Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD,
        )
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (
            2,
            Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        # ERRR {FPU_8A_FUEL_TANK}
        VSN_Fuel_Tank_330_gallons = (2, WeaponsFA18D.VSN_Fuel_Tank_330_gallons)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            2,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (
            2,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            2,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            2,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            2,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            2,
            Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            2,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )

    # ERRR <CLEAN>

    class Pylon3:
        LAU_115_2_LAU_127_AIM_9M = (3, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (3, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (3, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (3, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_LAU_127_AIM_9X = (3, Weapons.LAU_115_LAU_127_AIM_9X)
        LAU_115_LAU_127_CATM_9M = (3, Weapons.LAU_115_LAU_127_CATM_9M)
        LAU_115_LAU_127_AIM_9L = (3, Weapons.LAU_115_LAU_127_AIM_9L)
        LAU_115_LAU_127_AIM_9M = (3, Weapons.LAU_115_LAU_127_AIM_9M)
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (
            3,
            Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (
            3,
            Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (
            3,
            Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (
            3,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (
            3,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_2_LAU_127_AIM_120B = (3, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (3, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (
            3,
            Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_,
        )
        LAU_117_AGM_65F = (3, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            3,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     3,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     3,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
        #     3,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
        #     3,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        # )
        # BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     3,
        #     Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     3,
        #     Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     3,
        #     Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     3,
        #     Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            3,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            3,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD,
        )
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (
            3,
            Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            3,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (
            3,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            3,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            3,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            3,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            3,
            Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            3,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            3,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            3,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )

    # ERRR <CLEAN>

    class Pylon4:
        Smoke_Generator___red_ = (4, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (4, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (4, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (4, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (4, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (4, Weapons.Smoke_Generator___orange_)
        L_081_Fantasmagoria_ELINT_pod = (4, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon5:
        AIM_7M_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (
            5,
            Weapons.AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        AIM_120B_AMRAAM___Active_Radar_AAM = (
            5,
            Weapons.AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        AIM_120C_AMRAAM___Active_Radar_AAM = (
            5,
            Weapons.AIM_120C_AMRAAM___Active_Radar_AAM,
        )

    # ERRR {FPU_8A_FUEL_TANK}

    class Pylon6:
        VSN_Fuel_Tank_330_gallons = (6, WeaponsFA18D.VSN_Fuel_Tank_330_gallons)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            6,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (6, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            6,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            6,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            6,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            6,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            6,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            6,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            6,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )

    # ERRR <CLEAN>

    class Pylon7:
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (
            7,
            Weapons.AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        AIM_120B_AMRAAM___Active_Radar_AAM = (
            7,
            Weapons.AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        AIM_120C_AMRAAM___Active_Radar_AAM = (
            7,
            Weapons.AIM_120C_AMRAAM___Active_Radar_AAM,
        )

    class Pylon8:
        L005_Sorbtsiya_ECM_pod__left_ = (8, Weapons.L005_Sorbtsiya_ECM_pod__left_)

    class Pylon9:
        LAU_115_2_LAU_127_AIM_9M = (9, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (9, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (9, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (9, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_LAU_127_AIM_9X = (9, Weapons.LAU_115_LAU_127_AIM_9X)
        LAU_115_LAU_127_CATM_9M = (9, Weapons.LAU_115_LAU_127_CATM_9M)
        LAU_115_LAU_127_AIM_9L = (9, Weapons.LAU_115_LAU_127_AIM_9L)
        LAU_115_LAU_127_AIM_9M = (9, Weapons.LAU_115_LAU_127_AIM_9M)
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (
            9,
            Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (
            9,
            Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (
            9,
            Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (
            9,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (
            9,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_2_LAU_127_AIM_120B = (9, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (9, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (
            9,
            Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_,
        )
        LAU_117_AGM_65F = (9, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            9,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     9,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     9,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
        #     9,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
        #     9,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        # )
        # BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     9,
        #     Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     9,
        #     Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     9,
        #     Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     9,
        #     Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (9, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            9,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (9, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            9,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD,
        )
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (
            9,
            Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            9,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (9, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (
            9,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            9,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            9,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            9,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            9,
            Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            9,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            9,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            9,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )

    # ERRR <CLEAN>

    class Pylon10:
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (
            10,
            Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (
            10,
            Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (
            10,
            Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (
            10,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (
            10,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_2_LAU_127_AIM_120B = (10, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (10, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (
            10,
            Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_,
        )
        LAU_117_AGM_65F = (10, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            10,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     10,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     10,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     10,
        #     Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     10,
        #     Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     10,
        #     Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     10,
        #     Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            10,
            Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            10,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (10, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (10, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            10,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            10,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            10,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            10,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (
            10,
            Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD,
        )
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (
            10,
            Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        # ERRR {FPU_8A_FUEL_TANK}
        VSN_Fuel_Tank_330_gallons = (10, WeaponsFA18D.VSN_Fuel_Tank_330_gallons)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_16___1000lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            10,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            10,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            10,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            10,
            Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            10,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )

    # ERRR <CLEAN>

    class Pylon11:
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        CATM_9M = (11, Weapons.CATM_9M)
        AIM_9L_Sidewinder_IR_AAM = (11, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (11, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.Intercept,
        task.Reconnaissance,
        task.GroundAttack,
        task.CAS,
        task.AFAC,
        task.RunwayAttack,
    ]
    task_default = task.CAP


@planemod
class VSN_FA18D_AG(PlaneType):
    id = "VSN_FA18D_AG"
    flyable = True
    height = 4.66
    width = 11.43
    length = 17.07
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        CATM_9M = (1, Weapons.CATM_9M)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (1, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (
            2,
            Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (
            2,
            Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (
            2,
            Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (
            2,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (
            2,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_2_LAU_127_AIM_120B = (2, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (2, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (
            2,
            Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_,
        )
        LAU_117_AGM_65F = (2, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            2,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     2,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     2,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     2,
        #     Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     2,
        #     Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     2,
        #     Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     2,
        #     Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (2, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            2,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (2, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            2,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            2,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            2,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            2,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (
            2,
            Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD,
        )
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (
            2,
            Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        # ERRR {FPU_8A_FUEL_TANK}
        VSN_Fuel_Tank_330_gallons = (2, WeaponsFA18D.VSN_Fuel_Tank_330_gallons)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            2,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (
            2,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            2,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            2,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            2,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            2,
            Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            2,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            2,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )

    # ERRR <CLEAN>

    class Pylon3:
        LAU_115_2_LAU_127_AIM_9M = (3, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (3, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (3, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (3, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_LAU_127_AIM_9X = (3, Weapons.LAU_115_LAU_127_AIM_9X)
        LAU_115_LAU_127_CATM_9M = (3, Weapons.LAU_115_LAU_127_CATM_9M)
        LAU_115_LAU_127_AIM_9L = (3, Weapons.LAU_115_LAU_127_AIM_9L)
        LAU_115_LAU_127_AIM_9M = (3, Weapons.LAU_115_LAU_127_AIM_9M)
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (
            3,
            Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (
            3,
            Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (
            3,
            Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (
            3,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (
            3,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_2_LAU_127_AIM_120B = (3, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (3, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (
            3,
            Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_,
        )
        LAU_117_AGM_65F = (3, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            3,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     3,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     3,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
        #     3,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
        #     3,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        # )
        # BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     3,
        #     Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     3,
        #     Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     3,
        #     Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     3,
        #     Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            3,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            3,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (
            3,
            Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD,
        )
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (
            3,
            Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            3,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (
            3,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            3,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            3,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            3,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            3,
            Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            3,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            3,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            3,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )

    # ERRR <CLEAN>

    class Pylon4:
        Smoke_Generator___red_ = (4, Weapons.Smoke_Generator___red_)
        Smoke_Generator___green_ = (4, Weapons.Smoke_Generator___green_)
        Smoke_Generator___blue_ = (4, Weapons.Smoke_Generator___blue_)
        Smoke_Generator___white_ = (4, Weapons.Smoke_Generator___white_)
        Smoke_Generator___yellow_ = (4, Weapons.Smoke_Generator___yellow_)
        Smoke_Generator___orange_ = (4, Weapons.Smoke_Generator___orange_)
        L_081_Fantasmagoria_ELINT_pod = (4, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon5:
        AIM_7M_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (
            5,
            Weapons.AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        AIM_120B_AMRAAM___Active_Radar_AAM = (
            5,
            Weapons.AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        AIM_120C_AMRAAM___Active_Radar_AAM = (
            5,
            Weapons.AIM_120C_AMRAAM___Active_Radar_AAM,
        )

    # ERRR {FPU_8A_FUEL_TANK}

    class Pylon6:
        VSN_Fuel_Tank_330_gallons = (6, WeaponsFA18D.VSN_Fuel_Tank_330_gallons)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            6,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (6, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            6,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            6,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            6,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            6,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            6,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            6,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            6,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )

    # ERRR <CLEAN>

    class Pylon7:
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AIM_7F_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7F_Sparrow_Semi_Active_Radar)
        AIM_7MH_Sparrow_Semi_Active_Radar = (
            7,
            Weapons.AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        AIM_120B_AMRAAM___Active_Radar_AAM = (
            7,
            Weapons.AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        AIM_120C_AMRAAM___Active_Radar_AAM = (
            7,
            Weapons.AIM_120C_AMRAAM___Active_Radar_AAM,
        )

    class Pylon8:
        L005_Sorbtsiya_ECM_pod__left_ = (8, Weapons.L005_Sorbtsiya_ECM_pod__left_)

    class Pylon9:
        LAU_115_2_LAU_127_AIM_9M = (9, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (9, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (9, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (9, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_LAU_127_AIM_9X = (9, Weapons.LAU_115_LAU_127_AIM_9X)
        LAU_115_LAU_127_CATM_9M = (9, Weapons.LAU_115_LAU_127_CATM_9M)
        LAU_115_LAU_127_AIM_9L = (9, Weapons.LAU_115_LAU_127_AIM_9L)
        LAU_115_LAU_127_AIM_9M = (9, Weapons.LAU_115_LAU_127_AIM_9M)
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (
            9,
            Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (
            9,
            Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (
            9,
            Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (
            9,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (
            9,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_2_LAU_127_AIM_120B = (9, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (9, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (
            9,
            Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_,
        )
        LAU_117_AGM_65F = (9, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            9,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     9,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     9,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
        #     9,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT = (
        #     9,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_Mk5__HEAT,
        # )
        # BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     9,
        #     Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     9,
        #     Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     9,
        #     Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     9,
        #     Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (9, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            9,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (9, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            9,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (
            9,
            Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD,
        )
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (
            9,
            Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        GBU_10___2000lb_Laser_Guided_Bomb = (
            9,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (9, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (
            9,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            9,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            9,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            9,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            9,
            Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            9,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            9,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            9,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )

    # ERRR <CLEAN>

    class Pylon10:
        LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar = (
            10,
            Weapons.LAU_115C_with_AIM_7M_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar = (
            10,
            Weapons.LAU_115C_with_AIM_7F_Sparrow_Semi_Active_Radar,
        )
        LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar = (
            10,
            Weapons.LAU_115C_with_AIM_7MH_Sparrow_Semi_Active_Radar,
        )
        LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM = (
            10,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120B_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM = (
            10,
            Weapons.LAU_115_with_1_x_LAU_127_AIM_120C_AMRAAM___Active_Radar_AAM,
        )
        LAU_115_2_LAU_127_AIM_120B = (10, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (10, Weapons.LAU_115_2_LAU_127_AIM_120C)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (
            10,
            Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_,
        )
        LAU_117_AGM_65F = (10, Weapons.LAU_117_AGM_65F)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (
            10,
            Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_,
        )
        # BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     10,
        #     Weapons.BRU_33_with_1_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     10,
        #     Weapons.BRU_33_with_2_x_LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     10,
        #     Weapons.BRU_33_with_1_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (
        #     10,
        #     Weapons.BRU_33_with_2_x_LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG,
        # )
        # BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     10,
        #     Weapons.BRU_33_with_1_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        # BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (
        #     10,
        #     Weapons.BRU_33_with_2_x_LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE,
        # )
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            10,
            Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            10,
            Weapons.Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        Mk_83___1000lb_GP_Bomb_LD = (10, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (10, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            10,
            Weapons.BRU_33_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            10,
            Weapons.BRU_33_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD = (
            10,
            Weapons.BRU_33_with_2_x_Mk_82Y___500lb_GP_Chute_Retarded_HD,
        )
        BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            10,
            Weapons.BRU_33_with_2_x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD = (
            10,
            Weapons.BRU_33_with_2_x_Mk_83___1000lb_GP_Bomb_LD,
        )
        BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD = (
            10,
            Weapons.BRU_41A_with_6_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        # ERRR {FPU_8A_FUEL_TANK}
        VSN_Fuel_Tank_330_gallons = (10, WeaponsFA18D.VSN_Fuel_Tank_330_gallons)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_16___1000lb_Laser_Guided_Bomb = (
            10,
            Weapons.GBU_16___1000lb_Laser_Guided_Bomb,
        )
        CBU_99___490lbs__247_x_HEAT_Bomblets = (
            10,
            Weapons.CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets = (
            10,
            Weapons.BRU_33_with_2_x_CBU_99___490lbs__247_x_HEAT_Bomblets,
        )
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (
            10,
            Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets,
        )
        BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            10,
            Weapons.BRU_33_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb,
        )
        GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb = (
            10,
            Weapons.GBU_31_V_3_B___JDAM__2000lb_GPS_Guided_Penetrator_Bomb,
        )
        GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb = (
            10,
            Weapons.GBU_38_V_1_B___JDAM__500lb_GPS_Guided_Bomb,
        )

    # ERRR <CLEAN>

    class Pylon11:
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        CATM_9M = (11, Weapons.CATM_9M)
        AIM_9L_Sidewinder_IR_AAM = (11, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (11, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [
        task.CAP,
        task.Escort,
        task.FighterSweep,
        task.Intercept,
        task.Reconnaissance,
        task.GroundAttack,
        task.CAS,
        task.AFAC,
        task.RunwayAttack,
    ]
    task_default = task.CAP
