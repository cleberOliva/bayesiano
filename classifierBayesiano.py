# https://gist.github.com/tuttelikz/94f750ef3bf14f8a126a
import sys
class ClassificadorBayesiano:
    def main(self):
        x_dataset = []
        x_questions = []
        # get file name by the arguments
        x_filename = sys.argv[1]
        
        # open file
        x_file = open(x_filename, "r")
        x_cabecalho = x_file.readline().replace('\n', '').split(' ')
        # print(_cabecalho[-1])
        # print(_cabecalho)
        
        for lines in x_file:
            x_replace = lines.replace('\n', '')
            if x_replace != '---':
                x_dataset.append(x_replace.split(' '))
            else:
                break
        for lines in x_file:
            x_replace = lines.replace('\n', '')
            x_questions.append(x_replace.split(' '))
        x_file.close()

        x_dictionary = {}
        for i in range(len(x_dataset)):
            x_linha = x_dataset[i]
            if (x_linha[-1] not in x_dictionary):
                x_dictionary[x_linha[-1]] = []
            x_dictionary[x_linha[-1]].append(x_linha)
        
        print((x_dictionary['N'][0][0]))
        print(len(x_dictionary['S']))

        for x_counter_line_questions in range(len(x_questions)):
            for x_index in x_dictionary:
                print(x_index)
                x_produtorio = 1
                for x_counter_column in range(len(x_cabecalho)):
                    print('Elemento Questão:    ' + str(x_questions[x_counter_line_questions][x_counter_column]))
                    if x_questions[x_counter_line_questions][x_counter_column] == '?':
                        pass
                    else:
                        x_somatorio = 0
                        for x_counter_line_dict in range(len(x_dictionary[x_index])):
                            print('Elemento Dicionario: ' + str(x_dictionary[x_index][x_counter_line_dict][x_counter_column]))
                            if (x_questions[x_counter_line_questions][x_counter_column] == x_dictionary[x_index][x_counter_line_dict][x_counter_column]):
                                x_somatorio = x_somatorio + 1
                        x_porcentagem = x_somatorio / len(x_dictionary[x_index])
                        x_produtorio = x_produtorio * x_porcentagem
                        print('%.4f' % x_porcentagem)
                
                print('%.4f' % x_produtorio)
                print('=========================================')
                # print(_cabecalho[_counter_column] + '=' + str(_questions[_counter_line_questions][_counter_column]))
ClassificadorBayesiano().main()
