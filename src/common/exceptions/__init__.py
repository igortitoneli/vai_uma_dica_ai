http_status_code_to_error_code_dict = {
    200: "@VaiUmaDicaAi/ok",
    400: "@VaiUmaDicaAi/bad-request",
    401: "@VaiUmaDicaAi/unauthorized",
    402: "@VaiUmaDicaAi/payment-required",
    403: "@VaiUmaDicaAi/forbidden",
    404: "@VaiUmaDicaAi/not-found",
    405: "@VaiUmaDicaAi/method-not-allowed",
    406: "@VaiUmaDicaAi/not-acceptable",
    407: "@VaiUmaDicaAi/proxy-authentication-required",
    408: "@VaiUmaDicaAi/request-timeout",
    409: "@VaiUmaDicaAi/conflict",
    410: "@VaiUmaDicaAi/gone",
    411: "@VaiUmaDicaAi/length-required",
    412: "@VaiUmaDicaAi/precondition-failed",
    413: "@VaiUmaDicaAi/payload-too-large",
    414: "@VaiUmaDicaAi/uri-too-long",
    415: "@VaiUmaDicaAi/unsupported-media-type",
    416: "@VaiUmaDicaAi/range-not-satisfiable",
    417: "@VaiUmaDicaAi/expectation-failed",
    418: "@VaiUmaDicaAi/i-am-a-teapot",
    421: "@VaiUmaDicaAi/misdirected-request",
    422: "@VaiUmaDicaAi/unprocessable-entity",
    423: "@VaiUmaDicaAi/locked",
    424: "@VaiUmaDicaAi/failed-dependency",
    425: "@VaiUmaDicaAi/too-early",
    426: "@VaiUmaDicaAi/upgrade-required",
    428: "@VaiUmaDicaAi/precondition-required",
    429: "@VaiUmaDicaAi/too-many-requests",
    431: "@VaiUmaDicaAi/request-header-fields-too-large",
    451: "@VaiUmaDicaAi/unavailable-for-legal-reasons",
    500: "@VaiUmaDicaAi/internal-server-error",
    501: "@VaiUmaDicaAi/not-implemented",
    505: "@VaiUmaDicaAi/http-version-not-supported",
}


def http_status_code_to_error_code(status_code: int) -> str:
    error_code = http_status_code_to_error_code_dict.get(status_code)
    if error_code is not None:
        return error_code
    return http_status_code_to_error_code_dict[500]
