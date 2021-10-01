from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDropEvent
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem


class TableWidgetDragRows(QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropOverwriteMode(False)
        self.setDropIndicatorShown(True)

        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        if 'drop_event_callback' in kwargs.keys():
            self.drop_event_callback = kwargs['drop_event_callback']

    def set_drop_event_callback(self, drop_event_callback):
        self.drop_event_callback = drop_event_callback

    def get_all_rows_content(self):
        self.selectAll()
        rows = [item.text() for item in self.selectedItems()]
        self.clearSelection()
        return rows

    def dropEvent(self, event: QDropEvent):
        if not event.isAccepted() and event.source() == self:
            drop_row = self.drop_on(event)
            if drop_row == self.rowCount():
                return
            rows = sorted({item.row() for item in self.selectedItems()})
            rows_to_move = [
                [QTableWidgetItem(self.item(row_index, column_index)) for column_index in range(self.columnCount())]
                for row_index in rows
            ]

            for row_index in reversed(rows):
                self.removeRow(row_index)

            for row_index, data in enumerate(rows_to_move):
                row_index += drop_row
                self.insertRow(row_index)
                for column_index, column_data in enumerate(data):
                    self.setItem(row_index, column_index, column_data)
            event.accept()
            if self.drop_event_callback:
                self.drop_event_callback(drop_row, rows_to_move)
        super().dropEvent(event)

    def drop_on(self, event):
        index = self.indexAt(event.pos())
        if not index.isValid():
            return self.rowCount()

        return index.row() + 1 if self.is_below(event.pos(), index) else index.row()

    def is_below(self, pos, index):
        rect = self.visualRect(index)
        margin = 2
        if pos.y() - rect.top() < margin:
            return False
        elif rect.bottom() - pos.y() < margin:
            return True
        return rect.contains(pos, True) \
            and not (int(self.model().flags(index)) & Qt.ItemIsDropEnabled) \
            and pos.y() >= rect.center().y()
