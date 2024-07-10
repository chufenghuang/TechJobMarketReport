import os
from crewai import Crew, Process
from agents import NewsLetterAgents
from tasks import NewsLetterTasks

from IPython.display import Markdown
import datetime

def get_ordinal_suffix(day):
    if 11 <= day <= 13:
        return 'th'
    elif day % 10 == 1:
        return 'st'
    elif day % 10 == 2:
        return 'nd'
    elif day % 10 == 3:
        return 'rd'
    else:
        return 'th'

def get_formatted_date():
    today = datetime.datetime.today()
    day = today.day
    suffix = get_ordinal_suffix(day)
    formatted_date = today.strftime(f"%B {day}{suffix} %Y")
    return formatted_date

todayDate = get_formatted_date()

## You can set up your api keys below
# os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
# os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key


#Set the model you want to use
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

#The agents will be working in the crew
agents = NewsLetterAgents()

interest_rate_researcher = agents.interest_rate_researcher()
interest_rate_analyst = agents.interest_rate_analyst()
job_market_researcher = agents.job_market_researcher()
job_market_analyst = agents.job_market_analyst()
newsletter_writer = agents.newsletter_writer()

#The tasks will be assigned to the agents
tasks = NewsLetterTasks()
task_search_interest_rate_news = tasks.task_search_interest_rate_news(interest_rate_researcher)
task_write_interest_rate_report = tasks.task_write_interest_rate_report(interest_rate_analyst,task_search_interest_rate_news)
task_search_job_market = tasks.task_search_job_market(job_market_researcher)
task_write_job_market_report = tasks.task_write_job_market_report(job_market_analyst,task_search_job_market)
task_write_newsletter = tasks.task_write_newsletter(agent=newsletter_writer,interest_writting_task=task_write_interest_rate_report,tech_job_market_writting_task=task_write_job_market_report)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[interest_rate_researcher,
          interest_rate_analyst,
          job_market_researcher,
          job_market_analyst,
          newsletter_writer],
  tasks=[task_search_interest_rate_news,
         task_search_job_market,
         task_write_interest_rate_report,
         task_write_job_market_report,
         task_write_newsletter],
  verbose=2, # You can set it to 1 or 2 to different logging levels
  process = Process.sequential
)

# Get your crew to work!
print("\n######################")
result = crew.kickoff(inputs={"date": todayDate})
Markdown(result)
print("######################\n")