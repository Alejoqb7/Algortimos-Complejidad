def age_expression(dr_o_age, alyssa_age, konari_age):
    # Iterar posibles valores de Alyssa
    max_a = (dr_o_age - konari_age) // alyssa_age if dr_o_age - konari_age >= alyssa_age else 0

    for a in range(1, max_a + 1):
        remaining = dr_o_age - a * alyssa_age  # Lo que falta cubrir con Konari
        if remaining > 0 and remaining % konari_age == 0:
            return 1

    return 0

#return 1 si hay alguna combinación válida, return 0 si no
