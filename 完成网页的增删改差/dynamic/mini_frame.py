from pymysql import connect
import re
import logging
import urllib.parse


# URL_FUNC_DICT = {
#     "/index.py": index,
#     "/login.py": login
# }

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT["/index.py"] = index()
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


def openfile(url):
    with open("./templates/" + url) as f:
        content = f.read()
    return content


def mysql(url, sql):
    content = openfile(url)
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='gbk')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute(sql)
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    return stock_infos, content


@route(r"/index.html")
def index(ret):
    url = "index.html"
    sql = "select f.id,g.name,c.name,b.name,g.price,f.beizhu from focus as f left join goods as g on f.goods_id=g.id left join goods_cates as c on g.cate_id=c.id left join goods_brands as b  on g.brand_id=b.id;"
    stock_infos, content = mysql(url, sql)
    tr_template = """
          <tr>
              <td>%s</td>
              <td>%s</td>
              <td>%s</td>
              <td>%s</td>
              <td>%s</td>
              <td>
                <a type="button" href="update/%d.html" style="color:red;"class="update">修改</a>
              </td>
              <td>
                <input type="button" value="删除"  id="toDel" name="toDel" onclick="del(%d)" >   
              </td>
          </tr>    
      """
    html = ""
    for line_info in stock_infos:
        html += tr_template % (
            line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[0],
            line_info[0])
    content = re.sub(r"\{%content%\}", html, content)
    return content


@route(r"/main.html")
def main(ret):
    url = "main.html"
    sql = "select g.id,g.name,c.name,b.name,g.price,g.is_now,g.is_saleoff from goods as g left join goods_cates as c on g.cate_id=c.id left join goods_brands as b  on g.brand_id=b.id;"
    stock_infos, content = mysql(url, sql)
    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input type="button" value="关注" id="toAdd" name="toAdd" onclick="add(this,%d)">
            </td>
        </tr>    
    """
    html = ""
    for line_info in stock_infos:
        html += tr_template % (
            line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6],
            line_info[0])
    content = re.sub(r"\{%content%\}", html, content)
    return content


@route(r"/add/(\d+).html")
def add_focus(ret):
    # 1.获取股票代码
    stock_code = ret.group(1)
    # 2.判断是否有这个股票代码
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='gbk')
    # 获得Cursor对象
    cs = conn.cursor()
    sql = """select * from goods where id=%s;"""
    cs.execute(sql, stock_code)
    # 判断是否存在该商品
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "暂时没有该商品"
    # 3.判断以下是否已经关注过
    sql = """  select * from goods as g inner join focus as f on g.id = f.goods_id where g.id = %s;"""
    cs.execute(sql, stock_code)
    # 如果查出来了，那么表示已经关注过了
    if cs.fetchone():
        cs.close()
        conn.close()
        return "已经关注过了，请勿重复关注....."

    # 4.添加关注
    sql = """ insert into focus (goods_id)select id from goods where id=%s;"""
    cs.execute(sql, stock_code)
    conn.commit()
    cs.close()
    conn.close()
    return "关注成功...."


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    # 1.获取股票代码
    stock_code = ret.group(1)
    # 2.判断是否有这个股票代码
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='gbk')
    # 获得Cursor对象
    cs = conn.cursor()
    # 3.判断是否已经关注过
    sql = """  select * from goods as g inner join focus as f on g.id = f.goods_id where g.id = (select goods_id from focus where id=%s);"""
    cs.execute(sql, stock_code)
    # 如果没有查出来了，那么表示非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "非法请求....."

    # 4.取消关注
    sql = """ delete from focus where id=%s;"""
    cs.execute(sql, stock_code)
    conn.commit()
    cs.close()
    conn.close()
    return "删除成功...."


@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    """显示修改页面"""
    # 1.获取股票代码
    stock_code = ret.group(1)
    # 2.打开模板
    url = "update.html"
    content = openfile(url)
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='gbk')
    # 获得Cursor对象
    cs = conn.cursor()
    sql = """select beizhu from focus where id=%s;"""
    cs.execute(sql, stock_code)
    bz = cs.fetchone()[0]  # 获取这个股票对应的备注信息
    if not bz:
        bz = ""
    cs.close()
    conn.close()
    content = re.sub(r"\{%note_info%\}", stock_code, content)
    content = re.sub(r"\{%code%\}", bz, content)
    return content


@route(r"/update/(\d+)/(.*)\.html")
def save_update_page(ret):
    """保存修改的信息"""
    stock_code = ret.group(1)
    comment = ret.group(2)
    comment = urllib.parse.unquote(comment)  # url解码
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='gbk')
    cs = conn.cursor()
    sql = """update focus set beizhu=%s where id=%s;"""
    cs.execute(sql, (comment, stock_code))
    conn.commit()
    cs.close()
    conn.close()
    return comment


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=gbk')])
    file_name = environ['PATH_INFO']

    # log日志
    # 第一步，创建一个logger对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO) # Log等级总开关

    # 第二步，创建一个handler，用于写入日志文件
    logfile = './log.txt'
    fh = logging.FileHandler(logfile, mode='a') # open的打开模式这里可以进行参考
    fh.setLevel(logging.DEBUG) # 输出到file的log等级的开关

    # 第三歩，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)  # 输出到console的log等级开关

    # 第四步，定义handler的输出恶格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 第五步，将logger添加到handle里面
    logger.addHandler(fh)
    logger.addHandler(ch)

    # logging.basicConfig(level=logging.INFO,
    #                     filename='./log.txt',
    #                     filemode='a',
    #                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # logging.debug('这是 logger debug message')
    # logging.info('这是 logger info message')
    # logging.warning('这是 logger warning message')
    # logging.error('这是 logger error message')
    # logging.critical('这是 logger critical message')
    logging.info("访问的是:%s" % file_name)
    try:
        # return URL_FUNC_DICT[file_name]()
        for url, func in URL_FUNC_DICT.items():
            # {
            #     r"/index.html":index,
            #     r"/main.html":main,
            #     r"/add/\d+\.html":add_focus
            # }
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            logging.warning("没有对应的函数～")
            return "请求的url(%s)没有对应的函数" % file_name
    except Exception as ret:
        return "产生了异常：%s" % str(ret)
