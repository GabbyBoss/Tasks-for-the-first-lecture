def domain_name(url):
    if url.find('//') != -1:
        s_domain = url.partition('//')  
        if s_domain[2].rsplit('.')[0] != 'www':
            return s_domain[2].rsplit('.')[0]
        else:
            return s_domain[2].rsplit('.')[1]
    elif url.find('.') != -1:
        return url.split('.')[1]

print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))       
print(domain_name('http://github.com/carbonfive/raygun'))











