# CATIAService主类，负责连接和基础对象管理
import pycatia
import logging
from dotenv import load_dotenv


class CATIAService:
    def __init__(self):
        self.catia = None
        self.documents = None
        self.part_document = None
        self.part = None
        self.hybrid_bodies = None
        self.parameters = None
        self.sketches = None
        self.bodies = None
        self.measure = None
        self.analysis = None
        self.drawing = None
        self.product = None
        self.system = None
        load_dotenv()

    def connect(self):
        try:
            self.catia = pycatia.catia_application()
            self.documents = self.catia.documents
            self.system = self.catia.system
            return True
        except Exception as e:
            logging.error(f"连接CATIA失败: {str(e)}")
            return False

    def open_document(self, file_path: str) -> bool:
        try:
            self.part_document = self.documents.open(file_path)
            self._initialize_document_objects()
            return True
        except Exception as e:
            logging.error(f"打开文档失败: {str(e)}")
            return False

    def _initialize_document_objects(self):
        if self.part_document:
            if self.part_document.type == "Part":
                self.part = self.part_document.part
                self.hybrid_bodies = self.part.hybrid_bodies
                self.parameters = self.part.parameters
                self.sketches = self.part.sketches
                self.bodies = self.part.bodies
                self.measure = self.part.measure
                self.analysis = self.part.analysis
            elif self.part_document.type == "Product":
                self.product = self.part_document.product
            elif self.part_document.type == "Drawing":
                self.drawing = self.part_document.drawing
