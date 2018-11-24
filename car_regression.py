"""
This has nothing to do with the course, I'm just brushing up on linear regression
"""
import collections

stepSize = 0.01


def sale_for_data(constant, slope, data):
    return constant + slope * data  # y = c + ax


def step_cost_function_for(gdp_sale, constant, slope):
    global stepSize
    diff_sum_constant = 0
    diff_sum_slope = 0
    gdp_for_years = list(gdp_sale.keys())

    for year_gdp in gdp_for_years:
        trg_data_sale = sale_for_data(constant, slope, year_gdp)
        a_year_sale = gdp_sale.get(year_gdp)
        diff_sum_slope = diff_sum_slope + ((trg_data_sale - a_year_sale) * year_gdp)
        diff_sum_constant = diff_sum_constant + (trg_data_sale - a_year_sale)

    step_for_constant = (stepSize / len(gdp_sale)) * diff_sum_constant
    step_for_slope = (stepSize / len(gdp_sale)) * diff_sum_slope
    new_constant = constant - step_for_constant
    new_slope = slope - step_for_slope

    return new_constant, new_slope


def get_weights(gdp_sale):
    constant = 1
    slope = 1
    accepted_diff = 0.01

    while 1 == 1:
        new_constant, new_slope = step_cost_function_for(gdp_sale, constant, slope)
        if (abs(constant - new_constant) <= accepted_diff) and (abs(slope - new_slope) <= accepted_diff):
            return new_constant, new_slope
        else:
            constant = new_constant
            slope = new_slope


def read():
    data = open('assets/car_sales.csv')
    gdp_sale = collections.OrderedDict()
    for line in data.readlines()[1:]:
        record = line.split(',')
        gdp_sale[float(record[1])] = float(record[2].replace('\n', ''))

    return gdp_sale


def basic():
    gdp_sale = read()
    constant, slope = get_weights(gdp_sale)
    print('Constant is ' + str(constant) + ', and slope is ', str(slope))


def main():
    print('Doing it basic: ')
    basic()
