from pymysql import connect


def create_db_response(db_config, sql):
    result = []
    try:
        with connect(**db_config) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)

            schema = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                result.append(dict(zip(schema, row)))

            connection.commit()
            cursor.close()
    except Exception:
        pass

    return result


def select(db_config, sql, limit=10):
    if not db_config:
        raise ValueError("db_config is not provided")
    db_output = create_db_response(db_config, sql)
    return db_output[:limit]
