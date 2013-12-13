import pickle, glob
for filename in glob.glob('*.pkl'):   # Модуль glob для получения списка файлов по шаблону
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)


suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])

