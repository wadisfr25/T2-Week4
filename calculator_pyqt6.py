import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QComboBox, QMessageBox
)
from PyQt6.QtCore import Qt


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator PyQt6")
        self.setGeometry(100, 100, 300, 250)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Input 1
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Angka Pertama")
        self.input1.textChanged.connect(self.validate_input)
        layout.addWidget(self.input1)

        # Combo operasi
        self.combo = QComboBox()
        self.combo.addItems(["+", "-", "*", "/"])
        layout.addWidget(self.combo)

        # Input 2
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Angka Kedua")
        self.input2.textChanged.connect(self.validate_input)
        layout.addWidget(self.input2)

        # Error label
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        layout.addWidget(self.error_label)

        # Tombol hitung
        self.btn_hitung = QPushButton("Hitung (Enter)")
        self.btn_hitung.clicked.connect(self.hitung)
        self.btn_hitung.setEnabled(False)
        layout.addWidget(self.btn_hitung)

        # Tombol clear
        self.btn_clear = QPushButton("Clear (Esc)")
        self.btn_clear.clicked.connect(self.clear)
        layout.addWidget(self.btn_clear)

        # Hasil
        self.result_label = QLabel("Hasil: -")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    # VALIDASI
    def validate_input(self):
        valid1 = self.is_number(self.input1.text())
        valid2 = self.is_number(self.input2.text())

        # Border merah jika error
        self.input1.setStyleSheet("border: 2px solid red;" if not valid1 else "")
        self.input2.setStyleSheet("border: 2px solid red;" if not valid2 else "")

        if not valid1 or not valid2:
            self.error_label.setText("Input harus berupa angka")
            self.btn_hitung.setEnabled(False)
        else:
            self.error_label.setText("")
            self.btn_hitung.setEnabled(True)

    def is_number(self, text):
        try:
            float(text)
            return True
        except:
            return False

    # HITUNG
    def hitung(self):
        a = float(self.input1.text())
        b = float(self.input2.text())
        op = self.combo.currentText()

        try:
            if op == "+":
                hasil = a + b
            elif op == "-":
                hasil = a - b
            elif op == "*":
                hasil = a * b
            elif op == "/":
                hasil = a / b

            self.result_label.setText(f"Hasil: {hasil}")
        except:
            self.result_label.setText("Error")

    # CLEAR
    def clear(self):
        self.input1.clear()
        self.input2.clear()
        self.result_label.setText("Hasil: -")

    # SHORTCUT (PyQt6 beda sedikit)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            if self.btn_hitung.isEnabled():
                self.hitung()
        elif event.key() == Qt.Key.Key_Escape:
            self.clear()

    # KONFIRMASI EXIT
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Konfirmasi",
            "Yakin ingin keluar?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
    
def initUI(self):
    from PyQt6.QtWidgets import QFormLayout, QHBoxLayout, QFrame

    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(15, 15, 15, 15)

    # CARD (biar mirip kotak di gambar)
    card = QFrame()
    card.setObjectName("card")
    card_layout = QVBoxLayout()
    card_layout.setSpacing(10)

    form = QFormLayout()

    # Input 1
    self.input1 = QLineEdit()
    self.input1.setText("25")
    self.input1.textChanged.connect(self.validate_input)
    form.addRow("Angka Pertama", self.input1)

    # Combo
    self.combo = QComboBox()
    self.combo.addItems(["+ Tambah", "- Kurang", "× Kali", "÷ Bagi"])
    form.addRow("Operasi", self.combo)

    # Input 2
    self.input2 = QLineEdit()
    self.input2.textChanged.connect(self.validate_input)
    form.addRow("Angka Kedua", self.input2)

    card_layout.addLayout(form)

    # Error
    self.error_label = QLabel("")
    self.error_label.setObjectName("error")
    card_layout.addWidget(self.error_label)

    # BUTTONS (sejajar)
    btn_layout = QHBoxLayout()

    self.btn_hitung = QPushButton("Hitung (Enter)")
    self.btn_hitung.setEnabled(False)

    self.btn_clear = QPushButton("Clear (Esc)")
    self.btn_clear.setObjectName("clearBtn")

    self.btn_hitung.clicked.connect(self.hitung)
    self.btn_clear.clicked.connect(self.clear)

    btn_layout.addWidget(self.btn_hitung)
    btn_layout.addWidget(self.btn_clear)

    card_layout.addLayout(btn_layout)

    # HASIL BOX
    self.result_label = QLabel("Hasil: —")
    self.result_label.setObjectName("resultBox")
    self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    card_layout.addWidget(self.result_label)

    # INFO BAWAH
    self.info_label = QLabel("⚠ Input tidak valid — tombol Hitung dinonaktifkan")
    self.info_label.setObjectName("info")
    card_layout.addWidget(self.info_label)

    card.setLayout(card_layout)
    main_layout.addWidget(card)

    self.setLayout(main_layout)

    # STYLE
    self.setStyleSheet("""
        QWidget {
            background-color: #ecf0f1;
            font-family: Segoe UI;
        }

        #card {
            background: white;
            border-radius: 10px;
            padding: 15px;
        }

        QLineEdit {
            padding: 6px;
            border-radius: 6px;
            border: 1px solid #ccc;
        }

        QLineEdit:focus {
            border: 2px solid #3498db;
        }

        QComboBox {
            padding: 6px;
            border-radius: 6px;
            border: 1px solid #ccc;
        }

        QPushButton {
            padding: 8px;
            border-radius: 6px;
            font-weight: bold;
        }

        QPushButton:enabled {
            background-color: #bdc3c7;
            color: white;
        }

        QPushButton:disabled {
            background-color: #dcdde1;
            color: #7f8c8d;
        }

        #clearBtn {
            background-color: #e74c3c;
            color: white;
        }

        #resultBox {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 6px;
            font-weight: bold;
        }

        #error {
            color: red;
            font-size: 12px;
        }

        #info {
            color: red;
            font-size: 11px;
        }
    """)