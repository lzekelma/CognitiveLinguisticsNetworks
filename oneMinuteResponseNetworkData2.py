# Written by Siyu Chen based on Leo's Lemmatization code
# Created on Feb 12 2016
#
import csv
from nltk.stem.wordnet import WordNetLemmatizer
import sys

class NetworkClass:
    def __init__(self):
        self.actual_row_count = 3

    def process_one_question(self, each_row, cell_index, output_file):
        if each_row[cell_index] == "" or each_row[cell_index + 1] == "":
            return

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

        #vac = each_row[]

        words = each_row[cell_index].split("||")[:-1]
        responselength = len(words)
        times = each_row[cell_index + 1].split("||")[:-1] # list of string


        for i in range(len(times)):
            times[i] = times[i].split(",")[0]


        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if times[i] == "null" or times[j] == "null":
                    continue
                output_string = " ".join([str(subject), language, finished, str(question3), str(question4), str(question5), str(question6), str(question7), str(responselength), words[i], words[j], str(i+1), str(j+1), times[i], times[j], str(int(times[j]) - int(times[i]))])
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

        input_file.close()
        output_file.close()


if __name__ == "__main__":
    NetworkClass().main()