import os
import time

# 1.需要备份的文件与目录将被指定在一个列表中。
# 例如在Windows下： 下面的路径是我电脑上的路径，需要进行修改后才可以使用
source = ['C:\\Users\liyue\Downloads']
# 又例如在Mac OS X 与 Linux 下：
# source = ['/Users/swa/notes']
# 在这里要注意到我们必须在字符中使用双引号。用以括起其中包含空格的名称。

# 2.备份文件必须存储在一个
# 主备份目录中。例如在windows下：（以下目录如果不存在，会自动创建）
target_dir = 'F:\\FTP'
# 又例如在Mac OS X 和 Linux 下：
# target_dir = '/Users/swa/backup'
# 要记得将这里的目录地址修改至你将使用的路径

# 如果目标目录不存在则创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录
    

# 3.备份文件将打包压缩成zip文件。
# 4.将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')

# zip 文件名称格式
target = today + os.sep + now + '.zip'

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

# 5.我们使用zip命令将文件打包成zip格式。 zip下载：http://gnuwin32.sourceforge.net/packages/zip.htm
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
