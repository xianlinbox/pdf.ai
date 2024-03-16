import random
from langchain.chat_models import ChatOpenAI
from app.chat.models import ChatArgs
from app.web.api import get_conversation_components, set_conversation_components
from app.chat.vector_store.pinecone import retrievers_map
from app.chat.memories import memories_map
from app.chat.llms.open_ai import llms_map
from app.chat.streaming.conversational_stream_chain import CoversationalStreamableChain
from .score import weighted_pick_component


def select_component(type, component_map: map, chat_args: ChatArgs):
    components_in_use = get_conversation_components(chat_args.conversation_id)
    component_name = components_in_use[type]
    if component_name is None:
        component_picked_name = weighted_pick_component(type, component_map)
        return component_picked_name, component_map[component_picked_name](chat_args)
    return component_name, component_map[component_name](chat_args)


def build_chat(chat_args: ChatArgs):

    retriever_name, retriever = select_component(
        type="retriever", component_map=retrievers_map, chat_args=chat_args
    )
    memory_name, memory = select_component(
        type="memory", component_map=memories_map, chat_args=chat_args
    )
    llm_name, llm = select_component(
        type="llm", component_map=llms_map, chat_args=chat_args
    )

    set_conversation_components(
        conversation_id=chat_args.conversation_id,
        llm=llm_name,
        retriever=retriever_name,
        memory=memory_name,
    )
    condense_llm = ChatOpenAI(streaming=False)
    return CoversationalStreamableChain.from_llm(
        memory=memory,
        retriever=retriever,
        llm=llm,
        condense_question_llm=condense_llm,
        meta_data=chat_args.metadata,
    )
