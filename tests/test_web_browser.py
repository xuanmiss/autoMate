import logging
import unittest

from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.messages import HumanMessage
from langchain_core.prompts import SystemMessagePromptTemplate, PromptTemplate, MessagesPlaceholder, \
    HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI

from tools.web_browser_tool import WebBrowserTool
from utils.llm_util import LLMUtil


class TestWebBrowser:
    def test_web_browser(self):
        model = LLMUtil().llm()
        tools = [WebBrowserTool()]
        model_with_functions = model.bind_functions(tools)
        s = model_with_functions.invoke([HumanMessage(
            content="帮我查询一下这个网页的内容 https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9510051560337988929%22%7D&n_type=-1&p_from=-1")])
        print(s.additional_kwargs["function_call"])

    def test_agent(self):
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate(
                    prompt=PromptTemplate(input_variables=[], template='你是一个工作助手')),
                MessagesPlaceholder(variable_name='chat_history', optional=True),
                HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], template='{input}')),
                MessagesPlaceholder(variable_name='agent_scratchpad')
            ]
        )
        model = LLMUtil().llm()
        tools = [WebBrowserTool()]
        agent = create_openai_functions_agent(model, tools, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, return_intermediate_steps=True)
        # agent_executor.invoke({"input": "你好!你是谁"})
        agent_executor.invoke({"input": "帮我查询一下这个网页的内容 https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9510051560337988929%22%7D&n_type=-1&p_from=-1"})