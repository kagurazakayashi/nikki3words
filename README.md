# nikki3words
从第三方奇迹暖暖资料库中获得所有服装名称列表，可自定义输入输出和分隔符。可以用来创建输入法的细胞词库，方便在游戏中输入服装名称。

# 直接安装词库

- 搜狗拼音输入法细胞词库官网安装： [陆服](http://pinyin.sogou.com/dict/detail/index/70514)　[台服](http://pinyin.sogou.com/dict/detail/index/70994)
- TXT UTF-8 词库文件： [陆服-通用](https://github.com/cxchope/nikki3words/blob/master/up2u3word_cn.txt)　[台服-通用](https://github.com/cxchope/nikki3words/blob/master/up2u3word_tw.txt)
- 搜狗输入法： [陆服-拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/sogou_cn.txt)　[台服-拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/sogou_tw.txt)
- 百度输入法： [陆服-拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/baidupy_cn.txt)　[陆服-手机拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/mobile_baidu_cn.txt)
- QQ输入法： [陆服-拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/qqpy_cn.txt)　[陆服-五笔](https://github.com/cxchope/nikki3words/blob/master/thesaurus/qqwb_cn.txt)　[陆服-手机拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/mobile_qq_cn.txt)
- 必应输入法： [陆服-拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/baidupy_cn.txt)
- 谷歌输入法： [陆服-拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/googlepy_cn.txt)
- 极点输入法： [陆服-五笔](https://github.com/cxchope/nikki3words/blob/master/thesaurus/jidianwb_cn.txt)　[陆服-郑码](https://github.com/cxchope/nikki3words/blob/master/thesaurus/jidianzm_cn.txt)　[台服-郑码](https://github.com/cxchope/nikki3words/blob/master/thesaurus/jidianzm_tw.txt)
- 讯飞输入法： [陆服-手机拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/mobile_xunfei_cn.txt)
- 微软拼音输入法： [陆服-拼音](https://github.com/cxchope/nikki3words/blob/master/thesaurus/mspy_cn.txt)
- 五笔输入法： [陆服-五笔86](https://github.com/cxchope/nikki3words/blob/master/thesaurus/wb86_cn.txt)　[陆服-五笔98](https://github.com/cxchope/nikki3words/blob/master/thesaurus/wb98_cn.txt)
- 仓颉输入法： [陆服-仓颉](https://github.com/cxchope/nikki3words/blob/master/thesaurus/cangjie_cn.txt)　[台服-仓颉](https://github.com/cxchope/nikki3words/blob/master/thesaurus/cangjie_tw.txt)

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

# 默认数据源

- 国服：[http://seal100x.github.io/nikkiup2u3_data/wardrobe.js](http://seal100x.github.io/nikkiup2u3/)
- 台服：[https://nikkitw.github.io/nikkitw/data/wardrobe.js](https://nikkitw.github.io/nikkitw/)

# 致谢

该项目使用了来自以下项目中的部分资源：

- [seal100x/seal100x.github.io](https://github.com/seal100x/seal100x.github.io)
- - 奇迹暖暖在线工具 by @黑的升华 modified from ivangift's github
- [studyzy/imewlconverter](https://github.com/studyzy/imewlconverter)
- - 深蓝词库转换