import sys
class Main:

    def porcentagem(self, elementos):
        return len(elementos)

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
        
        for _index, _atributos in _dictionary.items():
            print(_index + " - " + str(_atributos))
Main().main()
