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

def sendNotification(body):
 olApp = win32.Dispatch('Outlook.Application')
 # olNS = olApp.GetNameSpace('MAPI')

 mailItem = olApp.CreateItem(0)
 mailItem.Subject = body['subject']
 mailItem.BodyFormat = 2
 mailItem.HTMLBody = getHtmlContent(
  body['name'],
  body['description'],
  body['url'],
  body['taskNumber'],
  body['toDo'],
  body['revisionType'],
  body['title'],
  body['module'],
  body['level'],
  body['structureType'],
  ', '.join(body['referenceDrawings']),
  body['teklaPhase'],
  body['eCFNumber'],
  ', '.join(body['relatedPeopleInitials']),
  body['note']
 )
 mailItem.To = '; '.join(body['emails'])
 mailItem.Sensitivity  = 2
 # optional (account you want to use to send the email)
 # mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, olNS.Accounts.Item('elvin.bashirli@azfen.com')))
#  mailItem.Display()
 mailItem.Save()
 mailItem.Send()

def getHtmlContent(
 name,
 description,
 url,
 taskNumber,
 toDo,
 revisionType,
 title,
 module,
 level,
 structureType,
 referenceDrawing,
 teklaPhase,
 eCFNumber,
 relatedPeople,
 note,
):

  style = '''
    table, th, td {
      border: 1px solid black;
    }
    table {
      width: 40em;
    }
    .key {
      width: 15em;
    }
    .value {
      width: 60em;
    }
  '''
  html = f'''
  <head>
    <style>
      {style}
    </style>
  </head>
  <body>
    <h4>{name},</h4>
    <p>{description}</p>
    <table>
      <tr>
        <td class="key">Task number</td>
        <td class="value"><a href="{url}">{taskNumber}</a></td>
      </tr>

      <tr>
        <td class="key">To do</td>
        <td class="value">{toDo}</td>
      </tr>

      <tr>
        <td class="key">Revision type</td>
        <td class="value">{revisionType}</td>
      </tr>

      <tr>
        <td class="key">Title</td>
        <td class="value">{title}</td>
      </tr>

      <tr>
        <td class="key">Module</td>
        <td class="value">{module}</td>
      </tr>

      <tr>
        <td class="key">Level</td>
        <td class="value">{level}</td>
      </tr>

      <tr>
        <td class="key">Structure Type</td>
        <td class="value">{structureType}</td>
      </tr>

      <tr>
        <td class="key">Reference Drawings</td>
        <td class="value">{referenceDrawing}</td>
      </tr>

      <tr>
        <td class="key">Tekla Phase</td>
        <td class="value">{teklaPhase}</td>
      </tr>

      <tr>
        <td class="key">ECF Number</td>
        <td class="value">{eCFNumber}</td>
      </tr>

      <tr>
        <td class="key">Related People</td>
        <td class="value">{relatedPeople}</td>
      </tr>

      <tr>
        <td class="key">Note</td>
        <td class="value">{note}</td>
      </tr>
    </table>
    <p><b>Note: </b>This is a system generated email.</p>
  </body>

  '''

  return html


