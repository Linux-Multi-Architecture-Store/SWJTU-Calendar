# !/bin/bash
pyi-makespec -F -w --osx-bundle-identifier "ga.swjtu.calendar" --codesign-identity "Apple Development: ganyuanzhen@vip.qq.com (Z958D862N2)" -n "SWJTU 日历" -i assets/imgs/logo.png main.py
pyinstaller --clean -y "SWJTU 日历.spec"
# https://github.com/create-dmg/create-dmg
