# Requires Swedish Military Assets for DCS by Currenthill:
# https://forum.dcs.world/topic/295202-swedish-military-assets-for-dcs-by-currenthill/
#

from typing import Set

from dcs import unittype, task
from dcs.helicopters import HelicopterType

from game.modsupport import vehiclemod, shipmod, helicoptermod


@vehiclemod
class M142_HIMARS_GMLRS(unittype.VehicleType):
    id = "M142_HIMARS_GMLRS"
    name = "[CH] M142 HIMARS (GMLRS)"
    detection_range = 0
    threat_range = 92000
    air_weapon_dist = 92000
    eplrs = True
