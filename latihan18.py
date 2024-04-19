# Pengecekan Style Guide PEP8
"""untuk cek Style Guide:
flake8 nama_file.py
pycodestyle nama_file.py
pylint nama_file.py

untuk auto format file code dengan library black, yapf, autopep8
black nama_file.py
yapf nama_file.py
autopep8 nama_file.py atau autopep8 --in-place --aggressive --aggressive nama_file.py
"""


class Kalkulator:
    """kalkulator tambah kurang"""

    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i):
        return self.i + _i

    def kurang(self, _i):
        return self.i - _i
