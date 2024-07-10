import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool
# from crewai_tools import SerperDevTool
from tools.search_tools import SearchTools

# search_tool = SerperDevTool()
browser_tool = ScrapeWebsiteTool()
from langchain.llms import Ollama


# Agents
class NewsLetterAgents():         
    def job_market_researcher(self): 
        return  Agent(
                role="Chief Tech Job Market Researcher",
                goal="Gather the latest information about tech job market in USA up to {date}.",
                backstory="You're working on research about the tech job market of USA."
                        "You need to gather the latest and biggest news in last 2 weeks."
                        "Your domain focus is on tech job, such as software engineer, product manager, reseacher, etc, not general labor market."
                        "The infomation you collect will be crucial for your reader to understand the current tech job market, positive or negitive."
                        "You need to pay attention to the quality of the sources, so never forget to attach the original web page link of your information.",
                allow_delegation=False,
                verbose=True,
                tools=[SearchTools.search_internet,
                       browser_tool]
            )

    def job_market_analyst(self):
        return Agent(
            role="Chief Tech Job Market Analyst",
            goal="Write an informative analysis on current tech job market.",
            backstory="You're working on analyst about the tech job market of USA."
                    "Your co-worker will feed you the latest information they found online."
                    "Your domain focus is on tech job, such as software engineer, product manager, reseacher, etc, not general labor market."
                    "The infomation you collect will be crucial for your reader to understand the current tech job market, positive or negitive."
                    "You need to pay attention to the quality of the sources, so never forget to attach the original web page link of your information."
                    "You should have your own brief opinion instead of just simply listing links.",
            allow_delegation=False,
            tools=[browser_tool],
            verbose=True
        )

    def interest_rate_researcher(self):
        return Agent(
            role="Chief Interest Rate Researcher",
            goal="Gather the latest information about interest rate in USA up to {date}.",
            backstory="You're working on research about the updates or predictions on interest rate of USA."
                    "You need to gather the latest and biggest news in last 2 weeks."
                    "Interest rate cut can be a good thing to tech job market because it may increase the funds to the tech industry and create more job demands."
                    "You need to pay attention to the quality of the sources, so never forget to attach the original web page link of your information.",
            allow_delegation=False,
            verbose=True,
            tools=[SearchTools.search_internet,
                   browser_tool]
        )

    def interest_rate_analyst(self):
        return Agent(
            role="Chief Interest Rate Analyst",
            goal="Write an informative analysis on current interest rate and how it impacts the tech industry.",
            backstory="You're working on analyst about the interest rate news of USA."
                    "Your co-worker will feed you the latest information they found online."
                    "The infomation you collect will be crucial for your reader to understand how the fundings will flow to tech industry, positive or negitive."
                    "You need to pay attention to the quality of the sources, so never forget to attach the original web page link of your information."
                    "You should have your own brief opinion instead of just simply listing links.",
            allow_delegation=False,
            tools=[browser_tool],
            verbose=True
        )

    def newsletter_writer(self):
        return Agent(
            role='Chief Content Strategist',
            goal='Craft informative newsletter content on tech job market news',
            backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles. 
            Your co-worker will write about the tech job market news and the interest rate news.
            You will write a newsletter to tell the job seekers in tech industry what they should pay attention to or be informed.
            They already know that tech job seekers should stay informed, adaptable, and focused on in-demand skills to navigate this evolving landscape successfully. So, you do not need to repeat this kind of stuff.
            Do not forget the original web link for reference.
            You should give your own opinion rather than just list information links. 
            You transform complex concepts into compelling narratives.""",
            verbose=True,
            allow_delegation=True
        )