#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
__author__ = 'Cha'

import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zhuanqspidersys.settings")
django.setup()

def main():
    from spiderapp.models import Author

    KUGOU_LIST = [
        ['河图', 'http://5sing.kugou.com/462455/default.html'],
        ['司夏', 'http://5sing.kugou.com/ariel/default.html'],
        ['喵☆酱', 'http://5sing.kugou.com/6339738/default.html'],
        ['绯村柯北', 'http://5sing.kugou.com/676529/default.html'],
        ['猫饭', 'http://5sing.kugou.com/676550/default.html'],
        ['zhucool', 'http://5sing.kugou.com/zhucool/default.html'],
        ['红烧狮子头', 'http://5sing.kugou.com/crazyman/default.html'],
        ['橙翼', 'http://5sing.kugou.com/jarellee/default.html'],
        ['不纯君', 'http://5sing.kugou.com/sibyliest/default.html'],
        ['流月Ryutsuki', 'http://5sing.kugou.com/ryutsuki/default.html'],
        ['清弄', 'http://5sing.kugou.com/qingnong/default.html'],
        ['Aki阿杰', 'http://5sing.kugou.com/fairyaki/default.html'],
        ['HITA', 'http://5sing.kugou.com/141092/default.html'],
        ['小爱的妈', 'http://5sing.kugou.com/GaaraEmma/default.html'],
        ['清莞', 'http://5sing.kugou.com/3705892/default.html'],
        ['梦璟SAYA', 'http://5sing.kugou.com/6536715/default.html'],
        ['只有影子', 'http://5sing.kugou.com/zhiyouyingzi/default.html'],
        ['许多葵', 'http://5sing.kugou.com/xuduokui/default.html'],
        ['齐栾', 'http://5sing.kugou.com/zica2335072748/default.html'],
        ['TetraCalyx', 'http://5sing.kugou.com/15139626/default.html'],
        ['兰芽yaya', 'http://5sing.kugou.com/17327156/default.html	'],
        ['东篱', 'http://5sing.kugou.com/dongli/default.html'],
        ['玉璇玑', 'http://5sing.kugou.com/yuxuanji/default.html'],
        ['玉面', 'http://5sing.kugou.com/1125409/default.html'],
        ['Billyo', 'http://5sing.kugou.com/C210491/default.html'],
        ['CcccEs', 'http://5sing.kugou.com/CcccEs/default.html'],
        ['吾恩', 'http://5sing.kugou.com/wuen/default.html'],
        ['裂天', 'http://5sing.kugou.com/lietian/default.html'],
        ['骄阳', 'http://5sing.kugou.com/2449235/default.html'],
        ['小魂', 'http://5sing.kugou.com/soul/default.html'],
        ['Misia小雨', 'http://5sing.kugou.com/misiaxiaoyu/default.html'],
        ['晴愔', 'http://5sing.kugou.com/9847237/default.html'],
        ['玉采田', 'http://5sing.kugou.com/35524722/default.html'],
        ['丝音', 'http://5sing.kugou.com/34698480/default.html'],
        ['人衣大人', 'http://5sing.kugou.com/lazysnoopy/default.html'],
        ['Assen捷', 'http://5sing.kugou.com/assen/default.html'],
        ['五音Jw', 'http://5sing.kugou.com/wuyinjw/default.html'],
        ['大个壹玖三', 'http://5sing.kugou.com/30070422/default.html'],
        ['Braska', 'http://5sing.kugou.com/braska/default.html'],
        ['横颜君', 'http://5sing.kugou.com/tenderjun/default.html'],
        ['小曲儿', 'http://5sing.kugou.com/xiaoqu/default.html'],
        ['卡修Rui', 'http://5sing.kugou.com/kaxiu/default.html'],
        ['伦桑', 'http://5sing.kugou.com/21769331/default.html'],
        ['纱朵', 'http://5sing.kugou.com/8308175/default.html'],
        ['阡陌', 'http://5sing.kugou.com/11750769/default.html'],
        ['慕寒', 'http://5sing.kugou.com/muhan/default.html'],
        ['奇然', 'http://5sing.kugou.com/qiran/default.html'],
        ['RaJor', 'http://5sing.kugou.com/rajor/default.html'],
        ['小坠', 'http://5sing.kugou.com/xiaozhui/default.html'],
        ['五色石南叶', 'http://5sing.kugou.com/wuseshinanye/default.html'],
        ['CB菌', 'http://5sing.kugou.com/12292483/default.html'],
        ['翘课迟到', 'http://5sing.kugou.com/qiaokechidao/default.html'],
        ['萧忆情', 'http://5sing.kugou.com/xiaoyiqing/default.html'],
        ['lao干妈', 'http://5sing.kugou.com/lgmcc/default.html'],
        ['特曼', 'http://5sing.kugou.com/teman/default.html'],
        ['赫赫kazuki', 'http://5sing.kugou.com/kazuki/default.html'],
        ['Winky诗', 'http://5sing.kugou.com/winky/default.html'],
        ['CRITTY', 'http://5sing.kugou.com/critty/default.html'],
        ['Mario', 'http://5sing.kugou.com/mario/default.html'],
        ['Tacke竹桑', 'http://5sing.kugou.com/Tacke/default.html'],
        ['云の泣', 'http://5sing.kugou.com/weepclouds/default.html'],
        ['银临', 'http://5sing.kugou.com/yinlin/default.html'],
        ['Smile小千', 'http://5sing.kugou.com/zhixuan/default.html'],
        ['不才', 'http://5sing.kugou.com/10789829/default.html'],
        ['董贞', 'http://5sing.kugou.com/3877985/default.html'],
        ['晃儿', 'http://5sing.kugou.com/huanger/default.html'],
        ['玄觞', 'http://5sing.kugou.com/xuanshang/default.html'],
        ['重小烟', 'http://5sing.kugou.com/echien/default.html'],
        ['凌之轩', 'http://5sing.kugou.com/lingzhixuan/default.html'],
        ['兔裹煎蛋卷', 'http://5sing.kugou.com/9035866/default.html'],
        ['Doris小武', 'http://5sing.kugou.com/4803845/default.html'],
        ['Midaho', 'http://5sing.kugou.com/midaho/default.html'],
        ['南风', 'http://5sing.kugou.com/nanfengzjn/default.html'],
        ['少司命', 'http://5sing.kugou.com/shaosiming/default.html'],
        ['柯暮卿', 'http://5sing.kugou.com/kemuqing/default.html'],
        ['西瓜JUN', 'http://5sing.kugou.com/XGJUN/default.html'],
        ['昼夜', 'http://5sing.kugou.com/9808742/default.html'],
        ['双笙', 'http://5sing.kugou.com/35341590/default.html'],
        ['泠鸢yousa', 'http://5sing.kugou.com/yousa/default.html'],
        ['祈Inory', 'http://5sing.kugou.com/inory/default.html'],
        ['戴荃', 'http://5sing.kugou.com/daiquan/default.html'],
        ['安九', 'http://5sing.kugou.com/5632611/default.html'],
        ['排骨教主', 'http://5sing.kugou.com/paigu/default.html'],
        ['江南诚', 'http://5sing.kugou.com/jiangnancheng/default.html'],
        ['流浪的蛙蛙', 'http://5sing.kugou.com/7047532/default.html'],
        ['叶洛洛', 'http://5sing.kugou.com/yeluoluo/default.html'],
        ['佑可猫', 'http://5sing.kugou.com/nekoouka/default.html'],
        ['少年霜', 'http://5sing.kugou.com/1923131/default.html'],
        ['慕岱', 'http://5sing.kugou.com/33884712/default.html'],
        ['云横', 'http://5sing.kugou.com/45709658/default.html'],
        ['魏展眉', 'http://5sing.kugou.com/20232028/default.html'],
        ['冬子', 'http://5sing.kugou.com/dongzi/default.html'],
        ['情桑', 'http://5sing.kugou.com/12634904/default.html'],
        ['青阳', 'http://5sing.kugou.com/929497/default.html'],
        ['鸦青', 'http://5sing.kugou.com/yaqing/default.html'],
        ['NL不分', 'http://5sing.kugou.com/NLbufen/default.html'],
        ['根小八', 'http://5sing.kugou.com/genxiaoba/default.html'],
        ['梦岚', 'http://5sing.kugou.com/1981560/default.html'],
        ['KBShinya', 'http://5sing.kugou.com/kbshinya/default.html'],
        ['哦漏', 'http://5sing.kugou.com/38798531/default.html'],
        ['樱九', 'http://5sing.kugou.com/733942/default.html'],
        ['御皇七', 'http://5sing.kugou.com/siqi647/default.html'],
        ['琉輝liuki', 'http://5sing.kugou.com/9286091/default.html'],
        ['樱小狼', 'http://5sing.kugou.com/sakuraookami/default.html']
    ]
    for k in KUGOU_LIST:
        Author.objects.create(name=k[0], kugou_url=k[1])
    # a = Author(name='中文1', kugou_url='www.baidu.com')
    # a.save()

if __name__ == "__main__":
    main()

