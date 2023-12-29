
end

presets = {
	upgrades = {
		basic = {
			tent = Preset:new({
				display = 'Tent',
				cost = 1500,
				type = 'upgrade',
				template = "tent"
			}),
			comPost = Preset:new({
				display = 'Barracks',
				cost = 1500,
				type = 'upgrade',
				template = "barracks"
			}),
			outpost = Preset:new({
				display = 'Outpost',
				cost = 1500,
				type = 'upgrade',
				template = "outpost"
			})
		},
		attack = {
			ammoCache = Preset:new({
				display = 'Ammo Cache',
				cost = 1500,
				type = 'upgrade',
				template = "ammo-cache"
			}),
			ammoDepot = Preset:new({
				display = 'Ammo Depot',
				cost = 2000,
				type = 'upgrade',
				template = "ammo-depot"
			}),
            shipTankerSeawisegiant = Preset:new({
                display = 'Tanker Seawise Giant',
                cost = 1500,
                type = 'upgrade',
                template = "ship-tanker-seawisegiant"
            }),
            shipLandingShipSamuelChase = Preset:new({
                display = 'LST USS Samuel Chase',
                cost = 1500,
                type = 'upgrade',
                template = "ship-landingship-samuelchase"
            }),
            shipLandingShipRopucha = Preset:new({
                display = 'LS Ropucha',
                cost = 1500,
                type = 'upgrade',
                template = "ship-landingship-ropucha"
            }),
            shipTankerElnya = Preset:new({
                display = 'Tanker Elnya',
                cost = 1500,
                type = 'upgrade',
                template = "ship-tanker-elnya"
            })
		},
		supply = {
			fuelCache = Preset:new({
				display = 'Fuel Cache',
				cost = 1500,
				type = 'upgrade',
				template = "fuel-cache"
			}),
			fuelTank = Preset:new({
				display = 'Fuel Tank',
				cost = 1500,
				type = 'upgrade',
				template = "fuel-tank-big"
			}),
			fuelTankFarp = Preset:new({
				display = 'Fuel Tank',
				cost = 1500,
				type = 'upgrade',
				template = "fuel-tank-small"
			}),
			factory1 = Preset:new({
				display='Factory',
				cost = 2000,
				type ='upgrade',
				income = 20,
				template = "factory-1"
			}),
			factory2 = Preset:new({
				display='Factory',
				cost = 2000,
				type ='upgrade',
				income = 20,
				template = "factory-2"
			}),
			factoryTank = Preset:new({
				display='Storage Tank',
				cost = 1500,
				type ='upgrade',
				income = 10,
				template = "chem-tank"
			}),
			ammoDepot = Preset:new({
				display = 'Ammo Depot',
				cost = 2000,
				type = 'upgrade',
				income = 40,
				template = "ammo-depot"
			}),
			oilPump = Preset:new({
				display = 'Oil Pump',
				cost = 1500,
				type = 'upgrade',
				income = 20,
				template = "oil-pump"
			}),
			hangar = Preset:new({
				display = 'Hangar',
				cost = 2000,
				type = 'upgrade',
				income = 30,
				template = "hangar"
			}),
			excavator = Preset:new({
				display = 'Excavator',
				cost = 2000,
				type = 'upgrade',
				income = 20,
				template = "excavator"
			}),
			farm1 = Preset:new({
				display = 'Farm House',
				cost = 2000,
				type = 'upgrade',
				income = 40,
				template = "farm-house-1"
			}),
			farm2 = Preset:new({
				display = 'Farm House',
				cost = 2000,
				type = 'upgrade',
				income = 40,
				template = "farm-house-2"
			}),
			refinery1 = Preset:new({
				display='Refinery',
				cost = 2000,
				type ='upgrade',
				income = 100,
				template = "factory-1"
			}),
			powerplant1 = Preset:new({
				display='Power Plant',
				cost = 1500,
				type ='upgrade',
				income = 25,
				template = "factory-1"
			}),
			powerplant2 = Preset:new({
				display='Power Plant',
				cost = 1500,
				type ='upgrade',
				income = 25,
				template = "factory-2"
			}),
			antenna = Preset:new({
				display='Antenna',
				cost = 1000,
				type ='upgrade',
				income = 10,
				template = "antenna"
			}),
			hq = Preset:new({
				display='HQ Building',
				cost = 2000,
				type ='upgrade',
				income = 50,
				template = "tv-tower"
			}),
            shipSupplyTilde = Preset:new({
                display = 'Ship_Tilde_Supply',
                cost = 1500,
                type = 'upgrade',
                template = "ship-supply-tilde"
            }),
            shipLandingShipLstMk2 = Preset:new({
                display = 'LST Mk.II',
                cost = 1500,
                type = 'upgrade',
                template = "ship-landingship-lstmk2"
            }),
            shipBulkerYakushev = Preset:new({
                display = 'Bulker Yakushev',
                cost = 1500,
                type = 'upgrade',
                template = "ship-bulker-yakushev"
            }),
            shipCargoIvanov = Preset:new({
                display = 'Cargo Ivanov',
                cost = 1500,
                type = 'upgrade',
                template = "ship-cargo-ivanov"
            })
		},
		airdef = {
			bunker = Preset:new({
				display = 'Excavator',
				cost = 1500,
				type = 'upgrade',
				template = "excavator"
			}),
			comCenter = Preset:new({
				display = 'Command Center',
				cost = 12500,
				type = 'upgrade',
				template = "command-center"
			})
		}
	},
	defenses = {
		red = {
			infantry = Preset:new({
				display = 'Infantry', 
				cost=2000, 
				type='defense', 
				template='infantry-red',
			}),
			shorad = Preset:new({
				display = 'SAM', 
				cost=2500, 
				type='defense', 
				template='shorad-red',
			}),
			sa2 = Preset:new({
				display = 'SAM',
				cost=3000,
				type='defense',
				template='sa2',
			}),
			sa10 = Preset:new({
				display = 'SAM',
				cost=30000,
				type='defense',
				template='sa10',
			}),
			sa5 = Preset:new({
				display = 'SAM',
				cost=20000,
				type='defense',
				template='sa5',
			}),
			sa3 = Preset:new({
				display = 'SAM',
				cost=4000,
				type='defense',
				template='sa3',
			}),
			sa6 = Preset:new({
				display = 'SAM',
				cost=6000,
				type='defense',
				template='sa6',
			}),
			sa11 = Preset:new({
				display = 'SAM',
				cost=10000,
				type='defense',
				template='sa11',
			}),
			hawk = Preset:new({
				display = 'SAM',
				cost=6000,
				type='defense',
				template='hawk',
			}),
			patriot = Preset:new({
				display = 'SAM',
				cost=30000,
				type='defense',
				template='patriot',
			}),
			nasams = Preset:new({
				display = 'SAM',
				cost=3000,
				type='defense',
				template='nasams',
			}),
			redShipGroup = Preset:new({
				display = 'SAM',
				cost=3000,
				type='defense',
				template='redShipGroup',
			})
		},
		blue = {
			infantry = Preset:new({
				display = 'Infantry',
				cost=2000,
				type='defense',
				template='infantry-blue',
			}),
			shorad = Preset:new({
				display = 'SAM',
				cost=2500,
				type='defense',
				template='shorad-blue',
			}),
			sa2 = Preset:new({
				display = 'SAM',
				cost=3000,
				type='defense',
				template='sa2',
			}),
			sa10 = Preset:new({
				display = 'SAM',
				cost=30000,
				type='defense',
				template='sa10',
			}),
			sa5 = Preset:new({
				display = 'SAM',
				cost=20000,
				type='defense',
				template='sa5',
			}),
			sa3 = Preset:new({
				display = 'SAM',
				cost=4000,
				type='defense',
				template='sa3',
			}),
			sa6 = Preset:new({
				display = 'SAM',
				cost=6000,
				type='defense',
				template='sa6',
			}),
			sa11 = Preset:new({
				display = 'SAM',
				cost=10000,
				type='defense',
				template='sa11',
			}),
			hawk = Preset:new({
				display = 'SAM',
				cost=6000,
				type='defense',
				template='hawk',
			}),
			patriot = Preset:new({
				display = 'SAM',
				cost=30000,
				type='defense',
				template='patriot',
			}),
			nasams = Preset:new({
				display = 'SAM',
				cost=3000,
				type='defense',
				template='nasams',
			}),
			blueShipGroup = Preset:new({
				display = 'SAM',
				cost=3000,
				type='defense',
				template='blueShipGroup',
			})
		}
	},
	missions = {
		supply = {
			convoy = Preset:new({
				display = 'Supply convoy',
				cost = 4000,
				type = 'mission',
				missionType = ZoneCommand.missionTypes.supply_convoy
			}),
			convoy_escorted = Preset:new({
				display = 'Supply convoy',
				cost = 3000,
				type = 'mission',
				missionType = ZoneCommand.missionTypes.supply_convoy
			}),
			helo = Preset:new({
				display = 'Supply helicopter',
				cost = 2500,
				type='mission',
				missionType = ZoneCommand.missionTypes.supply_air
			}),
			transfer = Preset:new({
				display = 'Supply transfer',
				cost = 1000,
				type='mission',
				missionType = ZoneCommand.missionTypes.supply_transfer
			})
		},
		attack = {
			surface = Preset:new({
				display = 'Ground assault',
				cost = 100,
				type = 'mission',
				missionType = ZoneCommand.missionTypes.assault,
			}),
			cas = Preset:new({
				display = 'CAS',
				cost = 200,
				type='mission',
				missionType = ZoneCommand.missionTypes.cas
			}),
			bai = Preset:new({
				display = 'BAI',
				cost = 200,
				type='mission',
				missionType = ZoneCommand.missionTypes.bai
			}),
			strike = Preset:new({
				display = 'Strike',
				cost = 300,
				type='mission',
				missionType = ZoneCommand.missionTypes.strike
			}),
			sead = Preset:new({
				display = 'SEAD',
				cost = 200,
				type='mission',
				missionType = ZoneCommand.missionTypes.sead
			}),
			helo = Preset:new({
				display = 'CAS',
				cost = 100,
				type='mission',
				missionType = ZoneCommand.missionTypes.cas_helo
			})
		},
		patrol={
			aircraft = Preset:new({
				display= "Patrol",
				cost = 100,
				type='mission',
				missionType = ZoneCommand.missionTypes.patrol
			})
		},
		support ={
			awacs = Preset:new({
				display= "AWACS",
				cost = 300,
				type='mission',
				bias='5',
				missionType = ZoneCommand.missionTypes.awacs
			}),
			tanker = Preset:new({
				display= "Tanker",
				cost = 200,
				type='mission',
				bias='2',
				missionType = ZoneCommand.missionTypes.tanker
			})
		}
	},
	special = {
		red = {
			infantry = Preset:new({
				display = 'Infantry', 
				cost=-1, 
				type='defense', 
				template='defense-red',
			}),
		},
		blue = {
			infantry = Preset:new({
				display = 'Infantry', 
				cost=-1, 
				type='defense', 
				template='defense-blue',
			})
		}
	}
}

zones = {}
do

