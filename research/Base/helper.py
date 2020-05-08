import os,configparser,pymysql
from selenium import webdriver

class Configparser():
    def config(arg,kwarg = None):
        """
        配置文件的读取(固定Config.basedata.conf)
        :param arg:conf中option
        :param kwarg: 可选参数——option的值
        :return: 单个值或者数组
        """
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../Config/basedata.conf')
        # 使用了ExtendedInterpolation配置文件将会进行解析eg：${...}
        conf = configparser.ConfigParser(interpolation = configparser.ExtendedInterpolation())
        conf.read(path,encoding='utf-8')
        dic = dict(conf._sections)
        for i in dic:
           dic[i] = dict(dic[i])
        if kwarg:
            try:
                dic[arg][kwarg]
            except KeyError as msg:
                return ('KeyError:' + str(msg))
            else:
                return dic[arg][kwarg]
        else:
            try:
                dic[arg]
            except KeyError as msg:
                return ('KeyError:' + str(msg))
            else:
                return dic[arg]

    def get_webdriver(self, brower='Chrome'):
        """
               获取浏览器参数，并生成一个浏览器，之后的所有浏览器调用都使用同一个
               :return: NONE
               """
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-infobars')  # 禁止策略化
        options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug,这个是禁止GUU加速
        options.add_argument('--incognito')  # 隐身模式（无痕模式）
        options.add_argument('--disable-javascript')  # 禁用javascript
        options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
        options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
        options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        # options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        return webdriver.Chrome(options=options)
class PyMysql():
    def __init__(self,database='luowei'):
        self._conf = Helper.config("database")
        self.conn = pymysql.connect(
            # 给连接添加数据库参数
            host=self._conf['host'],
            port=int(self._conf['port']),
            user=self._conf['user'],
            password=self._conf['password'],
            database=database,
            charset=self._conf['charset']
            )
    def insert_mysql(self,sql,data):
        '''
        # 插入多条数据
        :param sql:insert into mytable(user,pwd) values(%s,%s)
        :param data:数组类型
        '''
        cursor = self.conn.cursor()
        cursor.executemany(sql,data)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        print('sql_insert')

    def delete_mysql( self,sql, database='luowei'):
        """
        :param sql:delete from USER1 where id = "1"
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        # 写操作需要提交
        self.conn.commit()
        # 关闭连接
        cursor.close()
        self.conn.close()

    def update_mysql( self,sql, database='luowei'):
        """
        :param sql: update USER1 set name = "ceshi" where id = "2"
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        # 写操作需要提交
        self.conn.commit()
        # 关闭连接
        cursor.close()
        self.conn.close()

    def write_mysql(self,sql, database='luowei'):
        """
        单条写入
        :param sql: insert into USER1(name,age) values("测试1","100")
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        # 写操作需要提交
        self.conn.commit()
        # 关闭连接
        cursor.close()
        self.conn.close()

    def select_mysql(self, sql):
        """
        :param sql:select * from USER1
        :return: list
        """
        # 按照字典返回参数
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        # 写操作需要提交
        return cursor.fetchall()
        cursor.close()
        self.conn.close()
