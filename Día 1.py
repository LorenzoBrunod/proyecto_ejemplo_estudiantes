import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import shapiro

import Funciones
import Funciones as Fc
import seaborn as sns

# Ahora el modelo será de clasificación:


from scipy.stats import  f_oneway



df=pd.read_excel(r"C:\Users\loren\Downloads\datos_estudiantes_proyecto.xlsx")
Funciones.mostrar_primeras_filas(df,5)
Funciones.mostrar_informacion(df)
Funciones.mostrar_descripcion(df)
Funciones.cantidad_de_columnas(df)
Funciones.cantidad_de_nulos(df)
Funciones.promedio_de_categoria("Promedio","curso","nota",df)
Funciones.desviacion_estandar("nota",df)
print("........................................................")
Funciones.cantidad_de_elementos_por_columna("nombre","nombre","estudiantes",df)

print("Cantidad de alumnos por sexo: ", Fc.contador_sexos(df))
print("........................................................")
print("........................................................")
print("Situacion de curso ",Fc.contador_estados_alumnos(df))
print("........................................................")
print("........................................................")
print("Contexto geográfico",Fc.ocntador_zona(df))

Funciones.posicion_rank("Ranking","curso","nota",df)
columord=Funciones.ordanenar_culman_menor_mayor("nota",df)
Funciones.mostrar_solo_un_grupo("curso","Inglés",columord)
Funciones.grafico_plot_promedio("curso","nota","bar","Premdios por curso","Promedio de notas",df,plt)
Funciones.histograma_seoborn(df,"nota",20,True,"Distribucion de notas","notas","Frecuecnia",sns,plt)
Funciones.categorizar_columna(df,"sexo","Sexo_categorizado","Femenino","Masculino")
# 👉 Ver correlación entre variables numéricas
Funciones.matriz_correlacion(df,"nota","ingreso_mensual","asistencia_%","sexo_codificado")

# 👉 Heatmap para visualizar la correlación
Funciones.mapa_correlacion(df,"nota","ingreso_mensual","asistencia_%","sexo_codificado",plt,sns,"coolwarm","Mapa de correalción")

Funciones.tipo_de_distribucion(Fc,shapiro,df,"nota")

Funciones.tipo_tendencia_central(df,"nota",Fc)

Funciones.tabla_de_frecuencia(sns,plt,df,"curso","premiados","Premiados por curso")
Funciones.tabla_de_frecuencia(sns,plt,df,"sexo","premiados","Relación sexo-premiados")
Funciones.grafico_violin(sns,plt,df,"sexo","nota","Distribución de notas por sexo")
Funciones.graficos_de_relaciones_cruzadas(sns,plt,df,"nota","ingreso_mensual","asistencia_%","sexo_codificado")

Funciones.grafico_circular(df,plt,"sexo","Distribución por sexo")
Funciones.graficoapiladoconporcentaje(df,sns,plt,"Distribución por sexo con porcentaje","sexo","premiados")


Analisis_Machine_Learning=Funciones.machine_simple(df[["ingreso_mensual","asistencia_%","sexo_codificado"]],df["nota"])
print("(R^2 , MAE) :\n",Analisis_Machine_Learning)
print(df[["nota", "ingreso_mensual", "asistencia_%", "sexo_codificado"]].corr())

Funciones.grafico_arbol(df,"ingreso_mensual","asistencia_%","sexo_codificado","nota")


Funciones.grafico_de_dispersion(sns,df,plt,"asistencia_%","nota","Relación entre asistencia y nota","Asistencia (%)","Nota")

df.to_excel(r"C:\Users\loren\Downloads\datos_estudiantes_proyecto.xlsx", index=False)

#En grafico de dispersion No se usa bins, porque aquí no agrupas datos en intervalos.


# Creamos una nueva variable binaria: aprobado o no
df["aprobado"] = df["nota"] >= 4
Funciones.modelo_clasificacion_binaria(df,["ingreso_mensual","asistencia_%","sexo_codificado"],"aprobado")

modelo, X, y_test, predicciones = Funciones.modelo_clasificacion_binaria(df,["ingreso_mensual", "asistencia_%", "sexo_codificado"],"aprobado")

Funciones.visualizar_arbol_y_confusion(modelo,X, y_test, predicciones)


# 1. Separamos los grupos (por ejemplo: por sexo)
grupo1 = df[df["sexo"] == "Femenino"]["nota"]
grupo2 = df[df["sexo"] == "Masculino"]["nota"]

Funciones.prueba_t(grupo1,grupo2)
# 4. ANOVA para comparar 3 o más grupos
Funciones.anova(df,"nota","curso")
