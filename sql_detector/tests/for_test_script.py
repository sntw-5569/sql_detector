
def test_method01(args01: list, args02: str, args03: dict):
    result = 'test_method01: ' + str(args01) + args02 + str(args03)

    return result


def test_method02(args01, args02: list):
    args01 = dbaccess(args01)
    result = 'test_method02: ' + str(args01) + str(args02)

    return result


def dbaccess(sql: str):
    return f'foo!{sql}'
