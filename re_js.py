#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:zhang yechong
import pandas as pd


class InternationalizationReplacement:
    """
    国际化替换
    """

    def __init__(self, input_js_path, input_excel_path, output_js_path=None, old_title="对照英文", new_title="阿拉伯语",
                 is_csv=False):
        """
        :param input_js_path: 输入的js文件路径
        :param input_excel_path: 输入的excel文件路径/也可是csv文件路径，csv文件必要要设置is_csv为True
        :param output_js_path: 输出的js文件路径
        :param old_title: excel文件中源数据所在列的title
        :param new_title: excel文件中目标数据所在列的title
        :param is_csv: 是否传入的为csv文件
        """

        self.input_js_path = input_js_path
        self.input_excel_path = input_excel_path
        self.output_js_path = output_js_path if output_js_path else "./output.js"
        self.old_title = old_title
        self.new_title = new_title
        self.is_csv = is_csv

    def _read_input_js(self):
        # 读取 JavaScript 文件
        try:
            with open(rf"{self.input_js_path}", "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"读取js文件失败，错误代码如下\n"
                  f"{str(e)}")
            return None

    def _replace_data(self, javascript_data):
        """
        替换数据
        :param  javascript_data: 替换数据前的js数据
        :return: javascript_data 替换数据后的js数据
        """
        try:
            if self.is_csv:
                df = pd.read_csv(rf"{self.input_excel_path}")
            else:
                df = pd.read_excel(rf"{self.input_excel_path}")

            en = df[self.old_title].tolist()
            ala = df[self.new_title].tolist()
            my_dict = dict(zip(en, ala))

            for i, v in my_dict.items():
                if str(i) == "nan":
                    continue
                # 替换文本
                javascript_data = javascript_data.replace("'" + str(i) + "'", "'" + str(v) + "'")
            return javascript_data
        except Exception as e:
            print(f"读取数据失败，错误代码如下\n"
                  f"{str(e)}")
            return None

    def _save_output_js(self, javascript_data):
        """
        保存成新生成js文件
        :param javascript_data :替换数据后得js数据
        :return:
        """
        # 写入修改后的 JavaScript 代码到新文件
        try:
            with open(rf"{self.output_js_path}", "w", encoding="utf-8") as file:
                file.write(javascript_data)
        except Exception as e:
            print(f"保存新的数据失败，错误代码如下\n"
                  f"{str(e)}")

    def run(self):
        print("step 1 => 读取源js文件")
        javascript_data = self._read_input_js()
        print("step 2 => 替换对应数据")
        new_javascript_data = self._replace_data(javascript_data)
        print("step 3 => 保存新js文件")
        self._save_output_js(new_javascript_data)
        print("end...")


if __name__ == '__main__':

    print(r"输入js文件路径示例：D:\Desktop\pytest\tests\exec_js\en.js")
    input_js = input("请输入js文件所在路径：")
    print("----------------------------------------")

    print("传入文件是否为csv:1为是，0为否")
    print("###可传空值，默认为0")
    is_csv = input("请输入excel/csv文件所在路径：")
    if not is_csv:
        is_csv = 0
    if int(is_csv) != 1:
        is_csv = 0
    print("----------------------------------------")

    print(r"输入excel/csv文件路径示例：D:\Desktop\pytest\tests\exec_js\Arabic Translation - Platform.xlsx")
    input_excel = input("请输入excel/csv文件所在路径：")
    print("----------------------------------------")

    print(r"输出js文件路径示例：D:\Desktop\pytest\tests\exec_js\output.js")
    print("###可传空，则文件生成在当前运行目录，名为output.js")
    output_js = input("输出js文件所在路径：")
    print("----------------------------------------")

    print("输入源数据title示例：对照英文")
    old_title = input("excel/csv文件中源数据title：")
    print("----------------------------------------")

    print("输入目标数据title示例：阿拉伯语")
    new_title = input("excel/csv文件中目标数据title：")
    print("----------------------------------------")


    internation_replace = InternationalizationReplacement(input_js, input_excel, output_js,old_title,new_title,is_csv)
    internation_replace.run()
