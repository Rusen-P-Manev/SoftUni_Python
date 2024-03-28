def filter_data(data: list):

    return [round(float(ele)) for ele in data]


data = input().split()
print(filter_data(data))
