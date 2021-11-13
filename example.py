import openpyxl

from WhatsAppUIAutomation.automation import WhatsAppUi


def load_excel():
    workbook = openpyxl.load_workbook('./whatsapp_ui.xlsx')
    print(str(workbook) + " Workbook Opened...")
    sheet = workbook['whatsapp']
    print(str(sheet) + " Reading...")
    for r in range(2, 3):
        sl_no = sheet.cell(row=r, column=1).value
        number = sheet.cell(row=r, column=2).value
        message = sheet.cell(row=r, column=3).value
        sent_status = sheet.cell(row=r, column=4).value
        checking_status = sheet.cell(row=r, column=4).value
        login_status = sheet.cell(row=r, column=5).value
        logout_status = sheet.cell(row=r, column=6).value

        print(f'SL No : {sl_no} \n Number : {number} \n '
              f'Message : {message} \n Sent Status : {sent_status} \n '
              f'Checked : {checking_status} \n '
              f'Login : {login_status} \n Logout : {logout_status}')


if __name__ == "__main__":
    load_excel()
    exit()
    whatsapp = WhatsAppUi()
    whatsapp.search_number("+8801750519919")
    whatsapp.send_message("Another Text Message")
    whatsapp.verify_successfully_send_message()
    whatsapp.send_message_status()
    whatsapp.verify_logout()
