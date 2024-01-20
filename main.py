from agent.manager_agent import ManagerAgent
from work_principle.okr_principle import OKR_Object


class AutoMate:
    def __init__(self):
        pass
    
    
    def rule_define(self):
        # 与用户对齐任务
        while True:
            o_kr = OKR_Object("对比一下copilot和curson谁更好用，比较提示词数量、安装易用性，给出不少于100字的文章")
            ManagerAgent().optimization_Object(o_kr)
            r = input(f"最终对齐的任务是：{o_kr.raw_user_task}，一切都OK对吧？y/n")
            if r == "y":
                break



if __name__ == "__main__":
    automator = AutoMate()
    automator.rule_define()
    # print(automator.call_chatgpt_api("Hello"))
