import sys
class Main:
    def main(self):
        dataset = []
        datasetFinal = []
        dsClass = {}
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
        
        # for i in range(len(dataset)):
        #     linha = dataset[i]
        #     if (linha[-1] not in dsClass):
        #         dsClass[linha[-1]] = []
        #     dsClass[linha[-1]].append(linha)
        
        # print(dsClass)
        
        for values in dsClass:
            print(len(dsClass[values]))
        numColunas = len(dataset[0])
        numLines = len(dataset[1:])
        for i in range(numColunas):
            text = ""
            for j in range(len(dataset)):
                text = text + dataset[j][i] + " "
            
            datasetFinal.append(text.split(' '))
            datasetFinal[i].pop()
        for teste in datasetFinal:
            print(teste)
Main().main()