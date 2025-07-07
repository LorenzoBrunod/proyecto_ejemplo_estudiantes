
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


def contador_sexos(lista):
    contador={"Masculino":0,"Femenino":0}
    for _,x in lista.iterrows():
       valor =str(x["sexo"])
       if valor in contador:
            contador[valor]+=1
    return contador

def contador_estados_alumnos(lista):
    contador={"False":0,"True":0}
    for _,x in lista.iterrows():
        value=str(x["repitente"])
        if value in contador:
            contador[value]+=1
    return contador

def ocntador_zona(lista):
    contador={"Rural":0,"Urbana":0}
    for _,x in lista.iterrows():
        vals=str(x["zona"])
        if vals in contador:
            contador[vals]+=1
    return contador


def posicion(n):
    if n==1.0:
        return "primer lugar"
    elif n==2.0:
        return "Segundo lugar"
    elif n==3.0:
        return "Tercer lugar"
    else:
        return "No premiado"


def compartamientodis(p):
     if p >0.5:
         return " Tiene un compartamiento normal\nPuedes ocupar los siguiente metodos paramtricos metodos paramétricos :\nt-test (Student o Welch) : Comparar promedios entre 2 grupos\nANOVA (análisis de varianza) : Comparar promedios entre >2 grupos\nCorrelación de Pearson : Ver relación entre dos variables numéricas\nRegresión lineal: Ajustar una línea o modelo\nt de una muestra : Comparar una muestra con un valor esperado\nF-test o Levene: Comparar varianzas"
     elif p > 0.10:
         return " ◉Normalidad muy probable\nPuedes ocupar los siguiente metodos paramtricos metodos paramétricos :\n\n◉t-test (Student o Welch) : Comparar promedios entre 2 grupos\n◉ANOVA (análisis de varianza) : Comparar promedios entre >2 grupos\n◉Correlación de Pearson : Ver relación entre dos variables numéricas\n◉Regresión lineal: Ajustar una línea o modelo\n◉t de una muestra : Comparar una muestra con un valor esperado\n◉F-test o Levene: Comparar varianzas"
     elif 0.05 < p <= 0.10:
         return "Podría ser normal, pero con dudas"
     elif  0.01 < p <=0.05:
         return "Considera métodos no paramétricos"
     elif p <= 0.01:
         return "Usa análisis no paramétricos, o transforma los datos"


def medianaomedia(skew):

    if abs(skew) < 0.5:
     return "Distribución aproximadamente simétrica → usar media"
    else:
     return "Distribución sesgada → usar mediana"

