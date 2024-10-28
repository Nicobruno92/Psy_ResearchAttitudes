import pandas as pd
import os
import math
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess_sheet(sheet_id, output_filename='preprocessed.csv'):
    
    # 1. Load the data from Google Sheets
    df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
    
    # 2. Rename the columns
    column_mappings = {
        '¿Desea participar de la investigación?':'participacion',
        'Edad': 's1_edad',
        'Género':'s1_genero',
        'Años de Experiencia en la Clínica ':'s1_experiencia_clinica',
        'Nivel de Educación MÁXIMO Adquirido':'s1_educacion',
        'En caso de haber respondido Terciario u otro, ¿cuál fue su título?':'s1_titulo_terciario',
        '¿Cuál es tu título?':'s1_titulo',
        'En caso de haber respondido "no tengo título universitario", ¿cuál fue su título máximo adquirido?':'s1_no_titulo_universitario',
        'Número de Horas por Semana Atendiendo Pacientes (Aproximado)':'s1_horas_semana_pacientes_atendidos',
        'Contexto de Trabajo': 's1_contexto_trabajo',
        'Orientación Teórica':'s1_orientacion_teo',
        'Indique qué disciplina realiza:':'s1_marco_teo_terapia_basada_arte',
        'Indique qué marco teórico del psicoanálisis sigue usted:':'s1_marco_teo_psa',
        'Indique qué marco teórico utiliza usted en la clínica:':'s1_marco_teo_tcc',
        'Indique qué marco teórico utiliza en la práctica:':'s1_marco_teo_humanista',
        'Indique qué tipo marco teórico utiliza en la práctica:':'s1_marco_teo_eclectico',
        'Evidencia Científica':'s2_evidencia_cientifica',
        'Experiencia Personal con Consultantes (es decir la propia experiencia ejerciendo)':'s2_experiencia_personal',
        'Entrenamiento Práctico en Clínica':'s2_entrenamiento_clinica',
        'El tratamiento de Preferencia de los Consultantes ':'s2_tratamiento_preferencia_consultantes',
        'Intuición':'s2_intuicion',
        'Terapia Personal':'s2_terapia_personal',
        'Experiencia Personal con Consultantes':'s3_tratamiento_personal_consultantes',
        'Investigación Empírica con Ensayos Controlados ':'s3_investigacion_empirica_ensayos_controlados',
        'Supervisión':'s3_supervision',
        'Investigación Empírica de Estudios de Caso ':'s3_estudios_de_caso',
        'Discusión con Pares':'s3_discusion_pares',
        'Libros':'s3_libros',
        'Observaciones de Casos Clínicos (por ejemplo en ateneos, prácticas, etc)':'s3_observaciones_casos_clinicos',
        'Medidas de resultado (resultados de escalas, cuestionarios, etc)':'s3_medidas_resultado',
        'Guías o manuales clínicos':'s3_guias_manuales_clinicos',
        'Estoy dispuesto a utilizar nuevos y diferentes tipos de terapia desarrollados por investigadores':'s4_apertura_terapias_desarrolladas_por_investigadores',
        'Es mi deber profesional estar al día con los nuevos desarrollos en la investigación clínica (entendiendo a la investigación como un proceso que sigue el método científico)':'s4_actualizacion_info_cientifica',
        'Mi formación clínica hizo énfasis en la investigación (entendiendo a la investigación como un proceso que sigue el método científico)':'s4_formacion_enfasis_investigacion',
        'Mis supervisores requieren/han requerido que use tratamientos basados ​​en la evidencia (es decir, con apoyo del método científico)':'s4_supervisores_terapia_evidencia_requerimiento',
        'Los tratamientos basados ​​en el método científico son eficientes/costo-efectivos ':'s4_tratamientos_cientificos_eficientes',
        'Puedo atraer nuevos consultantes aprendiendo un tratamiento basado en evidencia (como resultado del método científico)':'s4_atraer_consultantes_con_tbe',
        'Es importante incorporar los hallazgos científicos en mi práctica diaria':'s4_hallazgos_cientificos_practica_diaria',
        'Intentaría una nueva terapia incluso si fuera muy diferente de lo que estoy acostumbrado a hacer (es decir muy diferente a lo que ejerzo)':'s4_nueva_terapia_intento',
        'Estoy interesado en aprender tratamientos basados ​​en evidencia (como resultado del método científico)':'s4_interes_aprender_tbe',
        'Los tratamientos que uso con mis consultantes tienen una base empírica (es decir cuentan con apoyo del método científico)':'s4_tratamientos_utilizados_base_empirica',
        'Mis consultantes son más complejos y diversos que los de los ensayos clínicos (provenientes de la investigación científica, ejemplo ensayos aleatorizados y controlados)':'s4_complejidad_consultantes_ensayos_clinicos',
        'Mis consultantes prefieren otros tratamientos que los tratamientos basados ​​en evidencia (como resultado del método científico)':'s4_consultantes_prefieren_otros_tratamientos',
        'La terapia no puede ser manualizada':'s4_terapia_manualizada',
        'Los diagnósticos utilizados en los ensayos clínicos son demasiado simples (ejemplo ensayos aleatorizados y controlados)':'s4_diagnosticos_utilizados_son_simples',
        'Los tratamientos que prefiero no se han probado en un ensayo controlado aleatorio':'s4_tratamientos_preferencia_no_probados_ensayo_controlado',
        'Tengo un enfoque de tratamiento individual para cada consultante':'s4_enfoque_tratamiento_individual',
        'No tengo tiempo para aprender tratamientos basados ​​en evidencia (como resultado del método científico)':'s4_no_tiempo_aprender_tbe',
        'La capacitación en tratamientos basados ​​en evidencia me costaría demasiado dinero (evidencia como resultado del método científico)':'s4_capacitacion_tbe_demasiado_dinero',
        'No sé cuáles tratamientos están basados ​​en evidencia (como resultado del método científico)':'s4_no_saber_tbe',
        'Mi entrenamiento clínico no proporcionó información suficiente sobre tratamientos basados ​​en evidencia (como resultado del método científico)':'s4_entrenamiento_clinico_no_info_tbe',
        'La alianza terapéutica es más importante que aprender cómo hacer una forma específica de psicoterapia':'s4_alianza_terapeutica_mas_importante',
        'La mayoría de las terapias son igualmente efectivas':'s4_terapias_igualmente_efectivas',
        'Mi empleador no tiene los fondos para pagarme una capacitación en tratamientos basados ​​en evidencia (como resultado del método científico)':'s4_empleador_no_fondos_capacitacion_tbe',
        'La experiencia clínica es más importante como guía para el tratamiento que la evidencia científica':'s4_exp_clinica_mas_importante_que_evidencia_cientifica',
        '¿Le parecieron claras todas las preguntas?':'claridad_preguntas',
        'En el caso de que haya respondido NO, ¿cuál/es no le parecieron CLARAS y por qué?':'claridad_preguntas_comentario',
        '¿Cree que alguna pregunta es inapropiada?':'pregunta_inapropiada',
        'En el caso de que haya respondido NO, ¿cuál/es no le parecieron APROPIADAS y por qué?':'pregunta_inapropiada_comentario',
        '¿Considera que se podrían hacer otras preguntas que aporten información valiosa a lo que se intenta estudiar?':'preguntas_adicionales',
        'En el caso de que haya respondido SÍ, ¿cuál/es?':'preguntas_adicionales_sugerencias',
        '¿Le gustaría agregar otro comentario?':'comentario_extra',
        '¿Usted ha tenido formación universitaria pública o privada?':'formacion_publica_vs_privada',
        'Provincia de Residencia':'provincia_residencia',
        'Considero fundamental el uso del consentimiento informado y lo uso siempre al tomar pacientes nuevos\n\n0 = No sabe/No contesta, 1 = Muy en desacuerdo , 4 = Ni de acuerdo ni en desacuerdo , 7 = Muy de acuerdo':'consentimiento_informado'
    }
    
    # 3. Apply renaming
    df = df.rename(columns=column_mappings)
    
    # 4. Define the relative path to save the file to '../../data' (two directories up)
    output_dir = os.path.join(os.getcwd(), '../../data')
    
    # Ensure the 'data' folder exists
    if not os.path.exists(output_dir):
        raise FileNotFoundError(f"The directory '{output_dir}' does not exist.")
    
    # Create full path for the output file
    output_file = os.path.join(output_dir, output_filename)
    
    # 5. Save to CSV
    df.to_csv(output_file, index=False)
    
    return df

