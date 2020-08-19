#导入模块
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams

#设置读取、输出文件路径
pdf_file = r'C:\Users\bowei\Desktop\test\Python.pdf'
txt_file = r'C:\Users\bowei\Desktop\test\Python.txt'
# pdf_file = 'C:\Users\bowei\Desktop\test\'Python.pdf'
# txt_file =  'C:\Users\bowei\Desktop\test\Python.txt'

#生成对象并读取文件
device = PDFPageAggregator(PDFResourceManager(), laparams=LAParams())
interpreter = PDFPageInterpreter(PDFResourceManager(), device)
document = PDFDocument()
parser = PDFParser(open(pdf_file, 'rb'))
parser.set_document(document)
document.set_parser(parser)
document.initialize()

#打开TXT文档写入内容
with open(txt_file, 'w', encoding='utf-8') as f:
    page_list = list(document.get_pages())
    page_list_length = len(page_list)
    print('The number of PDF is: ', page_list_length)

    for page in document.get_pages():
        # 接受LTPage对象
        interpreter.process_page(page)

        # 获取LTPage对象的text文本属性
        layout = device.get_result()
        for x in layout:
            if isinstance(x, LTTextBoxHorizontal):
                results = x.get_text()
                f.write(results)

#检验是否转换成TXT文档（用于下一步的作词云图）
with open(txt_file, encoding='utf-8') as f:
    txt_text = f.readlines()
txt_text[:10]


#导入模块
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#读取生成的TXT文档
with open(txt_file, encoding='utf-8') as f:
    mytext = f.readlines()

#生成我的词云对象
mycloud = WordCloud().generate(str(mytext))

#奇迹出现（展示词云图）
plt.imshow(mycloud)
plt.axis('off')  # 关闭词云图坐标显示
plt.savefig('out.jpg', dpi=1000, edgecolor='blue', bbox_inches='tight', quality=95)  # 保存词云图（到工作路径下）
plt.show()