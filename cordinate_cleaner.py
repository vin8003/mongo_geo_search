from dbconnect import dbconnect
import re
import json

db = dbconnect()


def cleaner(one):
    value = one.split(' ')[0]
    degree_sign = re.sub('[0-9.]', '', value)
    cleaned = value.split(degree_sign)[0]

    return cleaned


def dict_cleaner(total_data):
    gps_n = total_data['gps'].split(',')[0]
    clean_gps_n = cleaner(gps_n)

    gps_e = total_data['gps'].split(', ')[1]
    clean_gps_e = cleaner(gps_e)

    new_list_of_cordinates = [float(clean_gps_n), float(clean_gps_e)]

    final_dict = {}
    for key, value in total_data.items():
        if key != 'gps':
            final_dict[key] = value

    final_dict['gps'] = new_list_of_cordinates
    return final_dict


if __name__ == '__main__':
    result = db.uncleaned_data.find({}, {'_id': False})

    orignal_list = []
    for i in result:
        orignal_list.append(i)

    output_list = []
    for i in orignal_list:
        try:
            cleaned_dict = dict_cleaner(i)
            output_list.append(cleaned_dict)

        except Exception as e:
            print('Exception occured:', e, '\n\n', i)

    # FOR SAVING TO A FILE
    out_list = open('cleaned_list.json', 'w')
    out_list.write(json.dumps(output_list))
    out_list.close()

    # FOR SAVING TO THE DATABASE
    # for i in output_list:
    #     db.states.insert_one(i)
