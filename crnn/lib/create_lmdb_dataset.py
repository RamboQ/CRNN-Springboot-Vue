
import lmdb
import cv2
import numpy as np
import os

OUT_PATH = 'D:/BaiduNetdiskDownload/test_lmdb'
IN_PATH = 'D:/BaiduNetdiskDownload/data_test.txt'
PREFIX = 'D:/BaiduNetdiskDownload/images'


def checkImageIsValid(imageBin):
    if imageBin is None:
        return False
    try:
        imageBuf = np.fromstring(imageBin, dtype=np.uint8)
        img = cv2.imdecode(imageBuf, cv2.IMREAD_GRAYSCALE)
        imgH, imgW = img.shape[0], img.shape[1]
    except:
        return False
    else:
        if imgH * imgW == 0:
            return False
    return True


def writeCache(env, cache):
    with env.begin(write=True) as txn:
        for k, v in cache.items():
            #print('k:' + k)
            #print(v)
            #print('\n')
            txn.put(k, v.decode())


def createDataset(outputPath, imagePathList, labelList, lexiconList=None, checkValid=True):
    """
    Create LMDB dataset for CRNN training.
    ARGS:
        outputPath    : LMDB output path
        imagePathList : list of image path
        labelList     : list of corresponding groundtruth texts
        lexiconList   : (optional) list of lexicon lists
        checkValid    : if true, check the validity of every image
    """
    assert (len(imagePathList) == len(labelList))
    nSamples = len(imagePathList)
    env = lmdb.open(outputPath, map_size=399511627776)
    cache = {}
    cnt = 1
    for i in range(nSamples):
        #print(imagePathList[i])
        imagePath = ''.join(imagePathList[i]).split()[0].replace('\n', '').replace('\r\n', '')
        #imagePath=PREFIX + '/' + imagePathList[i].split()[0]
        #print(imagePath)
        label = ''.join(labelList[i])
        #print(label)
        # if not os.path.exists(imagePath):
        #     print('%s does not exist' % imagePath)
        #     continue

        with open('.' + imagePath, 'r') as f:
            imageBin = f.read()

        if checkValid:
            if not checkImageIsValid(imageBin):
                print('%s is not a valid image' % imagePath)
                continue
        imageKey = 'image-%09d' % cnt
        labelKey = 'label-%09d' % cnt
        cache[imageKey] = imageBin
        cache[labelKey] = label
        if lexiconList:
            lexiconKey = 'lexicon-%09d' % cnt
            cache[lexiconKey] = ' '.join(lexiconList[i])
        if cnt % 1000 == 0:
            #print(cache)
            writeCache(env, cache)
            cache = {}
            print('Written %d / %d' % (cnt, nSamples))
        cnt += 1
        print(cnt)
    nSamples = cnt - 1
    cache['num-samples'] = str(nSamples)
    writeCache(env, cache)
    print('Created dataset with %d samples' % nSamples)


if __name__ == '__main__':
    outputPath = OUT_PATH
    if not os.path.exists(OUT_PATH):
        os.mkdir(OUT_PATH)
    imgdata = open(IN_PATH)
    imagePathList = list(imgdata)

    labelList = []
    for line in imagePathList:
        word = line.split()[1]
        labelList.append(word)
    createDataset(outputPath, imagePathList, labelList)
