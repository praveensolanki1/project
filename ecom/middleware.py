from typing import Any


class SimpleMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response=get_response

    def __call__(self, request):
        print("before response")
        response=self.get_response(request)
        print("after callable response")
        return response

