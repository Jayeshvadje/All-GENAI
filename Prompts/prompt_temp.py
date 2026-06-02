from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage

template = PromptTemplate(template="""
        You are a master storyteller and a wise historian. Your job is to tell 
        the story requested by the user. Adapt your tone to match the story's mood. 
        Make the narration engaging, vivid, and easy to read.
        Please tell me the story of '{story_name}' matching a {genre} style.""" ,
                              input_variables=['story_name', 'genre'],validate_template=True)

template.save("template.json")


