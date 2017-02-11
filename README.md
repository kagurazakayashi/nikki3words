# nikki3words
从第三方奇迹暖暖资料库中获得所有服装名称列表，可自定义输入输出和分隔符。可以用来创建输入法的细胞词库，方便在游戏中输入服装名称。数据源：http://seal100x.github.io/nikkiup2u3/

# 参数说明

python nikkiup2u3word.py <--help> <--source (url)> <--output (file)> <--separate (string)>

- 不加任何参数：全部参数按照默认值进行提取。
- --help 或 -h 或 /? ：显示帮助文本。
- --source 或 -s 或 /s <网址> ：指定数据源。
- 　　默认值：http://seal100x.github.io/nikkiup2u3/
- --output 或 -o 或 /o <文件路径> ：指定输出到文件。
- 　　默认值：up2u3word.txt
- --separate 或 -e 或 /e <分隔符>：修改分隔符。
- 　　默认值：Windows换行符（\r\n）

# 许可协议
WTFPL

# 生成文件示例

- 谷歌拼音输入法：
- - 设置 > 字典 > 导入用户字典 > 选择路径
- 搜狗拼音输入法：
- - 相关细胞词库正在审核中。