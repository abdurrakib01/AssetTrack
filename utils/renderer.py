import contextlib
from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # separate data from response
        message = errors = None
        if data is not None:
            message = (
                data.pop("detail")
                if "detail" in data
                else (data.pop("message") if "message" in data else "")
            )
            errors = data.pop("errors") if "errors" in data else None
            data = data.pop("data") if "data" in data else data

        stats_code = renderer_context["response"].status_code
        status = "success" if 199 < stats_code < 299 else "failure"

        # modify error message
        error_msg = ""
        if errors:
            try:
                """to avoid any kind of exception during parsing error log exception used"""
                error_log = errors[0].split(":")
                field_name_list = error_log[0].split("_")
                field_name = " ".join(field_name_list).capitalize().strip()
                error_msg = (
                    f"{field_name} {error_log[1].lower().replace('this', '').strip()}"
                )
            except Exception:
                error_msg = errors[0].split(":")[1].strip()

        response_data = {
            "message": error_msg if errors else message,
            "errors": errors,
            "status": status,
            "status_code": stats_code,
            "data": data or [],
        }

        with contextlib.suppress(Exception):
            getattr(
                renderer_context.get("view").get_serializer().Meta,
                "resource_name",
                "objects",
            )

        return super(CustomJSONRenderer, self).render(
            response_data, accepted_media_type, renderer_context
        )
