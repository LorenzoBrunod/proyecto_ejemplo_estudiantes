import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import shapiro

import Funciones
import Funciones as Fc
import seaborn as sns


df = pd.read_excel("datos_estudiantes_proyecto.xlsx")
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
Funciones.grafico_plot_promedio("curso","nota","bar","Promedios por curso","Promedio de notas",df,plt)
Funciones.histograma_seoborn(df,"nota",20,True,"Distribución de notas","notas","Frecuencia",sns,plt)
Funciones.categorizar_columna(df,"sexo","Sexo_categorizado","Femenino","Masculino")

Funciones.matriz_correlacion(df,"nota","ingreso_mensual","asistencia_%","sexo_codificado")


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



df["aprobado"] = df["nota"] >= 4
Funciones.modelo_clasificacion_binaria(df,["ingreso_mensual","asistencia_%","sexo_codificado"],"aprobado")

modelo, X, y_test, predicciones = Funciones.modelo_clasificacion_binaria(df,["ingreso_mensual", "asistencia_%", "sexo_codificado"],"aprobado")

Funciones.visualizar_arbol_y_confusion(modelo,X, y_test, predicciones)



grupo1 = df[df["sexo"] == "Femenino"]["nota"]
grupo2 = df[df["sexo"] == "Masculino"]["nota"]

Funciones.prueba_t(grupo1,grupo2)

Funciones.anova(df,"nota","curso")

df.to_excel(r"C:\Users\loren\Downloads\datos_estudiantes_proyecto.xlsx", index=False)