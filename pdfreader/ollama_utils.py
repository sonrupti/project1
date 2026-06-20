from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")


def ask_llm(context, question):

    prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

If answer is not in context, say:
"Not found in provided context"
"""

    response = llm.invoke(prompt)
    return response.content


def ask_pdf(chunks, question):

    context = "\n\n".join(chunks[:4]).strip()

    if context:
        prompt = f"""
You are a helpful assistant.

If the answer is in the context → use it.
If not → answer using general knowledge.

Context:
{context}

Question:
{question}

Answer:
"""
    else:
        prompt = f"""
Answer the question using general knowledge.

Question:
{question}
"""

    return llm.invoke(prompt).content