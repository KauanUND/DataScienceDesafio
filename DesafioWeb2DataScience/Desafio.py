import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv"
df = pd.read_csv(url)


print(df.columns)


df = df.rename(columns={
    'deaths': 'totalDeaths',
    'totalCases': 'totalCases',
    'deaths_per_100k_inhabitants': 'deathsPer100kInhabitants',
    'totalCases_per_100k_inhabitants': 'totalCasesPer100kInhabitants',
    'deaths_by_totalCases': 'deathsByTotalCases',
    'newCases': 'newCases',
    'newDeaths': 'newDeaths'
})


print(df.head())


cidade_mais_casos = df.loc[df['totalCases'].idxmax()]
print(f"Cidade com mais casos de covid: {cidade_mais_casos['city']} com {cidade_mais_casos['totalCases']} casos")


cidade_menos_casos = df.loc[df['totalCases'].idxmin()]
print(f"Cidade com menos casos de covid: {cidade_menos_casos['city']} com {cidade_menos_casos['totalCases']} casos")


estados = df.groupby('state').sum()


estado_mais_casos = estados['totalCases'].idxmax()
print(f"Estado com mais casos de covid: {estado_mais_casos} com {estados['totalCases'].max()} casos")


estado_menos_casos = estados['totalCases'].idxmin()
print(f"Estado com menos casos de covid: {estado_menos_casos} com {estados['totalCases'].min()} casos")


cidade_mais_mortes = df.loc[df['totalDeaths'].idxmax()]
print(f"Cidade com mais mortes por covid: {cidade_mais_mortes['city']} com {cidade_mais_mortes['totalDeaths']} mortes")


cidade_menos_mortes = df.loc[df['totalDeaths'].idxmin()]
print(f"Cidade com menos mortes por covid: {cidade_menos_mortes['city']} com {cidade_menos_mortes['totalDeaths']} mortes")


estado_mais_mortes = estados['totalDeaths'].idxmax()
print(f"Estado com mais mortes por covid: {estado_mais_mortes} com {estados['totalDeaths'].max()} mortes")


estado_menos_mortes = estados['totalDeaths'].idxmin()
print(f"Estado com menos mortes por covid: {estado_menos_mortes} com {estados['totalDeaths'].min()} mortes")


total_casos_brasil = df['totalCases'].sum()
print(f"Total de casos de covid no Brasil: {total_casos_brasil}")


total_mortes_brasil = df['totalDeaths'].sum()
print(f"Total de mortes por covid no Brasil: {total_mortes_brasil}")


top5_estados_mais_mortes = estados['totalDeaths'].nlargest(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top5_estados_mais_mortes.values, y=top5_estados_mais_mortes.index)
plt.title("Top 5 estados com mais mortes por Covid")
plt.xlabel("Total de Mortes")
plt.ylabel("Estados")
plt.show()


top5_estados_menos_mortes = estados['totalDeaths'].nsmallest(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top5_estados_menos_mortes.values, y=top5_estados_menos_mortes.index)
plt.title("Top 5 estados com menos mortes por Covid")
plt.xlabel("Total de Mortes")
plt.ylabel("Estados")
plt.show()
