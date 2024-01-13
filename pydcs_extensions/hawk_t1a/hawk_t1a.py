from enum import Enum
from typing import Dict, Any

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons


class WeaponsHawkT1A:
    ADEN_GUNPOD_ = {"clsid": "{ADEN_GUNPOD}", "name": "ADEN GUNPOD", "weight": 87}


inject_weapons(WeaponsHawkT1A)


@planemod
class Hawk_T1A(PlaneType):
    id = "Hawk-T1A"
    flyable = True
    height = 4.02
    width = 9.418
    length = 11.98
    fuel_max = 1272
    max_speed = 2880
    category = "Interceptor"  # {78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

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
                11: 267,
                3: 260,
                6: 259,
                12: 254,
                13: 264,
                7: 262,
                14: 266,
                15: 265,
            },
        },
    }

    class Liveries:
        class Georgia(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Australia(Enum):
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Israel(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Combined_Joint_Task_Forces_Blue(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            _12th_FTW__Randolph_AFB__Texas__RA = "12th FTW, Randolph AFB, Texas (RA)"
            _1st_RS__Beale_AFB__California__BB = "1st RS, Beale AFB, California (BB)"
            XX218___208Sqn = "XX218 - 208Sqn"
            _25th_FTS__Vance_AFB__Oklahoma__VN = "25th FTS, Vance AFB, Oklahoma (VN)"
            _509th_BS__Whitman_AFB__Missouri__WM = (
                "509th BS, Whitman AFB, Missouri (WM)"
            )
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            _88th_FTS__Sheppard_AFB__Texas__EN = "88th FTS, Sheppard AFB, Texas (EN)"
            Finland_HW_329_Green_Brown = "Finland HW-329 Green Brown"
            Finland_HW_341_Grey = "Finland HW-341 Grey"
            Finland_HW_373_Ex_Swiss_Air_Force = "Finland HW-373 Ex-Swiss Air Force"
            NAS_Meridian__Mississippi_Seven__VT_7 = (
                "NAS Meridian, Mississippi Seven (VT-7)"
            )
            XX179___Red_Arrows_1979_2007 = "XX179 - Red Arrows 1979-2007"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX159___FRADU_Royal_Navy_Anniversary = (
                "XX159 - FRADU Royal Navy Anniversary"
            )
            XX175___FRADU_Royal_Navy = "XX175 - FRADU Royal Navy"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            XX100___TFC = "XX100 - TFC"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1252___Normal = "Swiss U-1252 - Normal"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            Swiss_U_1270___Wallis = "Swiss U-1270 - Wallis"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Norway(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Ukraine(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Belgium(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class UK(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX218___208Sqn = "XX218 - 208Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_1979_2007 = "XX179 - Red Arrows 1979-2007"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX159___FRADU_Royal_Navy_Anniversary = (
                "XX159 - FRADU Royal Navy Anniversary"
            )
            XX175___FRADU_Royal_Navy = "XX175 - FRADU Royal Navy"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            XX100___TFC = "XX100 - TFC"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Abkhazia(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Switzerland(Enum):
            Swiss_U_1252___Normal = "Swiss U-1252 - Normal"
            Swiss_U_1270___Wallis = "Swiss U-1270 - Wallis"

        class SouthOssetia(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class TheNetherlands(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Finland(Enum):
            Finland_HW_329_Green_Brown = "Finland HW-329 Green Brown"
            Finland_HW_341_Grey = "Finland HW-341 Grey"
            Finland_HW_373_Ex_Swiss_Air_Force = "Finland HW-373 Ex-Swiss Air Force"

        class Denmark(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Combined_Joint_Task_Forces_Red(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            _12th_FTW__Randolph_AFB__Texas__RA = "12th FTW, Randolph AFB, Texas (RA)"
            _1st_RS__Beale_AFB__California__BB = "1st RS, Beale AFB, California (BB)"
            XX218___208Sqn = "XX218 - 208Sqn"
            _25th_FTS__Vance_AFB__Oklahoma__VN = "25th FTS, Vance AFB, Oklahoma (VN)"
            _509th_BS__Whitman_AFB__Missouri__WM = (
                "509th BS, Whitman AFB, Missouri (WM)"
            )
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            _88th_FTS__Sheppard_AFB__Texas__EN = "88th FTS, Sheppard AFB, Texas (EN)"
            Finland_HW_329_Green_Brown = "Finland HW-329 Green Brown"
            Finland_HW_341_Grey = "Finland HW-341 Grey"
            Finland_HW_373_Ex_Swiss_Air_Force = "Finland HW-373 Ex-Swiss Air Force"
            NAS_Meridian__Mississippi_Seven__VT_7 = (
                "NAS Meridian, Mississippi Seven (VT-7)"
            )
            XX179___Red_Arrows_1979_2007 = "XX179 - Red Arrows 1979-2007"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX159___FRADU_Royal_Navy_Anniversary = (
                "XX159 - FRADU Royal Navy Anniversary"
            )
            XX175___FRADU_Royal_Navy = "XX175 - FRADU Royal Navy"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            XX100___TFC = "XX100 - TFC"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1252___Normal = "Swiss U-1252 - Normal"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            Swiss_U_1270___Wallis = "Swiss U-1270 - Wallis"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Insurgents(Enum):
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class France(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class USA(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            _12th_FTW__Randolph_AFB__Texas__RA = "12th FTW, Randolph AFB, Texas (RA)"
            _1st_RS__Beale_AFB__California__BB = "1st RS, Beale AFB, California (BB)"
            _25th_FTS__Vance_AFB__Oklahoma__VN = "25th FTS, Vance AFB, Oklahoma (VN)"
            _509th_BS__Whitman_AFB__Missouri__WM = (
                "509th BS, Whitman AFB, Missouri (WM)"
            )
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            _88th_FTS__Sheppard_AFB__Texas__EN = "88th FTS, Sheppard AFB, Texas (EN)"
            NAS_Meridian__Mississippi_Seven__VT_7 = (
                "NAS Meridian, Mississippi Seven (VT-7)"
            )
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Russia(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Italy(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Turkey(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Germany(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Spain(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

        class Canada(Enum):
            XX189___100Sqn = "XX189 - 100Sqn"
            XX226___74Sqn_1992_2000 = "XX226 - 74Sqn 1992-2000"
            XX316___74Sqn_1998_2000 = "XX316 - 74Sqn 1998-2000"
            XX179___Red_Arrows_2008_2012 = "XX179 - Red Arrows 2008-2012"
            XX316___FRADU_Royal_Navy = "XX316 - FRADU Royal Navy"
            Swiss_U_1251___White = "Swiss U-1251 - White"
            Swiss_U_1268___ByeByeHawk = "Swiss U-1268 - ByeByeHawk"
            USAF_Aggressor_269 = "USAF Aggressor 269"
            _1018___United_Arab_Emirates = "1018 - United Arab Emirates"
            XX228___VEAO = "XX228 - VEAO"
            XX159___2004_RAF_Hawk_Display = "XX159 - 2004 RAF Hawk Display"
            XX178___1994_RAF_Hawk_Display = "XX178 - 1994 RAF Hawk Display"
            XX201___2010_RAF_Hawk_Display = "XX201 - 2010 RAF Hawk Display"
            XX245___2009_RAF_Hawk_Display = "XX245 - 2009 RAF Hawk Display"
            XX337___92_Sqn_Blue_Tail = "XX337 - 92 Sqn Blue Tail"

    class Pylon1:
        LAU_7_with_AIM_9M_Sidewinder_IR_AAM = (
            1,
            Weapons.LAU_7_with_AIM_9M_Sidewinder_IR_AAM,
        )

    class Pylon2:
        Matra_Type_155_Rocket_Pod = (2, Weapons.Matra_Type_155_Rocket_Pod)
        CBU_87___202_x_CEM_Cluster_Bomb = (2, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BRU_42_3_BDU_33 = (2, Weapons.BRU_42_3_BDU_33)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon3:
        ADEN_GUNPOD_ = (3, WeaponsHawkT1A.ADEN_GUNPOD_)

    class Pylon4:
        Matra_Type_155_Rocket_Pod = (4, Weapons.Matra_Type_155_Rocket_Pod)
        CBU_87___202_x_CEM_Cluster_Bomb = (4, Weapons.CBU_87___202_x_CEM_Cluster_Bomb)
        BRU_42_3_BDU_33 = (4, Weapons.BRU_42_3_BDU_33)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon5:
        LAU_7_with_AIM_9M_Sidewinder_IR_AAM = (
            5,
            Weapons.LAU_7_with_AIM_9M_Sidewinder_IR_AAM,
        )

    class Pylon6:
        Smoke_Generator___red = (6, Weapons.Smoke_Generator___red)
        Smoke_Generator___white = (6, Weapons.Smoke_Generator___white)
        Smoke_Generator___blue = (6, Weapons.Smoke_Generator___blue)

    pylons = {1, 2, 3, 4, 5, 6}

    tasks = [
        task.CAP,
        task.CAS,
        task.Escort,
        task.FighterSweep,
        task.GroundAttack,
        task.Intercept,
    ]
    task_default = task.CAP
