import socket
import re
import multiprocessing
# from dynamic import mini_frame
import sys


class WSGIServer(object):
    def __init__(self, port, app, static_path):
        # 1.创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2.绑定
        self.tcp_server_socket.bind(("", port))
        # 3.变为监听字
        self.tcp_server_socket.listen(128)
        self.application = app
        self.static_path = static_path

    def service_client(self, new_socket):
        """为这个客户端返回数据"""
        "接收浏览器发送过 来的请求，即http请求"
        # GET / HTTP/1.1
        # ......
        request = new_socket.recv(1024).decode("utf-8")
        # print(">>>>>>>" * 10)
        # print(request)
        # 将request转化成列表,获取返回的request[0]
        request_lines = request.splitlines()
        print("")
        print(">" * 20)
        print(request_lines)
        # 2.返回http格式的数据给浏览器

        # GET /index.html HTTP/1.1
        # get post del put
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            # print("*" * 30, file_name)
            if file_name == "/":
                file_name = "/main.html"

        # 2. 返回http格式的数据，给浏览器
        # 2.1 如果请求的资源不是以.py结尾，那么就认为是静态资源（html/css/js/png,jpg等）
        if not file_name.endswith(".html"):
            try:
                f = open(self.static_path + file_name, "rb")
            except:
                response = "HTTP/1.1 404 FOUND\r\n"
                response += "\r\n"
                response += "------没有找到文件-------"
                new_socket.send(response.encode("gbk"))
            else:
                html_content = f.read()
                # 2.1 准备发送给浏览器的数据----header
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # 2.2 准备发送给浏览器的数据----body
                # 将response header发送给浏览器
                new_socket.send(response.encode("gbk"))
                # 将response body发送给浏览器
                new_socket.send(html_content)
                f.close()
        else:
            # 2.2 如果是以.py结尾，那么就认为是动态资源的请求
            env = dict()
            env['PATH_INFO'] = file_name
            body = self.application(env, self.set_response_header)

            header = "HTTP/1.1 %s\r\n" % self.status

            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])
            header += "\r\n"
            response = header + body
            # 发送response给浏览器
            new_socket.send(response.encode("gbk"))
        # 关闭套接字
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [("server", "mini_web v8.8")]
        self.headers += headers

    def run_forever(self):
        """用来完成整体的控制"""
        while True:
            # 4.等待新客户
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5.为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            new_socket.close()
        # 关闭套接字
        tcp_server_socket.close()


def main():
    """控制im整体，创建一个web服务器对象，然后调用这个对象的run_forever方法运行"""
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])
            frame_app_name = sys.argv[2]
        except Exception as ret:
            print("端口输入错误...")
    else:
        print("请按照以下的方式运行：")
        print("python3 xxx.py 7890 ")
        return

    # min_frame:application
    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1)  # mini_frame
        app_name = ret.group(2)  # application
    else:
        print("请按照以下的方式运行：")
        print("python3 xxx.py 7890 mini_frame:appliccation")
        return

    with open("./web_server.conf") as f:
        conf_info = eval(f.read())
        # 此时conf_info是一个字典里面的数据为：
        # {
        #     "static_path": "./static",
        #     "dynamic_path": "./dynamic"
        # }

    sys.path.append(conf_info["dynamic_path"])

    # import frame_name------->找frame-name.py
    # 返回值标记 导入的这个模块
    frame = __import__(frame_name)
    # 此时app就指向了dynamic/
    app = getattr(frame, app_name)
    # port = int(input("请设置服务器端口号："))
    wsgi_server = WSGIServer(port, app, conf_info["static_path"])
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()
