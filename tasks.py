from crewai import Task
from agents import NewsLetterAgents

class NewsLetterTasks():

    def task_search_job_market(self, agent):
        return   Task(
        description="""Conduct a comprehensive search of the latest tech job market,not general labor market, news.
        Pick the top 3 popular and significant articles on this topic.
        Do not forget the original link for reference.""",
        expected_output="Your search result report in bullet points",
        agent= agent
        )
    
    def task_write_job_market_report(self, agent, prev_research_task):
        return Task(
        description="""Writet a comprehensive and informative report of the latest tech job market news.
        Identify key trends, big news, and potential industry impacts. Extract the insights from the articles.
        Newsletter is time sensitive. So, remember to mention what date your information source is up to.
        """,
        expected_output="Full analysis report in bullet points",
        agent= agent,
        dependencies=[prev_research_task]
        )
    
    def task_search_interest_rate_news(self, agent):
        return Task(
        description="""Conduct a comprehensive search of the latest interest rate news of USA.
        Analysis how that will impact the operations and hirings of the tech industry.
        Pick the top 3 popular and significant articles on this topic.
    
        Do not forget the original link for reference.""",
        expected_output="Your search result report in bullet points",
        agent=agent
        )
    
    def task_write_interest_rate_report(self, agent,prev_research_task):
        return Task(
        description="""Writet a comprehensive and informative report of the latest interest rate, in USA, news.
        Identify key trends, big news, and potential impacts on tech industry. Extract the insights from the articles.
        Newsletter is time sensitive. So, remember to mention what date your information source is up to.""",
        expected_output="Full analysis report in bullet points",
        agent=agent,
        dependencies=[prev_research_task]
        )
    
    def task_write_newsletter(self, agent,interest_writting_task, tech_job_market_writting_task):
        return Task(
        description="""Write a comprehensive and informative newsletter of the job market analysis.
        Identify key trends, big announcements, and important opinions. 
        Your most important opinion is at the title.
        Do not forget the original link for reference.
        Tell the current tech job seeker what they should pay attention to. Give a summary at the end.
        Newsletter is time sensitive. So, remember to mention what date your information source is up to.""",
        expected_output="Full newsletter which can be read in 3 minutes.",
        agent=agent,
        dependencies=[interest_writting_task, tech_job_market_writting_task]
        )

            
