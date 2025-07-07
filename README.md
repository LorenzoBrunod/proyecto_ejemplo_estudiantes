# Ejemplo de Análisis Exploratorio de Datos 

## Análisis Rendimiento Estudiantil con Python

## Introducción

El rendimiento académico de los estudiantes es un tema central en la investigación educativa. Este proyecto aplica herramientas de ciencia de datos para identificar patrones relevantes que influyen en las calificaciones de los alumnos, considerando variables académicas (nota, asistencia) y sociales (ingreso mensual, sexo, zona geográfica). A través de análisis exploratorios, estadísticos y predictivos, se busca entender no solo el desempeño general, sino también sus determinantes, con el objetivo de facilitar decisiones pedagógicas basadas en datos.

## Objetivos del Proyecto

1_Analizar patrones y correlaciones en el rendimiento estudiantil.
2_Detectar diferencias significativas por grupo (curso, sexo, zona).
3_Predecir el rendimiento con modelos estadísticos interpretables.
4_Comunicar hallazgos de forma visual y profesional.

## Limpieza y Transformaciones de Datos

Se aplicaron los siguientes pasos antes del análisis:

### Revisión de nulos ( df.isnull().sum() ): no se encontraron vacíos relevantes.
1_Tipificación: "nota", "ingreso_mensual", "asistencia_%" como numéricos; "sexo", "curso", "zona" como categóricos.
2_Codificación: se creó la variable "sexo_codificado" (1 = femenino, 0 = masculino).
3_Variable "aprobado": booleana basada en si la nota es mayor o igual a 4.0.
4_Creación de "Ranking": ordena alumnos dentro de su curso según nota.
5_Clasificación de premiados: 1er, 2do, 3er lugar según ranking.
6_Limpieza textual de variables categóricas (estandarización de texto).

##  Análisis de Distribución

- **Shapiro-Wilk test**: p > 0.05 → la variable "nota" sigue una distribución normal.
- **Skewness**: cercano a 0 → distribución simétrica.

**Se concluye que es válido aplicar media como medida de tendencia central, y usar pruebas paramétricas como ANOVA, t-test, regresión y correlación de Pearson**


##  Justificación Técnica de Métodos Utilizados

| Método                           | Justificación                                                  |
|----------------------------------|----------------------------------------------------------------|
| .info(), .describe()             | Comprensión general del dataset.                               |
| Histograma + KDE                 | Verificar forma de la distribución.                            |
| Shapiro-Wilk                     | Confirmar normalidad.                                          |
| Skewness                         | Validar uso de media.                                          |
| t-test                           | Comparar promedios entre sexos.                                |
| ANOVA                            | Comparar notas entre cursos.                                   |
| Pearson                          | Medir correlaciones.                                           |
| Regresión lineal                 | Estimar nota desde ingreso, asistencia y sexo.                 |
| Árbol de decisión (regresión)    | Segmentar con reglas claras.                                   |
| Árbol de clasificación + matriz  | Predecir probabilidad de aprobar.                              |

---

## Visualizaciones y su Interpretación

### 1. Promedios por Curso  
![Promedios por curso](Graficos/Promedios%20por%20curso.png)
**Interpretación**: Este gráfico muestra que los cursos de Inglés y Lenguaje tienen promedios superiores, mientras que Matemáticas presenta una media más baja. Esto puede indicar diferencias en dificultad o metodologías docentes.

---

### 2. Histograma de Notas  
![Distribución de notas](Graficos/Distribución%20de%20notas%20%28histograma%20con%20KDE%29.png)  
**Interpretación**: La curva tiene forma aproximadamente normal, centrada entre 4.5 y 5.5. Esto respalda el uso de métodos estadísticos paramétricos como la regresión o ANOVA. No se observan sesgos extremos.

---

### 3. Distribución por Sexo  
![Distribución por sexo](Graficos/Gráfico%20circular%20%28distribución%20por%20sexo%29.png)
**Interpretación**: La proporción entre hombres y mujeres está balanceada, lo que permite realizar comparaciones por sexo sin riesgo de sesgo muestral.

---

### 4. Distribución por Sexo con Porcentaje  
![Distribución sexo-premios](Graficos/Gráfico%20apilado%20con%20porcentaje%20por%20sexo%20y%20premios.png)
**Interpretación**: La cantidad de premiados es proporcional entre hombres y mujeres, lo cual sugiere que no existen diferencias significativas de rendimiento por género.

---

