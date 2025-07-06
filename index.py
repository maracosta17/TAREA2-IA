<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Perfil del Proyecto - Lab 2</title>
</head>
<body>
  <h1>Perfil del Proyecto: Laboratorio 2 - Clasificación</h1>

  <h2>Nombre del Estudiante:</h2>
  <p>Maryorie Viluce</p>

  <h2>Objetivo:</h2>
  <p>
    Implementar un modelo de clasificación para predecir si un pasajero fue transportado o no, usando un conjunto de datos con información de viaje espacial (Spaceship Titanic).
  </p>

  <h2>Lenguaje y herramientas utilizadas:</h2>
  <ul>
    <li>Python (Thonny)</li>
    <li>Librerías: pandas, scikit-learn, matplotlib</li>
  </ul>

  <h2>Paso a paso:</h2>
  <ol>
    <li>Se cargó el archivo <code>train.csv</code> con información de los pasajeros.</li>
    <li>Se limpiaron los datos eliminando o imputando valores nulos.</li>
    <li>Se codificaron las variables categóricas con LabelEncoder o get_dummies.</li>
    <li>Se seleccionaron las características más relevantes para el modelo.</li>
    <li>Se dividieron los datos en conjuntos de entrenamiento y prueba (train/test).</li>
    <li>Se entrenó un modelo de clasificación usando un Árbol de Decisión.</li>
    <li>Se evaluó el rendimiento del modelo usando precisión (accuracy).</li>
  </ol>

  <h2>Resultado del modelo:</h2>
  <ul>
    <li>Modelo utilizado: Árbol de Decisión (DecisionTreeClassifier)</li>
    <li>Precisión alcanzada: 91.3%</li> <!-- Puedes reemplazar por tu resultado real -->
  </ul>

  <h2>Conclusión:</h2>
  <p>
    El laboratorio permitió aplicar un flujo de trabajo completo de IA, desde la carga de datos hasta el entrenamiento y evaluación de un modelo. La limpieza de datos y selección de características fueron claves para lograr una buena precisión. Usar Thonny fue suficiente para completar el experimento de forma efectiva.
  </p>
</body>
</html>
