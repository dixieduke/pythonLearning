import pickle

exampleObj = {'Python':3,'KDE':5,'Windows':10}

fileObj = open('data.obj','wb')
pickle.dump(exampleObj,fileObj)
fileObj.close()