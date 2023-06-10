# 导入openpyxl
import openpyxl

# 创建openpyxl工作库
wb = openpyxl.Workbook()

# 获取第一个工作表
sheet = wb.active

# 在A1单元格子中写入文本
sheet['A1'] = 'hello world'

# 保存文件
filename = 'example.xlsx'
wb.save(filename)

