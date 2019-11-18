import sys
class Main:
    def main(self):
        dataset = []
        list = []
        listFinal = []
        # get file name by the arguments
        fileName = sys.argv[1]
        
        # open file
        file = open(fileName, "r")
        for lines in file:
            fReplace = lines.replace('\n', '')
            if fReplace != '---':
                dataset.append(fReplace.split(' '))
        file.close()

        numColunas = len(dataset[0])

        for i in range(numColunas):
            text = ""
            for j in range(len(dataset)):
                text = text + dataset[j][i] + " "
            
            list.append(text.split(' '))
            list[i].pop()
        print(list)
        print(numColunas)
Main().main()