from WhatsAppUIAutomation.automation import WhatsAppUi
whatsapp = WhatsAppUi()
whatsapp.search_number("+8801750519919")
whatsapp.send_message("Another Text Message")
whatsapp.verify_successfully_send_message()
whatsapp.send_message_status()
whatsapp.verify_logout()
