from typing import Any, Iterable, Optional
from project.category import Category
from project.document import Document
from project.topic import Topic

class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)
        return self
    
    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)
        return self
    
    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)
        return self
    
    def get_item(self, item_id: int, item_collection: Iterable[Any]) -> Optional[Any]:
        return next((item for item in item_collection if item.id == item_id), None)
    
    def edit_category(self, category_id: int, new_name: str):
        category = self.get_item(category_id, self.categories)
        if category:
            category.name = new_name
        return self
    
    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.get_item(topic_id, self.topics)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder
        return self
    
    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_item(document_id, self.documents)
        if document:
            document.file_name = new_file_name
        return self
    
    def delete_category(self, category_id: int):
        category = self.get_item(category_id, self.categories)
        if category:
            self.categories.remove(category)
            del category
        return self
    
    def delete_topic(self, topic_id: int):
        topic = self.get_item(topic_id, self.topics)
        if topic:
            self.topics.remove(topic)
            del topic
        return self
    
    def delete_document(self, document_id: int):
        document = self.get_item(document_id, self.documents)
        if document:
            self.documents.remove(document)
            del document
        return self
        
    def get_document(self, document_id: int) -> Document | None:
        return self.get_item(document_id, self.documents)
    
    def __repr__(self) -> str:
        return "\n".join(document.__repr__() for document in self.documents)
