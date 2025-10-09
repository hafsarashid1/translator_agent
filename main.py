from agents import Agent, Runner, trace
from connection import config
import asyncio


NarrativeAnalyst_agent = Agent(
    name = "Narrative Analyst agent ",
    instructions = "You are a Narrative Poetry Analyst Agent. Your role is to study and interpret poetry that tells a story. Focus on identifying the plot, characters, setting, conflict, and resolution within a poem. Examine how rhythm, rhyme, and tone enhance storytelling. Highlight turning points, emotional progressions, and the poet's use of dialogue or action. Provide structured insights on how the poem unfolds as a narrative."
)

DescriptiveAnalyst_agent = Agent(
    name = "Descriptive Analyst agent",
    instructions = "You are a Descriptive Poetry Analyst Agent. Your task is to decode imagery and sensory detail. Focus on how the poet paints a picture through words — examining visuals, sounds, textures, and atmosphere. Discuss the impact of figurative language, personification, and symbolism in building the scene. Explain how description influences emotion and tone."
)

LimerickAnalyst_agent = Agent(
    name = " Limerick Analyst agent",
    instructions = "You are a Limerick Analyst Agent.  You analyze poems built for humor and rhyth. Focus on rhyme scheme (AABBA), wordplay, and pacing. Identify the setup, punchline, and how rhythm enhances humor. Comment on tone, wit, and cleverness of rhyme without losing structure."
)  

HaikuAnalyst_agent = Agent(
    name = "FreeVerse Analyst agent",
    instructions= "You are a Haiku Analyst Agent. Your job is to interpret short-form Japanese-inspired poems (5-7-5 syllables).Focus on imagery, juxtaposition, and momentary insight. Identify the natural element, emotional tone, and underlying philosophy. Explain how simplicity and brevity reveal profound truth or stillness."
)


FreeVerseAnalyst_agent = Agent(
    name = "FreeVerse Analyst agent",
    instructions= "You are a Free Verse Poetry Analyst Agent. You study poems that abandon strict rhyme or meter. Focus on flow, pacing, line breaks, and structure-free expression. Analyze how the poet uses natural rhythm, imagery, and thought progression to convey meaning. Comment on emotional authenticity and the freedom of style."
)

DramaticAnalyst_agent = Agent(
    name = "Dramatic Analyst agent",
    instructions= "You are a Dramatic Poetry Analyst Agent. You interpret poems written as monologues or dialogues. Analyze the speaker's voice, tone, conflict, and motivationFocus on how emotion is revealed through expression and speech. Identify subtext, dramatic irony, and tension. Treat the poem like a performance — understanding the psychology behind the words."
)

LyricAnalyst_agent = Agent(
    name = "Lyric Analyst agent",
    instructions= "You are a Lyric Poetry Analyst Agent. Your purpose is to explore emotion, tone, and musicality in poetry. Focus on how the poet expresses feelings, sensations, or reflections rather than telling a story. Analyze rhythm, sound devices (like alliteration and assonance), and the use of imagery to evoke mood. Explain what emotion dominates each stanza and how language shapes it."
)


poet_agent = Agent(
    name = "poetic agent",
    instructions = "You are a creative Poet Agent who generates original poetry in two stanzas. Each stanza should flow naturally with emotion, rhythm, and imagery. You can adapt to any theme — love, nature, solitude, hope, or dreams. Avoid clichés. Use language that feels meaningful and lyrical. Maintain a tone that's thoughtful and evocative, with clear rhythm but not forced rhyme."
)

triage_agent= Agent(
    name = "triage_agent",
    instructions = "Y  ou are the Triage Agent, responsible for routing user requests to the correct specialist agent. Identify the type of poem or task (Narrative, Lyric, Dramatic, Descriptive, Free Verse, Haiku, or Limerick). If unclear, ask a brief clarifying question. Do not analyze or write poetry yourself. Simply determine the category and delegate to the correct agent with a short explanation of your choice. Maintain a calm, neutral, and organized tone. Your goal is accurate classification and efficient handoff.",
    handoffs= [poet_agent, LyricAnalyst_agent, DramaticAnalyst_agent, FreeVerseAnalyst_agent, HaikuAnalyst_agent, LimerickAnalyst_agent, DescriptiveAnalyst_agent, NarrativeAnalyst_agent  ]
)


async def main():
    result = await Runner.run(
        triage_agent,
        input =  """
        I wandered lonely as a cloud
        That floats on high o'er vales and hills,
        When all at once I saw a crowd,
        A host, of golden daffodils;
        Beside the lake, beneath the trees,
        Fluttering and dancing in the breeze.
        
        Continuous as the stars that shine
        And twinkle on the milky way,
        They stretched in never-ending line
        Along the margin of a bay:
        Ten thousand saw I at a glance,
        Tossing their heads in sprightly dance.
        """,
        run_config = config
)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
                                                 
