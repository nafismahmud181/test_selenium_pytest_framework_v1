import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from utils.logger import logger

class AddDocumentsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_documents(self):
        logger.info("Adding documents to the profile.")
        DocumentType = self.driver.execute_script("return document.activeElement")
        self.driver.execute_script("return document.activeElement").send_keys(Keys.TAB)
        self.driver.execute_script("return document.activeElement").send_keys(Keys.TAB)
        self.driver.execute_script("return document.activeElement").send_keys(Keys.TAB)
        self.driver.execute_script("return document.activeElement").send_keys(Keys.TAB)
        self.driver.execute_script("return document.activeElement").send_keys(Keys.TAB)
        self.driver.execute_script("return document.activeElement").send_keys(Keys.TAB)
        self.driver.execute_script("return document.activeElement").send_keys(Keys.TAB)
        AddDocument = self.driver.execute_script("return document.activeElement")
        time.sleep(1)
        AddDocumentCount = self.driver.execute_script("return document.activeElement")

        # Excell Implementation
        df = pd.read_excel("utils/documents_data.xlsx", sheet_name="Sheet3")
        df.columns = df.columns.str.strip()
        df = df.fillna("")
        documents_data = df.to_dict("records")

        if len(documents_data) > 1:
            AddDocumentCount.send_keys(str(len(documents_data) - 1))
            AddDocument.send_keys(Keys.RETURN)
        print(documents_data)
        for document in documents_data:
            DocumentType.send_keys(document['document_type'])
            DocumentType.send_keys(Keys.RETURN)
            time.sleep(1)
            DocumentType.send_keys(Keys.TAB)

            ContentLocation = self.driver.execute_script("return document.activeElement")
            ContentLocation.send_keys(document['content_location'])
            ContentLocation.send_keys(Keys.RETURN)
            time.sleep(1)
            ContentLocation.send_keys(Keys.TAB)

            NameMatching = self.driver.execute_script("return document.activeElement")
            NameMatching.send_keys(document['name_matching'])
            NameMatching.send_keys(Keys.RETURN)
            time.sleep(1)
            NameMatching.send_keys(Keys.TAB)

            if document.get('name_matching_text'):
                NameMatchingText = self.driver.execute_script("return document.activeElement")
                NameMatchingText.send_keys(document['name_matching_text'])
                time.sleep(1)
                NameMatchingText.send_keys(Keys.TAB)

            Category = self.driver.execute_script("return document.activeElement")
            Category.send_keys(document['category'])
            time.sleep(5)
            Category.send_keys(Keys.RETURN)
            time.sleep(1)
            Category.send_keys(Keys.TAB)

            Language = self.driver.execute_script("return document.activeElement")
            Language.send_keys(document['language'])
            Language.send_keys(Keys.RETURN)
            time.sleep(1)
            Language.send_keys(Keys.TAB)

            OCR = self.driver.execute_script("return document.activeElement")
            OCR.send_keys(document['ocr'])
            OCR.send_keys(Keys.RETURN)
            time.sleep(1)
            OCR.send_keys(Keys.TAB)
            DocumentType = self.driver.execute_script("return document.activeElement")

        logger.info("Document addition completed.")