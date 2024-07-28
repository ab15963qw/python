import tkinter as tk
from tkinter import messagebox

class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("星辰的覺醒")
        
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.story_text = tk.Text(self.frame, wrap=tk.WORD, state=tk.DISABLED)
        self.story_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.options_frame = tk.Frame(self.frame)
        self.options_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.start_game()
        
    def start_game(self):
        self.show_story("第一章：星辰的覺醒\n\n場景1：天文社團的夜晚\n\n"
                        "星月和莉娜在學校的天文社團觀測星空，宇轩前來查看活動。\n")
        self.show_options(["觀測獵戶座", "觀測大熊座"], [self.observe_orion, self.observe_ursa_major])
    
    def show_story(self, text):
        self.story_text.config(state=tk.NORMAL)
        self.story_text.delete(1.0, tk.END)
        self.story_text.insert(tk.END, text)
        self.story_text.config(state=tk.DISABLED)
    
    def show_options(self, options, commands):
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        for option, command in zip(options, commands):
            button = tk.Button(self.options_frame, text=option, command=command)
            button.pack(fill=tk.X)
    
    def observe_orion(self):
        self.show_story("你選擇了觀測獵戶座。星月分享獵人傳說，宇轩補充天文知識。\n"
                        "一顆流星劃過天際，星月許願，流星墜落，她獲得魔法力量。\n")
        self.show_options(["叫救護車", "直接查看"], [self.call_ambulance, self.check_meteor])
    
    def observe_ursa_major(self):
        self.show_story("你選擇了觀測大熊座。莉娜分享觀星故事，宇轩分享冒險故事。\n"
                        "一顆流星劃過天際，星月許願，流星墜落，她獲得魔法力量。\n")
        self.show_options(["叫救護車", "直接查看"], [self.call_ambulance, self.check_meteor])
    
    def call_ambulance(self):
        self.show_story("你選擇了叫救護車。遇到救援隊，與一成員成為朋友。\n"
                        "莉娜和宇轩幫助星月控制魔法，發現一本魔法書。\n")
        self.show_options(["選擇防禦技能", "選擇攻擊技能", "選擇治療技能"], [self.learn_defense, self.learn_attack, self.learn_heal])
    
    def check_meteor(self):
        self.show_story("你選擇了直接查看。星月接觸流星，獲得魔法，宇轩目睹。\n"
                        "莉娜和宇轩幫助星月控制魔法，發現一本魔法書。\n")
        self.show_options(["選擇防禦技能", "選擇攻擊技能", "選擇治療技能"], [self.learn_defense, self.learn_attack, self.learn_heal])
    
    def learn_defense(self):
        self.show_story("你選擇了防禦技能，獲得強大防護罩。\n"
                        "宇轩透露守護者身份，表示保護她們。\n"
                        "第一章結束。\n")
        messagebox.showinfo("第一章結束", "你已完成第一章：星辰的覺醒。")
    
    def learn_attack(self):
        self.show_story("你選擇了攻擊技能，學會火焰球術。\n"
                        "宇轩透露守護者身份，表示保護她們。\n"
                        "第一章結束。\n")
        messagebox.showinfo("第一章結束", "你已完成第一章：星辰的覺醒。")
    
    def learn_heal(self):
        self.show_story("你選擇了治療技能，掌握治癒術。\n"
                        "宇轩透露守護者身份，表示保護她們。\n"
                        "第一章結束。\n")
        messagebox.showinfo("第一章結束", "你已完成第一章：星辰的覺醒。")

if __name__ == "__main__":
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()