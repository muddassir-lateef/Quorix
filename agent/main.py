from dotenv import load_dotenv


load_dotenv()

from livekit import agents
from livekit.agents import (
    AgentSession,
    Agent,
    RoomInputOptions
)
from livekit.plugins import (
    groq,
    silero,
    noise_cancellation,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are the Groq voice assistant. Be nice. Your interaction with the user will via voice.")


async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=groq.STT(),
        llm=groq.LLM(),
        tts=groq.TTS(voice="Cheyenne-PlayAI"),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )
    # if using realtime api, use the following
    #session = AgentSession(
    #    llm=openai.realtime.RealtimeModel(voice="echo"),
    #)

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # Instruct the agent to speak first
    await session.generate_reply(instructions="say hello to the user")
    
if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint,agent_name="groq-agent"))