class Application:
    from peewee import Model
    from time import time as now
    db = None

    def __init__(self, sid, service_token, secret_key,
                 use_db=True, db_name=None, db_expires=99999999999999):
        self.id = int(sid)
        self.service_token = service_token
        self._secret_key = secret_key

        if use_db:
            self.db = self.db_connect(db_name)
            if self.tables_exist():
                self.load_from_db()

    def db_connect(self, db_name):
        db_name = db_name or "app" + str(self.sid)
        from peewee import SqliteDatabase
        return SqliteDatabase(db_name).connect()

    def load_from_db(self):
        objects = self.ObjectDB.select().where(self.ObjectDB.data_expires > self.now())
        for obj in objects:
            if obj.category == "User":
                self.user_validate(obj)
            elif obj.category == "Group":
                self.group_validate(obj)

    def tables_exist(self):
        if not self.db.table_exists(table_name=self.ObjectDB):
            self.db.create_tables([self.ObjectDB])
            return False
        return True

    class ObjectDB(Model):
        from peewee import UUIDField, CharField, BooleanField, TimestampField, TextField
        from time import time as now

        sid = UUIDField()
        token = CharField(max_length=72)
        auth = BooleanField()
        data_expires = TimestampField(default=now() + 60*60*24)
        data = TextField()
        category = CharField(max_length=8)

    def user_validate(self, user):
        pass

    def group_validate(self, group):
        pass

    def user(self):
        pass

