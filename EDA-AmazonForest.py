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
                print(f"{'-'*5}El archivo CSV fue cargado exitosamente{'-'*5}")
            elif type == 'xls' or type == 'xlsx' or type == 'xlsm' or type == 'excel':
                self.df = pd.read_excel(path)
                print(f"{'-'*5}El archivo Excel fue cargado exitosamente{'-'*5}")
            elif type == 'sqlite' and sql_query or type == "sql" and sql_query:
                connect = sqlite3.connect(path)
                self.df = pd.read_sql_query(sql_query,connect)
                print(f"{'-'*5}El archivo SQL fue cargado exitosamente{'-'*5}")
            elif type == 'dataframe' or type == 'pd':
                self.df = path
            else:
                raise ValueError("Tipo de archivo no admisible o consulta SQL faltante")
        except FileNotFoundError:
            print(f"ERROR: Archivo no encontrado: {path}")
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta en SQLite: {e}")
        except Exception as e:
            print(f"Error inesperado al cargar el dataset: {e}")

    '''Metodos'''
    def show_columns_types(self):
        print(f"\n{'-'*5}El Dataset posee esta información:{'-'*5}\n")
        print(self.df.info())

    def missing_values(self):
        if self.df.isnull().sum().sum() <= 0:
            print(f"\n{'-'*5}En el dataset no se presentan valores nulos{'-'*5}")
        elif self.df.isnull().sum().sum() > 0:
            print("\nPorcentaje de valores nulos en cada columna:")
            print((self.df.isnull().sum() / self.df.shape[0]) * 100)
            #Grafico Heatmap:
            plt.figure(figsize=(10, 5))
            corr = self.df.isnull()
            sns.heatmap(corr, cbar=True, cmap='cividis')
            plt.title("Heatmap de los valores nulos en el Dataset")
            plt.show()

    def detect_duplicates(self):
        duplicated_rows = self.df.duplicated()
        if any(duplicated_rows) is False:
            print(f"\n{'-'*5}No existen filas duplicadas en el Dataset{'-'*5}")
        else:
            print(f"\n{'-'*5}Existen filas duplicadas en el dataset{'-'*5}\n")
            print(self.df.duplicated().value_counts())
            self.df.drop_duplicates(inplace=True)
            print(f"{'-'*5}Las filas duplicadas fueron borradas con éxito{'-'*5}")

    def forest_fires_year(self):
        print(f"\nSe registraron los incendios forestales ocurridos desde el año {self.df['year'].min()}"
              f" hasta el año {self.df['year'].max()}")
        print(f"Donde ocurrieron un total de {int(self.df['number'].sum().round())}"
              f" incendios en el periodo analizado")

    def show_first_last_row(self):
        print(f"\nPrimeras columnas:\n{self.df.head()}\n"
              f"\nÚltimas columnas:\n{self.df.tail()}\n")

    def wildfire_season(self):
        yeargroup = self.df.groupby('year')['number'].sum()
        print(f"El año que más incendios tuvo fue: {yeargroup.idxmax()}"
              f"\nEl año que menos incendios tuvo fue: {yeargroup.idxmin()}")
        fire_season = self.df[(self.df['year'] == yeargroup.idxmax())]
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=fire_season, x=fire_season['month'], y=fire_season['number'])
        plt.title(f"Año que más incendios tuvo ({yeargroup.idxmax()})")
        plt.xticks(rotation=45)
        plt.xlabel("Meses")
        plt.ylabel("Número de incendios")
        plt.grid(True)
        plt.show()

    def wildfire_months(self):
        wildfire_months = self.df.groupby('month')['number'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        sns.barplot(data=wildfire_months, x=wildfire_months['month'], y=wildfire_months['number'], color='orange')
        plt.xticks(rotation=45)
        plt.title(f"Incendios de cada mes para todos los años")
        plt.grid(axis='y')
        plt.xlabel("Meses")
        plt.ylabel("Número de incendios")
        plt.show()

    def fire_state(self):
        fire_states = self.df.groupby('state')['number'].sum()
        plt.figure(figsize=(10, 5))
        sns.barplot(data=fire_states)
        plt.grid(axis='y')
        plt.xticks(rotation=45)
        plt.title("Estado con más incendios")
        plt.xlabel("Estados")
        plt.ylabel("Número de incendios")
        plt.show()

    def year_register(self):
        plt.figure(figsize=(10, 5))
        sns.boxplot(data=self.df, x=self.df['year'], y=self.df['number'], color="lightgreen")
        plt.title("Box-plot de incendios por año")
        plt.xlabel("Años")
        plt.ylabel("Número de incendios")
        plt.xticks(rotation=45)
        plt.show()

    def most_fire_state(self):
        fire_states = self.df.groupby('state')['number'].sum()
        most_state = self.df[(self.df['state'] == fire_states.idxmax())]
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=most_state, x=most_state['month'], y=most_state['number'], legend=True,color='red')
        plt.title(f"Estado que más incendios tuvo ({fire_states.idxmax()})")
        plt.xticks(rotation=45)
        plt.xlabel("Meses")
        plt.ylabel("Número de incendios")
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
            f"Comparacion del estado con más incendios ({fire_states.idxmax()}) Vs el de menos ({fire_states.idxmin()})")
        plt.xticks(rotation=45)
        plt.xlabel("Meses")
        plt.ylabel("Número de incendios")
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