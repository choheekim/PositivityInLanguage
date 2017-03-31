import openpyxl
import os

EXCEL_FILE = "/LIWCPosemoNegemo-2-2.xlsx"

class PosemoNegemo:

    def __init__(self):
        self.sheet = self.getExcelFile()
        self.posLemma = []
        self.negLemma = []
        self.updateDictionaries()

    def get_excel_file(self):
        cwd = os.getcwd()
        wb = openpyxl.load_workbook(cwd + EXCEL_FILE)
        return wb.get_sheet_by_name('Sheet1')

    def update_dictionaries(self):
        self.add_to_dic(self.posLemma, 'A', 'C')
        self.add_to_dic(self.negLemma, 'D', 'G')

    def get_posLemma(self):
        return self.posemo

    def get_negLemma(self):
        return self.negemo

    def add_to_dic(self, lemma, range_from, range_to):
        for column in range(ord(range_from), ord(range_to) + 1):
            for row in range(3, self.sheet.max_row + 1):
                cur_word = str(self.sheet[chr(column) + str(row)].value)
                if cur_word != 'None':
                    lemma.append(cur_word)






