# Tools dos perfis de IA (Fique à vontade para criar tools que façam sentido aos agentes)

# automatizador

# ai_first

# multitool

# gestora

# cetico

# sensei

# criadora

# executor
def produtividade(horas: int) -> dict:
    """
    Calcula a distribuição ideal de tempo baseada no Nível A de produtividade.
    
    Args:
        horas: Número inteiro de horas totais para distribuir
        
    Returns:
        dict: Dicionário com a distribuição de tempo em cada categoria
        
    Exemplo:
        >>> resultado = produtividade(20)
        >>> print(resultado)
        {'com_margem': 8.0, 'sem_margem': 6.0, 'obrigatoria': 4.0, 'dispensavel': 2.0}
    """
    distribuicao = {
        'com_margem': horas * 0.40,
        'sem_margem': horas * 0.30,
        'obrigatoria': horas * 0.20,
        'dispensavel': horas * 0.10
    }
    
    return distribuicao

# evangelizador

# artista