def data_featuring(df):

    columns_to_remove = [
        'Timestamp', 'participacion', 'claridad_preguntas', 
        's4_pregunta_inapropiada_comentario', 's4_preguntas_adicionales', 
        's4_preguntas_adicionales_sugerencias', 'comentario_extra', 
        'formacion_publica_vs_privada', 
        '¿Le parecieron claras todas las preguntas?.1', 
        'En el caso de que haya respondido NO, ¿cuál/es no le parecieron CLARAS y por qué?.1', 
        '¿Cree que alguna pregunta es inapropiada?.1', 
        'En el caso de que haya respondido SÍ, ¿cuál/es no le parecieron APROPIADAS y por qué?', 
        '¿Considera que se podrían hacer otras preguntas que aporten información valiosa a lo que se intenta estudiar?.1', 
        'En el caso de que haya respondido SÍ, ¿cuál/es?.1', 
        '¿Le gustaría agregar otro comentario?.1',
        'claridad_preguntas_comentario',
        'pregunta_inapropiada',
        'pregunta_inapropiada_comentario',
        'preguntas_adicionales',
        'preguntas_adicionales_sugerencias'
    ]
    
    # Drop the unwanted columns
    df_cleaned = df.drop(columns=columns_to_remove, errors='ignore')

    columns = ['s2_evidencia_cientifica', 's2_experiencia_personal', 's2_entrenamiento_clinica', 
               's2_tratamiento_preferencia_consultantes', 's2_intuicion', 's2_terapia_personal']

    for column in columns:
        df_cleaned[column] = df_cleaned[column].replace(0, np.nan)

    # Replace 8 with 0 in the following columns
    columns_replace_8_with_0 = [
        's4_actualizacion_info_cientifica', 's4_formacion_enfasis_investigacion',
        's4_supervisores_terapia_evidencia_requerimiento', 's4_tratamientos_cientificos_eficientes',
        's4_atraer_consultantes_con_tbe', 's4_hallazgos_cientificos_practica_diaria', 
        's4_interes_aprender_tbe', 's4_tratamientos_utilizados_base_empirica', 
        's4_complejidad_consultantes_ensayos_clinicos', 's4_consultantes_prefieren_otros_tratamientos',
        's4_no_tiempo_aprender_tbe', 's4_capacitacion_tbe_demasiado_dinero', 's4_no_saber_tbe', 
        's4_entrenamiento_clinico_no_info_tbe', 's4_empleador_no_fondos_capacitacion_tbe'
    ]
    
    for column in columns_replace_8_with_0:
        df_cleaned[column] = df_cleaned[column].replace(8, 0)
    
    # Save the DataFrame to the correct data folder using '../../data'
    output_file = '../../data/featured_data.csv'

    # Save the DataFrame as CSV
    df_cleaned.to_csv(output_file, index=False)
    
    return df_cleaned

