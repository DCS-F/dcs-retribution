from datetime import timedelta

from PySide2.QtCore import QItemSelectionModel, QPoint, QModelIndex
from PySide2.QtGui import QStandardItem, QStandardItemModel
from PySide2.QtWidgets import (
    QHeaderView,
    QTableView,
    QStyledItemDelegate,
    QWidget,
    QStyleOptionViewItem,
    QDoubleSpinBox,
)

from game.ato.flight import Flight
from game.ato.flightwaypoint import FlightWaypoint
from game.ato.flightwaypointtype import FlightWaypointType
from game.ato.package import Package
from game.utils import Distance
from qt_ui.windows.mission.flight.waypoints.QFlightWaypointItem import QWaypointItem

HEADER_LABELS = ["Name", "Alt (ft)", "Alt Type", "TOT/DEPART"]


class AltitudeEditorDelegate(QStyledItemDelegate):
    def createEditor(
        self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex
    ) -> QDoubleSpinBox:
        editor = QDoubleSpinBox(parent)
        editor.setMinimum(0)
        editor.setMaximum(40000)
        return editor


class QFlightWaypointList(QTableView):
    def __init__(self, package: Package, flight: Flight):
        super().__init__()
        self.package = package
        self.flight = flight

        self.model = QStandardItemModel(self)
        self.model.itemChanged.connect(self.on_changed)
        self.setModel(self.model)
        self.model.setHorizontalHeaderLabels(HEADER_LABELS)

        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.update_list()

        self.selectionModel().setCurrentIndex(
            self.indexAt(QPoint(1, 1)), QItemSelectionModel.Select
        )

        self.altitude_editor_delegate = AltitudeEditorDelegate(self)
        self.setItemDelegateForColumn(1, self.altitude_editor_delegate)

    def update_list(self) -> None:
        # ignore signals when updating list so on_changed does not fire
        self.model.blockSignals(True)
        try:
            # We need to keep just the row and rebuild the index later because the
            # QModelIndex will not be valid after the model is cleared.
            current_index = self.currentIndex().row()
            self.model.clear()

            self.model.setHorizontalHeaderLabels(HEADER_LABELS)

            waypoints = self.flight.flight_plan.waypoints
            for row, waypoint in enumerate(waypoints):
                self._add_waypoint_row(row, self.flight, waypoint)
            self.selectionModel().setCurrentIndex(
                self.model.index(current_index, 0), QItemSelectionModel.Select
            )
            self.resizeColumnsToContents()
            total_column_width = self.verticalHeader().width() + self.lineWidth()
            for i in range(0, self.model.columnCount()):
                total_column_width += self.columnWidth(i) + self.lineWidth()
            self.setFixedWidth(total_column_width)
        finally:
            # stop ignoring signals
            self.model.blockSignals(False)

    def _add_waypoint_row(
        self, row: int, flight: Flight, waypoint: FlightWaypoint
    ) -> None:
        self.model.insertRow(self.model.rowCount())

        self.model.setItem(row, 0, QWaypointItem(waypoint, row))

        altitude = int(waypoint.alt.feet)
        altitude_item = QStandardItem(f"{altitude}")
        altitude_item.setEditable(True)
        self.model.setItem(row, 1, altitude_item)

        altitude_type = "AGL" if waypoint.alt_type == "RADIO" else "MSL"
        altitude_type_item = QStandardItem(f"{altitude_type}")
        altitude_type_item.setEditable(False)
        self.model.setItem(row, 2, altitude_type_item)

        tot = self.tot_text(flight, waypoint)
        tot_item = QStandardItem(tot)
        tot_item.setEditable(False)
        self.model.setItem(row, 3, tot_item)

    def on_changed(self) -> None:
        for i in range(self.model.rowCount()):
            altitude = self.model.item(i, 1).text()
            altitude_feet = float(altitude)
            self.flight.flight_plan.waypoints[i].alt = Distance.from_feet(altitude_feet)

    def tot_text(self, flight: Flight, waypoint: FlightWaypoint) -> str:
        if waypoint.waypoint_type == FlightWaypointType.TAKEOFF:
            return self.takeoff_text(flight)
        prefix = ""
        time = flight.flight_plan.tot_for_waypoint(waypoint)
        if time is None:
            prefix = "Depart "
            time = flight.flight_plan.depart_time_for_waypoint(waypoint)
        if time is None:
            return ""
        time = timedelta(seconds=int(time.total_seconds()))
        return f"{prefix}T+{time}"

    @staticmethod
    def takeoff_text(flight: Flight) -> str:
        takeoff_time = flight.flight_plan.takeoff_time()
        # Handle custom flight plans where we can't estimate the takeoff time.
        if takeoff_time is None:
            takeoff_time = timedelta()
        start_time = timedelta(seconds=int(takeoff_time.total_seconds()))
        return f"T+{start_time}"
