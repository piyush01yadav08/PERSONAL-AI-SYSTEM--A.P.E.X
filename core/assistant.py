from abc import ABC, abstractmethod

class BaseModule(ABC):
    @abstractmethod
    def can_handle(self, query):
        pass

    @abstractmethod
    def execute(self, query, user_id):
        pass