import random
from .redis import redis_client


def weighted_pick_component(component_type, component_map: map):
    average_scores = {}
    values = redis_client.hgetall(f"{component_type}_score_values")
    counts = redis_client.hgetall(f"{component_type}_score_count")

    for name in component_map.keys():
        score = values.get(name)
        count = counts.get(name)
        average_score = score / count
        average_scores[name] = average_score

    average_score_total = sum(average_scores.values())
    random_value = random.uniform(0, average_score_total)
    cumulative = 0
    for name, score in average_scores.items():
        if random_value < cumulative + score:
            return name


def score_conversation(
    conversation_id: str, score: float, llm: str, retriever: str, memory: str
) -> None:
    score = min(max(score, 0), 1)
    redis_client.hincrby("llm_score_values", llm, score)
    redis_client.hincrby("llm_score_count", llm, 1)
    redis_client.hincrby("retriever_score_values", retriever, score)
    redis_client.hincrby("retriever_score_count", retriever, 1)
    redis_client.hincrby("memory_score_values", memory, score)
    redis_client.hincrby("memory_score_count", memory, 1)


def get_scores():
    """
    Retrieves and organizes scores from the langfuse client for different component types and names.
    The scores are categorized and aggregated in a nested dictionary format where the outer key represents
    the component type and the inner key represents the component name, with each score listed in an array.

    The function accesses the langfuse client's score endpoint to obtain scores.
    If the score name cannot be parsed into JSON, it is skipped.

    :return: A dictionary organized by component type and name, containing arrays of scores.

    Example:

        {
            'llm': {
                'chatopenai-3.5-turbo': [score1, score2],
                'chatopenai-4': [score3, score4]
            },
            'retriever': { 'pinecone_store': [score5, score6] },
            'memory': { 'persist_memory': [score7, score8] }
        }
    """

    scores = {"llm": {}, "retriever": {}, "memory": {}}

    for component_type in scores.keys:
        values = redis_client.hgetall(f"{component_type}_score_values")
        counts = redis_client.hgetall(f"{component_type}_score_count")
        for name in values.keys():
            score = values.get(name)
            count = counts.get(name)
            average_score = score / count
            score[component_type][name] = average_score

    return scores
