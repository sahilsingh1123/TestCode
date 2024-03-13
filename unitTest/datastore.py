from pathlib import Path
import pandas as pd


class Datastore:
    def __init__(self) -> None:
        self.data_store_file_name = "datastore.pkl"
        self.file_dir = "./data/"
        self.storage_location = self.file_dir + self.data_store_file_name
        self.dataset = None

    def get_dataset(self):
        if self.dataset is None:
            self.get_pd_dataframe()
        return self.dataset

    def set_dataset(self, dataset):
        self.dataset = dataset

    def get_pd_dataframe(self):
        # create an empty dataframe or load
        # the existing one
        data_file_path = Path(self.file_dir + self.data_store_file_name)
        if data_file_path.is_file():
            dataframe = pd.read_pickle(data_file_path)
        else:
            # create empty dataframe with columns
            columns = self.get_all_columns_name
            dataframe = pd.DataFrame(columns=columns)
        self.set_dataset(dataframe)

    def save_dataset(self, dataframe=None):
        if dataframe is None:
            dataframe = self.get_dataset()
        dataframe.to_pickle(self.storage_location)

    def update_dataset(self, row, dataset=None):
        if not dataset:
            dataset = self.get_dataset()
        new_row_df = pd.DataFrame([row])
        updated_dataset = pd.concat([dataset, new_row_df], ignore_index=True)
        self.set_dataset(updated_dataset)

    def get_dataset_row_dict_structure(self):
        return {key: None for key in self.get_all_columns_name}

    @property
    def get_all_columns_name(self):
        columns = [
            "CaseId",
            "Alert",
            "AlertDescription",
            "Assessment",
            "Status",
            "AssessmentDetails",
            "RemediationDetails",
            "ActivityDetails",
        ]
        return columns

if __name__ == "__main__":
    ds = Datastore()
    print(dir(ds))


"""
import json


def get_json_data():
    json_file_path = 'assess_data.json'
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        return json_data


json_data = get_json_data()
rows = []
dataset = ds.get_dataset()
row = ds.get_dataset_row_dict_structure()
for j_data in json_data:
    # j_data = json.dumps(j_data)
    caseId = j_data["Ticket ID"]
    alertDesc = j_data["threat_description"]
    row["CaseId"] = caseId
    row["AlertDescription"] = alertDesc
    row["Alert"] = j_data
    row["Status"] = "Pending"
    ds.update_dataset(row)
final_dataset = ds.get_dataset()
ds.save_dataset()

"""