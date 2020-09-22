def db_test():
    from peewee import SqliteDatabase, Model, CharField, TextField

    db = SqliteDatabase("test.db")

    class my_table(Model):
        key = CharField(max_length=32)
        value = TextField()

        class Meta:
            database = db

    db.connect()
    if not db.table_exists(table_name=my_table):
        db.create_tables([my_table])
    r = my_table.create(key="123", value="345")
    r.key = 478
    r.save()
    db.close()


def class_test():
    class first:
        def __init__(self):
            print('first')

    class second:
        def __init__(self):
            print('second')

    class third(second, first):
        __test = 0

        def __init__(self):
            print(1)

    b = third()
    print(third.__test)


if __name__ == "__main__":
    class_test()
