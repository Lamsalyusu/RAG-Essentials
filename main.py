from dotenv import load_dotenv
# import metadata.reps
from importlib.metadata import version
load_dotenv()
from langchain_core import __version__ as core_version
# from langgraph import __version__ as lg_version
from langchain import __version__ as lg_version
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq 


print(f"langchain - core version as {core_version}");
print(f"langgraph version {lg_version}")

def main() -> str:
    # llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)
    # resp = llm.invoke("Say 'setup complete! in one word")
    # print(f"Response from ChatOpenAI {resp}")

    # llm_a = ChatAnthropic(model_name="claude-sonner-4-5-20250929",temperature=0)
    # resp_A = llm_a.invoke("Say setup complete in one word!")
    # print(f"Response from anthropic {resp_A}")

    llm_groq = ChatGroq(
        model = "llama-3.3-70b-versatile",
        temperature=0
    )
    response = llm_groq.invoke("Say 'setup complete' in one word")
    print(f"Response from Groq: {response.content}")


if __name__ == "__main__":
    main()
