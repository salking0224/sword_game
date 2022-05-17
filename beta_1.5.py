# -*- coding: utf-8 -*-
import time
import random
import os
import pickle
from colorama import Fore
from colorama import Style

if os.path.exists("user_data.txt"):
    f = open("user_data.txt", 'rb')
    data = pickle.load(f)
else:
    f = open("user_data.txt", 'wb')
    data = {
        1 : 100000000,
        2 : 7,
        3 : 7,
        4 : 5,
        5 : [],
    }
    pickle.dump(data, f)
    f.close()

enchant_book = []

#색깔들
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
black = Fore.BLACK
white = Fore.WHITE

#리셋
reset = Style.RESET_ALL

coin = data[1]
monster_level = data[2]
sword_level = data[3]
shield_level = data[4]
enchant_book = data[5]

#만약 검레벨이 1레벨, 돈이 1000원이라면
if sword_level == 1 and coin == 1000:
    print(f"허허허 나는 이세계에 정령일세 너에게 1000코인을 줄테니 몬스터를 잡고 {Fore.RED}신의 검과 신의 방패{reset}를 얻고 최종 보스를 물리쳐주게!!")
    print("""(bot) (기본 아이템 나무검, 나무방패, 1000원을 받았다!)
    
---------------------------------------------------------------------------------------------------------------------------------------------------------------

""")
else:
    pass

#클래스들
class Sword:
    def __init__(self, level, name, upgrade_coin, message, power, percentage):
        self.level = level
        self.name = name
        self.upgrade_coin = upgrade_coin
        self.message = message
        self.power = power
        self.percentage = percentage

class Shield:
    def __init__(self, level, name, upgrade_coin, message, power, percentage):
        self.level = level
        self.name = name
        self.upgrade_coin = upgrade_coin
        self.message = message
        self.power = power
        self.percentage = percentage

class Monster:
    def __init__(self, level, name, boss, reward, power, message):
        self.level = level
        self.name = name
        self.boss = boss
        self.reward = reward
        self.power = power
        self.message = message
class Enchant:
    def __init__(self, level, name, percentage, power):
        self.level = level
        self.name = name
        self.percentage = percentage
        self.power = power


#정보
sword_info = {
    1 : Sword(1, "나무 검", 0, "나무검을", 10 ,1),
    2 : Sword(2, "돌 검", 10, "돌검을", 30, 0.8),
    3 : Sword(3, "철 검", 50, "철검을", 100, 0.7),
    4 : Sword(4, "금 검", 300, "금검을", 200, 0.6),
    5 : Sword(5, "루비 검", 500, "루비검을", 350, 0.5),
    6 : Sword(6, "다이아몬드 검", 1000, "다이아몬드검을", 600, 0.4),
    7 : Sword(7, "번개 검", 1500, "번개 검을", 1000, 0.3),
    8 : Sword(8, "투명 검", 3000, "투명 검을", 1700, 0.25),
    9 : Sword(9, "신의 검", 10000, "신의 검을", 4000, 0.1)
}

shield_info = {
    1 : Shield(1, "나무 방패", 0, "나무방패를", 10 ,1),
    2 : Shield(2, "돌 방패", 10, "돌방패를", 30, 0.8),
    3 : Shield(3, "철 방패", 50, "철방패를", 100, 0.7),
    4 : Shield(4, "금 방패", 300, "금방패를", 200, 0.6),
    5 : Shield(5, "루비 빙페", 500, "루비방패를", 350, 0.5),
    6 : Shield(6, "다이아몬드 방패", 1000, "다이아몬드방패를", 600, 0.4),
    7 : Shield(7, "번개 방패", 1500, "번개 방패를", 1000, 0.3),
    8 : Shield(8, "투명 방패", 3000, "투명 방패를", 1700, 0.25),
    9 : Shield(9, "신의 방패", 10000, "신의 방패를", 4000, 0.1)
}

