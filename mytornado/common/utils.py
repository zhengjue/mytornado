# _*_ coding:utf-8 _*_
import os
import sys
import hashlib
import mongoengine
import settings


def connect_db():
    mongoengine.connect(settings.DB_NAME, host=settings.DB_ADDRESS, port=settings.DB_PORT)


def md5(astring):
    return hashlib.md5(astring).hexdigest()


def make_card_id():
    import pymongo
    conn = pymongo.MongoClient("localhost", 27017)
    db = conn.office
    card_coll = db.card_id

    # card_coll.save({"card_id": 10000})
    # old method
    new_id = card_coll.find_and_modify(update={"$inc": {"card_id": 1}}, new=True).get("card_id")
    #  new_id = card_coll.find_and_modify(update={"$inc": {"card_id": 1}}, upsert=True).get("card_id")
    #  new_id = card_coll.find_and_modify(update={"$inc": {"card_id": 1}}, upsert=True)["card_id"]
    return new_id

if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    #  print md5("11111")
    make_card_id()
