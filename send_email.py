import win32com.client as win32
baseUrl = 'http://172.30.134.63:5000/'

def send(drawing_no, filing_id, nesting_ids, email, note):
 olApp = win32.Dispatch('Outlook.Application')
 # olNS = olApp.GetNameSpace('MAPI')
 nesting_ids = '|'.join(nesting_ids)

 mailItem = olApp.CreateItem(0)
 mailItem.Subject = f'Files for {drawing_no}'
 mailItem.BodyFormat = 2
 mailItem.HTMLBody = f'''
  <a href="{baseUrl}getFiles/?drawing_no={drawing_no}&filing_id={filing_id}&nesting_ids={nesting_ids}">Get files</a>
  <p>{note}</p>
 '''
 mailItem.To = email
 mailItem.Sensitivity  = 2
 # optional (account you want to use to send the email)
 # mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item('elvin.bashirli@azfen.com')))
 # mailItem.Display()
 mailItem.Save()
 mailItem.Send()