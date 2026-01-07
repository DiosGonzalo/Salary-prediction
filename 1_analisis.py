import pandas as pd

print("⏳ Cargando datos limpios...")
df = pd.read_csv('salary_clean.csv')

# --- MISIÓN 1: REDUCIR PAÍSES (Lógica de Cutoff) ---
# Queremos eliminar países con pocos datos porque confunden a la IA.

# 1. Calculamos cuántos datos hay por país
conteo_paises = df['Country'].value_counts()
print("\n--- Top 5 Países antes de filtrar ---")
print(conteo_paises.head())

# 2. Definimos el "Corte" (Cutoff)
# Si un país tiene menos de 100 programadores, lo borramos.
umbral = 100 

# 3. Filtramos
# Nos quedamos con los nombres de los países que superan el umbral
paises_grandes = conteo_paises[conteo_paises >= umbral].index

# 4. Aplicamos el filtro al DataFrame
# "Quédate solo con las filas cuyo país esté EN (isin) la lista de grandes"
df = df[df['Country'].isin(paises_grandes)]

print(f"\n📉 Después de filtrar países pequeños nos quedan: {df.shape[0]} filas.")


# --- MISIÓN 2: LIMPIAR ESTUDIOS (Lógica de Mapeo) ---
# Vamos a convertir frases largas en 4 categorías simples.

def limpiar_estudios(texto):
    # Esta función recibe un texto y devuelve una categoría simple
    if 'Bachelor' in texto:
        return 'Bachelor'
    if 'Master' in texto:
        return 'Master'
    if 'Professional' in texto or 'Other doctoral' in texto:
        return 'Post grad'
    return 'Less than a Bachelors'

# Aplicamos la función a toda la columna EdLevel
df['EdLevel'] = df['EdLevel'].apply(limpiar_estudios)

print("\n--- Categorías de Estudios resultantes ---")
print(df['EdLevel'].value_counts())


# --- MISIÓN 3: SIMPLIFICAR EXPERIENCIA (Opcional pero recomendado) ---
# A veces la experiencia tiene demasiados decimales. Redondeamos.
df = df.reset_index(drop=True) # Reseteamos el índice para que quede limpio

# --- GUARDADO FINAL ---
# Este archivo es ORO PURO. Listo para entrenar.
df.to_csv('datos_listos_para_ia.csv', index=False)
print("\n✅ ¡Todo listo! Guardado como 'datos_listos_para_ia.csv'")