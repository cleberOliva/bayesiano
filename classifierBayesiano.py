# https://gist.github.com/tuttelikz/94f750ef3bf14f8a126a
import sys
import os.path
import operator
class ClassificadorBayesiano:
    def __init__(self):
        self.x_cabecalho    = []
        self.x_dataset      = []
        self.x_questions    = []
        self.x_dictionary   = {}
        self.x_dict_result  = {}
        self.x_total_lines  = None

    def printarResultados(self, p_line_counter):
        x_texto = ""
        for x_indice in range(len(self.x_cabecalho)):
            if self.x_cabecalho[x_indice] == self.x_cabecalho[-2]:
                x_texto = x_texto + self.x_cabecalho[x_indice] + '=' + str(self.x_questions[p_line_counter][x_indice]) + ' ==> '
            elif self.x_cabecalho[x_indice] == self.x_cabecalho[-1]:
                x_texto = x_texto + self.x_cabecalho[x_indice] + '=' + max(self.x_dict_result.items(), key=operator.itemgetter(1))[0] + ' '
                for x_in_dict_result, x_valor in self.x_dict_result.items():
                    for x_column_dict_result in range(len(self.x_dict_result[x_in_dict_result])):
                        x_texto = x_texto + ' ' + x_in_dict_result + '=' + '%.4f' % x_valor[x_column_dict_result] + ';'
            else:
                x_texto = x_texto + self.x_cabecalho[x_indice] + '=' + str(self.x_questions[p_line_counter][x_indice]) + ', '
        print(x_texto)

    def processarDataSet(self):
        self.x_total_lines = len(self.x_dataset)

        for i in range(len(self.x_dataset)):
            x_linha = self.x_dataset[i]
            if (x_linha[-1] not in self.x_dictionary):
                self.x_dictionary[x_linha[-1]] = []
            self.x_dictionary[x_linha[-1]].append(x_linha)
        
        for x_counter_line_questions in range(len(self.x_questions)):
            x_results = []
            for x_index in self.x_dictionary:
                self.x_dict_result[x_index] = []
                x_produtorio = float(len(self.x_dictionary[x_index])) / float(self.x_total_lines)
                for x_counter_column in range(len(self.x_cabecalho)):
                    if self.x_questions[x_counter_line_questions][x_counter_column] == '?':
                        pass
                    else:
                        x_somatorio = 0.0
                        for x_counter_line_dict in range(len(self.x_dictionary[x_index])):
                            if (self.x_questions[x_counter_line_questions][x_counter_column] == self.x_dictionary[x_index][x_counter_line_dict][x_counter_column]):
                                x_somatorio = x_somatorio + 1.0
                        x_porcentagem = x_somatorio / float(len(self.x_dictionary[x_index]))
                        x_produtorio = x_produtorio * x_porcentagem
                self.x_dict_result[x_index].append(x_produtorio)
            self.printarResultados(x_counter_line_questions)
    
    def lerArquivo(self):
        # open file
        x_filename = sys.argv[1]
        x_file = open(x_filename, "r")
        self.x_cabecalho = x_file.readline().replace('\n', '').split(' ')
        # print(_cabecalho[-1])
        # print(_cabecalho)
        
        for lines in x_file:
            x_replace = lines.replace('\n', '')
            if x_replace != '---':
                self.x_dataset.append(x_replace.split(' '))
            else:
                break
        for lines in x_file:
            x_replace = lines.replace('\n', '')
            self.x_questions.append(x_replace.split(' '))
        x_file.close()
        
        self.processarDataSet()
        # print(os.path.splitext(x_filename))[1]
    def main(self):

        # abrir/ler arquivo e criar dataset
        self.lerArquivo()
ClassificadorBayesiano().main()
