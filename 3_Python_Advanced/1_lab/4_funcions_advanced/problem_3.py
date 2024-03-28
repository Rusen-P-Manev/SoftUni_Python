def sorting_cheeses(**kwargs):

    final_result = ''
    result = sorted(
        kwargs.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0])
    )

    for cheese_name, quantityis in result:
        final_result += cheese_name + '\n'
        for quanti in sorted(quantityis, reverse=True):
            final_result += f'{quanti}\n'
    return final_result



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)