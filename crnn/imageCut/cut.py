import numpy as np
import cv2


def get_list(list_data):
    # 取出list中像素存在的区间
    vv_list = list()
    v_list = list()
    for index, i in enumerate(list_data):
        if i > 0:
            v_list.append(index)
        else:
            if v_list:
                vv_list.append(v_list)
                # list的clear与[]有区别
                v_list = []
    return vv_list


def img_cut(image, dir_out='../test_images/part%d.png'):
    print('开始切割')
    img_bgr = image
    if img_bgr is not None:
        img = img_bgr.copy()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 二值化
        t, binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
        '''
        水平投影从左向右投射，计算每一行的黑色像素总数
        '''
        rows, cols = binary.shape
        hor_list = [0] * rows
        for i in range(rows):
            for j in range(cols):
                # 统计每一行的黑色像素总数
                if binary.item(i, j) == 0:
                    hor_list[i] = hor_list[i] + 1
        '''
        对hor_list中的元素进行筛选，可以去除一些噪点
        '''
        hor_arr = np.array(hor_list)
        hor_arr[np.where(hor_arr < 5)] = 0
        hor_list = hor_arr.tolist()

        # 绘制水平投影
        # img_white = np.ones(shape=(rows, cols), dtype=np.uint8) * 255
        # for i in range(rows):
        #    pt1 = (cols - 1, i)
        #    pt2 = (cols - 1 - hor_list[i], i)
        #    cv2.line(img_white, pt1, pt2, (0,), 1)
        #    cv2.imshow('水平投影', img_white)
        #    cv2.waitKey(0)

        # 取出各个文字区间
        vv_list = get_list(hor_list)
        j = 1
        for i in vv_list:
            img_hor = img_bgr[i[0]:i[-1], :, :]
            # cv2.imshow('文本行', img_hor)
            cv2.imwrite(dir_out % j, img_hor, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            j = j + 1
        print('完成切割')
        return True


if __name__ == '__main__':
    print('test')
    img_cut()
