# Written by Siyu Chen based on Leo's Lemmatization code
# Created on Feb 12 2016
#
import csv
from nltk.stem.wordnet import WordNetLemmatizer
import sys

class NetworkClass:
    def __init__(self):
        self.actual_row_count = 3
        self.vac_error = 0

    def process_one_question(self, each_row, cell_index, output_file):
        if each_row[cell_index] == "" or each_row[cell_index + 1] == "":
            return

        # questions, language and subject
        language = each_row[0]
        if each_row[12] == '':
            subject = self.actual_row_count
        else:
            subject = each_row[12] 
        finished = each_row[10]
        if each_row[15] == '':
            question3 = '0'
        else:
            question3 = each_row[15]  
        
        if each_row[16] == '':
            question4 = '0'
        else:  
            question4 = each_row[16]  
        
        if each_row[17] == '':
            question5 = '0'
        else:
            question5 = each_row[17]

        if each_row[18] == '':
            question6 = '0'
        else: 
            question6 = each_row[18]

        if each_row[19] == '':
            question7 = '0'
        else:
            question7 = each_row[19].replace(" ", "_")

        #vacs
        if cell_index == 21:
            vac = "sample_vac"
        elif cell_index == 24:
            vac = "he____about_the…"
        elif cell_index == 26 :
            vac = "it____across_the…"
        elif cell_index == 28: 
            vac = "she____after_the" 
        elif cell_index == 30: 
            vac = "it____against_the" 
        elif cell_index == 32: 
            vac = "it____among_the…" 
        elif cell_index == 34: 
            vac = "he____around_the…" 
        elif cell_index == 36: 
            vac = "it____as_the…" 
        elif cell_index == 38: 
            vac = "she____at_the…" 
        elif cell_index == 40: 
            vac = "he____between_the…" 
        elif cell_index == 42: 
            vac = "it____for_the…" 
        elif cell_index == 44: 
            vac = "she____in_the…" 
        elif cell_index == 46: 
            vac = "it____into_the…" 
        elif cell_index == 48: 
            vac = "he____like_the…" 
        elif cell_index == 50: 
            vac = "she____of_the…"
        elif cell_index == 52: 
            vac = "it____off_the…" 
        elif cell_index == 54: 
            vac = "it____over_the…" 
        elif cell_index == 56: 
            vac = "he____through_the…" 
        elif cell_index == 58: 
            vac = "it____towards_the…" 
        elif cell_index == 60: 
            vac = "she____under_the…" 
        elif cell_index == 62: 
            vac = "it____with_the…" 
        elif cell_index == 64: 
            vac = "it____about_the…" 
        elif cell_index == 66: 
            vac = "she____across_the…" 
        elif cell_index == 68: 
            vac = "it____after_the…" 
        elif cell_index == 70: 
            vac = "he____against_the…" 
        elif cell_index == 72: 
            vac = "she____among_the…" 
        elif cell_index == 74: 
            vac = "it____around_the…" 
        elif cell_index == 76: 
            vac = "he____as_the…" 
        elif cell_index == 78: 
            vac = "it____at_the…" 
        elif cell_index == 80: 
            vac = "it____between_the…" 
        elif cell_index == 82: 
            vac = "she____for_the…"
        elif cell_index == 84: 
            vac = "it____in_the…" 
        elif cell_index == 86: 
            vac = "he____into_the…" 
        elif cell_index == 88: 
            vac = "it____like_the…" 
        elif cell_index == 90: 
            vac = "it____of_the…" 
        elif cell_index == 92: 
            vac = "she____off_the…" 
        elif cell_index == 94: 
            vac = "he____over_the…" 
        elif cell_index == 96: 
            vac = "it____through_the…" 
        elif cell_index == 98: 
            vac = "she____towards_the…" 
        elif cell_index == 100: 
            vac = "it____under_the…" 
        elif cell_index == 102: 
            vac = "he____with_the…" 
        elif cell_index == 104: 
            vac = "it_is____that_the…_" 
        elif cell_index == 106: 
            vac = "it____like____…" 
        elif cell_index == 108: 
            vac = "there____a____…" 
        elif cell_index == 110: 
            vac = "we____together." 
        elif cell_index == 112: 
            vac = "it____to_him_that…" 
        elif cell_index == 114: 
            vac = "he____ahead." 
        elif cell_index == 116: 
            vac = "it____as_if…" 
        elif cell_index == 118: 
            vac = "he____down_the…" 
        elif cell_index == 120: 
            vac = "she____in_favor_of_the…" 
        elif cell_index == 122: 
            vac = "it____like_the…" 
        elif cell_index == 124: 
            vac = "he____it_against_the…" 
        elif cell_index == 126: 
            vac = "it____them_among_the…" 
        elif cell_index == 128: 
            vac = "she____it_around_the…" 
        elif cell_index == 130: 
            vac = "it____not." 
        elif cell_index == 132: 
            vac = "he____her_the…" 
        elif cell_index == 134: 
            vac = "it____itself." 
        elif cell_index == 136: 
            vac = "she____so." 
        elif cell_index == 138: 
            vac = "it____its_way_to_the…" 
        elif cell_index == 140: 
            vac = "she____." 
        elif cell_index == 142: 
            vac = "it____the…" 
        elif cell_index == 144: 
            vac = "it_is____that_the_" 
        elif cell_index == 146: 
            vac = "it____like…" 
        elif cell_index == 148: 
            vac = "there________the…" 
        elif cell_index == 150: 
            vac = "they____together." 
        elif cell_index == 152: 
            vac = "it____to_me_that…" 
        elif cell_index == 154: 
            vac = "it____ahead." 
        elif cell_index == 156: 
            vac = "she____as_if…" 
        elif cell_index == 158: 
            vac = "it____down_the…" 
        elif cell_index == 160: 
            vac = "it____in_favor_of_the…" 
        elif cell_index == 162: 
            vac = "she____like_the…" 
        elif cell_index == 164:
            vac = "it____her_against_the…"
        elif cell_index == 166:
            vac = "he____it_among_the…"
        elif cell_index == 168:
            vac = "it____them_around_the…"
        elif cell_index == 170:
            vac = "she____not."
        elif cell_index == 172:
            vac = "it____him_the…"
        elif cell_index == 174:
            vac = "she____herself."
        elif cell_index == 176:
            vac = "it____so."
        elif cell_index == 178:
            vac = "he____his_way_through_the…"
        elif cell_index == 180:
            vac = "it____."
        elif cell_index == 182:
            vac = "he____the…"
        else: 
            vac = "unknown"
            vac_error += 1





           

        words = each_row[cell_index].split("||")[:-1]
        responselength = len(words)
        times = each_row[cell_index + 1].split("||")[:-1] # list of string


        for i in range(len(times)):
            times[i] = times[i].split(",")[0]


        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if times[i] == "null" or times[j] == "null":
                    continue
                output_string = " ".join([str(subject), language, finished, str(question3), str(question4), str(question5), str(question6), str(question7), str(responselength), words[i], words[j], str(i+1), str(j+1), times[i], times[j], str(int(times[j]) - int(times[i])), str(vac)])
                output_file.write(output_string + "\n")
                #sys.exit(0)
        return True


    def main(self):
    # read in lemmatized responses and tranform into network data format
        input_file = open("OutputData/One_Minute_Responses_Sorted.csv","r")
        one_minute_data = csv.reader(input_file)





        output_file = open("OutputData/One_Minute_Responses_Network_Data.tsv","w")

        row_index = 0
        for each_row in one_minute_data:
            if row_index == 0 or row_index ==1:
                row_index += 1
                continue


        # process the sample question explicitly
        # two weird rows that the first words cell does not start at index 21
            if row_index == 864:
                self.process_one_question(each_row, 70, output_file)
            elif row_index == 635:
                self.process_one_question(each_row, 26, output_file)
            else:
                self.process_one_question(each_row, 21, output_file)
                cell_index = 24


        # process the other quesitons and responses
            while cell_index < len(each_row):
                if (row_index == 394 and cell_index >= 70) or (row_index == 532 and cell_index >= 54): #special cells that do not have corresponding time
                    cell_index += 1
                    continue
                self.process_one_question(each_row, cell_index, output_file)
                cell_index += 2
            row_index += 1
            self.actual_row_count += 1

        print("vac error count:", self.vac_error)
        input_file.close()
        output_file.close()


if __name__ == "__main__":
    NetworkClass().main()