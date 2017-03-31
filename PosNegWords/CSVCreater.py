from PosemoNegemo import PosemoNegemo
import csv

WORDPATH = "/usr/share/dict/words"

class CSVCreater:

    def __init__(self):
        self.posemo_negemo = PosemoNegemo()

    def create_cvs_file(self, file_name, word_list):
        with open(file_name, "w") as output:
            writer = csv.writer(output)
            for val in word_list:
                writer.writerow([val])

    def create_two_files(self):
        pos_lemma = self.posemo_negemo.get_posLemma()
        neg_lemma = self.posemo_negemo.get_negLemma()

        all_pos_words = self.get_list(pos_lemma)
        all_nega_words = self.get_list(neg_lemma)

        self.createCVSFile("./positive_word_lists.cvs", all_pos_words)
        self.createCVSFile("./negative_word_lists.cvs", all_nega_words)

    def get_list(self, lemma):
        words = open(WORDPATH, "r")
        result_words = []
        size = len(lemma)
        idx = 0
        found = False

        for word in words:
            if idx > size - 1:
                break
            dic_word = str.lower(word[0: int(len(word) - 1)])
            cur_word = lemma[idx]
            if str.__contains__(cur_word, "*"):
                prefix = cur_word[0: len(cur_word) - 1]

                if str.startswith(dic_word, prefix):
                    result_words.append(dic_word)
                    found = True
                else:
                    if found:
                        idx += 1
                        found = False
                    else:
                        if prefix < dic_word:
                            idx += 1
                            found = False
            else:
                result_words.append(cur_word)
                idx += 1
        words.close()

        return result_words