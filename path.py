import os


def main():
    rootpath = os.getcwd()
    print(f'当前工作路径为:{rootpath}')
    pippath = rootpath + '\\requirements.txt'
    pipmake = 'pip install --no-index --find-links=' + rootpath + '\\Emerge-Console依赖包 -r requirements.txt'  # 安装方式一
    pipmakes = 'pip install --no-index --find-links=' + rootpath + '\\Emerge-Console依赖包wheel模式 -r requirements.txt'  # 安装方式二

    print(pipmake)
    make = os.popen(pipmake)
    print(make)

    print(pipmakes)
    makes = os.popen(pipmakes)
    print(makes)


if __name__ == '__main__':
    main()