def create_section_2(df):

    # Define the columns you want to include in the subset
    section_2_columns = [
        's1_edad', 's1_genero', 's1_horas_semana_pacientes_atendidos',
        's1_orientacion_teo','s2_evidencia_cientifica', 's2_experiencia_personal', 's2_entrenamiento_clinica',
        's2_tratamiento_preferencia_consultantes', 's2_intuicion', 's2_terapia_personal'
    ]

    # Define the orientations you want to filter
    subset_orientations = ['Ecléctico (más de una de estas opciones)', 'Terapias Cognitivas/Comportamentales', 'Psicoanálisis', 'Sistémica']

    # Filter the DataFrame based on 'orientacion_teo' and select the relevant columns
    s2_df = df[df['s1_orientacion_teo'].isin(subset_orientations)][section_2_columns]

    return s2_df

def create_section_2_dataframe(tcc, psa, eclectico, sistemico, other):
    # Define the columns to calculate the mean for Section 2
    section_2_columns = [
        's2_evidencia_cientifica', 's2_experiencia_personal', 's2_entrenamiento_clinica',
        's2_tratamiento_preferencia_consultantes', 's2_intuicion', 's2_terapia_personal'
    ]

    # Calculate the mean for each orientation
    s2_tcc = tcc[section_2_columns].mean()
    s2_psa = psa[section_2_columns].mean()
    s2_eclectico = eclectico[section_2_columns].mean()
    s2_sistemico = sistemico[section_2_columns].mean()
    s2_other = other[section_2_columns].mean()

    # Create a DataFrame from the rounded means
    df2 = {
        'PSA': s2_psa.round(2),
        'TCC': s2_tcc.round(2),
        'ECLECTICO': s2_eclectico.round(2),
        'SISTEMICA': s2_sistemico.round(2),
        'OTHER': s2_other.round(2)
    }

    df2 = pd.DataFrame(df2)

    return df2

