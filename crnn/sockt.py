import base64
import cv2
import numpy as np
import infer
from socket import *


def main():
    HOST = '127.0.0.1'
    PORT = 9999
    BUFSIZ = 1024 * 20
    ADDR = (HOST, PORT)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    while True:
        rec_d = bytes([])
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...connected from:', addr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data or len(data) == 0:
                break
            else:
                rec_d = rec_d + data
        rec_d = base64.b64decode(rec_d)
        np_arr = np.fromstring(rec_d, np.uint8)
        image = cv2.imdecode(np_arr, 1)
        #cv2.imshow('image', image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        res = infer.infer_run(image)
        tcpCliSock.send(res.encode())
        tcpCliSock.close()
    tcpSerSock.close()


if __name__ == "__main__":
    main()