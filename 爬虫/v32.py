from lxml import etree


html = etree.parse("./v301.html")

print(type(html))

rst = html.xpath('//book')
print(rst)
print(type(rst))

#查找带有sport属性值的book
rst = html.xpath('//book[@category="sport"]')
print(rst)
print(type(rst))

rst = html.xpath('//book[@category="sport"]/year')
print(rst)
print(type(rst))
rst0=rst[0]
print(rst0.tag)
print(rst0.text)
print(type(rst0))