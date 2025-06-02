def remover_duplicados(nums):
    if not nums:
        return 0

    i = 0 #para inicializar
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]  # Mueve el valor único adelante

    return i + 1  # Longitud de la lista sin duplicados
