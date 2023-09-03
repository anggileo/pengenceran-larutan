import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QRadioButton, QButtonGroup

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Larutan')
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        self.radio_button1 = QRadioButton('cari volume pekatan yang dibutuhkan')
        layout.addWidget(self.radio_button1)

        self.radio_button2 = QRadioButton('larutkan semua pekatan')
        layout.addWidget(self.radio_button2)

        self.group = QButtonGroup(self)
        self.group.addButton(self.radio_button1)
        self.group.addButton(self.radio_button2)

        self.label1 = QLabel('Volume pekatan:')
        layout.addWidget(self.label1)

        self.input1 = QLineEdit()
        layout.addWidget(self.input1)

        self.label2 = QLabel('Konsentrasi pekatan:')
        layout.addWidget(self.label2)

        self.input2 = QLineEdit()
        layout.addWidget(self.input2)

        self.label3 = QLabel('Volume akhir yang diinginkan:')
        layout.addWidget(self.label3)

        self.input3 = QLineEdit()
        layout.addWidget(self.input3)

        self.label4 = QLabel('Konsentrasi akhir yang diinginkan:')
        layout.addWidget(self.label4)

        self.input4 = QLineEdit()
        layout.addWidget(self.input4)

        self.calculate_button = QPushButton('Hitung')
        self.calculate_button.clicked.connect(self.calculate_and_fill)
        layout.addWidget(self.calculate_button)

        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(self.clear_inputs)
        layout.addWidget(self.clear_button)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        self.program_label = QLabel('')
        layout.addWidget(self.program_label)

        self.iloveyou_label = QLabel('(C) Anggi Enggar Firdinan, 2023')
        layout.addWidget(self.iloveyou_label)

        self.radio_button1.toggled.connect(self.disable_input1)
        self.radio_button2.toggled.connect(self.disable_input3)

        self.setLayout(layout)

    def calculate_and_fill(self):
        # Mengambil nilai dari input box
        val1 = self.input1.text()
        val2 = self.input2.text()
        val3 = self.input3.text()
        val4 = self.input4.text()

        # Konversi nilai ke float (pastikan input valid)
        try:
            val1 = float(val1)
        except ValueError:
            val1 = None

        try:
            val2 = float(val2)
        except ValueError:
            val2 = None

        try:
            val3 = float(val3)
        except ValueError:
            val3 = None

        try:
            val4 = float(val4)
        except ValueError:
            val4 = None

        # Logika pengisian input yang kosong
        if val1 is None:
            self.input1.setText(str((val3 * val4) / val2))
        if val2 is None:
            self.input2.setText(str((val3 * val4) / val1))
        if val3 is None:
            self.input3.setText(str((val1 * val2) / val4))
        if val4 is None:
            self.input4.setText(str((val1 * val2) / val3))

        # Hitung hasil perhitungan
        if val1 is not None and val3 is not None:
            result = val3 - val1
            self.result_label.setText(f'Anda perlu pekatan sebanyak {val1:.2f}')
            self.program_label.setText(f'Anda juga perlu pelarut sebanyak: {result:.2f}')

    def clear_inputs(self):
        self.input1.clear()
        self.input2.clear()
        self.input3.clear()
        self.input4.clear()
        self.result_label.clear()
        self.program_label.clear()

        # Mengatur semua radio button menjadi belum terpilih
        self.group.setExclusive(False)
        self.radio_button1.setChecked(False)
        self.radio_button2.setChecked(False)
        self.group.setExclusive(True)

        # Mengembalikan input box menjadi editable
        self.input1.setReadOnly(False)
        self.input3.setReadOnly(False)

    def disable_input1(self):
        # Mengatur input box 1 menjadi read-only jika radio button 1 terpilih
        if self.radio_button1.isChecked():
            self.input1.setReadOnly(True)
        else:
            self.input1.setReadOnly(False)

    def disable_input3(self):
        # Mengatur input box 3 menjadi read-only jika radio button 2 terpilih
        if self.radio_button2.isChecked():
            self.input3.setReadOnly(True)
        else:
            self.input3.setReadOnly(False)

def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

