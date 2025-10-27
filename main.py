import os
from typing import TypedDict, Optional, Annotated
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from dotenv import load_dotenv
from langsmith import traceable
from agent.tools import extract_text  # Adjust import if needed

load_dotenv()

# ---- Define Agent State ----
class AgentState(TypedDict):
    input_file: Optional[str]
    messages: Annotated[list[AnyMessage], add_messages]

# ---- Initialize LLM + Tools ----
tools = [extract_text]
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)

# ---- Assistant Node ----
def assistant(state: AgentState):
    textual_description_of_tools = """
    def extract_text(img_path: str) -> str:
        Extracts text from an image specified by its file path.
        Encodes and sends the image to Gemini Vision model for text extraction.
    """
    image = state["input_file"]
    sys_msg = SystemMessage(content=f"""
    You are a helpful assistant. You can analyze documents with provided tools:\n{textual_description_of_tools}.
    You have access to some optional images. Currently loaded image: {image}
    """)

    return {
        "messages": [llm_with_tools.invoke([sys_msg] + state["messages"])],
        "input_file": state["input_file"]
    }

# ---- Build Graph ----
builder = StateGraph(AgentState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")
react_graph = builder.compile()

# ---- Traceable Graph Runner ----
@traceable(name="image_text_extraction_pipeline")
def run_pipeline(image_path: str, prompt: str = "Please transcribe the provided image."):
    messages = [HumanMessage(content=prompt)]
    result = react_graph.invoke({
        "messages": messages,
        "input_file": image_path
    })
    return result


# ---- Entry Point ----
if __name__ == "__main__":
    result = run_pipeline("Images/chocolate_cake_recipe.png")

    for msg in result["messages"]:
        if msg.__class__.__name__ == "ToolMessage" and hasattr(msg, 'content') and msg.content.strip():
            print("Transcribed text:\n")
            print(msg.content)
            break