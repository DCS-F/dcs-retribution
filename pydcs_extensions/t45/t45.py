from enum import Enum
from typing import Dict, Any

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons


class WeaponsT45:
    PMBR___6_x_BDU_33 = {
        "clsid": "{PMBR_6X_BDU-33}",
        "name": "PMBR - 6 x BDU-33",
        "weight": 107.2625,
    }


inject_weapons(WeaponsT45)


@planemod
class T_45(PlaneType):
    id = "T-45"
    flyable = True
    height = 4.0891968
    width = 9.396984
    length = 11.987784
    fuel_max = 1317.2338090011
    max_speed = 1080
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 305

    panel_radio = {
        1: {
            "channels": {
                1: 225,
                2: 258,
                4: 270,
                8: 257,
                16: 252,
                17: 268,
                9: 253,
                18: 269,
                5: 255,
                10: 263,
                20: 269,
                30: 263,
                21: 225,
                11: 267,
                22: 258,
                3: 260,
                6: 259,
                12: 254,
                24: 270,
                19: 268,
                25: 255,
                13: 264,
                26: 259,
                27: 262,
                7: 262,
                14: 266,
                28: 257,
                23: 260,
                29: 253,
                15: 265,
            },
        },
    }

    property_defaults: Dict[str, Any] = {
        "SoloFlight": False,
        "NetCrewControlPriority": -2,
    }

    class Properties:
        class SoloFlight:
            id = "SoloFlight"

        class NetCrewControlPriority:
            id = "NetCrewControlPriority"

            class Values:
                Pilot = 0
                Instructor = 1
                Ask_Always = -1
                Equally_Responsible = -2

    class Liveries:
        class Georgia(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Israel(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Combined_Joint_Task_Forces_Blue(Enum):
            default = "default"
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Norway(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Ukraine(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Belgium(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class UK(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Abkhazia(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class SouthOssetia(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class TheNetherlands(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Denmark(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Combined_Joint_Task_Forces_Red(Enum):
            default = "default"
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class France(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class USA(Enum):
            default = "default"
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Russia(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Turkey(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Germany(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Spain(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

        class Canada(Enum):
            TW_1_Meridian = "TW-1 Meridian"
            TW_2_CONA = "TW-2 CONA"
            TW_1_CONA = "TW-1 CONA"
            TW_2_Kingsville = "TW-2 Kingsville"
            TW_2_Texas_Flag_CAG = "TW-2 Texas Flag CAG"
            TW_2_Golden_Eagles_CAG = "TW-2 Golden Eagles CAG"
            VT_86_Sabrehawks = "VT-86 Sabrehawks"
            VT_86_Snake_Plane_DTOM = "VT-86 Snake Plane DTOM"
            VX_23_Salty_Dogs = "VX-23 Salty Dogs"

    class Pylon1:
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (
            1,
            Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk,
        )
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (
            1,
            Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice,
        )
        PMBR___6_x_BDU_33 = (1, WeaponsT45.PMBR___6_x_BDU_33)

    class Pylon2:
        MXU_648_TP = (2, Weapons.MXU_648_TP)

    class Pylon3:
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk = (
            3,
            Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_M274__Practice_Smk,
        )
        LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice = (
            3,
            Weapons.LAU_68_pod___7_x_2_75_Hydra__UnGd_Rkts_WTU_1_B__Practice,
        )
        PMBR___6_x_BDU_33 = (3, WeaponsT45.PMBR___6_x_BDU_33)

    pylons = {1, 2, 3}

    tasks = [task.GroundAttack, task.Reconnaissance, task.AFAC]
    task_default = task.Reconnaissance
