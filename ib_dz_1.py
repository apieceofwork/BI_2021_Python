while True:
    nucl_string = input()
    new_string = nucl_string.lower()

#проверка, что послед. нуклеотидов введена правильно

    if nucl_string == 'exit': #завершение работы программы
        print('Good luck!')
        break
    else:
        is_seq_correct = True
        for i in new_string: #если в послд. хотя бы один посторонний символ
            if (i != 't' and i != 'a' and i != 'u' and i != 'c' and i != 'g'):
                is_seq_correct = False


        if ('a' in new_string and 'c' in new_string and 'g' in new_string):
            if ('t' in new_string and 'u' in new_string):
                is_seq_correct = False
        else:
            is_seq_correct = False

        if is_seq_correct == False:
            print('Sequence is incorrect. Try again!')
        else:
            print('Sequence is correct. Continue')

        reversed_string = nucl_string[len(nucl_string):: -1]

        if is_seq_correct == True:
            seq_task = input()
            if seq_task == 'reverse':
                print(reversed_string)


            if seq_task == 'complement': #построение комплементарной посл
                if "T" in nucl_string or ('t' in nucl_string): #для ДНК
                    compl_string = ''
                    for i in nucl_string:
                            if i == "T":
                                compl_string += "A"
                            if i == 't':
                                compl_string += "a"
                            if i == "A":
                                compl_string += "T"
                            if i == "a":
                                compl_string += "t"
                            if i == "G":
                                compl_string += "C"
                            if i == "g":
                                compl_string += "c"
                            if i == "C":
                                compl_string += "G"
                            if i == "c":
                                compl_string += "g"
                    print(compl_string)


                if ("U" in nucl_string) or ("u" in nucl_string):  #для рнк
                    compl_str = ''
                    for j in nucl_string:
                        if j == "U":
                            compl_str += "A"
                        if j == 'u':
                            compl_str += "a"
                        if j == "A":
                            compl_str += "U"
                        if j == "a":
                            compl_str += "u"
                        if j == "G":
                            compl_str += "C"
                        if j == "g":
                            compl_str += "c"
                        if j == "C":
                            compl_str += "G"
                        if j == "c":
                            compl_str += "g"
                    print(compl_str)


            if seq_task == 'reverse complement': #построение обратной компл.последовательности
                if "T" in nucl_string or ('t' in nucl_string):  #для ДНК
                    compl_dna = ''
                    for i in nucl_string:
                        if i == "T":
                            compl_dna += "A"
                        if i == 't':
                            compl_dna += "a"
                        if i == "A":
                            compl_dna += "T"
                        if i == "a":
                            compl_dna += "t"
                        if i == "G":
                            compl_dna += "C"
                        if i == "g":
                            compl_dna += "c"
                        if i == "C":
                            compl_dna += "G"
                        if i == "c":
                            compl_dna += "g"
                    print(compl_dna[len(compl_dna):: -1])

                if ("U" in nucl_string) or ("u" in nucl_string): #для рнк
                    compl_rna = ''
                    for j in nucl_string:
                        if j == "U":
                            compl_rna += "A"
                        if j == 'u':
                            compl_rna += "a"
                        if j == "A":
                            compl_rna += "U"
                        if j == "a":
                            compl_rna += "u"
                        if j == "G":
                            compl_rna += "C"
                        if j == "g":
                            compl_rna += "c"
                        if j == "C":
                            compl_rna += "G"
                        if j == "c":
                            compl_rna += "g"
                    print(compl_rna[len(compl_rna):: -1])

            if seq_task == 'transcribe': #транскрипция
                if ("U" in nucl_string) or ("u" in nucl_string):
                    print('Wrong!Cannot be implemented with RNA. Try again!')
                if "T" in nucl_string or ('t' in nucl_string):
                    transcribe_str = ''
                    for k in nucl_string:
                        if k == "T":
                            transcribe_str += "U"
                        if k == 't':
                            transcribe_str += "u"
                        if k == "A":
                            transcribe_str += "A"
                        if k == "a":
                            transcribe_str += "a"
                        if k == "G":
                            transcribe_str += "G"
                        if k == "g":
                            transcribe_str += "g"
                        if k == "C":
                            transcribe_str += "C"
                        if k == "c":
                            transcribe_str += "c"
                    print(transcribe_str)













