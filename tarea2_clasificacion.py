# tarea2_clasificacion.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# 1. Cargar los datos
df = pd.read_csv("train.csv")

# 2. Preprocesamiento
# Llenar valores nulos
df.fillna(method="ffill", inplace=True)

# Eliminar columnas que no sirven directamente (como nombres)
df.drop(columns=["Name", "Cabin", "PassengerId"], inplace=True)

# Codificar variables categóricas
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object' or df[col].dtype == 'bool':
        df[col] = le.fit_transform(df[col].astype(str))

# 3. Separar variables
X = df.drop("Transported", axis=1)
y = df["Transported"]

# 4. Separar en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Entrenar modelo
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 6. Evaluar
y_pred = clf.predict(X_test)
print("🔍 Precisión:", accuracy_score(y_test, y_pred))
print("📋 Reporte:")
print(classification_report(y_test, y_pred))
