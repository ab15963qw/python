import random

class 角色:
    def __init__(self, 名字, 生命值, 攻擊力):
        self.名字 = 名字
        self.生命值 = 生命值
        self.攻擊力 = 攻擊力

    def 是否存活(self):
        return self.生命值 > 0

    def 承受傷害(self, 傷害):
        self.生命值 -= 傷害
        if self.生命值 < 0:
            self.生命值 = 0

    def 攻擊敵人(self, 敵人):
        傷害 = random.randint(1, self.攻擊力)
        print(f"{self.名字} 對 {敵人.名字} 造成 {傷害} 點傷害！")
        敵人.承受傷害(傷害)

class 玩家(角色):
    def __init__(self, 名字, 生命值, 攻擊力, 金幣=50):
        super().__init__(名字, 生命值, 攻擊力)
        self.金幣 = 金幣
        self.背包 = []
        self.技能 = []

    def 治療(self):
        恢復量 = random.randint(1, 10)
        self.生命值 += 恢復量
        print(f"{self.名字} 恢復了 {恢復量} 點生命值。")

    def 使用技能(self, 敵人):
        if self.技能:
            技能 = random.choice(self.技能)
            傷害 = random.randint(1, 技能['傷害'])
            print(f"{self.名字} 使用 {技能['名稱']} 對 {敵人.名字} 造成 {傷害} 點傷害！")
            敵人.承受傷害(傷害)
        else:
            print("你沒有任何技能！")

class 敵人(角色):
    def __init__(self, 名字, 生命值, 攻擊力):
        super().__init__(名字, 生命值, 攻擊力)

class NPC(角色):
    def __init__(self, 名字, 生命值, 攻擊力, 任務=None):
        super().__init__(名字, 生命值, 攻擊力)
        self.任務 = 任務

class 傳聞:
    def __init__(self):
        self.傳聞列表 = [
            "森林裡藏著一件強大的武器。",
            "附近的村莊正遭受強盜的襲擊。",
            "山中已經有人目擊到了一隻巨龍。",
            "沙漠中埋藏著一個神秘的寶藏。"
        ]

    def 獲取傳聞(self):
        return random.choice(self.傳聞列表)

class  Shop:
    def __init__(self):
        self.物品列表 = {
            "生命藥水": {"價格": 10, "效果": "治療"},
            "劍": {"價格": 20, "效果": "傷害"},
            "火球卷軸": {"價格": 30, "效果": "傷害"}
        }

    def 列出物品(self):
        print("歡迎光臨商店！以下是我們的商品：")
        for 物品, 資訊 in self.物品列表.items():
            print(f"{物品}: 價格 - {資訊['價格']} 金幣")

    def 購買物品(self, 玩家, 物品名):
        if 物品名 in self.物品列表:
            物品資訊 = self.物品列表[物品名]
            if 玩家.金幣 >= 物品資訊['價格']:
                if 物品資訊['效果'] == '治療':
                    玩家.治療()
                elif 物品資訊['效果'] == '傷害':
                    玩家.技能.append({"名稱": 物品名, "傷害": 10})
                玩家.金幣 -= 物品資訊['價格']
                print(f"你花費 {物品資訊['價格']} 金幣購買了 {物品名}！")
            else:
                print("你沒有足夠的金幣！")
        else:
            print("商店沒有這個物品。")

class 地圖:
    def __init__(self):
        self.事件列表 = ["遭遇怪物", "尋找寶藏", "遇見NPC", "什麼都沒有"]
        self.傳聞 = 傳聞()

    def 探索(self, 玩家):
        事件 = random.choice(self.事件列表)
        print("你正在探險...")
        print(f"事件: {事件}")
        if 事件 == "遭遇怪物":
            敵人物件 = 敵人("哥布林", 30, 10)
            print(f"一隻野生的 {敵人物件.名字} 出現了！")
            while 敵人物件.是否存活() and 玩家.是否存活():
                玩家.攻擊敵人(敵人物件)
                if 敵人物件.是否存活():
                    敵人物件.攻擊敵人(玩家)
            if not 敵人物件.是否存活():
                print(f"{敵人物件.名字} 已經被打敗了！")
        elif 事件 == "尋找寶藏":
            寶藏 = random.choice(["金幣", "武器", "生命藥水"])
            print(f"你找到了 {寶藏}！")
            玩家.背包.append(寶藏)
        elif 事件 == "遇見NPC":
            npc = NPC("任務接受者", 50, 0, 任務="打敗巨龍")
            print(f"你遇到了 {npc.名字}！")
            if npc.任務:
                print(f"{npc.名字}: 拜託幫幫我！{npc.任務}")
        elif 事件 == "什麼都沒有":
            print("什麼有趣的事情都沒發生。")
        
        # 添加傳聞事件
        print("你聽到了一個傳聞:")
        print(self.傳聞.獲取傳聞())

def main():
    玩家角色 = 玩家("英雄", 100, 20)
    遊戲地圖 = 地圖()
    商店物件 = Shop()

    print("歡迎來到RPG遊戲！")
    while 玩家角色.是否存活():
        行動 = input("你想要做什麼？ [探險/背包/技能/商店]").lower()
        if 行動 == "探險":
            遊戲地圖.探索(玩家角色)
        elif 行動 == "背包":
            print("背包:")
            print(玩家角色.背包)
        elif 行動 == "技能":
            print("技能:")
            print([技能['名稱'] for 技能 in 玩家角色.技能])
        elif 行動 == "商店":
            商店物件.列出物品()
            物品 = input("你想要買什麼？").capitalize()
            商店物件.購買物品(玩家角色, 物品)
        else:
            print("無效的動作！請選擇 '探險'、'背包'、'技能' 或 '商店'。")

if __name__ == "__main__":
    main()
