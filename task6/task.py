import json


def fuzzification(temp_now, data):
    result = {}

    for name, points in data.items():
        attachment_degree = 0
        for (start_x, start_y), (end_x, end_y) in zip(points, points[1:]):
            if start_x <= temp_now <= end_x:
                attachment_degree = start_y if start_x == end_x else start_y + (end_y - start_y) * (temp_now - start_x) / (end_x - start_x)
                break
        result[name] = attachment_degree

    return result


def map_fuzzification_results_to_output(fuzzification_results, control_mapping):
    fuzzification_control_output = {}

    for input_label, value in fuzzification_results.items():
        if input_label in control_mapping:
            output_label = control_mapping[input_label]
            if output_label in fuzzification_control_output:
                fuzzification_control_output[output_label] = max(fuzzification_control_output[output_label], value)
            else:
                fuzzification_control_output[output_label] = value

    return fuzzification_control_output


def defuzzification(warming_values, data):
    weighted_sum = 0
    total_weight = 0

    for name, attachment_degree in warming_values.items():
        if attachment_degree > 0:
            points = data[name]
            term_centroid = sum([x for x, _ in points]) / len(points)
            weighted_sum += attachment_degree * term_centroid
            total_weight += attachment_degree

    if total_weight != 0:
        return weighted_sum / total_weight 
    else: return 0



def main(temperature_file, warming_file, control_file, temperature_now):
    with open(temperature_file) as file1:
        temperature_data = json.load(file1)
    with open(warming_file) as file2:
        warming_data = json.load(file2)
    with open(control_file) as file3:
        control_data = json.load(file3)
    
    fuzzification_results = fuzzification(temperature_now, temperature_data)
    fuzzification_control_output = map_fuzzification_results_to_output(fuzzification_results, control_data)
    optimal_control = defuzzification(fuzzification_control_output, warming_data)

    return round(optimal_control, 2)


print(main('task6/temperature.json', 'task6/warming.json', 'task6/control.json', 25.1))
