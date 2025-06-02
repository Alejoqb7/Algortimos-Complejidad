def remover_elemento(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]  #elementos diferentes a 'val'
            i += 1
    return i  # Longitud de la lista sin el elemento que se quitó
