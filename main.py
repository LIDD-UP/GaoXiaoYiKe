from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute('scrapy crawl gaoxiao'.split(' '))
    # cmdline.execute('scrapy crawl crawl_user'.split(' '))

    # from random import choice
    # print(choice([1,2,3,4]))s