def create_section_3(df):

    # Define the columns you want to include in the subset
    section_3_columns = [
        's1_edad', 's1_genero', 's1_horas_semana_pacientes_atendidos',
        's1_orientacion_teo','s3_tratamiento_personal_consultantes', 's3_investigacion_empirica_ensayos_controlados',
        's3_supervision', 's3_estudios_de_caso', 's3_discusion_pares', 's3_libros', 
        's3_observaciones_casos_clinicos', 's3_medidas_resultado', 's3_guias_manuales_clinicos'
    ]

    # Define the orientations you want to filter
    subset_orientations = ['Ecléctico (más de una de estas opciones)', 'Terapias Cognitivas/Comportamentales', 'Psicoanálisis', 'Sistémica']

    # Filter the DataFrame based on 'orientacion_teo' and select the relevant columns
    s3_df = df[df['s1_orientacion_teo'].isin(subset_orientations)][section_3_columns]

    return s3_df

def create_section_3_dataframe(tcc, psa, eclectico, sistemico, other):
    # Define the columns to calculate the mean for Section 3
    section_3_columns = [
        's3_tratamiento_personal_consultantes', 's3_investigacion_empirica_ensayos_controlados',
        's3_supervision', 's3_estudios_de_caso', 's3_discusion_pares', 's3_libros', 
        's3_observaciones_casos_clinicos', 's3_medidas_resultado', 's3_guias_manuales_clinicos'
    ]

    # Calculate the mean for each orientation
    s3_tcc = tcc[section_3_columns].mean()
    s3_psa = psa[section_3_columns].mean()
    s3_eclectico = eclectico[section_3_columns].mean()
    s3_sistemico = sistemico[section_3_columns].mean()
    s3_other = other[section_3_columns].mean()

    # Create a DataFrame from the rounded means
    df3 = {
        'PSA': s3_psa.round(2),
        'TCC': s3_tcc.round(2),
        'ECLECTICO': s3_eclectico.round(2),
        'SISTEMICA': s3_sistemico.round(2),
        'OTHER': s3_other.round(2)
    }

    df3 = pd.DataFrame(df3)

    return df3

def create_section_4(df):

    # Define the columns you want to include in the subset
    section_4_columns = [
        's1_edad', 's1_genero', 's1_horas_semana_pacientes_atendidos',
        's1_orientacion_teo','s4_apertura_terapias_desarrolladas_por_investigadores', 's4_nueva_terapia_intento',
        's4_terapia_manualizada', 's4_diagnosticos_utilizados_son_simples', 
        's4_tratamientos_preferencia_no_probados_ensayo_controlado', 's4_enfoque_tratamiento_individual', 
        's4_alianza_terapeutica_mas_importante', 's4_terapias_igualmente_efectivas', 
        's4_exp_clinica_mas_importante_que_evidencia_cientifica', 's4_actualizacion_info_cientifica', 
        's4_formacion_enfasis_investigacion', 's4_supervisores_terapia_evidencia_requerimiento', 
        's4_atraer_consultantes_con_tbe', 's4_hallazgos_cientificos_practica_diaria', 
        's4_interes_aprender_tbe', 's4_tratamientos_utilizados_base_empirica', 
        's4_complejidad_consultantes_ensayos_clinicos', 's4_consultantes_prefieren_otros_tratamientos', 
        's4_no_tiempo_aprender_tbe', 's4_capacitacion_tbe_demasiado_dinero', 
        's4_no_saber_tbe', 's4_entrenamiento_clinico_no_info_tbe', 
        's4_empleador_no_fondos_capacitacion_tbe'
    ]

    # Define the orientations you want to filter
    subset_orientations = ['Ecléctico (más de una de estas opciones)', 'Terapias Cognitivas/Comportamentales', 'Psicoanálisis', 'Sistémica']

    # Filter the DataFrame based on 'orientacion_teo' and select the relevant columns
    s4_df = df[df['s1_orientacion_teo'].isin(subset_orientations)][section_4_columns]

    return s4_df

