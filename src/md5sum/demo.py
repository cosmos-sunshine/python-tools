# -*- coding: utf-8 -*-
import hashlib
import sys
import os


def md5hex(word):
    """ MD5加密算法，返回32位小写16进制符号 """
    if isinstance(word, unicode):
        word = word.encode("utf-8")
    elif not isinstance(word, str):
        word = str(word)
    m = hashlib.md5()
    m.update(word)
    return m.hexdigest()


def md5sum(fname):
    """ 计算文件的MD5值 """

    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else:  # 最后要将游标放回文件开头
            fh.seek(0)

    m = hashlib.md5()
    if isinstance(fname, basestring) and os.path.exists(fname):
        with open(fname, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
                # 上传的文件缓存 或 已打开的文件流
    elif fname.__class__.__name__ in ["StringIO", "StringO"] or isinstance(fname, file):
        for chunk in read_chunks(fname):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()


if __name__ == "__main__":
    print(md5hex(sys.argv[1]))
    print(md5sum(sys.argv[2]))
    //https://www.iteye.com/blog/ggsonic-1402454
    //https://www.cnblogs.com/lanyangsh/p/8543689.html
    //https://www.jb51.net/article/60635.htm
    //https://blog.csdn.net/qq_24452475/article/details/79623051
    //https://www.cnblogs.com/jjzd/p/7010801.html