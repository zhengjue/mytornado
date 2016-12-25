#!/bin/env python
# _*_ coding:utf-8 _*_
import xlsxwriter

def fun1():
    workbook = xlsxwriter.Workbook("demo1.xlsx")
    worksheet1 = workbook.add_worksheet()
    worksheet2 = workbook.add_worksheet("Foglio2")
    worksheet3 = workbook.add_worksheet("Data")
    worksheet4 = workbook.add_worksheet()
    workbook.close()


def fun2():
    workbook = xlsxwriter.Workbook("demo2.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'Hello')            # write_string ()
    worksheet.write(1, 0, 'World')            # write_string ()
    worksheet.write(2, 0, 2)                  # write_number ()
    worksheet.write(3, 0, 3.00001)            # write_number ()
    worksheet.write(4, 0, '=SIN (PI ()/4)')   # write_formula ()
    worksheet.write(5, 0, '')                 # write_blank ()
    worksheet.write(6, 0, None)               # write_blank ()
    workbook.close()


def fun3():
    workbook = xlsxwriter.Workbook("demo3.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write ('A1', 'Hello')     #在A1单元格写入'Hellow'字符串
    cell_format = workbook.add_format ({'bold': True})    #定义一个加粗的格式对象
    worksheet.set_row(0, 40, cell_format)    # 设置第1行单元格高度为40像素, 且引用加粗格式对象
    worksheet.set_row (1, None, None, {'hidden': True})    # 隐藏第2行单元格
    workbook.close()


def fun4():
    workbook = xlsxwriter.Workbook("demo4.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Hello')     #在A1单元格写入'Hellow'字符串
    worksheet.write('B1', 'world')
    cell_format = workbook.add_format({'bold': True})    #定义一个加粗的格式对象
    worksheet.set_column(0, 1, 10, cell_format)   # 设置0到1即 (A到B) 列单元格宽度为10像素,且引用加粗格式对象
    worksheet.set_column('C:D', 20)    # 设置C到D列单元格宽度为20像素
    worksheet.set_column('E:G', None, None, {'hidden': 1})    #隐藏E到G列单元格
    workbook.close()


def fun5():
    workbook = xlsxwriter.Workbook("demo5.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.insert_image ('B5', 'img/python-logo.png', {'url': 'http://python.org'})
    workbook.close()


def fun6():
    """
    更多图表类型说明：
    area：创建一个面积样式的图表；
    bar：创建一个条形样式的图表；
    column：创建一个柱形样式的图表；
    line：创建一个线条样式的图表；
    pie：创建一个饼图样式的图表；
    scatter：创建一个散点样式的图表；
    stock：创建一个股票样式的图表；
    radar：创建一个雷达样式的图表。

    workbook = xlsxwriter.Workbook("demo6.xlsx")
    worksheet = workbook.add_worksheet()
    chart = workbook.add_chart({type, 'column'})    #创建一个column (柱形)图表
    chart.add_series ({
        'categories': '=Sheet1!$A$1:$A$5',
        'values':     '=Sheet1!$B$1:$B$5',
        'line':       {'color': 'red'},
    })
    chart.set_x_axis({
        'name': 'Earnings per Quarter',    #设置X轴标题名称
        'name_font': {'size': 14, 'bold': True},  #设置X轴标题字体属性
        'num_font':  {'italic': True },    #设置X轴数字字体属性
    })
    chart.set_size({'width':720, 'height':576})  # 其中width为宽度，height为高度
    chart.set_title({'name':'Year End Results'})  # 设置图表标题
    chart.set_style(37)  # 设置图表样式，style_id为不同数字则代表不同样式
    chart.set_table()   # 设置X轴为数据表格形式
    worksheet.insert_chart('A7', chart)    #在A7单元格插入图表
    workbook.close()
    """

fun5()
