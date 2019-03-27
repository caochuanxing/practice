#!/usr/bin/python
# coding: utf-8
import psutil


class system_status_info():
    def __init__(self):
        root_catalog = '/'

    def get_cpu_info(self):
        cpu_result = psutil.cpu_times()
        cpu_count = psutil.cpu_count()
        print "用户cpu时间占比：%s" % cpu_result.user
        print "系统cpu时间占比：%s" % cpu_result.system
        print "cpu核数：%s" % cpu_count

    def get_mem_info(self):
        mem = psutil.virtual_memory()
        swap_info = psutil.swap_memory()
        print "内存总量(字节): %d" % mem.total
        print "内存可用量(字节)：%d" % mem.available
        print "swap总量(字节)：%d" % swap_info.total
        print "swap使用率：%f%%" % swap_info.percent



if __name__ == '__main__':
    sys_info = system_status_info()
    sys_info.get_cpu_info()
    sys_info.get_mem_info()
