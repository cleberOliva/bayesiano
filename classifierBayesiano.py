# https://gist.github.com/tuttelikz/94f750ef3bf14f8a126a
import sys
class ClassificadorBayesiano:
    def main(self):
        _dataset = []
        _questions = []
        # get file name by the arguments
        _filename = sys.argv[1]
        
        # open file
        _file = open(_filename, "r")
        _cabecalho = _file.readline().replace('\n', '').split(' ')
        # print(_cabecalho[-1])
        # print(_cabecalho)
        
        for lines in _file:
            _replace = lines.replace('\n', '')
            if _replace != '---':
                _dataset.append(_replace.split(' '))
            else:
                break
        for lines in _file:
            _replace = lines.replace('\n', '')
            _questions.append(_replace.split(' '))
        _file.close()

        _dictionary = {}
        for i in range(len(_dataset)):
            _linha = _dataset[i]
            if (_linha[-1] not in _dictionary):
                _dictionary[_linha[-1]] = []
            _dictionary[_linha[-1]].append(_linha)
        
        print((_dictionary['N'][0][0]))
        print(len(_dictionary['S']))
        for _index in _dictionary:
            print(_index)
            for _counter_line_questions in range(len(_questions)):
                for _counter_column in range(len(_cabecalho)):
                    print('Elemento Questão:    ' + str(_questions[_counter_line_questions][_counter_column]))
                    _somatorio = 0
                    for _counter_line_dict in range(len(_dictionary[_index])):
                        # print('Elemento Dicionario: ' + str(_dictionary[_index][_counter_line_dict][_counter_column]))
                        if (_questions[_counter_line_questions][_counter_column] == _dictionary[_index][_counter_line_dict][_counter_column]):
                            _somatorio = _somatorio + 1
                    # _porcentagem = _somatorio / len(_dictionary[_index])
                    # print(_porcentagem)
                    # print('=========================================')
                    print(_cabecalho[_counter_column] + '=' + str(_questions[_counter_line_questions][_counter_column]))
ClassificadorBayesiano().main()