monster_info = {
    1 : Monster(1, "slime", False, 30, 10, "몬스터를 잡았다! 리워드로 30코인을 받았다!"),
    2 : Monster(2, "stone", False, 50, 20, "돌멩이뇌를 잡았다! 벌로 사형을 받았다!"),
    3 : Monster(3, "stone", False, 100, 50, "몬스터를 잡았다! 리워드로 100코인을 받았다!"),
    4 : Monster(4, "slime", False, 200, 100, "몬스터를 잡았다! 리워드로 200코인을 받았다!"),
    5 : Monster(5, "slime and stone", False, 350, 150, "몬스터를 잡았다! 리워드로 350코인을 받았다!"),
    6 : Monster(6, "fapoo", False, 500, 400, "몬스터를 잡았다! 리워드로 500코인을 받았다!"),
    7 : Monster(7, "indana", False, 700, 600, "몬스터를 잡았다! 리워드로 700코인을 받았다!"),
    8 : Monster(8, "big slime", False, 1000, 1000, "몬스터를 잡았다! 리워드로 1000코인을 받았다!"),
    9 : Monster(9, "very big slime", False, 1300, 10, "몬스터를 잡았다! 리워드로 1300코인을 받았다!"),
    10 : Monster(10, "boss", True, 2000, 10, "몬스터를 잡았다! 리워드로 2000코인을 받았다!"),
    11 : Monster(11, "slime", False, 1800, 10, "몬스터를 잡았다! 리워드로 1800코인을 받았다!"),
    12 : Monster(12, "slime", False, 2000, 10, "몬스터를 잡았다! 리워드로 2000코인을 받았다!"),
    13 : Monster(13, "slime", False, 2500, 10, "몬스터를 잡았다! 리워드로 2500코인을 받았다!"),
    14 : Monster(14, "slime", False, 3000, 10, "몬스터를 잡았다! 리워드로 3000코인을 받았다!"),
    15 : Monster(15, "slime", False, 3000, 10, "몬스터를 잡았다! 리워드로 3000코인을 받았다!"),
    16 : Monster(16, "slime", True, 5000, 7900, "몬스터를 잡았다! 리워드로 5000코인을 받았다!"),
}
#class Enchant:
##    def __init__(self, level, name, percentage, power):
##        self.level = level
#        self.name = name
 #       self.percentage = percentage
  #      self.power = power
enchant_book_info = {
    1 : Enchant(1, "날카로움1", 0.8, 100),
    2 : Enchant(2, "날카로움2", 0.75, 300),
    3 : Enchant(3, "날카로움3", 0.5, 800),
    4 : Enchant(4, "날카로움4", 0.4, 1500),
    5 : Enchant(1, "방어1", 0.8, 100),
    6 : Enchant(2, "방어2", 0.75, 300),
    7 : Enchant(3, "방어3", 0.5, 800),
    8 : Enchant(4, "방어4", 0.4, 1500),
}

power = shield_info[shield_level].power + sword_info[sword_level].power


