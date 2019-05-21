from db import DataBaseConnector

dbc = DataBaseConnector()


def get_operator_name(target_id: str):
    sql = f"select name from accounts where id = '{target_id}' limit 1;"
    result = dbc.execute(sql)
    return result


def get_id_list(is_option: bool):
    sql = "select id, name from accounts "
    if is_option:
        sql += "where status = 'ENABLE'"
    result = dbc.execute(sql + ';')
    return result
