#Turns Django funtion into an API endpoint
from rest_framework.decorators import api_view
from rest_framework.response import Response    #Dict to JSON response
from rest_framework import status   #HTTP status codes

from agents.graph import build_graph
from .models import Conversation    #Imports DB model to save conversation

#POST request to ask/question endpoint
@api_view(["POST"])
def ask_question(request):
    question = request.data.get("question")

    # 1️⃣ Validate input
    if not question or not question.strip():
        return Response(
            {"error": "Question is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # 2️⃣ Build and run agent graph, multiagent flow
        graph = build_graph()

        result = graph.invoke({
            "question": question,
            "plan": "",
            "research_result": "",
            "final_answer": ""
        })

        # 3️⃣ Validate agent output if non-dict, raise error
        if not isinstance(result, dict):
            raise ValueError("Agent returned non-dict result")

        # 4️⃣ Persist conversation, write to DB
        Conversation.objects.create(
            question=question,
            answer=result.get("final_answer", "")
        )

        # 5️⃣ Always return JSON
        return Response(result, status=status.HTTP_200_OK)

    except Exception as e:
        # 6️⃣ Catch ALL errors and return JSON
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )