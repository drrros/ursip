import random
from abc import ABC, abstractmethod
from datetime import datetime

import pandas as pd
from openpyxl import load_workbook

from .models import CompanyData


class Parser(ABC):
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def parse_and_save(self):
        pass


class XLSParser(Parser):

    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        wb = load_workbook(self.file_path)
        ws = wb.active
        data = ws.values
        columns = [field.name for field in CompanyData.get_fields() if 'date' not in field.name]

        df = pd.DataFrame(data)
        df = df.iloc[3:, :-2]
        df.columns = columns
        return df

    def parse_and_save(self):
        df = self.read_data()
        to_create_list = []

        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 30)
        random_date = start_date + (end_date - start_date) * random.random()

        for index, row in df.iterrows():
            to_create_list.append(CompanyData(
                date=random_date.date(),
                company=row['company'],
                fact_qliq_data1=row['fact_qliq_data1'],
                fact_qliq_data2=row['fact_qliq_data2'],
                fact_qoil_data1=row['fact_qoil_data1'],
                fact_qoil_data2=row['fact_qoil_data2'],
                forecast_qliq_data1=row['forecast_qliq_data1'],
                forecast_qliq_data2=row['forecast_qliq_data2'],
                forecast_qoil_data1=row['forecast_qoil_data1'],
                forecast_qoil_data2=row['forecast_qoil_data2'],
            ))
        CompanyData.objects.bulk_create(to_create_list)
