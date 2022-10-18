from enum import Enum
from typing import Dict, Any

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod


@planemod
class VSN_F16CMBL50(PlaneType):
    id = "VSN_F16CMBL50"
    flyable = True
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:
        class USSR(Enum):
            default = "default"

        class Georgia(Enum):
            default = "default"

        class Venezuela(Enum):
            default = "default"

        class Australia(Enum):
            default = "default"

        class Israel(Enum):
            default = "default"

        class Combined_Joint_Task_Forces_Blue(Enum):
            default = "default"

        class Sudan(Enum):
            default = "default"

        class Norway(Enum):
            default = "default"

        class Romania(Enum):
            default = "default"

        class Iran(Enum):
            default = "default"

        class Ukraine(Enum):
            default = "default"

        class Libya(Enum):
            default = "default"

        class Belgium(Enum):
            default = "default"

        class Slovakia(Enum):
            default = "default"

        class Greece(Enum):
            default = "default"

        class UK(Enum):
            default = "default"

        class Third_Reich(Enum):
            default = "default"

        class Hungary(Enum):
            default = "default"

        class Abkhazia(Enum):
            default = "default"

        class Morocco(Enum):
            default = "default"

        class United_Nations_Peacekeepers(Enum):
            default = "default"

        class Switzerland(Enum):
            default = "default"

        class SouthOssetia(Enum):
            default = "default"

        class Vietnam(Enum):
            default = "default"

        class China(Enum):
            default = "default"

        class Yemen(Enum):
            default = "default"

        class Kuwait(Enum):
            default = "default"

        class Serbia(Enum):
            default = "default"

        class Oman(Enum):
            default = "default"

        class India(Enum):
            default = "default"

        class Egypt(Enum):
            default = "default"

        class TheNetherlands(Enum):
            default = "default"

        class Poland(Enum):
            default = "default"

        class Syria(Enum):
            default = "default"

        class Finland(Enum):
            default = "default"

        class Kazakhstan(Enum):
            default = "default"

        class Denmark(Enum):
            default = "default"

        class Sweden(Enum):
            default = "default"

        class Croatia(Enum):
            default = "default"

        class CzechRepublic(Enum):
            default = "default"

        class GDR(Enum):
            default = "default"

        class Yugoslavia(Enum):
            default = "default"

        class Bulgaria(Enum):
            default = "default"

        class SouthKorea(Enum):
            default = "default"

        class Tunisia(Enum):
            default = "default"

        class Combined_Joint_Task_Forces_Red(Enum):
            default = "default"

        class Lebanon(Enum):
            default = "default"

        class Portugal(Enum):
            default = "default"

        class Cuba(Enum):
            default = "default"

        class Insurgents(Enum):
            default = "default"

        class SaudiArabia(Enum):
            default = "default"

        class France(Enum):
            default = "default"

        class USA(Enum):
            default = "default"

        class Honduras(Enum):
            default = "default"

        class Qatar(Enum):
            default = "default"

        class Russia(Enum):
            default = "default"

        class United_Arab_Emirates(Enum):
            default = "default"

        class Italian_Social_Republi(Enum):
            default = "default"

        class Austria(Enum):
            default = "default"

        class Bahrain(Enum):
            default = "default"

        class Italy(Enum):
            default = "default"

        class Chile(Enum):
            default = "default"

        class Turkey(Enum):
            default = "default"

        class Philippines(Enum):
            default = "default"

        class Algeria(Enum):
            default = "default"

        class Pakistan(Enum):
            default = "default"

        class Malaysia(Enum):
            default = "default"

        class Indonesia(Enum):
            default = "default"

        class Iraq(Enum):
            default = "default"

        class Germany(Enum):
            default = "default"

        class South_Africa(Enum):
            default = "default"

        class Jordan(Enum):
            default = "default"

        class Mexico(Enum):
            default = "default"

        class USAFAggressors(Enum):
            default = "default"

        class Brazil(Enum):
            default = "default"

        class Spain(Enum):
            default = "default"

        class Belarus(Enum):
            default = "default"

        class Canada(Enum):
            default = "default"

        class NorthKorea(Enum):
            default = "default"

        class Ethiopia(Enum):
            default = "default"

        class Japan(Enum):
            default = "default"

        class Thailand(Enum):
            default = "default"

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (1, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            1,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (1, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (2, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (2, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            2,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (2, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (2, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    # ERRR <CLEAN>

    class Pylon3:
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (3, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            3,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (3, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        LAU3_WP156 = (3, Weapons.LAU3_WP156)
        LAU3_WP1B = (3, Weapons.LAU3_WP1B)
        LAU3_WP61 = (3, Weapons.LAU3_WP61)
        LAU3_HE5 = (3, Weapons.LAU3_HE5)
        LAU3_HE151 = (3, Weapons.LAU3_HE151)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            3,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            3,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            3,
            Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            3,
            Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            3,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (3, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (
            3,
            Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        # ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            3,
            Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            3,
            Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            3,
            Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            3,
            Weapons.TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb = (
            3,
            Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb,
        )
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb = (
            3,
            Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb,
        )

    class Pylon4:
        LAU3_WP156 = (4, Weapons.LAU3_WP156)
        LAU3_WP1B = (4, Weapons.LAU3_WP1B)
        LAU3_WP61 = (4, Weapons.LAU3_WP61)
        LAU3_HE5 = (4, Weapons.LAU3_HE5)
        LAU3_HE151 = (4, Weapons.LAU3_HE151)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            4,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            4,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            4,
            Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            4,
            Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            4,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb = (
            4,
            Weapons.TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb,
        )
        TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb = (
            4,
            Weapons.TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb,
        )
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (
            4,
            Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        # ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            4,
            Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            4,
            Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            4,
            Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb = (
            4,
            Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb,
        )
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb = (
            4,
            Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb,
        )

    class Pylon5:
        Fuel_tank_300_gal = (5, Weapons.Fuel_tank_300_gal)

    # ERRR <CLEAN>

    class Pylon6:
        LAU3_WP156 = (6, Weapons.LAU3_WP156)
        LAU3_WP1B = (6, Weapons.LAU3_WP1B)
        LAU3_WP61 = (6, Weapons.LAU3_WP61)
        LAU3_HE5 = (6, Weapons.LAU3_HE5)
        LAU3_HE151 = (6, Weapons.LAU3_HE151)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            6,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            6,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            6,
            Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            6,
            Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            6,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (6, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (6, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb = (
            6,
            Weapons.TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb,
        )
        TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb = (
            6,
            Weapons.TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb,
        )
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (
            6,
            Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        Fuel_tank_370_gal = (6, Weapons.Fuel_tank_370_gal)
        # ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_ = (
            6,
            Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_,
        )
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_ = (
            6,
            Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_,
        )
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_ = (
            6,
            Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_,
        )
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_ = (
            6,
            Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_,
        )
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_ = (
            6,
            Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_,
        )

    class Pylon7:
        AIM_9M_Sidewinder_IR_AAM = (7, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (7, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (7, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            7,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (7, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (7, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        LAU3_WP156 = (7, Weapons.LAU3_WP156)
        LAU3_WP1B = (7, Weapons.LAU3_WP1B)
        LAU3_WP61 = (7, Weapons.LAU3_WP61)
        LAU3_HE5 = (7, Weapons.LAU3_HE5)
        LAU3_HE151 = (7, Weapons.LAU3_HE151)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            7,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            7,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            7,
            Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            7,
            Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            7,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (7, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (7, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (
            7,
            Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        # ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_ = (
            7,
            Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_,
        )
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_ = (
            7,
            Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_,
        )
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_ = (
            7,
            Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_,
        )
        TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb_ = (
            7,
            Weapons.TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb_,
        )
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_ = (
            7,
            Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_,
        )
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_ = (
            7,
            Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_,
        )

    class Pylon8:
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (8, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (8, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            8,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (8, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (8, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    # ERRR <CLEAN>

    class Pylon9:
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (9, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            9,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (9, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon11:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            11,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}

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
class VSN_F16CMBL50_AG(PlaneType):
    id = "VSN_F16CMBL50_AG"
    flyable = True
    height = 5.02
    width = 9.45
    length = 14.52
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 60
    flare = 60
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:
        class USSR(Enum):
            default = "default"

        class Georgia(Enum):
            default = "default"

        class Venezuela(Enum):
            default = "default"

        class Australia(Enum):
            default = "default"

        class Israel(Enum):
            default = "default"

        class Combined_Joint_Task_Forces_Blue(Enum):
            default = "default"

        class Sudan(Enum):
            default = "default"

        class Norway(Enum):
            default = "default"

        class Romania(Enum):
            default = "default"

        class Iran(Enum):
            default = "default"

        class Ukraine(Enum):
            default = "default"

        class Libya(Enum):
            default = "default"

        class Belgium(Enum):
            default = "default"

        class Slovakia(Enum):
            default = "default"

        class Greece(Enum):
            default = "default"

        class UK(Enum):
            default = "default"

        class Third_Reich(Enum):
            default = "default"

        class Hungary(Enum):
            default = "default"

        class Abkhazia(Enum):
            default = "default"

        class Morocco(Enum):
            default = "default"

        class United_Nations_Peacekeepers(Enum):
            default = "default"

        class Switzerland(Enum):
            default = "default"

        class SouthOssetia(Enum):
            default = "default"

        class Vietnam(Enum):
            default = "default"

        class China(Enum):
            default = "default"

        class Yemen(Enum):
            default = "default"

        class Kuwait(Enum):
            default = "default"

        class Serbia(Enum):
            default = "default"

        class Oman(Enum):
            default = "default"

        class India(Enum):
            default = "default"

        class Egypt(Enum):
            default = "default"

        class TheNetherlands(Enum):
            default = "default"

        class Poland(Enum):
            default = "default"

        class Syria(Enum):
            default = "default"

        class Finland(Enum):
            default = "default"

        class Kazakhstan(Enum):
            default = "default"

        class Denmark(Enum):
            default = "default"

        class Sweden(Enum):
            default = "default"

        class Croatia(Enum):
            default = "default"

        class CzechRepublic(Enum):
            default = "default"

        class GDR(Enum):
            default = "default"

        class Yugoslavia(Enum):
            default = "default"

        class Bulgaria(Enum):
            default = "default"

        class SouthKorea(Enum):
            default = "default"

        class Tunisia(Enum):
            default = "default"

        class Combined_Joint_Task_Forces_Red(Enum):
            default = "default"

        class Lebanon(Enum):
            default = "default"

        class Portugal(Enum):
            default = "default"

        class Cuba(Enum):
            default = "default"

        class Insurgents(Enum):
            default = "default"

        class SaudiArabia(Enum):
            default = "default"

        class France(Enum):
            default = "default"

        class USA(Enum):
            default = "default"

        class Honduras(Enum):
            default = "default"

        class Qatar(Enum):
            default = "default"

        class Russia(Enum):
            default = "default"

        class United_Arab_Emirates(Enum):
            default = "default"

        class Italian_Social_Republi(Enum):
            default = "default"

        class Austria(Enum):
            default = "default"

        class Bahrain(Enum):
            default = "default"

        class Italy(Enum):
            default = "default"

        class Chile(Enum):
            default = "default"

        class Turkey(Enum):
            default = "default"

        class Philippines(Enum):
            default = "default"

        class Algeria(Enum):
            default = "default"

        class Pakistan(Enum):
            default = "default"

        class Malaysia(Enum):
            default = "default"

        class Indonesia(Enum):
            default = "default"

        class Iraq(Enum):
            default = "default"

        class Germany(Enum):
            default = "default"

        class South_Africa(Enum):
            default = "default"

        class Jordan(Enum):
            default = "default"

        class Mexico(Enum):
            default = "default"

        class USAFAggressors(Enum):
            default = "default"

        class Brazil(Enum):
            default = "default"

        class Spain(Enum):
            default = "default"

        class Belarus(Enum):
            default = "default"

        class Canada(Enum):
            default = "default"

        class NorthKorea(Enum):
            default = "default"

        class Ethiopia(Enum):
            default = "default"

        class Japan(Enum):
            default = "default"

        class Thailand(Enum):
            default = "default"

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (1, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (1, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            1,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (1, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (2, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (2, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            2,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (2, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (2, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    # ERRR <CLEAN>

    class Pylon3:
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (3, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (3, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            3,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (3, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (3, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        LAU3_WP156 = (3, Weapons.LAU3_WP156)
        LAU3_WP1B = (3, Weapons.LAU3_WP1B)
        LAU3_WP61 = (3, Weapons.LAU3_WP61)
        LAU3_HE5 = (3, Weapons.LAU3_HE5)
        LAU3_HE151 = (3, Weapons.LAU3_HE151)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (3, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            3,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            3,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            3,
            Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            3,
            Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            3,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (3, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (
            3,
            Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        # ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            3,
            Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            3,
            Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            3,
            Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb = (
            3,
            Weapons.TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb,
        )
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb = (
            3,
            Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb,
        )
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb = (
            3,
            Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb,
        )

    class Pylon4:
        LAU3_WP156 = (4, Weapons.LAU3_WP156)
        LAU3_WP1B = (4, Weapons.LAU3_WP1B)
        LAU3_WP61 = (4, Weapons.LAU3_WP61)
        LAU3_HE5 = (4, Weapons.LAU3_HE5)
        LAU3_HE151 = (4, Weapons.LAU3_HE151)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (4, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            4,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            4,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            4,
            Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            4,
            Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            4,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (4, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb = (
            4,
            Weapons.TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb,
        )
        TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb = (
            4,
            Weapons.TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb,
        )
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (
            4,
            Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        Fuel_tank_370_gal = (4, Weapons.Fuel_tank_370_gal)
        # ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD = (
            4,
            Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            4,
            Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            4,
            Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb = (
            4,
            Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb,
        )
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb = (
            4,
            Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb,
        )

    class Pylon5:
        Fuel_tank_300_gal = (5, Weapons.Fuel_tank_300_gal)

    # ERRR <CLEAN>

    class Pylon6:
        LAU3_WP156 = (6, Weapons.LAU3_WP156)
        LAU3_WP1B = (6, Weapons.LAU3_WP1B)
        LAU3_WP61 = (6, Weapons.LAU3_WP61)
        LAU3_HE5 = (6, Weapons.LAU3_HE5)
        LAU3_HE151 = (6, Weapons.LAU3_HE151)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (6, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            6,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            6,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            6,
            Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            6,
            Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            6,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (6, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (6, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (6, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb = (
            6,
            Weapons.TER_9A_with_3_x_CBU_87___202_x_CEM_Cluster_Bomb,
        )
        TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb = (
            6,
            Weapons.TER_9A_with_3_x_CBU_97___10_x_SFW_Cluster_Bomb,
        )
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (
            6,
            Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        Fuel_tank_370_gal = (6, Weapons.Fuel_tank_370_gal)
        # ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_ = (
            6,
            Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_,
        )
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_ = (
            6,
            Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_,
        )
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_ = (
            6,
            Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_,
        )
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_ = (
            6,
            Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_,
        )
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_ = (
            6,
            Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_,
        )

    class Pylon7:
        AIM_9M_Sidewinder_IR_AAM = (7, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (7, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (7, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            7,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (7, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (7, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        LAU3_WP156 = (7, Weapons.LAU3_WP156)
        LAU3_WP1B = (7, Weapons.LAU3_WP1B)
        LAU3_WP61 = (7, Weapons.LAU3_WP61)
        LAU3_HE5 = (7, Weapons.LAU3_HE5)
        LAU3_HE151 = (7, Weapons.LAU3_HE151)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_82_Snakeye___500lb_GP_Bomb_HD = (7, Weapons.Mk_82_Snakeye___500lb_GP_Bomb_HD)
        Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            7,
            Weapons.Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD = (
            7,
            Weapons.TER_9A_with_3_x_Mk_82___500lb_GP_Bomb_LD,
        )
        TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD = (
            7,
            Weapons.TER_9A_with_3_x_Mk_82_Snakeye___500lb_GP_Bomb_HD,
        )
        TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD = (
            7,
            Weapons.TER_9A_with_3_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD,
        )
        Mk_84___2000lb_GP_Bomb_LD = (7, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        GBU_10___2000lb_Laser_Guided_Bomb = (
            7,
            Weapons.GBU_10___2000lb_Laser_Guided_Bomb,
        )
        GBU_12___500lb_Laser_Guided_Bomb = (7, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        CBU_87___202_x_CEM_Cluster_Bomb = (7, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        CBU_97___10_x_SFW_Cluster_Bomb = (7, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD = (
            7,
            Weapons.TER_9A_with_3_x_BDU_33___25lb_Practice_Bomb_LD,
        )
        # ERRR <CLEAN>
        TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_ = (
            7,
            Weapons.TER_9A_with_2_x_Mk_82___500lb_GP_Bomb_LD_,
        )
        TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_ = (
            7,
            Weapons.TER_9A_with_2_x_Mk_82_Snakeye___500lb_GP_Bomb_HD_,
        )
        TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_ = (
            7,
            Weapons.TER_9A_with_2_x_Mk_82_AIR_Ballute___500lb_GP_Bomb_HD_,
        )
        TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb_ = (
            7,
            Weapons.TER_9A_with_2_x_GBU_12___500lb_Laser_Guided_Bomb_,
        )
        TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_ = (
            7,
            Weapons.TER_9A_with_2_x_CBU_87___202_x_CEM_Cluster_Bomb_,
        )
        TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_ = (
            7,
            Weapons.TER_9A_with_2_x_CBU_97___10_x_SFW_Cluster_Bomb_,
        )

    class Pylon8:
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (8, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (8, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            8,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (8, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (8, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    # ERRR <CLEAN>

    class Pylon9:
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9L_Sidewinder_IR_AAM = (9, Weapons.AIM_9L_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (9, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (
            9,
            Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM,
        )
        CATM_9M = (9, Weapons.CATM_9M)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (9, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon11:
        AN_AAQ_28_LITENING___Targeting_Pod = (
            11,
            Weapons.AN_AAQ_28_LITENING___Targeting_Pod,
        )

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11}

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