### 5. Mapa de Correlación  
![Mapa de correlación](Graficos/Mapa%20de%20correlación%20%28heatmap%29.png) 
**Interpretación**: Se observa una correlación positiva entre `nota` y `asistencia_%`, y una leve correlación con `ingreso_mensual`. Esto indica que una mayor asistencia está asociada con mejor rendimiento académico.

---

### 6. Pairplot de Variables  
![Pairplot](Graficos/Matriz%20de%20dispersión%20%28pairplot%29.png)  
**Interpretación**: Este gráfico muestra las relaciones cruzadas entre todas las variables numéricas. Destaca la ligera linealidad entre `nota` y `asistencia_%`. No se observan agrupamientos atípicos o no lineales.

---

### 7. Premiados por Curso  
![Premiados por curso](Graficos/Premiados%20por%20curso%20%28categorías%29.png)
**Interpretación**: Inglés y Lenguaje tienen la mayor cantidad de premiados. Esto está alineado con los promedios por curso y puede reflejar políticas internas o enfoque pedagógico.

---

### 8. Premiados por Sexo  
![Premiados por sexo](Graficos/Relación%20sexo-premiados.png)
**Interpretación**: La cantidad de premiados por género se mantiene pareja. Confirma que no hay un sesgo de género en la entrega de reconocimientos.

---

### 9. Violinplot de Notas por Sexo  
![Violinplot notas por sexo](Graficos/Gráfico%20de%20violín%20%28distribución%20notas%20por%20sexo%29.png)  
**Interpretación**: La distribución de notas es similar entre hombres y mujeres. Se valida que las medias son comparables. Este resultado es consistente con el t-test aplicado, que no encontró diferencias estadísticamente significativas.

---

### 10. Dispersión Asistencia vs Nota  
![Dispersión asistencia-nota](Graficos/Gráfico%20de%20dispersión_asistencia%20vs%20nota.png) 
**Interpretación**: Muestra que los estudiantes con mayor asistencia tienden a tener mejor rendimiento, aunque la relación no es estrictamente lineal. Sugiere que otros factores también influyen.

---

### 11. Árbol de Decisión (Regresión)  
![Árbol de decisión](Graficos/Árbol%20de%20decisión%20para%20regresión.png)
**Interpretación**: Modelo predictivo que permite estimar la nota basada en ingreso, asistencia y sexo. Los nodos del árbol explican qué combinaciones de variables conducen a un mejor o peor rendimiento. Es un modelo interpretable y útil para toma de decisiones pedagógicas.

---

##  Análisis Estadístico Aplicado

- **t-test**: se compararon notas entre sexos → no hay diferencias estadísticamente significativas.
- **ANOVA**: comparó notas entre cursos → se encontraron diferencias significativas, justificando el análisis por materia.
- **Correlación de Pearson**: `nota` tiene correlación positiva con `asistencia_%` y `ingreso_mensual`.
- **Regresión lineal**: buen ajuste al predecir `nota` con variables numéricas (R² > 0.6).
- **Clasificación binaria**: se predijo si un alumno aprueba usando un árbol de decisión. La matriz de confusión mostró buena precisión.
- **Ranking y premiación**: la columna `Ranking` permitió identificar a los mejores alumnos por curso de forma objetiva.

---

# Conclusiones

- La nota tiene distribución normal, lo que habilita métodos estadísticos clásicos.
- La asistencia es el principal predictor del rendimiento.
- No existen diferencias significativas por género.
- Los cursos muestran diferencias en promedio y premiación.
- La variable `Ranking` aporta valor en la segmentación de alto rendimiento.
- Modelos como regresión lineal y árboles permiten explicar y predecir el desempeño académico.

---

## 🛠 Herramientas Usadas

- Python 3.x  
- pandas  
- matplotlib  
- seaborn  
- scikit-learn  
- scipy

---

##  Ejecución del Proyecto

Sigue estos pasos para ejecutar el análisis:

```bash
git clone https://github.com/tu_usuario/proyecto_rendimiento_estudiantil.git
cd proyecto_rendimiento_estudiantil
pip install pandas matplotlib seaborn scikit-learn scipy openpyxl
python "Dia 1.py"

## Mis datos

Proyecto elaborado para un portafolio profesional a modo de ejemplo en ciencia de datos aplicada a educación.

- 📬lorenzoschiappacase@gmail.com  
- 📎https://www.linkedin.com/in/lorenzo-brunod-schiappacase-9a10191b9


