import glob
sourceDir = '.git/face/'
# print ('Reading Images...')
im_filelist = glob.glob(sourceDir+'*')
# print ('Sorting Images...')
im_filelist.sort()
# print ('Sorting done.')

# dic = {"coast":1, "fores":2, "highw":3, "insid":4, "mount":5, "openc":6, "stree":7, "tallb":8}
dic = {"AlexR":1, "Clive":2, "HughL":3, "Jared":4, "Miley":5, "Scarl":6, "Viggo":7, "ZacEf":8}
for fil in im_filelist:
    print (dic[fil[10:15]])
