from lxml import etree

'''
用来解析html代码 
'''


text='''
<div>
    <ul>
        <li class="item-0"> <a href="1.html"> first item </a></li>
        <li class="item-1"> <a href="2.html"> first item </a></li>
        <li class="item-2"> <a href="3.html"> first item </a></li>
        <li class="item-3"> <a href="4.html"> first item </a></li>
        <li class="item-4"> <a href="5.html"> first item </a></li>
        <li class="item-5"> <a href="6.html"> first item </a></li>
    </ul>
</div>
'''

# 利用etree、HTML吧字符串解析成html

html = etree.HTML(text)

s = etree.tostring(html)

print(s)