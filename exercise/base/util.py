import openpyxl, yaml, requests,os

class BaseRequests:
    def __init__(self):
        self.session = requests.session()

    def get(self,url,**kwargs):
        try:
            r = self.session.get(url,**kwargs)
        except Exception as e:
            print(f"发送post请求：{url},参数：{kwargs}异常，异常信息为：{e}")

    def getProjectPath(self):
        '''
        获取当前工程路径
        :return:
        '''
        current_file_path = os.path.realpath(__file__)  # 当前文件路径
        # print(current_file_path)
        dir_name = os.path.dirname(current_file_path)  # 文件所在目录
        # print(dir_name)
        dir_name = os.path.dirname(dir_name)  # 上一级目录
        # print(dir_name)
        dir_name = os.path.dirname(dir_name)  # 上一级目录
        return dir_name + "\\"

class GetExcelData:
    def load(self,workbook,worksheet):
        book = openpyxl.load_workbook(workbook)
        sheet = book[worksheet]
        casedatas = [cell.value for row in sheet['H2':'H9'] for cell in row]
        expects = [cell.value for row in sheet['J2':'J9'] for cell in row]
        data = []
        for i in range(len(casedatas)):
            data1={}
            acasedata = eval(casedatas[i])
            bexcept = eval(expects[i])
            data1['casedata'] = acasedata
            data1['except'] = bexcept
            data.append(data1)
        return data

class GetYamlData:
    def load(self,filepath):
        real_path = BaseRequests().getProjectPath() + filepath  # 拼接完整路径
        with open(real_path, "r", encoding="utf-8") as f:  # 打开文件
            content = yaml.load(f, Loader=yaml.FullLoader)  # 读取文件内容，放到变量content中
            return content



if __name__ == '__main__':
    GetExcelData().load(r'D:\ApiAutoTest\exercise\data\data.xlsx','Sheet1')