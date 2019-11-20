import sys
class Main:

    def porcentagem(self, elementos):
        return len(elementos)

    def main(self):
        dataset = []
        datasetFinal = []
        dsClass = {}
        lista2 = []
        # get file name by the arguments
        fileName = sys.argv[1]
        
        # open file
        file = open(fileName, "r")
        cabecalho = file.readline().replace('\n', '').split(' ')
        # print(cabecalho[-1])
        # print(cabecalho)
        
        for lines in file:
            fReplace = lines.replace('\n', '')
            if fReplace != '---':
                dataset.append(fReplace.split(' '))
            else:
                break
        file.close()
        
        for i in range(len(dataset)):
            linha = dataset[i]
            if (linha[-1] not in dsClass):
                dsClass[linha[-1]] = []
            dsClass[linha[-1]].append(linha)
        
        for index in dsClass:
            self.porcentagem(dsClass[index])
        
        for index, atributos in dsClass.items():
            print(atributos)
            lista2.append([index, self.porcentagem(atributos)])
        
        print(lista2)
Main().main()