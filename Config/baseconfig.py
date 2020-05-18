from functools import wraps
import time,os
from Include.commit.Base.helper import PyMysql

class LogMain(object):
    def __call__(self, function):
        @wraps(function)
        def file(*args,**kwargs):
            path = os.path.dirname(os.path.abspath(__name__))
            func_name = function.__name__
            start_time = time.time()
            otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(start_time))
            function(*args,**kwargs)
            end_time = time.time()
            log_string = ('方法路径:{},方法名称:{},执行开始时间:{},运行时间:{}\n'.
                            format(
                            path,
                            func_name,
                            otherStyleTime,
                            str(end_time-start_time)
                                    )
            )
            # 写入Config文件夹下的log文件
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"log.log")
            with open(path,'a',encoding='UTF-8') as file:
                file.write(log_string)
        return file
