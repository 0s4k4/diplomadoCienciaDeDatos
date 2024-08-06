##la eficencia general de os equipos es un indicar para calcular que tanto se aprovecha la maquinaria

##calculo de la eficiencia general de equipo

#OEE = eficineica_general(overall Equipment Effectiveness)
##eficiencia_general = disponibilidad x eficiencia x calidad
##disponibilidad = tiempo_disponible - tiempo_muerto
##eficiencia = produccion_total / (tiempo_operativo * capacidad)
##calidad = (produccion_total - defectos_y_procesos) / produccion_total




def calcular_oee(capacitad_maxima_por_hora, registro_de_horas, mantenimientos_preventivos_horas, hora_maquinaria_dejo_trabajar, maquina_se_detuvo, total_produccion, piezas_defectousas):
    ##calculo de intermedios
    tiempo_planeado  = registro_de_horas - mantenimientos_preventivos_horas - hora_maquinaria_dejo_trabajar
    tiempo_de_operacion = tiempo_planeado - maquina_se_detuvo
    produccion_ideal = tiempo_de_operacion * capacitad_maxima_por_hora
    piezas_buenas = total_produccion - piezas_defectousas
    
    
    #calculo del OEE
    
    disponiblidad = tiempo_de_operacion / tiempo_planeado
    rendimiento = total_produccion / produccion_ideal
    calidad = piezas_buenas / total_produccion
    oee = disponiblidad * rendimiento * calidad
    
    
    return disponiblidad, rendimiento,calidad,oee


##datos

capacidad_maxima_por_hora = 260
registro_de_horas = 300
mantenimientos_preventivos_horas = 16
hora_maquinaria_dejo_trabajar = 16
maquina_se_detuvo = 4
total_produccion = 45409
piezas_defectuosas = 3802


disponibilidad, rendimiento, calidad, oee = calcular_oee(
    capacidad_maxima_por_hora,
    registro_de_horas,
    mantenimientos_preventivos_horas,
    hora_maquinaria_dejo_trabajar,
    maquina_se_detuvo,
    total_produccion,
    piezas_defectuosas
)

print(f"Disponilidad: {disponibilidad * 100:.2f}%")
print(f"Rendimiento: {rendimiento * 100:.2f}%")
print(f"Calidad: {calidad * 100:.2f}%")
print(f"OEE: {oee * 100:.2f}%")