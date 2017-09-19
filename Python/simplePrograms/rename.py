#!python3

#멜론차트를 다운받았을때 노래제목에 원치않는 숫자가 들어감.
#그 숫자가 거슬려 지우려고 만듦.

import shutil, os, re

# 정규표현식을 통해 파일포맷을 정한다.
#다운받은 파일의 형식은 (3자리숫자)+ 가수명 + '-' + (2자리숫자) + '-' + 제목 이다.
#여기서 괄호안의 숫자와 가수명뒤의 '-'를 제거하려한다.

filePattern = re.compile(r"""
    (\d\d\d)
    (.*?)
    (-\d\d)-
    (.*?)$
    """, re.VERBOSE)

# 현재 디렉토리의 리스트를 oldFilename에 모두 대입
for oldFilename in os.listdir('.'):
    mo = filePattern.search(oldFilename)
# 정규표현식에 포함되지않으면 그 파일은 건너뜀
    if mo == None:
        continue

    firstInts = mo.group(1)
    singer = mo.group(2)
    secondInts = mo.group(3)
    subject = mo.group(4)
# 새로운 파일명 포맷
    newFilename = singer + '-' + subject

    absWorkingDir = os.path.abspath('.')
    oldFilename = os.path.join(absWorkingDir, oldFilename)
    newFilename = os.path.join(absWorkingDir, newFilename)

    print('Renaming "%s" to "%s"...' % (oldFilename, newFilename))
# 파일명을 바꿈!
    shutil.move(oldFilename, newFilename)
