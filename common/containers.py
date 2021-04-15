
import dependency_injector.providers as providers
from data.mongo_context import MongoDbContext



class DBContext:
    """DI class for furute dev"""


    mongo_db_context = providers.Singleton(MongoDbContext)