def graficoapiladoconporcentaje(df,sns,plt,titulo,x,hue):
    ax = sns.countplot(data=df, x=x, hue=hue)
    total = len(df)
    for p in ax.patches:
     count = p.get_height()
     porcentaje = 100 * count / total
     ax.annotate(f'{porcentaje:.1f}%',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom')
    plt.title(titulo)
    return plt.show()

def cantidad_de_columnas(df):
    for col in df.select_dtypes(include=object).columns:
     print(f"{col}{df[col].unique()}")
    return

def mostrar_primeras_filas(df,n):
    print(df.head(n))
    print(".......................................................................")

def mostrar_descripcion(df):
    print(df.describe())
    print(".......................................................................")

def mostrar_informacion(df):
    print(df.info())
    print(".......................................................................")

def cantidad_de_nulos(df):
    print("La cantidad de nulos :",df.isnull().sum())


def promedio_de_categoria(s,d,f,df):
    print("promedio",s,df.groupby(d)[f].mean())


def desviacion_estandar(columna_numerica,df):
    print("La desviacion estandar de ",columna_numerica,"es",df[columna_numerica].std())
    print(".......................................................................")


def cantidad_de_elementos_por_columna(name_columna,encabezado,elemento,df):
    print("En la columna ",name_columna,"hay",df[encabezado].count(),elemento)



def machine_simple(variables_predictoras,variable_a_predecir):
    variables_predictoras_train, variables_predictoras_test, variable_a_predecir_train, variable_a_predecir_test = train_test_split(variables_predictoras, variable_a_predecir, test_size=0.2, random_state=42)
    modelo = LinearRegression()
    modelo.fit(variables_predictoras_train, variable_a_predecir_train)
    variable_a_predecir_pred = modelo.predict(variables_predictoras_test)

    return r2_score(variable_a_predecir_test, variable_a_predecir_pred),mean_absolute_error(variable_a_predecir_test, variable_a_predecir_pred)

def posicion_rank(nueva_columna,columna_grupo,columna_calculada,df):
    df[nueva_columna] = df.groupby(columna_grupo)[columna_calculada].rank(method="dense", ascending=False)
    return df[nueva_columna]

def ordanenar_culman_menor_mayor(columna_a_ordenar,df):
    columna_ordenada = df.sort_values(by=columna_a_ordenar, ascending=False)
    return columna_ordenada

def mostrar_solo_un_grupo(colum_group,elemento_columngroup,columnord):
    print(columnord[columnord[colum_group] == elemento_columngroup])

def grafico_plot_promedio(columna_grupo,valorobjetivo_o_columnacaclulada,kind,titulo,etiquetay,df,modulo):
    df.groupby(columna_grupo)[valorobjetivo_o_columnacaclulada].mean().plot(kind=kind, title=titulo, ylabel=etiquetay)
    print("Grafico de promedio")
    return modulo.show()

def histograma_seoborn(df,varbiale_onejtivo_calculada,bins,kde,titlle,xlabel,ylabel,modulo,m_para_mostrar_etquetas):
    modulo.histplot(df[varbiale_onejtivo_calculada],bins=bins,kde=kde)
    m_para_mostrar_etquetas.title(titlle)
    m_para_mostrar_etquetas.xlabel(xlabel)
    m_para_mostrar_etquetas.ylabel(ylabel)
    print("Grafico de frecuencia ")
    return m_para_mostrar_etquetas.show()

def categorizar_columna(df,columna,columna_nueva_categorizada,elemento_1,elemento_2):
    df[columna_nueva_categorizada] = df[columna].map({elemento_1: 1, elemento_2: 0})
    x=df[columna_nueva_categorizada]
    return x

def matriz_correlacion(df,colum1,colum2,colum3,colum4):
    columnas_corr = [colum1,colum2,colum3,colum4]
    return print("Matriz Correlacion es :\n",df[columnas_corr].corr())

def mapa_correlacion(df,colum1,colum2,colum3,colum4,modulo1_labels,modulo2,cmap,titulo):
    columnas_corr = [colum1, colum2, colum3, colum4]
    modulo2.heatmap(df[columnas_corr].corr(), annot=True, cmap=cmap)
    modulo1_labels.title(titulo)
    return modulo1_labels.show()

def tipo_de_distribucion(modulo_origen,shapiro,df,valor_obejtivo):
    stat, p = shapiro(df[valor_obejtivo])
    print(modulo_origen.compartamientodis(p))
    if p >0.05 :
        return print("Valor de p es:",p,"\nPuede considerarse una distribucion normal")
    else:
        return print("Valor de p es:",p,"\nNo es distribucion normal\n *No usar Parametricos*")


def tipo_tendencia_central(df,valor_obejetivo,modulo_origen):
    skew = df[valor_obejetivo].skew()
    print(modulo_origen.medianaomedia(skew))
    if 0.5>= skew >=-0.5 :
        return print("ES SIMETRICO, por ende usar media")
    else:
        return print("sesgo a la izquierda, por ende usar mediana")

def tabla_de_frecuencia(modul1,modulo2_labels,df,barras_por_campo,barras_divididas_por_sexo,titulo):
    modul1.countplot(data=df, x=barras_por_campo, hue=barras_divididas_por_sexo)
    modulo2_labels.title(titulo)
    modulo2_labels.xticks(rotation=45)
    return modulo2_labels.show()

def grafico_violin(sns,modulo_labelplt,df,x,ynum,titulo):
    sns.violinplot(data=df, x=x, y=ynum)
    modulo_labelplt.title(titulo)
    return modulo_labelplt.show()

def graficos_de_relaciones_cruzadas(sns,plt,df,columna1,columna2,columna3,columna4):
    sns.pairplot(df[[columna1, columna2, columna3, columna4]])
    return plt.show()

def grafico_circular(df,plt,categoria_a_evaluar,titulo):
    df[categoria_a_evaluar].value_counts().plot.pie(autopct="%1.1f%%")
    plt.title(titulo)
    plt.ylabel("")
    return plt.show()

def grafico_arbol(df,categoria1,categoria2,categoria3,valor_objetivo):
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score, mean_absolute_error
    X = df[[categoria1,categoria2,categoria3]]
    y = df[valor_objetivo]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo_arbol = DecisionTreeRegressor(max_depth=4)
    modelo_arbol.fit(X_train, y_train)
    y_pred = modelo_arbol.predict(X_test)

    r2_arbol = r2_score(y_test, y_pred)
    mae_arbol = mean_absolute_error(y_test, y_pred)

    print("Árbol de Decisión:")
    print(f"R²: {r2_arbol}")
    print(f"MAE: {mae_arbol}")
    return r2_arbol, mae_arbol

def grafico_de_dispersion(sns,df,plt,x,y,titulo,etiquetax,etiquetay):
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(titulo)
    plt.xlabel(etiquetax)
    plt.ylabel(etiquetay)
    return plt.show()

def modelo_clasificacion_binaria(df, columnas_predictoras, columna_objetivo):
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, confusion_matrix

    X = df[columnas_predictoras]
    y = df[columna_objetivo]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = DecisionTreeClassifier()
    modelo.fit(X_train, y_train)

    predicciones = modelo.predict(X_test)

    accuracy = accuracy_score(y_test, predicciones)
    matriz = confusion_matrix(y_test, predicciones)

    print("Exactitud del modelo:", accuracy)
    print("Matriz de confusión:\n", matriz)


    return modelo, X, y_test, predicciones


def visualizar_arbol_y_confusion(modelo, X, y_test, predicciones):
    from sklearn.tree import plot_tree
    from sklearn.metrics import confusion_matrix
    import matplotlib.pyplot as plt
    """
    Dibuja el árbol de decisión y muestra la matriz de confusión.

    Parámetros:
    - modelo: Árbol entrenado (DecisionTreeClassifier o Regressor)
    - X: DataFrame con las variables predictoras (para obtener los nombres de columnas)
    - y_test: Valores reales de prueba
    - predicciones: Valores predichos por el modelo
    """
    plt.figure(figsize=(12, 8))
    plot_tree(modelo, feature_names=X.columns, class_names=["Reprobado", "Aprobado"], filled=True)
    plt.title("Árbol de Decisión")
    plt.show()
    print("Matriz de confusión:")
    print(confusion_matrix(y_test, predicciones))

def prueba_t(grupo1,grupo2):
    from scipy.stats import levene, ttest_ind
    stat_levene, p_levene = levene(grupo1, grupo2)
    print("Levene p-valor:", p_levene)
    if p_levene > 0.05:
        stat_t, p_t = ttest_ind(grupo1, grupo2, equal_var=True)  # Student
        return print("t-test p-valor:", p_t, "\nmetodo usado *Student* ")
    else:
        stat_t, p_t = ttest_ind(grupo1, grupo2, equal_var=False)  # Welch
        return print("t-test p-valor:", p_t,"\nmetodo usado *Welch*")

def anova(df,valor_objetivo,columna_de_grupos):
    from scipy.stats import f_oneway
    grupos_anova = [grupo[valor_objetivo] for nombre, grupo in df.groupby(columna_de_grupos)]
    stat_anova, p_anova = f_oneway(*grupos_anova)
    print("ANOVA p-valor:", p_anova)