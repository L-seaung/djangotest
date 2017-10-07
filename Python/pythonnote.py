0x1 python 缩进

python使用代码缩进的方式进行分层
例如：
if a > b:
    print(a)
else:
    print(b)
    
0x2 python中的注释
在python中使用#号进行代码的注释
在进行大段的注释可以用三个单引号或三个双引号把代码块包起来
例如：
 '''                          """
 this is a comment     or       this is a comment
 '''                          """  
 
0x3 python的基本输入输出函数
输入函数
input()#raw_input()python 2.x

使用如下：
    input("input your name")
    user = input("input your name")
    
输出函数
print()

0x4 python计算器
python math模块提供了丰富的数学函数
例如：
import math
math.cos(0.5)
math.sin(math.pi)
math.sin(0.6)
math.tan(0.6)
math.acos(0.6)
math.log10(x)#求x的10底对数
math.sqrt(x)#求x的平方根

0x5 python数据类型
整型和浮点型
在python2.x中数字类型共有4种。分别是：
整型（int）：一般意义上的数
长整型（long）：无限大小的数，在其结尾需要添加小写或大写字母l或L
浮点型（float）：小数或者用E或e表示幂，如：2.7， 1234e+10， 1.5E-10
复数型（complex）：复数的虚部以字母j或J结尾，如：1+2j， 1.2 + 2J
在python3着哦该已经没有long这种类型，不过int与python2.x中的long类型是相同的

算术运算符
**乘方
*乘法
/除法
//整除
%取余
+加法
-减法

逻辑运算符
|位或
^位异或
&位与
<< 左移
>> 右移

字符串

字符串通常用单引号，双引号，或三个双引号（三个单引号）
如：
  str="string"-->str="""string 
                         string
                         string
                     """
字符串操作函数
在这我只列出我比较常用的字符串操作函数
str = 'hi python!'
str.count('p')#获取字符串中p的数目
str.find('hello')#获取字符串中hello的起始位置
str.join("HI")#连接字符串(以str字符串为分隔符连接参数中的每一项)
str.split()#字符串分割
#str.join()并不改变原字符串，只是返回一个新的字符串，如果参数字符串只有一个就会返回参数字符串
#str.split([sep[,maxsplit]])sep可选参数指定分割的字符串，maxsplit可选参数指定分割次数
字符串的索引和分片([index][:][::])
>>>str = "pythoncode"
>>>str[2]
>>>'c'
>>>str[-1]
>>>'e'
>>>str[1:1]#从索引为1但是不包含1的索引
>>>    #输出为空






