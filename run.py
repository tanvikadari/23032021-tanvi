from multiprocessing import Pool
import json
import pytest
# from flask import Flask, make_response, jsonify
# app = Flask(__name__)
#
#
# @app.route("/bmi/calculator", methods=['GET'])

@pytest.fixture
def bmi_calculator():
    # Loading the input data
    with open('./input.json', 'r') as file:
        obj = file.read()
        file.close()
    base_data = json.loads(obj)
    '''
    Multiprocessing can be used to enhance performance on larger datasets by splitting them
    - the value of processes n can be changed further
    - skipped using multiprocessing now as the dataset size is very less
    pool = Pool(processes=1)
    count, result = pool.map_async(calculator, base_data)
    list.append(result)
    with open('./input.json', 'w') as file:
        json.dump(list, file)
        file.close()
    '''
    response = {'Overweight Count': calculator(base_data), 'status': 200}
    return response
    # return make_response(response, '200')


def calculator(base_data):
    try:
        category = 'BMI Category'
        risk = 'Health Risk'
        overweight_count = 0
        print(base_data)
        # Manipulation of data to derive Overweight count, BMI Category and Health Risk
        for i in base_data:
            i['BMI'] = i["WeightKg"] / (i["HeightCm"] / 100)
            if 18.4 <= i['BMI'] <= 24.9:
                i[category] = 'Underweight'
                i[risk] = 'Malnutrition risk'
            if 25 <= i['BMI'] <= 29.9:
                i[category] = 'Normal Weight'
                i[risk] = 'Low risk'
            if 30 <= i['BMI'] <= 34.9:
                i[category] = 'Overweight'
                i[risk] = 'Enhanced risk'
                overweight_count += 1
            if 35 <= i['BMI'] <= 39.9:
                i[category] = 'Moderately Obese'
                i[risk] = 'Medium risk'
                overweight_count += 1
            if 40 <= i['BMI']:
                i[category] = 'Severly Obese'
                i[risk] = 'High risk'
                overweight_count += 1
        return overweight_count
    except Exception as e:
        response = {'errorMessage': str(e)}
        return response
        # return make_response(jsonify(response), '500')


if __name__ == '__main__':
    bmi_calculator()