#무엇을 할까
while True:
    try:
        q = input(f"무엇을 하시겠습니까? ({yellow}검 강화{reset}, {yellow}방패 강화{reset}, {yellow}명령어 도움말{reset}({red}이거 해야지 게임 진행 됩니다{reset}){reset}, {blue}개발자 정보{reset}, {Fore.RED}게임 종료(강제종료 하면 게임이 저장되지 않습니다.{reset})) : ")
    except:
        break
    if q == "이 메시지는 씹힐 예정":
        print("안씹혔찌롱 ㅋ")
    if q == "검 강화":
        print("---------------------------------------------")
        while True:
            if sword_level == 9:
                print("검이 최대레벨입니다.") #터미널 예쁘게 해야됨
                break
            reinforce = input(f"""현재 검 : {yellow}{sword_info[sword_level].name}{reset} 강화하시겠습니까? 

            강화된 검 : {blue}{sword_info[sword_level+1].name}{reset}
            강화 성공 확률 : {green}{sword_info[sword_level].percentage * 100}%{reset}
            강화 비용 : {red}{sword_info[sword_level].upgrade_coin}코인{reset}
---------------------------------------------
여기에 입력(예, 아니요) : """)
            if reinforce == "예":
                if coin < sword_info[sword_level].upgrade_coin:
                    print(f"""돈이 {red}부족{reset}합니다...
---------------------------------------------""")
                    break
                coin -= sword_info[sword_level].upgrade_coin
                if random.random() < sword_info[sword_level].percentage:
                    sword_level += 1
                    print(f"""---------------------------------------------
{blue}{sword_info[sword_level].message}{reset} 획득하셨습니다!
---------------------------------------------""")
                else:
                    print(f"""---------------------------------------------
강화 {Fore.RED}실패{reset}
---------------------------------------------""")
            if reinforce == "아니요":
                print("---------------------------------------------")
                break
    if q == "방패 강화":
        print('---------------------------------------------')
        while True:
            if shield_level == 9:
                print("방패가 최대레벨입니다.") #이거도 예쁘게 해야됨
                break
            reinforce_shield = input(f"""현재 방패 : {yellow}{shield_info[shield_level].name}{reset} 강화하시겠습니까?

            강화된 검 : {blue}{shield_info[shield_level+1].name}{reset}
            강화 성공 확률 : {green}{shield_info[shield_level].percentage * 100}%{reset}
            강화 비용 : {red}{shield_info[shield_level].upgrade_coin}코인{reset}
---------------------------------------------
여기에 입력 (예, 아니요) : """)
            if reinforce_shield == "예":
                if coin < shield_info[shield_level].upgrade_coin:
                    print(f"돈이 {red}부족{reset}합니다...")
                    break
                coin -= shield_info[shield_level].upgrade_coin
                if random.random() < shield_info[shield_level].percentage:
                    shield_level += 1
                    print(f"""---------------------------------------------
{blue}{shield_info[shield_level].message}{reset} 획득하셨습니다!
---------------------------------------------""")
                else:
                    print(f"""---------------------------------------------
강화 {red}실패{reset}
---------------------------------------------""")
            if reinforce_shield == "아니요":
                break
    if q.startswith("마왕성 가기 "): #(-----------)이렇게 선좀 쳐놓기
        while True:
            print(f"---------------------------------------------")
            try:
                int(q[7:])
            except ValueError:
                print(f"올바른 {red}층{reset}이 아닙니다.")
                break

            level = int(q[7:])
            if level <= 0:
                print(f"""---------------------------------------------
올바른 {red}층{reset}이 아닙니다.
---------------------------------------------""")
                break
            if level > monster_level:
                print(f"""---------------------------------------------
현재 {red}클리어{reset}한 {red}레벨{reset}이 아닙니다.
---------------------------------------------""")
                break
            if monster_level == 1:
                print(f"""---------------------------------------------
우와 여기가 어디지? {yellow}몬스터 타워{reset} 인것 같아...들어가보자!
---------------------------------------------""")

            monster_yes = input(f"""---------------------------------------------
승리 가능한 공격력 : {red}{monster_info[level].power}{reset} 들어가시겠습니까? (예, 아니요) : """)
            if monster_yes == "예":
                if monster_info[level].power > power:
                    print(f"""---------------------------------------------
내가 이길수 있는 상대가 아니다...{red}공격력{reset}(현재 공격력 : {blue}{sword_info[sword_level].power + shield_info[shield_level].power}{reset})을 더 키워서 오자.
---------------------------------------------""")
                    break
                else:
                    print(f"{level}단계 {monster_info[level].message}")
                    if monster_level == level:
                        monster_level += 1
                    coin = coin + monster_info[level].reward
                    break
            if monster_yes == "아니요":
                break

    if q == f"인첸트북 뽑기":
        while True:
            if sword_info[sword_level].level <= 6:
                pass
            if sword_info[sword_level].level <= 5:
                if shield_info[shield_level].level <= 5:
                    print(f"아직 인첸트할수 있는 {blue}검{reset}이나 {blue}방패{reset}의 레벨이 아니다...{Fore.BLUE}(6레벨부터 가능!!){reset}")
                    break
            if sword_info[sword_level].level > 6:
                sword_enchant_q = input(f"{blue}인첸트북{reset}을 뽑으시겠습니까? {red}(3000원){reset} (예, 아니오) : ")
                if sword_enchant_q == "예":
                    coin -= 3000
                    enchant_book_random = random.choice(enchant_book_info).name
                    print(f"{yellow}{enchant_book_random}{reset}(을)를 뽑았습니다!")

                    enchant_book.append(enchant_book_random)
    
    if q == "내 인첸트북":
        print(', '.join(enchant_book))
                
    if q == "내 정보":
        print(f"코인 : {coin}, 검 : {blue}{sword_info[sword_level].name}{reset}, 방패 : {blue}{shield_info[shield_level].name}{reset}, 공격력 : {red}{sword_info[sword_level].power + shield_info[shield_level].power}{reset}, {yellow}몬스터 타워 레벨{reset} : {monster_level}층")
    if q == "내 검":    
        print(f"이름 : {blue}{sword_info[sword_level].name}{reset}, 공격력 : {red}{sword_info[sword_level].power}{reset}")
    if q == "내 방패":
        print(f"이름 : {blue}{shield_info[shield_level].name}{reset}, 공격력 : {red}{shield_info[shield_level].power}{reset}")
    if q == "게임 종료":
        break
    if q == "명령어 도움말":
        print(f"""---------------------------------------------
{yellow}검 강화{reset}, 
{yellow}방패 강화{reset}, 
{yellow}마왕성 가기 (여기에 가고싶은 몬스터 타워 레벨 적기){reset}, 
{yellow}인첸트북 뽑기{reset}, 
{yellow}인첸트 하기{reset}, 
{yellow}내 정보{reset}, 
{yellow}내 검{reset}, 
{yellow}내 방패{reset}, 
{yellow}내 인첸트북{reset}, 
{yellow}내 아이템{reset},
{yellow}개발자 정보{reset},
{yellow}도움말{reset}
---------------------------------------------""")

    if q == "개발자 정보":
        print(f"""---------------------------------------------
{red}age{reset} : 14
{yellow}youtube_name{reset} : 셀킹
{blue}discord{reset} : salking0224[YT]#0224
{green}gender{reset} : man
hobby : coding
MBTI : ENFP
{blue}e-mail : salkingemail@gmail.com{reset}
---------------------------------------------""")

f = open("user_data.txt", 'wb')
data = {
    1 : coin,
    2 : monster_level,
    3 : sword_level,
    4 : shield_level,
    5 : enchant_book
}
pickle.dump(data, f)
f.close()

#해야될거 : 터미널 예쁘게, 블로그, 색 추가, 몬스터 타워 좀 밸런스 패치, 인첸트북
