# 前端项目国际化脚本工具

> 前端项目经常会遇到国际化功能需求，但是好多都是根据excel文件或csv文件一行一行进行复制粘贴，效率非常低下，故下了该脚本帮助前端人员对js文件进行国际化替换操作。



## 场景描述

> 文件内容示例，如有需要可自行修改源代码

### 输入的js文件内容

> 将文件中的双引号全部替换成单引号，不然替换会不精确，替换单引号并不会影响程序运行

```js
export default {
    robot: {
        title: {
            robots_list: 'Robot list ',
            robot_information: 'Robot information',
            modify_robot_name: 'Modify device name',
        }
    }
    
}
```

### 输入的excel/csv文件内容

> 这只是示例，只要title指定，文件有多少列并不影响代码执行

| 对照英文           | 阿拉伯语         |
| ------------------ | ---------------- |
| Robot list         | قائمة الروبوت    |
| Robot information  | معلومات الروبوت  |
| Modify device name | تعديل اسم الجهاز |

### 输出的js文件内容

```js
export default {
    robot: {
        title: {
            robots_list: 'قائمة الروبوت',
            robot_information: 'معلومات الروبوت',
            modify_robot_name: 'تعديل اسم الجهاز',
        }
    }
}
```



## 环境准备

> 所需环境：python3.6以上版本

python官网地址：https://www.python.org/downloads/

安装步骤略...... (ps:安装过程勾上 Add python to path按钮)

安装包：`pip install pandas`



### 运行代码

```python
python re_js.py
#出现以下信息则表示运行成功
输入js文件路径示例：D:\Desktop\pytest\tests\exec_js\en.js
请输入js文件所在路径：
```



