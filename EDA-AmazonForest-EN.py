import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

class EDA:
    def __init__(self,path,type,sql_query=None):
        self.df = None
        try:
            if type == 'csv':
                self.df = pd.read_csv(path)
                print(f"{'-'*5}The CSV file was successfully loaded{'-'*5}")
            elif type == 'xls' or type == 'xlsx' or type == 'xlsm' or type == 'excel':
                self.df = pd.read_excel(path)
                print(f"{'-'*5}The Excel file was successfully loaded.{'-'*5}")
            elif type == 'sqlite' and sql_query or type == "sql" and sql_query:
                connect = sqlite3.connect(path)
                self.df = pd.read_sql_query(sql_query,connect)
                print(f"{'-'*5}The SQL file was successfully loaded{'-'*5}")
            elif type == 'dataframe' or type == 'pd':
                self.df = path
            else:
                raise ValueError("The file type is not acceptable or the SQL query is missing")
        except FileNotFoundError:
            print(f"ERROR: File not found: {path}")
        except sqlite3.Error as e:
            print(f"ERROR trying to execute the SQLite query: {e}")
        except Exception as e:
            print(f"Unexpected Error trying to load the dataset: {e}")

    '''Methods'''
    def show_columns_types(self):
        print(f"\n{'-'*5}The dataset contains this information:{'-'*5}\n")
        print(self.df.info())

    def missing_values(self):
        if self.df.isnull().sum().sum() <= 0:
            print(f"\n{'-'*5}There are no null values in the dataset{'-'*5}")
        elif self.df.isnull().sum().sum() > 0:
            print("\nPercentage of null values in each column:")
            print((self.df.isnull().sum() / self.df.shape[0]) * 100)
            # Heatmap:
            plt.figure(figsize=(10, 5))
            corr = self.df.isnull()
            sns.heatmap(corr, cbar=True, cmap='cividis')
            plt.title("Null values heatmap in the dataset")
            plt.show()

    def detect_duplicates(self):
        duplicated_rows = self.df.duplicated()
        if any(duplicated_rows) is False:
            print(f"\n{'-'*5}There are no duplicated rows in the dataset.{'-'*5}")
        else:
            print(f"\n{'-'*5}There are duplicate rows in the dataset{'-'*5}\n")
            print(self.df.duplicated().value_counts())
            self.df.drop_duplicates(inplace=True)
            print(f"{'-'*5}The duplicate rows were successfully deleted{'-'*5}")

    def forest_fires_year(self):
        print(f"\nForest fires occurring since the year {self.df['year'].min()}"
              f" to the year {self.df['year'].max()}")
        print(f"Where a total of {int(self.df['number'].sum().round())}"
              f" fires occurred during the analyzed period")

    def show_first_last_row(self):
        print(f"\nFirst rows:\n{self.df.head()}\n"
              f"\nLast rows:\n{self.df.tail()}\n")

    def wildfire_season(self):
        yeargroup = self.df.groupby('year')['number'].sum()
        print(f"The year with the most fires was: {yeargroup.idxmax()}"
              f"\nThe year with the fewest fires was: {yeargroup.idxmin()}")
        fire_season = self.df[(self.df['year'] == yeargroup.idxmax())]
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=fire_season, x=fire_season['month'], y=fire_season['number'])
        plt.title(f"The year with the most fires ({yeargroup.idxmax()})")
        plt.xticks(rotation=45)
        plt.xlabel("Month")
        plt.ylabel("Number of fires")
        plt.grid(True)
        plt.show()

    def wildfire_months(self):
        wildfire_months = self.df.groupby('month')['number'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        sns.barplot(data=wildfire_months, x=wildfire_months['month'], y=wildfire_months['number'], color='orange')
        plt.xticks(rotation=45)
        plt.title(f"Fires per month for all years")
        plt.grid(axis='y')
        plt.xlabel("Month")
        plt.ylabel("Number of fires")
        plt.show()

    def fire_state(self):
        fire_states = self.df.groupby('state')['number'].sum()
        plt.figure(figsize=(10, 5))
        sns.barplot(data=fire_states)
        plt.grid(axis='y')
        plt.xticks(rotation=45)
        plt.title("The state with the most fires")
        plt.xlabel("States")
        plt.ylabel("Number of fires")
        plt.show()

    def year_register(self):
        plt.figure(figsize=(10, 5))
        sns.boxplot(data=self.df, x=self.df['year'], y=self.df['number'], color="lightgreen")
        plt.title("Box-plot of fires per year")
        plt.xlabel("Years")
        plt.ylabel("Number of fires")
        plt.xticks(rotation=45)
        plt.show()

    def most_fire_state(self):
        fire_states = self.df.groupby('state')['number'].sum()
        most_state = self.df[(self.df['state'] == fire_states.idxmax())]
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=most_state, x=most_state['month'], y=most_state['number'], legend=True,color='red')
        plt.title(f"The state with the most fires ({fire_states.idxmax()})")
        plt.xticks(rotation=45)
        plt.xlabel("Months")
        plt.ylabel("Number of fires")
        plt.grid(True)
        plt.show()

    def diference_fire_state(self):
        fire_states = self.df.groupby('state')['number'].sum()
        vs_state = self.df[(self.df['state'] == fire_states.idxmax()) | (self.df['state'] == fire_states.idxmin())].copy()
        vs_state['difference'] = vs_state.groupby(['state', 'month'])['number'].diff().abs()
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=vs_state, x=vs_state['month'], y=vs_state['number'], hue=vs_state['state'], legend=True)
        sns.lineplot(data=vs_state, x=vs_state['month'], y=vs_state['difference'], linestyle='--', color='black',
                     label='Difference')
        plt.title(
            f"Comparison of the state with the most fires ({fire_states.idxmax()}) Vs the one with the least ({fire_states.idxmin()})")
        plt.xticks(rotation=45)
        plt.xlabel("Months")
        plt.ylabel("Number of fires")
        plt.grid(axis='x')
        plt.show()
def main():
    #Datasets
    dataframe = pd.read_csv("amazon.csv", encoding="ISO-8859-1")

    #EDA:
    data = EDA(dataframe,'pd')
    data.show_first_last_row()
    data.show_columns_types()
    data.missing_values()
    data.detect_duplicates()
    data.forest_fires_year()
    data.wildfire_season()
    data.wildfire_months()
    data.fire_state()
    data.year_register()
    data.most_fire_state()
    data.diference_fire_state()
if __name__ == "__main__":
    main()