def create_section_4_dataframe(tcc, psa, eclectico, sistemico, other):
    # Define the columns to calculate the mean for Section 4
    section_4_columns = [
        's4_apertura_terapias_desarrolladas_por_investigadores', 's4_nueva_terapia_intento',
        's4_terapia_manualizada', 's4_diagnosticos_utilizados_son_simples', 
        's4_tratamientos_preferencia_no_probados_ensayo_controlado', 's4_enfoque_tratamiento_individual', 
        's4_alianza_terapeutica_mas_importante', 's4_terapias_igualmente_efectivas', 
        's4_exp_clinica_+imp_que_evidencia_cientifica', 's4_actualizacion_info_cientifica', 
        's4_formacion_enfasis_investigacion', 's4_supervisores_terapia_evidencia_requerimiento', 
        's4_atraer_consultantes_con_tbe', 's4_hallazgos_cientificos_practica_diaria', 
        's4_interes_aprender_tbe', 's4_tratamientos_utilizados_base_empirica', 
        's4_complejidad_consultantes_ensayos_clinicos', 's4_consultantes_prefieren_otros_tratamientos', 
        's4_no_tiempo_aprender_tbe', 's4_capacitacion_tbe_demasiado_dinero', 
        's4_no_saber_tbe', 's4_entrenamiento_clinico_no_info_tbe', 
        's4_empleador_no_fondos_capacitacion_tbe', 's4_exp_clinica_+imp_que_evidencia_cientifica'
    ]

    # Calculate the mean for each orientation
    s4_tcc = tcc[section_4_columns].mean()
    s4_psa = psa[section_4_columns].mean()
    s4_eclectico = eclectico[section_4_columns].mean()
    s4_sistemico = sistemico[section_4_columns].mean()
    s4_other = other[section_4_columns].mean()

    # Create a DataFrame from the rounded means
    df4 = {
        'PSA': s4_psa.round(2),
        'TCC': s4_tcc.round(2),
        'ECLECTICO': s4_eclectico.round(2),
        'SISTEMICA': s4_sistemico.round(2),
        'OTHER': s4_other.round(2)
    }

    df4 = pd.DataFrame(df4)

    return df4


def plot_section(df_subset, variables, y_variable='s1_orientacion_teo', num_cols=2, original_y_order=None):
    """
    Creates point plots for the given independent variables, handling duplicates and NaN counts.

    Parameters:
    - df_subset: DataFrame containing the data
    - variables: List of column names to create point plots for
    - y_variable: The dependent variable (default: 's1_orientacion_teo')
    - num_cols: Number of columns in the subplot grid (default: 2)
    - original_y_order: List of y-axis labels in the desired order (default: theoretical orientations)
    """

    # eliminate duplicate columns if any
    df_subset = df_subset.loc[:, ~df_subset.columns.duplicated()].drop_duplicates()

    # Reset index to avoid reindexing issues
    df_subset_cleaned = df_subset.reset_index(drop=True)

    # Calculate the number of rows needed in the subplot grid
    num_rows = math.ceil(len(variables) / num_cols)

    if original_y_order is None:
        original_y_order = ['Psicoanálisis', 'Ecléctico (más de una de estas opciones)', 
                            'Sistémica', 'Terapias Cognitivas/Comportamentales']

    # Create a subplot grid of the appropriate size
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 4*num_rows))
    fig.subplots_adjust(hspace=0.5)

    # Flatten the array of axes, so we can easily iterate over it
    axs = axs.flatten()

    for i, var in enumerate(variables):
        # Count the number of data points and NaNs for each 's1_orientacion_teo' value
        counts = df_subset_cleaned.groupby(y_variable)[var].count()
        nan_counts = df_subset_cleaned[df_subset_cleaned[var].isna()].groupby(y_variable).size()

        # Plot the point plot with updated linestyle parameter
        sns.pointplot(x=var, y=y_variable, hue=y_variable, 
                      data=df_subset_cleaned, orient="h", linestyle='none', 
                      capsize=0.2, ax=axs[i], order=original_y_order)

        # Check if a legend exists before trying to remove it
        if axs[i].get_legend() is not None:
            axs[i].get_legend().remove()  # Remove legend from each subplot if it exists

        axs[i].set_title(f'{var}')
        axs[i].set_xlabel('')  # Remove x-axis label
        axs[i].set_xlim(1, 7)  # Set x-axis limits to be between 1 and 7

        # Update y-axis labels with counts and NaN counts included
        new_labels = [f"{label.get_text()} (count={counts.get(label.get_text(), 0)}, NaN={nan_counts.get(label.get_text(), 0)})" 
                      for label in axs[i].get_yticklabels()]
        axs[i].set_yticks(range(len(new_labels)))
        axs[i].set_yticklabels(new_labels)

    # Remove unused subplots
    for j in range(i+1, len(axs)):
        fig.delaxes(axs[j])

    plt.tight_layout()
    plt.show()


