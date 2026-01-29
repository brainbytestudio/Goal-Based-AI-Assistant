
import asyncio
from dotenv import load_dotenv
from agents import Runner
from my_agents import strategist

load_dotenv()

async def run_project():
    # CLEAN START: Wipe the old research log at the very beginning of the run
    with open("raw_research.md", "w", encoding="utf-8") as f:
        f.write("# BrainByte Raw Research Log\nGenerated via Gemini Agent\n")

    
    # Read the external goal file
    with open("goal.txt", "r") as f:
        user_goal = f.read()

    print(f"🎬 Goal Received: {user_goal}")

    # Start the Planning Pattern Loop
    result = await Runner.run(strategist, input=user_goal, max_turns=15)

    # DEBUG: See what the result actually contains
    print(f"📊 Run Completed. Turns taken: {len(result.new_items)}")

    # Ensure final_output isn't None
    output_text = result.final_output
    
    if output_text:
        with open("final_output.md", "w", encoding="utf-8") as f:
            f.write(output_text)
        print("🚀 Script successfully generated in final_output.md")
    else:
        # If final_output is empty, save the last assistant message instead
        last_msg = [m for m in result.new_items if m.role == "assistant"][-1]
        with open("final_output.md", "w", encoding="utf-8") as f:
            f.write(str(last_msg.content))
        print("✅ Script generated from last message!")


if __name__ == "__main__":
    asyncio.run(run_project())