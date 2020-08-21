import openpyxl
from pathlib import Path

products_path = 'D:/Documents/GoogleDrive/StackIntel.IO/Projects/AlRehmanPharma/Al-Rehman-DEV/'
xls_filename = 'App initial list 13-3-20.xlsx'


def is_eof(row):
    for col in row:
        if col.value is not None:
            return False

    return True


if __name__ == "__main__":
    xlsx_file = Path(products_path, xls_filename)
    print(xlsx_file)
    wb_obj = openpyxl.load_workbook(xlsx_file)
    sheet = wb_obj.active

    category = 'something'

    # print(sheet["E12"].value)
    i = 1
    products = list()
    while True:
        if is_eof(sheet[i]):
            break

        #  Get Type
        Ai = sheet['A' + str(i)].value
        if isinstance(Ai, str):
            category = Ai
            i = i + 1
            continue

        product = {
            "row": i,
            "category": category,
        }
        if sheet['A' + str(i)].value is not None:
            product["id"] = sheet['A' + str(i)].value
            product["name"] = sheet['B' + str(i)].value
            product["generic_name"] = sheet['C' + str(i)].value
            product["strengths"] = list()
            strength = {
                "strength": sheet['D' + str(i)].value,
                "packaging": list()
            }
            strength['packaging'].append({
                "package_size": sheet['E' + str(i)].value,
                "net_price": sheet['F' + str(i)].value,
                "carton_size": sheet['G' + str(i)].value,
                "mrp": sheet['H' + str(i)].value
            })
            product["strengths"].append(strength)
            products.append(product)
        else:
            product["id"] = products[-1]['id']
            product["name"] = products[-1]['name']
            product["generic_name"] = products[-1]['generic_name']

            duplicate_strength = False
            strength = sheet['D' + str(i)].value
            if strength is None:
                duplicate_strength = True
                strength = products[-1]['strengths'][-1]['strength']

            package_size = sheet['E' + str(i)].value
            if package_size is None:
                package_size = products[-1]['strengths'][-1]['packaging'][-1]['package_size']

            carton_size = sheet['G' + str(i)].value
            if carton_size is None:
                carton_size = products[-1]['strengths'][-1]['packaging'][-1]['carton_size']

            packaging = {
                "package_size": package_size,
                "net_price": sheet['F' + str(i)].value,
                "carton_size": carton_size,
                "mrp": sheet['H' + str(i)].value
            }

            if not duplicate_strength:
                strength = {
                    "strength": strength,
                    "packaging": list()
                }
                strength['packaging'].append(packaging)
                products[-1]['strengths'].append(strength)
            else:
                products[-1]['strengths'][-1]['packaging'].append(packaging)

        i = i + 1

    for product in products:
        print(product)

    # for i, row in enumerate(sheet.iter_rows()):
    #     if i == 0:  # first row
    #         continue
    #
    #     Ai = sheet['A' + str(i + 1)].value
    #     if not isinstance(Ai, int) and Ai is not None:
    #         type = Ai
    #         continue
    #
    #     product = {
    #         "row": i + 1,
    #         "type": type,
    #     }
    #     if sheet['A' + str(i)].value is not None:
    #         product["id"] = sheet['A' + str(i + 1)].value
    #         product["name"] = sheet['B' + str(i + 1)].value
    #         product["generic_name"] = sheet['C' + str(i + 1)].value
    #     else:
    #         product["id"] = products[-1]['id']
    #         product["name"] = products[-1]['name']
    #         product["generic_name"] = products[-1]['generic_name']
    #
    #     products.append(product)
    #     print(product)
