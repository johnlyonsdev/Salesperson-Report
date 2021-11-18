"""Generate sales report showing total melons each salesperson sold."""

def generate_report():
    sales_report = {}

    file = open('sales-report.txt')
    for line in file:
        line = line.rstrip()
        data = line.split('|')

        salesperson = data[0]
        melons = int(data[2])

        if salesperson in sales_report:
            sales_report[salesperson] += melons
        else:
            sales_report[salesperson]=melons
    
    for key in sales_report:
        print(f'{key} sold {sales_report[key]} melons')

    file.close()

generate_report()