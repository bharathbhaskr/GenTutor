
# prompt_templates.py

def build_prompt(user_query: str, context: str, mode="default") -> str:
    if mode == "beginner":
        return f"""You're a Generative AI tutor. Explain the concept below in simple terms with analogies.

Context:
{context}

Question: {user_query}
Answer:"""

    elif mode == "developer":
        return f"""You're teaching a software developer about Generative AI. Give a technical explanation with code examples.

Context:
{context}

Question: {user_query}
Answer:"""

    elif mode == "researcher":
        return f"""You're explaining advanced Generative AI concepts to an ML researcher. Use correct terminology and cite relevant models or papers.

Context:
{context}

Question: {user_query}
Answer:"""

    else:
        return f"""Use the context below to answer the question clearly and helpfully.

Context:
{context}

Question: {user_query}
Answer:"""
