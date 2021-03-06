#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


#获取脚本路径
def cur_file_dir():
    pathx = sys.argv[0]
    path,_file = os.path.split(pathx)
    if cmp(path,'') == 0:
        path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
    
#获取父目录
def GetParentPath(strPath):
    if not strPath:
        return None;
    lsPath = os.path.split(strPath);
    if lsPath[1]:
        return lsPath[0];
    lsPath = os.path.split(lsPath[0]);
    return lsPath[0];

#获取所有界面的json文件列表
def getAllExtFile(path,fromatx = ".erl"):
    jsondir = path
    jsonfilelist = []
    for root, _dirs, files in os.walk(jsondir):
        for filex in files:          
            #print filex
            name,text = os.path.splitext(filex)
            if cmp(text,fromatx) == 0:
                jsonArr = []
                rootdir = path
                dirx = root[len(rootdir):]
                pathName = dirx +os.sep + filex
                jsonArr.append(pathName)
                (newPath,_name) = os.path.split(pathName)
                jsonArr.append(newPath)
                jsonArr.append(name)
                jsonfilelist.append(jsonArr)
    return jsonfilelist

def getAllTxtFileFromDir(txtpath = '/Users/junpengzhang/Documents/erlang/erltest'):
    txts = getAllExtFile(txtpath,'.erl')
    txtfs = []
    for dx in txts:
        txtfs.append(txtpath + dx[0])
    return txtfs

def compliteErl(fpth):
    print fpth
    pth,fil = os.path.split(fpth)
    cmd = 'cd ' + pth + '\n'
    cmd += 'erlc ' + fil + '\n'
    strx = os.popen(cmd).read()
    strx = strx.split('\n')
    for s in strx:
        if s:
            print s

def main(pth = None):
	if pth:
		erlFiles = getAllTxtFileFromDir(pth)
		for e in erlFiles:
			compliteErl(e)
	else:
		erlFiles = getAllTxtFileFromDir()
		for e in erlFiles:
			compliteErl(e)
	

if __name__ == '__main__':
    args = sys.argv
    print args
    epth = ''
    if len(args) > 1:
        epth = args[1]
        if os.path.isfile(epth):
            compliteErl(epth)
        else:
            main(epth)
    else:
        main()