# STANDARD IMPORTS
from decouple import config

# THIRD PART IMPORTS
from loguru import logger

# PROJECT IMPORTS
from src.infrastructure.mongo_db.infrastructure import MongoDBInfrastructure
# from src.domain.exceptions.exceptions import DataNotInsertedOnDatabase, NoDataWasFoundOnDatabase


class LaptopMongoRepository:
    infra = MongoDBInfrastructure
    database = config("MONGODB_DATABASE_NAME")  # set as - new_database
    collection = config("MONGODB_COLLECTION")  # set as - laptop_collection

    @classmethod
    def __get_collection(cls):
        mongo_client = cls.infra.get_client()
        try:
            database = mongo_client[cls.database]
            collection = database[cls.collection]
            return collection
        except Exception as error:
            message = (
                f"UserRepository::__get_collection::Error when trying to get collection"
            )
            logger.error(
                error=error,
                message=message
            )
            raise error

    @classmethod
    def save_laptops_on_database(
            cls,
            laptops: list
            ) -> bool:

        pass

        # collection = cls.__get_collection()
        # was_inserted = collection.insert_many(
        #     laptops
        # )
        #
        # if not type(was_inserted.inserted_ids) == list:
        #     raise DataNotInsertedOnDatabase
        #
        # return bool(was_inserted)

    @classmethod
    def find_laptops_on_database(
            cls
    ) -> list:

        pass

        # collection = cls.__get_collection()
        # laptops = collection.find({}, {'_id': 0})
        #
        # laptop_results = []
        #
        # for laptop in laptops:
        #     laptop_results.append(laptop)
        #
        # if laptop_results is None:
        #     raise NoDataWasFoundOnDatabase
        #
        # return laptop_results