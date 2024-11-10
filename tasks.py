from crewai import Task
from agents import researcher, writer, proof_reader
from tools import google_search_tool

# Create tasks

research_task = Task(
    description=("""
    Identify the next big trend in the topic: {topic}. Focus on identifying pros and cons and the overall narrative.
    Your final report should clearly and explicitly articulate the key points, market opportunities and potential risks
    associated with the given topic.
    """),
    expected_output="A comprehensive 3 paragraph long report on the latest information on the given topic: {topic}.",
    tools=[google_search_tool],
    agent=researcher
)

write_task = Task(
    description=("""
    Compose an insightful article on the topic: {topic}. Focus on the latest trends and how its impacting the industry.
    This article should be digestible, easy to understand, engaging and positive.
    """),
    expected_output="A 4 paragraph long article on the topic: {topic}, formatted as markdown.",
    tools=[google_search_tool],
    agent=writer,
    async_execution=False
)

proof_read_task = Task(
    description=("""
    Finalise an insightful article on the topic: {topic} which is already written by the writer. Focus on the information and how it is structured.
    It should not have any mistakes and should be very easy to digest. Make sure to put sources of the information where they come from.
    Also write 3 sources for further studying of the topic. This article should be digestible, easy to understand, engaging and positive.
    """),
    expected_output="A 4 paragraph long article on the topic: {topic}, formatted as markdown with all the relevant sources",
    tools=[google_search_tool],
    agent=proof_reader,
    async_execution=False,
    output_file="newsletter.md"
)