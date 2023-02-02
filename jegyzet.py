jegyzet = input('Adja meg amit szeretne jegyzetelni (írja be hogy stop ha le akarja állítani)!')
while jegyzet != 'stop':
    jegyzet = input('Adja meg amit szeretne jegyzetelni (írja be hogy stop ha le akarja állítani)!')
    file = open('H:\iras\jegyzet.txt', 'a')
    file.write(jegyzet)