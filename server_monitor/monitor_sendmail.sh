#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:$PATH
export PATH
basepath=$(cd `dirname $0`; pwd)
cd $basepath

function main()
{
echo "今日阿里云服务器状况如下：" >result.txt
python server_monitor.py >> result.txt
python sendmail.py > /dev/null 2>&1
}

main
