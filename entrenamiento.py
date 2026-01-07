import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import pickle  

print("⏳ Cargando datos listos...")
df = pd.read_csv('datos_listos_para_ia.csv')


le_country = LabelEncoder()
df['Country'] = le_country.fit_transform(df['Country'])

le_education = LabelEncoder()
df['EdLevel'] = le_education.fit_transform(df['EdLevel'])


X = df[['Country', 'EdLevel', 'Experience']]
y = df['Salary']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n🧠 Entrenando el modelo (esto puede tardar unos segundos)...")

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("✅ ¡Entrenamiento completado!")

predictions = model.predict(X_test)


error = np.sqrt(mean_squared_error(y_test, predictions))
print(f"\n📊 Margen de error promedio: ${error:,.0f}")

data = {
    "model": model,
    "le_country": le_country,
    "le_education": le_education
}

with open('modelo_entrenado.pkl', 'wb') as file:
    pickle.dump(data, file)

print("\n💾 Modelo guardado en 'modelo_entrenado.pkl'")
print("¡Ya tienes una IA portátil lista para usar en tu API!")