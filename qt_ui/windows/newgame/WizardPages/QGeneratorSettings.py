from __future__ import unicode_literals

from datetime import timedelta

from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout

from game.campaignloader import Campaign
from game.campaignloader.campaign import DEFAULT_BUDGET
from qt_ui.widgets.spinsliders import CurrencySpinner

DEFAULT_MISSION_LENGTH: timedelta = timedelta(minutes=60)


class BudgetInputs(QtWidgets.QGridLayout):
    def __init__(self, label: str, value: int) -> None:
        super().__init__()
        self.addWidget(QtWidgets.QLabel(label), 0, 0)

        minimum = 0
        maximum = 5000

        slider = QtWidgets.QSlider(Qt.Horizontal)
        slider.setMinimum(minimum)
        slider.setMaximum(maximum)
        slider.setValue(value)
        self.starting_money = CurrencySpinner(minimum, maximum, value)
        slider.valueChanged.connect(lambda x: self.starting_money.setValue(x))
        self.starting_money.valueChanged.connect(lambda x: slider.setValue(x))

        self.addWidget(slider, 1, 0)
        self.addWidget(self.starting_money, 1, 1)


class GeneratorOptions(QtWidgets.QWizardPage):
    def __init__(self, campaign: Campaign, parent=None):
        super().__init__(parent)

        self.setTitle("Generator settings")
        self.setSubTitle("\nOptions affecting the generation of the game.")
        self.setPixmap(
            QtWidgets.QWizard.LogoPixmap,
            QtGui.QPixmap("./resources/ui/wizard/logo1.png"),
        )

        # Campaign settings
        generatorSettingsGroup = QtWidgets.QGroupBox("Generator Settings")
        self.no_carrier = QtWidgets.QCheckBox()
        self.registerField("no_carrier", self.no_carrier)
        self.no_lha = QtWidgets.QCheckBox()
        self.registerField("no_lha", self.no_lha)
        self.no_player_navy = QtWidgets.QCheckBox()
        self.registerField("no_player_navy", self.no_player_navy)
        self.no_enemy_navy = QtWidgets.QCheckBox()
        self.registerField("no_enemy_navy", self.no_enemy_navy)
        self.squadrons_start_full = QtWidgets.QCheckBox()
        self.registerField("squadrons_start_full", self.squadrons_start_full)

        generatorLayout = QtWidgets.QGridLayout()
        generatorLayout.addWidget(QtWidgets.QLabel("No Aircraft Carriers"), 1, 0)
        generatorLayout.addWidget(self.no_carrier, 1, 1)
        generatorLayout.addWidget(QtWidgets.QLabel("No LHA"), 2, 0)
        generatorLayout.addWidget(self.no_lha, 2, 1)
        generatorLayout.addWidget(QtWidgets.QLabel("No Player Navy"), 3, 0)
        generatorLayout.addWidget(self.no_player_navy, 3, 1)
        generatorLayout.addWidget(QtWidgets.QLabel("No Enemy Navy"), 4, 0)
        generatorLayout.addWidget(self.no_enemy_navy, 4, 1)

        label = QtWidgets.QLabel("Squadrons start at full capacity")
        label.setToolTip(
            "Campaign will start with all squadrons at full strength "
            "given enough room at the airfield in question.\n"
            "Each squadron's capacity can be defined during Air Wing Configuration."
        )
        generatorLayout.addWidget(label, 5, 0)
        generatorLayout.addWidget(self.squadrons_start_full, 5, 1)
        generatorLayout.addWidget(QtWidgets.QWidget(), 6, 0)

        self.player_budget = BudgetInputs("Player starting budget", DEFAULT_BUDGET)
        self.registerField("starting_money", self.player_budget.starting_money)
        generatorLayout.addLayout(self.player_budget, 7, 0)

        self.enemy_budget = BudgetInputs("Enemy starting budget", DEFAULT_BUDGET)
        self.registerField("enemy_starting_money", self.enemy_budget.starting_money)
        generatorLayout.addLayout(self.enemy_budget, 8, 0)

        generatorSettingsGroup.setLayout(generatorLayout)

        modSettingsGroup = QtWidgets.QGroupBox("Mod Settings")
        self.a4_skyhawk = QtWidgets.QCheckBox()
        self.registerField("a4_skyhawk", self.a4_skyhawk)
        self.a6a_intruder = QtWidgets.QCheckBox()
        self.registerField("a6a_intruder", self.a6a_intruder)
        self.a7e_corsair2 = QtWidgets.QCheckBox()
        self.registerField("a7e_corsair2", self.a7e_corsair2)
        self.hercules = QtWidgets.QCheckBox()
        self.registerField("hercules", self.hercules)
        self.uh_60l = QtWidgets.QCheckBox()
        self.registerField("uh_60l", self.uh_60l)
        self.f4bc_phantom = QtWidgets.QCheckBox()
        self.registerField("f4bc_phantom", self.f4bc_phantom)
        self.f15d_baz = QtWidgets.QCheckBox()
        self.registerField("f15d_baz", self.f15d_baz)
        self.f_15_idf = QtWidgets.QCheckBox()
        self.registerField("f_15_idf", self.f_15_idf)
        self.f_16_idf = QtWidgets.QCheckBox()
        self.registerField("f_16_idf", self.f_16_idf)
        self.fa_18d = QtWidgets.QCheckBox()
        self.registerField("fa_18d", self.fa_18d)
        self.fa_18efg = QtWidgets.QCheckBox()
        self.registerField("fa_18efg", self.fa_18efg)
        self.f22_raptor = QtWidgets.QCheckBox()
        self.registerField("f22_raptor", self.f22_raptor)
        self.f84g_thunderjet = QtWidgets.QCheckBox()
        self.registerField("f84g_thunderjet", self.f84g_thunderjet)
        self.f100_supersabre = QtWidgets.QCheckBox()
        self.registerField("f100_supersabre", self.f100_supersabre)
        self.f104_starfighter = QtWidgets.QCheckBox()
        self.registerField("f104_starfighter", self.f104_starfighter)
        self.f105_thunderchief = QtWidgets.QCheckBox()
        self.registerField("f105_thunderchief", self.f105_thunderchief)
        self.jas39_gripen = QtWidgets.QCheckBox()
        self.registerField("jas39_gripen", self.jas39_gripen)
        self.mirage_3 = QtWidgets.QCheckBox()
        self.registerField("mirage_3", self.mirage_3)
        self.t45_goshawk = QtWidgets.QCheckBox()
        self.registerField("t45_goshawk", self.t45_goshawk)
        self.hawk_t1a = QtWidgets.QCheckBox()
        self.registerField("hawk_t1a", self.hawk_t1a)
        self.super_etendard = QtWidgets.QCheckBox()
        self.registerField("super_etendard", self.super_etendard)
        self.su30_flanker_h = QtWidgets.QCheckBox()
        self.registerField("su30_flanker_h", self.su30_flanker_h)
        self.su57_felon = QtWidgets.QCheckBox()
        self.registerField("su57_felon", self.su57_felon)
        self.ov10a_bronco = QtWidgets.QCheckBox()
        self.registerField("ov10a_bronco", self.ov10a_bronco)
        self.frenchpack = QtWidgets.QCheckBox()
        self.registerField("frenchpack", self.frenchpack)
        self.high_digit_sams = QtWidgets.QCheckBox()
        self.registerField("high_digit_sams", self.high_digit_sams)
        self.swedishmilitaryassetspack = QtWidgets.QCheckBox()
        self.registerField("swedishmilitaryassetspack", self.swedishmilitaryassetspack)
        self.SWPack = QtWidgets.QCheckBox()
        self.registerField("SWPack", self.SWPack)
        self.spanishnavypack = QtWidgets.QCheckBox()
        self.registerField("spanishnavypack", self.spanishnavypack)
        self.irondome = QtWidgets.QCheckBox()
        self.registerField("irondome", self.irondome)

        modHelpText = QtWidgets.QLabel(
            "<p>Select the mods you have installed. If your chosen factions support them, you'll be able to use these mods in your campaign.</p>"
        )
        modHelpText.setAlignment(Qt.AlignCenter)

        modLayout = QtWidgets.QGridLayout()
        modLayout_row = 1

        mod_pairs = [
            ("A-4E Skyhawk (v2.1.0)", self.a4_skyhawk),
            ("A-6A Intruder (v2.7.5.01)", self.a6a_intruder),
            ("A-7E Corsair II", self.a7e_corsair2),
            ("C-130J-30 Super Hercules", self.hercules),
            ("F-4B/C Phantom II (2.8.7.201)", self.f4bc_phantom),
            ("F-15D Baz (v1.0)", self.f15d_baz),
            ("F-15I Ra'am (v1.0 by IDF Mods Project)", self.f_15_idf),
            ("F-16I Sufa & F-16D (v3.6 by IDF Mods Project)", self.f_16_idf),
            ("F/A-18D Hornet (version v2.7.12.01)", self.fa_18d),
            ("F/A-18E/F/G Super Hornet (version 2.1)", self.fa_18efg),
            ("F-22A Raptor", self.f22_raptor),
            ("F-84G Thunderjet (v2.5.7.01)", self.f84g_thunderjet),
            ("F-100 Super Sabre (v2.7.18.30765 patch 20.10.22)", self.f100_supersabre),
            ("F-104 Starfighter (v2.7.11.222.01)", self.f104_starfighter),
            ("F-105 Thunderchief (v2.7.12.23x)", self.f105_thunderchief),
            ("Frenchpack", self.frenchpack),
            ("High Digit SAMs", self.high_digit_sams),
            ("Swedish Military Assets pack (1.10)", self.swedishmilitaryassetspack),
            ("JAS 39 Gripen (v1.8.5-beta)", self.jas39_gripen),
            ("Mirage III (v2.5.7.01)", self.mirage_3),
            ("T-45 Goshawk (version 1.01)", self.t45_goshawk),
            ("Hawk T1A", self.hawk_t1a),
            ("OV-10A Bronco", self.ov10a_bronco),
            ("Super Étendard (v2.5.5)", self.super_etendard),
            ("Su-30 Flanker-H (V2.1.12 beta)", self.su30_flanker_h),
            ("Su-57 Felon (build-04)", self.su57_felon),
            ("UH-60L Black Hawk (v1.3.1)", self.uh_60l),
            ("Star Wars Modpack 2.54+", self.SWPack),
            ("Spanish Naval Assets pack (desdemicabina 3.2.0)", self.spanishnavypack),
            ("IDF Assets Pack (v1.1 by IDF Mods Project)", self.irondome),
        ]

        for i in range(len(mod_pairs)):
            if i % 15 == 0:
                modLayout_row = 1
            col = 2 * (i // 15)
            if i % 5 == 0:
                # Section break here for readability
                modLayout.addWidget(QtWidgets.QWidget(), modLayout_row, col)
                modLayout_row += 1
            label, cb = mod_pairs[i]
            modLayout.addWidget(QLabel(label), modLayout_row, col)
            modLayout.addWidget(cb, modLayout_row, col + 1)
            modLayout_row += 1

        modSettingsGroup.setLayout(modLayout)

        mlayout = QVBoxLayout()
        mlayout.addWidget(generatorSettingsGroup)
        mlayout.addWidget(modSettingsGroup)
        mlayout.addWidget(modHelpText)
        self.setLayout(mlayout)
        self.update_settings(campaign)

    def update_settings(self, campaign: Campaign) -> None:
        s = campaign.settings

        self.player_budget.starting_money.setValue(campaign.recommended_player_money)
        self.enemy_budget.starting_money.setValue(campaign.recommended_enemy_money)

        self.no_carrier.setChecked(s.get("no_carrier", False))
        self.no_lha.setChecked(s.get("no_lha", False))
        self.no_player_navy.setChecked(s.get("no_player_navy", False))
        self.no_enemy_navy.setChecked(s.get("no_enemy_navy", False))
        self.squadrons_start_full.setChecked(s.get("squadron_start_full", False))

        self.a4_skyhawk.setChecked(s.get("a4_skyhawk", False))
        self.a6a_intruder.setChecked(s.get("a6a_intruder", False))
        self.a7e_corsair2.setChecked(s.get("a7e_corsair2", False))
        self.hercules.setChecked(s.get("hercules", False))
        self.uh_60l.setChecked(s.get("uh_60l", False))
        self.f4bc_phantom.setChecked(s.get("f4bc_phantom", False))
        self.f15d_baz.setChecked(s.get("f15d_baz", False))
        self.f_15_idf.setChecked(s.get("f_15_idf", False))
        self.f_16_idf.setChecked(s.get("f_16_idf", False))
        self.fa_18d.setChecked(s.get("fa_18d", False))
        self.fa_18efg.setChecked(s.get("fa_18efg", False))
        self.f22_raptor.setChecked(s.get("f22_raptor", False))
        self.f84g_thunderjet.setChecked(s.get("f84g_thunderjet", False))
        self.f100_supersabre.setChecked(s.get("f100_supersabre", False))
        self.f104_starfighter.setChecked(s.get("f104_starfighter", False))
        self.f105_thunderchief.setChecked(s.get("f105_thunderchief", False))
        self.jas39_gripen.setChecked(s.get("jas39_gripen", False))
        self.mirage_3.setChecked(s.get("mirage_3", False))
        self.t45_goshawk.setChecked(s.get("t45_goshawk", False))
        self.hawk_t1a.setChecked(s.get("hawk_t1a", False))
        self.super_etendard.setChecked(s.get("super_etendard", False))
        self.su30_flanker_h.setChecked(s.get("su30_flanker_h", False))
        self.su57_felon.setChecked(s.get("su57_felon", False))
        self.ov10a_bronco.setChecked(s.get("ov10a_bronco", False))
        self.frenchpack.setChecked(s.get("frenchpack", False))
        self.high_digit_sams.setChecked(s.get("high_digit_sams", False))
        self.spanishnavypack.setChecked(s.get("spanishnavypack", False))
        self.irondome.setChecked(s.get("irondome", False))
        self.swedishmilitaryassetspack.setChecked(
            s.get("swedishmilitaryassetspack", False)
        )
